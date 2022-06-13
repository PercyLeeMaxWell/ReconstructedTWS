# Descriptions for Dataset and scripts applied as Supporting Information for peer review purposes only

Here we provide:
1.	The principal components (PCs) and independent components (ICs) derived from groundwater levels during 200501-201812 as well as their spatial weights in the North China Plain (NCP) via the principal component analysis (PCA) and independent component analysis (ICA).
2.	The interpolated data derived from groundwater levels in the North China Plain (NCP) during 200501-201812 via the ordinary Kriging interpolation method. The area is at latitude 34.5~40.5 and longitude 113~119.5. The resolution is the same as the GRACE TWS data.
3.	The reconstructed GRACE-type TWS data during 200503-201812 in the NCP under case 5 of the manuscript. The area is at latitude 34.5~40.5 and longitude 113~119.5.
4.  THe Scripts of critical processes for the reconstruction, including the PCA, ICA, OK, STL, MLR, and RF methods.

**File descriptions**:

'01_PC.npy' saves the first eight principal components derived from groundwater levels in the North China Plain via the principal component analysis;

'01_PC_Ws.npy' saves the spatial weights of the first eight principal components derived from groundwater levels in the North China Plain via the principal component analysis;

'01_IC.npy' saves the four independent components derived from groundwater levels in the North China Plain via the independent component analysis;

'01_IC_Ws.npy' saves the spatial weights of the four independent components derived from groundwater levels in the North China Plain via the independent component analysis;

'01_OK.npy' saves the interpolated data derived from groundwater levels in the North China Plain (NCP) during 200501-201812 via the ordinary Kriging interpolation method.;

'02_NCP_reconstructed_TWS.npy' saves the reconstructed GRACE-type TWS data during 200503-201812 in the North China Plain under case 5 of the manuscript;

'03_Scripts.py' saves some relevant critical scripts for the reconstruction.

These data and script files can all be loaded via Python.
