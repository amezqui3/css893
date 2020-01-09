# markerD = {'S001','S003','S005','S007','S009','S011','S013','S015','S017','S019','S021','S023','S025','S027','S029','S031','S033','S035','S037','S039','S041','S043','S045','S047','S049','S051','S053','S055','S057','S059','S061','S063','S065','S067','S069','S071','S073','S075','S077','S079','S081','S083','S085','S087','S089','S091','S093','S095','S097','S099','S101','S103','S105','S107','S109','S111','S113','S115','S117','S119','S121','S123','S125','S127','S129','S131','S133','S135','S137','S139','S141','S143','S145','S147','S149','S151','S153','S155','S157','S159','S161','S163','S167','S169','S171','S172','S173','S175','S177','S179','S181','S183','S185','S187','S189','S191','S193','S195','S197','S199','S201','S203','S205','S207','S209','S211','S213','S215','S217','S219','S221','S223'}

# files = [
# ('S001','S001_l20_x105_y625_z94.tif'),
# ('S002','S002_l43_x908_y1587_z112.tif'),
# ('S003','S003_l10_x644_y156_z91.tif'),
# ('S004','S004_l29_x721_y1558_z115.tif'),
# ('S005','S005_l10_x605_y153_z94.tif'),
# ('S006','S006_l22_x1091_y1539_z115.tif'),
# ('S007','S007_l11_x220_y379_z94.tif'),
# ('S008','S008_l28_x1104_y139_z113.tif'),
# ('S009','S009_l44_x212_y1074_z95.tif'),
# ('S010','S010_l2_x279_y364_z50.tif'),
# ('S011','S011_l31_x564_y1466_z91.tif'),
# ('S012','S012_l53_x825_y1628_z98.tif'),
# ('S013','S013_l9_x290_y1288_z93.tif'),
# ('S014','S014_l21_x254_y1214_z112.tif'),
# ('S015','S015_l6_x209_y1075_z93.tif'),
# ('S016','S016_l26_x184_y1076_z120.tif'),
# ('S017','S017_l10_x420_y219_z100.tif'),
# ('S018','S018_l3_x209_y1063_z80.tif'),
# ('S019','S019_l11_x206_y1114_z98.tif'),
# ('S020','S020_l39_x150_y1023_z117.tif'),
# ('S021','S021_l14_x173_y1015_z98.tif'),
# ('S022','S022_l40_x181_y1101_z116.tif'),
# ('S023','S023_l20_x194_y1181_z97.tif'),
# ('S024','S024_l28_x163_y1070_z116.tif'),
# ('S025','S025_l16_x178_y1107_z98.tif'),
# ('S026','S026_l15_x108_y933_z117.tif'),
# ('S027','S027_l15_x175_y1052_z99.tif'),
# ('S028','S028_l13_x128_y778_z118.tif'),
# ('S029','S029_l10_x276_y1203_z99.tif'),
# ('S030','S030_l20_x160_y1095_z118.tif'),
# ('S031','S031_l14_x342_y250_z122.tif'),
# ('S032','S032_l32_x1313_y1451_z142.tif'),
# ('S033','S033_l16_x143_y539_z122.tif'),
# ('S034','S034_l27_x105_y634_z141.tif'),
# ('S035','S035_l6_x58_y742_z90.tif'),
# ('S036','S036_l13_x107_y862_z102.tif'),
# ('S037','S037_l33_x1617_y572_z168.tif'),
# ('S038','S038_l30_x245_y1175_z134.tif'),
# ('S039','S039_l20_x59_y755_z115.tif'),
# ('S040','S040_l24_x1461_y1209_z134.tif'),
# ('S041','S041_l14_x297_y318_z114.tif'),
# ('S042','S042_l12_x269_y1135_z132.tif'),
# ('S043','S043_l12_x177_y1070_z113.tif'),
# ('S044','S044_l24_x213_y1206_z131.tif'),
# ('S045','S045_l11_x126_y1029_z99.tif'),
# ('S046','S046_l17_x191_y1147_z118.tif'),
# ('S047','S047_l14_x223_y1231_z100.tif'),
# ('S048','S048_l17_x198_y1087_z118.tif'),
# ('S049','S049_l15_x191_y1102_z100.tif'),
# ('S050','S050_l110_x1458_y1261_z193.tif'),
# ('S051','S051_l23_x217_y1091_z141.tif'),
# ('S052','S052_l28_x188_y1102_z123.tif'),
# ('S053','S053_l13_x136_y1052_z105.tif'),
# ('S054','S054_l17_x136_y986_z124.tif'),
# ('S055','S055_l7_x178_y1052_z105.tif'),
# ('S056','S056_l24_x205_y1196_z131.tif'),
# ('S057','S057_l8_x249_y1243_z112.tif'),
# ('S058','S058_l18_x151_y952_z131.tif'),
# ('S059','S059_l10_x136_y994_z112.tif'),
# ('S060','S060_l17_x163_y1072_z130.tif'),
# ('S061','S061_l8_x318_y1186_z112.tif'),
# ('S062','S062_l18_x171_y1083_z130.tif'),
# ('S063','S063_l12_x189_y1077_z111.tif'),
# ('S064','S064_l64_x187_y1067_z198.tif'),
# ('S065','S065_l51_x210_y1141_z179.tif'),
# ('S066','S066_l26_x230_y1110_z137.tif'),
# ('S067','S067_l14_x226_y1178_z118.tif'),
# ('S068','S068_l26_x229_y1164_z136.tif'),
# ('S069','S069_l30_x277_y1224_z159.tif'),
# ('S070','S070_l10_x179_y1094_z116.tif'),
# ('S071','S071_l13_x253_y1051_z135.tif'),
# ('S072','S072_l19_x242_y1129_z153.tif'),
# ('S073','S073_l10_x265_y1158_z135.tif'),
# ('S074','S074_l19_x214_y1139_z153.tif'),
# ('S075','S075_l27_x161_y1045_z135.tif'),
# ('S076','S076_l29_x191_y1050_z153.tif'),
# ('S077','S077_l26_x196_y1098_z135.tif'),
# ('S078','S078_l25_x186_y1058_z153.tif'),
# ('S079','S079_l23_x168_y1088_z135.tif'),
# ('S080','S080_l26_x192_y1087_z153.tif'),
# ('S081','S081_l4_x238_y1037_z99.tif'),
# ('S082','S082_l11_x173_y1084_z118.tif'),
# ('S083','S083_l7_x137_y1041_z84.tif'),
# ('S084','S084_l12_x168_y1069_z102.tif'),
# ('S085','S085_l9_x212_y1137_z84.tif'),
# ('S086','S086_l12_x190_y1072_z120.tif'),
# ('S087','S087_l20_x242_y1157_z172.tif'),
# ('S088','S088_l9_x234_y1182_z98.tif'),
# ('S089','S089_l7_x232_y1147_z90.tif'),
# ('S090','S090_l16_x130_y1008_z122.tif'),
# ('S091','S091_l11_x219_y1049_z103.tif'),
# ('S092','S092_l35_x166_y993_z147.tif'),
# ('S093','S093_l12_x231_y1090_z100.tif'),
# ('S094','S094_l28_x187_y1021_z119.tif'),
# ('S095','S095_l13_x186_y1136_z101.tif'),
# ('S096','S096_l28_x152_y1051_z119.tif'),
# ('S097','S097_l15_x215_y1111_z119.tif'),
# ('S098','S098_l9_x196_y1091_z126.tif'),
# ('S099','S099_l14_x133_y1048_z107.tif'),
# ('S100','S100_l14_x187_y1105_z125.tif'),
# ('S101','S101_l11_x195_y1070_z107.tif'),
# ('S102','S102_l11_x159_y1064_z127.tif'),
# ('S103','S103_l7_x147_y1038_z108.tif'),
# ('S104','S104_l12_x145_y1009_z135.tif'),
# ('S105','S105_l13_x192_y1091_z117.tif'),
# ('S106','S106_l17_x114_y961_z135.tif'),
# ('S107','S107_l14_x131_y1026_z142.tif'),
# ('S108','S108_l16_x137_y990_z160.tif'),
# ('S109','S109_l10_x194_y1053_z142.tif'),
# ('S110','S110_l20_x117_y948_z160.tif'),
# ('S111','S111_l20_x173_y1043_z141.tif'),
# ('S112','S112_l14_x190_y1089_z160.tif'),
# ('S113','S113_l12_x133_y976_z142.tif'),
# ('S114','S114_l10_x146_y1006_z160.tif'),
# ('S115','S115_l9_x191_y1036_z142.tif'),
# ('S116','S116_l12_x179_y1000_z160.tif'),
# ('S117','S117_l12_x174_y1066_z142.tif'),
# ('S118','S118_l14_x103_y917_z160.tif'),
# ('S119','S119_l23_x128_y947_z167.tif'),
# ('S120','S120_l18_x199_y1099_z158.tif'),
# ('S121','S121_l16_x173_y1056_z140.tif'),
# ('S122','S122_l16_x179_y1052_z125.tif'),
# ('S123','S123_l10_x227_y1218_z108.tif'),
# ('S124','S124_l15_x223_y1106_z126.tif'),
# ('S125','S125_l7_x229_y1067_z107.tif'),
# ('S126','S126_l12_x169_y1069_z126.tif'),
# ('S127','S127_l11_x177_y980_z107.tif'),
# ('S128','S128_l13_x157_y985_z126.tif'),
# ('S129','S129_l9_x196_y950_z95.tif'),
# ('S130','S130_l9_x179_y1092_z135.tif'),
# ('S131','S131_l12_x218_y1094_z132.tif'),
# ('S132','S132_l18_x205_y1126_z151.tif'),
# ('S133','S133_l12_x236_y1125_z108.tif'),
# ('S134','S134_l13_x167_y1053_z125.tif'),
# ('S135','S135_l14_x153_y1019_z107.tif'),
# ('S136','S136_l18_x207_y1110_z125.tif'),
# ('S137','S137_l4_x513_y195_z90.tif'),
# ('S138','S138_l10_x203_y1047_z135.tif'),
# ('S139','S139_l10_x163_y1029_z116.tif'),
# ('S140','S140_l8_x179_y1048_z134.tif'),
# ('S141','S141_l11_x206_y1177_z117.tif'),
# ('S142','S142_l13_x151_y1045_z134.tif'),
# ('S143','S143_l8_x182_y1058_z116.tif'),
# ('S144','S144_l16_x156_y1030_z135.tif'),
# ('S145','S145_l12_x133_y1028_z116.tif'),
# ('S146','S146_l16_x168_y1083_z134.tif'),
# ('S147','S147_l10_x619_y116_z115.tif'),
# ('S148','S148_l9_x240_y1141_z135.tif'),
# ('S149','S149_l3_x164_y1049_z94.tif'),
# ('S150','S150_l6_x156_y1014_z112.tif'),
# ('S151','S151_l5_x254_y1197_z95.tif'),
# ('S152','S152_l10_x207_y1124_z149.tif'),
# ('S153','S153_l5_x263_y1159_z131.tif'),
# ('S154','S154_l11_x169_y1045_z150.tif'),
# ('S155','S155_l14_x154_y993_z131.tif'),
# ('S156','S156_l18_x205_y1066_z149.tif'),
# ('S157','S157_l16_x181_y1061_z131.tif'),
# ('S158','S158_l22_x193_y1088_z149.tif'),
# ('S159','S159_l15_x200_y1093_z131.tif'),
# ('S160','S160_l25_x182_y1057_z149.tif'),
# ('S161','S161_l14_x122_y950_z131.tif'),
# ('S162','S162_l24_x214_y1066_z149.tif'),
# ('S163','S163_l9_x211_y1061_z138.tif'),
# ('S164','S164_l21_x205_y1142_z157.tif'),
# ('S165','S165_l30_x140_y1021_z192.tif'),
# ('S166','S166_l14_x212_y1154_z152.tif'),
# ('S167','S167_l8_x146_y1042_z134.tif'),
# ('S168','S168_l17_x170_y1073_z152.tif'),
# ('S169','S169_l7_x220_y1102_z134.tif'),
# ('S170','S170_l13_x157_y1034_z152.tif'),
# ('S171','S171_l15_x180_y1085_z134.tif'),
# ('S172','S172_l23_x234_y1161_z174.tif'),
# ('S173','S173_l17_x236_y1032_z173.tif'),
# ('S174','S174_l31_x159_y1019_z192.tif'),
# ('S175','S175_l11_x239_y1156_z135.tif'),
# ('S176','S176_l18_x185_y1096_z153.tif'),
# ('S177','S177_l9_x175_y1087_z133.tif'),
# ('S178','S178_l15_x227_y1122_z152.tif'),
# ('S179','S179_l16_x202_y1092_z173.tif'),
# ('S180','S180_l12_x125_y1004_z136.tif'),
# ('S181','S181_l18_x223_y1156_z145.tif'),
# ('S182','S182_l23_x186_y1071_z163.tif'),
# ('S183','S183_l13_x214_y1108_z145.tif'),
# ('S184','S184_l19_x221_y1166_z143.tif'),
# ('S185','S185_l10_x190_y1110_z151.tif'),
# ('S186','S186_l26_x136_y1011_z169.tif'),
# ('S187','S187_l11_x195_y1095_z123.tif'),
# ('S188','S188_l17_x150_y1073_z141.tif'),
# ('S189','S189_l9_x167_y1012_z124.tif'),
# ('S190','S190_l17_x155_y1086_z143.tif'),
# ('S191','S191_l8_x225_y1130_z124.tif'),
# ('S192','S192_l18_x205_y1086_z165.tif'),
# ('S193','S193_l10_x167_y1043_z119.tif'),
# ('S194','S194_l15_x173_y1032_z137.tif'),
# ('S195','S195_l8_x161_y1126_z119.tif'),
# ('S196','S196_l28_x150_y1048_z170.tif'),
# ('S197','S197_l5_x178_y1111_z115.tif'),
# ('S198','S198_l14_x153_y1087_z133.tif'),
# ('S199','S199_l10_x205_y1107_z114.tif'),
# ('S200','S200_l19_x139_y1010_z143.tif'),
# ('S201','S201_l13_x145_y1055_z125.tif'),
# ('S202','S202_l19_x186_y1097_z143.tif'),
# ('S203','S203_l11_x169_y1030_z141.tif'),
# ('S204','S204_l18_x119_y943_z159.tif'),
# ('S205','S205_l11_x200_y1138_z141.tif'),
# ('S206','S206_l19_x164_y1058_z159.tif'),
# ('S207','S207_l10_x150_y1036_z141.tif'),
# ('S208','S208_l17_x181_y1089_z159.tif'),
# ('S209','S209_l6_x158_y1082_z115.tif'),
# ('S210','S210_l16_x160_y1073_z133.tif'),
# ('S211','S211_l6_x193_y1119_z115.tif'),
# ('S212','S212_l14_x137_y993_z133.tif'),
# ('S213','S213_l3_x160_y1056_z115.tif'),
# ('S214','S214_l14_x187_y1092_z133.tif'),
# ('S215','S215_l15_x167_y1054_z174.tif'),
# ('S216','S216_l26_x158_y1049_z192.tif'),
# ('S217','S217_l5_x105_y995_z104.tif'),
# ('S218','S218_l12_x179_y1083_z122.tif'),
# ('S219','S219_l5_x161_y1031_z106.tif'),
# ('S220','S220_l10_x225_y1163_z125.tif'),
# ('S221','S221_l4_x134_y1016_z106.tif'),
# ('S222','S222_l16_x165_y1033_z125.tif'),
# ('S223','S223_l7_x188_y1098_z106.tif'),
# ('S224','S224_l8_x107_y966_z124.tif'),
# ]


