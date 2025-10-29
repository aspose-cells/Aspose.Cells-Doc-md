---
title: 将Excel转换为Python数据
type: docs
weight: 30
url: /zh/python-net/convert-excel-to-list/
description: 通过Aspose.Cells for Python via .NET API将Excel转换为列表。
keywords: 使用Aspose.Cells for Python via .NET API，您可以将工作簿、工作表、区域、行、列和其他Excel数据转换为Python列表。
---

{{% alert color="primary" %}}

使用Aspose.Cells for Python via .NET API，您可以将工作簿、工作表、区域、行、列和其他Excel数据转换为Python列表。

{{% /alert %}}

## **如何将Excel工作簿转换为字典**
以下是一个示例代码片段，演示了如何使用Aspose.Cells for Python via .NET将Excel数据导出为字典：
1. 加载[样本文件](sample_data.xlsx)。
1.遍历所有工作表，使用Aspose.Cells for Python Excel库将工作簿转换为字典。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

输出结果：
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **如何将Excel工作簿转换为列表**
以下是一个示例代码片段，演示了如何使用Aspose.Cells for Python将Excel数据导出到列表中via .NET:
1. 加载[样本文件](sample_data.xlsx)。
1. 遍历所有工作表，并使用Aspose.Cells for Python Excel库将工作簿转换为列表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

输出结果：
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **如何将工作表转换为列表**
以下是一个示例代码片段，演示了如何使用Aspose.Cells for Python将工作表数据导出到列表中via .NET:
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 使用Aspose.Cells for Python Excel库将工作表数据转换为列表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

输出结果：
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **如何将Excel的ListObject转换为列表**
以下是一个示例代码片段，演示了如何使用Aspose.Cells for Python将ListObject数据导出到列表中via .NET:
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 创建ListObject对象。
1. 使用Aspose.Cells for Python Excel库将ListObject数据转换为列表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

输出结果：
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **如何将Excel的行转换为列表**
以下是一个示例代码片段，演示了如何使用Aspose.Cells for Python将行数据导出到列表中via .NET:
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 通过行索引获取行对象。
1. 使用Aspose.Cells for Python Excel库将行数据转换为列表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

输出结果：
```
['Detroit', 'Central', 3074]
```

## **如何将Excel列转换为列表**
以下是一个代码片段示例，演示如何使用Aspose.Cells for Python via .NET将列数据导出为列表：
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 通过列索引获取列对象。
1. 使用Aspose.Cells for Python Excel库将列数据转换为列表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

输出结果：
```
['Store', 3055, 3036, 3074]
```

## **如何将Excel范围转换为列表**
以下是一个代码片段示例，演示如何使用Aspose.Cells for Python via .NET将范围数据导出为列表：
1. 加载[样本文件](sample_data.xlsx)。
1. 获取第一个工作表。
1. 创建范围。
1. 使用Aspose.Cells for Python Excel库将范围数据转换为列表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

输出结果：
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
{{< app/cells/assistant language="python-net" >}}
