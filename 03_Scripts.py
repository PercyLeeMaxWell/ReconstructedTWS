from sklearn.decomposition import FastICA, PCA

#%% pca
pca = PCA(n_components=20)
H_x = pca.fit_transform(y)
PC_weights=pca.components_

#%% ica
ica = FastICA(n_components=4)
S_=ica.fit_transform(y)
A_=ica.mixing_

#%% OK
from pykrige.ok import OrdinaryKriging
kriging_grid=[]
test_data=[]
for i in range(168):
    OK=OrdinaryKriging(lons, lats, data[:,i], variogram_model='gaussian',nlags=6)
    z1, ss1 = OK.execute('grid', grid_lon, grid_lat)
    kriging_grid.append(z1)
    test_data.append(OK.get_variogram_points())
kriging_grid=np.array(kriging_grid)

#%% STL
from statsmodels.tsa.seasonal import STL
import pandas as pd
STL_sum_input=[]
for i in range(270):
    STL_input=[]
    for j in range(7):
        gl=data_ex[i,:,j]
        gl=pd.Series(gl,index=pd.date_range('01-01-2005', periods=len(gl), freq='M'), name = 'gl')
        stl = STL(gl, period=12, low_pass=13, trend=19, seasonal=35)
        res = stl.fit(inner_iter=5,outer_iter=0)
        recon_STL=np.array([res.resid, res.seasonal, res.trend]).T
        STL_input.append(recon_STL)
    STL_sum_input.append(np.array(STL_input))
    print('STL input finished %d'%(i+1))
STL_sum_input=np.array(STL_sum_input)
STL_sum_input_trans=np.transpose(STL_sum_input,axes=(1,0,2,3))
# trend components
data_input_LR=STL_sum_input_trans[:,:,:,-1]
# detrended components
data_input_RF=np.sum(STL_sum_input_trans[:,:,:,:-1],axis=3)

#%% MLR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV

lm=LinearRegression()
hyper_params = [{'n_features_to_select': list([len(input_list[k]),len(input_list[k])])}]

X_train=data_train[i,input_list[k],:,j]
Y_train=data_train[i,-1,:,j]
X_train=X_train.T
Y_train=Y_train[:,np.newaxis]
lm.fit(X_train,Y_train)
ref =RFE(lm)

clf = GridSearchCV(estimator=ref, param_grid=hyper_params,cv=4,
    scoring = 'neg_mean_squared_error', n_jobs=-1)
clf.fit(X_train,Y_train)
print('%d_%d_Best parameters:'%(i,j))

# predict trend simulation
Y_train_pre = np.asarray(clf.best_estimator_.predict(X_train))

#%% RF
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

model = RandomForestRegressor()
param_grid = [{'n_estimators': np.arange(100, 1001, 100),
           'max_features': ['auto','sqrt','log2']}]#auto和sqrt一样，实际上只有两个选择

clf = GridSearchCV(estimator=model,param_grid=param_grid, cv=4,
                    scoring = 'neg_mean_squared_error', n_jobs=-1)
X_train=data_train[i,input_list[k],:,j]
Y_train=data_train[i,-1,:,j]
X_train=X_train.T
Y_train=Y_train[:]
clf.fit(X_train,Y_train)
results = clf.cv_results_
print('%d_%d_%d_Best parameters:'%(k,i,j))

# predict detrended simulation
Y_train_pre = np.asarray(clf.best_estimator_.predict(X_train))