files = ['S010','S011','S012','S013','S014','S015','S016','S017','S018','S019']

import numpy as np
from matplotlib import pyplot as plt
import tifffile as tf
from math import log
import importlib
from unionfind import neoneopersistence
sname = 'S017'
C = None

for sname in files:
    print('---------')
    print('> starting with ',sname)
    img = tf.imread('../'+sname+'.tif')
    hist,bins = np.histogram(img,bins=256,range=(0,256))
    tot = img.size
    # hist[0] = 0
    # blur = [sum(hist[i+j]*a if 0<=i+j<len(hist) else 0 for j,a in kernel) for i in range(len(hist))]
    # btot = sum(blur)

    cumul = []
    s = 0
    for v in hist:
        s += v
        cumul.append(s)

    pers = sorted(neoneopersistence(hist),reverse=True)
    print(sname,': pers',pers)

    if not C:
        p0,p1,p2 = pers[:3]
        x0,x1,x2 = p0[2],p1[2],p2[2]
        anchors = [cumul[x0]/tot,cumul[x1]/tot,cumul[x2]/tot]
    else:
        x = np.array([1.0,2.0,3.0])
        for i,a in enumerate(anchors):
            for j,s in enumerate(cumul):
                if s>a*tot:
                    print('[',i,',',j,']: ',s,'>',a,'*',tot,'=',a*tot)
                    break
            if j > 0:
                x[i] = j-1+(a*tot-cumul[j-1])/(cumul[j]-cumul[j-1])
            else:
                x[i] = 0
    if not C:
        C = 1
        y = np.array([x0,x1,x2])
        plt.axvline(y[0])
        plt.axvline(y[1])
        plt.axvline(y[2])
        plt.plot([b for b in bins[:-1]],[log(h+1) for h in hist], label = sname)
    else:
        npz = np.polyfit(x,y,2)
        print(sname,': npz = ', npz)
        plt.plot([npz[0]*b*b + npz[1]*b + npz[2] for b in bins[:-1]],[log(h+1) for h in hist], label = sname)
    # plt.plot([X0+(b-x0)*(X1-X0)/(x1-x0) for b in bins[:-1]],[h*(x1-x0)/(X1-X0)/tot for h in hist])
    # plt.plot([m*x+b for x in bins[:-1]],[math.log(h+1) for h in hist], label=sname)
    # plt.plot([X0+(b-x0)*(X1-X0)/(x1-x0) for b in bins[:-1]],[h/tot for h in cumul])

plt.legend(bbox_to_anchor=(1.03,1.),loc=2,borderaxespad=0.)
plt.show()
