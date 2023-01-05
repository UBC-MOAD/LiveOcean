"""
A universal dictionary to deal with the varying column naming conventions
in the NANOOS bottle data.

The initial list was generate by dev_code.py and here I have added hand edits
just for the variables we want to keep.

Only the keys with a non-empty value will be used.

"""
v_dict = {
' Bottle':'',
' C0mS/cm':'',
' CStarAt0':'',
' CStarTr0':'',
' Cast':'',
' CruiseID':'cruise',
' Density00':'',
' DepSM':'',
' Dz/dtM':'',
' FlECO-AFL':'',
' Latitude':'lat',
' Longitude':'lon',
' NMEANlon':'',
' NMEAlat':'',
' NMEAtimeUTC':'',
' Par':'',
' Ph':'',
' Potemp090C':'PT',
' PrDM':'P (dbar)',
' Sal00':'SP',
' Sbeox0ML/L':'',
' Sbeox0Mg/L':'',
' Sbeox0PS':'',
' Sbeox0V':'',
' Sbox0Mm/Kg':'',
' Scan':'',
' Sigma-_00':'',
' Sigma-t00':'',
' Sigma-é00':'',
' Station':'',
' SvCM':'',
' SvCM1':'',
' Sva':'',
' T090C':'',
'AMMONIUM_UMOL_L':'NH4 (uM)',
'BOT OXY 2017 calc (umol/kg)':'',
'BOT OXY comment':'',
'BOT SAL':'',
'BOT_OXY_avg_mg_L':'',
'CHLA (ug/l)':'',
'CHLA 2 (ug/l)':'',
'CHLA avg (ug/l)':'ChlA (ug/L)',
'CHLA_FLAG':'',
'CRUISE_ID':'cruise',
'CTD FLU (mg/m3)':'',
'CTD OXY (umol/kg)':'',
'CTD/O2_COMMENTS':'',
'CTD/SAL_COMMENTS':'',
'CTD/TEMP_COMMENTS':'',
'CTDOXY_FLAG':'',
'CTDOXY_FLAG_W':'',
'CTDOXY_MG_L_1':'',
'CTDOXY_MG_L_2':'',
'CTDOXY_MG_L_AVG':'',
'CTDOXY_UMOL_KG_ADJ':'DO (umol/kg)',
'CTDOXY_UMOL_KG_uncorr':'',
'CTDPRS_DBAR':'P (dbar)',
'CTDSAL2_PSS78':'',
'CTDSAL_FLAG':'',
'CTDSAL_FLAG_W':'',
'CTDSAL_PSS78':'SP',
'CTDTMP2_DEC_C_ITS90':'',
'CTDTMP_DEG_C_ITS90':'PT', # is this in-situ temperature or potential?
'CTDTMP_FLAG_W':'',
'CTD_OXY_check (umol/kg)':'',
'CTD_PH':'',
'CTD_PH_SCALE(NBS?)':'',
'DATE_LOCAL':'',
'DATE_UTC':'date_utc',
'DEPTH (M)':'',
'DIC bottle #':'',
'DIC_FLAG_W':'',
'DIC_UMOL_KG':'DIC (umol/kg)',
'Date_LOCAL':'',
'Date_UTC':'date_utc',
'LATITUDE_DEC':'lat',
'LATITUDE_DEG':'',
'LONGITUDE_DEC':'lon',
'LONGITUDE_DEG':'',
'NISKIN_NO':'',
'NISKIN_NO_FLAG_W':'',
'NITRATE_UMOL_L':'NO3 (uM)',
'NITRITE_UMOL_L':'NO2 (uM)',
'NO3 +NO2 (uM)':'',
'NUTRIENTS_FLAG_W':'',
'Nutrient comments':'',
'Nutrient lab temperature':'',
'OXYGEN COMMENTS':'',
'OXYGEN_FLAG_W':'',
'OXYGEN_MG_L_1':'',
'OXYGEN_MG_L_2':'',
'OXYGEN_MG_L_3':'',
'OXYGEN_UMOL_KG':'',
'OXYGEN_avg_mg_L':'DO (mg/L)',
'PHAEOPIGMENT (ug/l)':'',
'PHAEOPIGMENT 2 (ug/l)':'',
'PHAEOPIGMENT avg (ug/l)':'',
'PHAEOPIGMENT_FLAG':'',
'PHOSPHATE_UMOL_L':'PO4 (uM)',
'SALINITY_FLAG':'',
'SALINITY_FLAG_W':'',
'SALINITY_PSS78':'',
'SECCHI DEPTH (m)':'',
'SIGMATHETA2_KG_M3':'',
'SIGMATHETA_KG_M3':'',
'SILICATE_UMOL_L':'SiO4 (uM)',
'STATION_NO':'name',
'Station number':'name',
'TA_FLAG_W':'',
'TA_UMOL_KG':'TA (umol/kg)',
'TIME_LOCAL':'',
'TIME_UTC':'time_utc',
'Time_LOCAL':'',
'Time_UTC':'time_utc',
'Uploadtime':'',
'record no':'',
}
