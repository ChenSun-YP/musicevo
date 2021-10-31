import h5py
import numpy as np
import os
import glob

def prt(name):
  print(name)


# we define this very useful function to iterate the files
def apply_to_all_files(basedir, func=lambda x: x, ext='.h5'):
  """
  From a base directory, go through all subdirectories,
  find all files with the given extension, apply the
  given function 'func' to all of them.
  If no 'func' is passed, we do nothing except counting.
  INPUT
     basedir  - base directory of the dataset
     func     - function to apply to all filenames
     ext      - extension, .h5 by default
  RETURN
     number of files
  """
  cnt = 0
  # iterate over all files in all subdirectories
  for root, dirs, files in os.walk(basedir):
    files = glob.glob(os.path.join(root, '*' + ext))
    # count files
    cnt += len(files)
    # apply function to all files
    for f in files:
      func(f)
  return cnt

if __name__ == '__main__':
  with h5py.File('MillionSongSubset/A/A/A/TRAAAAW128F429D538.h5', 'r') as f:
    f.visit(prt)
    print(f['analysis/bars_start'])
    st = np.array(f['analysis/bars_start'])
    print(st)
    # 
    # for key in f.keys():
    #   # print(f[key],key,f[key].name)
    #   for item in f[key]:
    #     print(f['/analysis/'])
  print(apply_to_all_files('MillionSongSubset/'))

# # -*- coding: utf-8 -*-
# #打开文件
# f = h5py.File('MillionSongSubset/A/A/A/TRAAAAW128F429D538.h5','r')
# #遍历文件中的一级组
# for group in f.keys():
#     print (group)
#     #根据一级组名获得其下面的组
#     group_read = f[group]
#     #遍历该一级组下面的子组
#     for subgroup in group_read.keys():
#         print (subgroup)     
#         #根据一级组和二级组名获取其下面的dataset          
#         dset_read = f[group+'/'+subgroup]                           
#         #遍历该子组下所有的dataset
#         # for dset in dset_read.keys():
#         #     #获取dataset数据
#         #     dset1 = f[group+'/'+subgroup+'/'+dset]
#         #     for dset2 in dset1.keys():
#         #       # 获取dataset数据
#         #       dset2 = f[group + '/' + subgroup + '/' + dset1+ '/' + dset2]
#             
#             
#             
# 
#         print (dset2.name)
#         data = np.array(dset1)
#         print (data.shape)
#         x = data[...,0]
#         y = data[...,1]
