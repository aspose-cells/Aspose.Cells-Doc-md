---
title: 将Excel转换为NumPy
type: docs
weight: 30
url: /zh/python-net/convert-excel-to-numpy/
description: 通过使用Aspose.Cells for Python via .NET API将Excel转换为NumPy。
keywords: Python将Excel转换为NumPy数组，在Python中将工作簿导出为NumPy数组via NET，Python将行转换为NumPy数组，Python将表格转换为NumPy数组，在Python中导出ListObject为NumPy数组via NET，使用Python将范围转换为NumPy数组，使用Python将列转换为NumPy数组。
---

## **NumPy简介**
NumPy（Numerical Python）是Python的开源数值计算扩展。该工具可用于存储和处理大型矩阵，比Python的嵌套列表结构效率更高（也可用于表示矩阵）。它支持大量的多维数组和矩阵操作，并为数组操作提供了大量的数学函数库。 

NumPy的主要功能：
1. Ndarray，一个多维数组对象，是一个快速、灵活、节省空间的数据结构。
1. 线性代数操作，包括矩阵乘法、转置、求逆等。
1. 快速傅里叶变换，在数组上执行快速傅里叶变换。
1. 浮点数组的快速操作。
1. 将C语言代码集成到Python中，使其运行速度更快。

使用Aspose.Cells for Python via .NET API，您可以将Excel、TSV、CSV、Json等多种格式转换为Numpy ndarray。

## **将Excel工作簿转换为NumPy ndarray的方法**
以下是一个示例代码片段，演示使用Aspose.Cells for Python via .NET将excel数据导出为NumPy数组的方法：
1. 加载[样本文件](sample_data.xlsx)。
1.遍历excel数据并使用Aspose.Cells for Python via .NET将数据导出为NumPy ndarray。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

输出结果：
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **将工作表转换为NumPy ndarray的方法**
以下是一个示例代码片段，演示使用Aspose.Cells for Python via .NET将工作表数据导出为NumPy ndarray的方法：
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1.使用Aspose.Cells for Python Excel库将工作表数据转换为Numpy ndarray。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

输出结果：
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **如何将Excel的范围转换为NumPy ndarray**
下面是一个示例代码片段，演示如何使用Aspose.Cells for Python via .NET将范围数据导出到NumPy ndarray中：
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 创建范围。
1. 使用Aspose.Cells for Python Excel库将范围数据转换为NumPy ndarray。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

输出结果：
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **如何将Excel的ListObject转换为NumPy ndarray**
下面是一个示例代码片段，演示如何使用Aspose.Cells for Python via .NET将ListObject数据导出为NumPy ndarray：
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 创建ListObject对象。
1. 使用Aspose.Cells for Python Excel库将ListObject数据转换为NumPy ndarray。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

输出结果：
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **如何将Excel的行转换为NumPy ndarray**
下面是一个示例代码片段，演示如何使用Aspose.Cells for Python via .NET将行数据导出为NumPy ndarray：
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 通过行索引获取行对象。
1. 使用Aspose.Cells for Python Excel库将行数据转换为NumPy ndarray。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

输出结果：
```
['Detroit' 'Central' '3074']
```

## **如何将Excel的列转换为NumPy ndarray**
以下是一个示例代码片段，演示如何使用Aspose.Cells for Python将列数据导出为NumPy ndarray via .NET：
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 通过列索引获取列对象。
1. 使用Aspose.Cells for Python Excel库将列数据转换为NumPy ndarray。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

输出结果：
```
['Store' '3055' '3036' '3074']
```
{{< app/cells/assistant language="python-net" >}}
