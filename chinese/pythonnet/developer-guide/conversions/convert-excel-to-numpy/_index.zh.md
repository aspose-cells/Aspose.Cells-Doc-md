---
title: 将Excel转换为NumPy
type: docs
weight: 30
url: /zh/python-net/convert-excel-to-numpy/
description: 通过使用Aspose.Cells for Python通过.NET API将Excel转换为NumPy。
keywords: Python将Excel转换为NumPy数组，在Python中通过.NET导出工作簿到NumPy数组，Python将行转换为NumPy数组，Python将表格转换为NumPy数组，在Python中通过.NET导出ListObject到NumPy数组，Python将范围转换为NumPy数组，使用Python将列转换为NumPy数组。
---

## **NumPy简介**
NumPy(数值Python)是Python的一个开源数值计算扩展工具。此工具可用于存储和处理大矩阵，有效率远胜于Python的嵌套列表结构(也可用于表示矩阵)。它支持大量的维数组和矩阵运算，并提供大量数学函数库供数组操作使用。 

NumPy的主要功能:
1. Ndarray，一个多维数组对象，是速度快、灵活、节省空间的数据结构。
1. 线性代数运算，包括矩阵乘法、转置、求逆等。
1. Fourier变换，对数组进行快速傅里叶变换。
1. 浮点数数组的快速操作。
1. 将C语言代码集成到Python中，使其运行更快。

通过Aspose.Cells for Python通过.NET API，您可以将Excel、TSV、CSV、Json等不同格式转换为NumPy数组。

## **如何将Excel工作簿转换为NumPy数组**
以下是一个示例代码片段，演示如何使用Aspose.Cells for Python通过.NET将Excel数据导出为NumPy数组：
1. 加载示例文件。
1. 遍历 Excel 数据并通过 Aspose.Cells for Python 通过 .NET 导出数据到 NumPy 的 ndarray。


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

## **如何将工作表转换为 NumPy ndarray**
以下是一个示例代码片段，演示如何使用 Aspose.Cells for Python 通过 .NET 导出工作表数据至 Numpy ndarray。
1. 加载示例文件。
1. 获取第一个工作表。
1. 使用 Aspose.Cells for Python Excel 库将工作表数据转换为 Numpy 的 ndarray。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

输出结果：
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **如何将 Excel 范围转换为 Numpy ndarray**
以下是一个示例代码片段，演示如何使用 Aspose.Cells for Python 通过 .NET 导出范围数据至 NumPy ndarray。
1. 加载示例文件。
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
以下是一个示例代码片段，演示如何通过.NET使用Aspose.Cells for Python将ListObject数据导出到NumPy ndarray：
1. 加载示例文件。
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
以下是一个示例代码片段，演示如何通过.NET使用Aspose.Cells for Python将行数据导出到NumPy ndarray：
1. 加载示例文件。
1. 获取第一个工作表。
1. 通过行索引获取行对象。
1. 使用Aspose.Cells for Python Excel库将行数据转换为NumPy ndarray。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

输出结果：
```
['Detroit' 'Central' '3074']
```

## **如何将Excel的列转换为NumPy ndarray**
以下是一个示例代码片段，演示如何通过.NET使用Aspose.Cells for Python将列数据导出到NumPy ndarray：
1. 加载示例文件。
1. 获取第一个工作表。
1. 通过列索引获取列对象。
1. 使用Aspose.Cells for Python Excel库将列数据转换为NumPy ndarray。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

输出结果：
```
['Store' '3055' '3036' '3074']
```
