# 变量
s = 64 #int
cube_name = "正方体" #str
追踪精度 = 1.001 #float
print("本场景的采样是 %d\n物体是 %s\n采样是 %f"%(s,cube_name,追踪精度))
print(f"本场景的采样是 {s}\n物体是 {cube_name}\n采样是 {追踪精度}")
print(f"本场景的采样是 {0}\n物体是 {1}\n采样是 {2}".format(s,cube_name,追踪精度))



# 强制类型转换，数学运输，if判断
print(type(s),type(cube_name),type(追踪精度))
s_sample = str(s)
print(type(s_sample))
print("iillya"+"_a")
samples = input("input")
samples = int(samples)
print(samples,type(samples))
if samples == 64:
    print(f"你的采样是{samples}")
else:
    print("你的采样不是64")
    pass