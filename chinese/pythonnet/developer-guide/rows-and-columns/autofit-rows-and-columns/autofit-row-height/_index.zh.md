---
title: 在加载文件时自动调整行高
type: docs
weight: 120
url: /zh/python-net/autofit-row-height/
description: 学习如何通过Aspose.Cells for Python via .NET API调整未自定义高度的行。
keywords: Python Excel库，Python在加载文件时自动调整行高，Python在打开Excel文件时自动调整行高。 
---

## **可能的使用场景**
行的高度会自动匹配内容的字体，但是当缓存行的高度不匹配文件中内容的高度时，MS Excel在加载文件时会自动调整行高，而Aspose.Cells for Python via .NET为了提高性能不会自动调整。如果需要在加载文件时使用Aspose.Cells for Python via .NET程序自动匹配行高，可以通过参数[LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/)来实现这一目标。

请参考以下图像数据。我们可以观察到第11行的缓存行高为15，但是Excel在加载文件时会自动调整行高。
<br>
<img src="1.png" width=70% />

## **使用Aspose.Cells for Python Excel库调整行高**
如果直接加载文件并将其保存为PDF，那么数据在PDF中将无法完全显示，因为其缓存行高仅为15。
<br>
<img src="2.png" width=70% />
<br>
如果在加载文件时将参数[LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/)设置为true，那么Aspose.Cells for Python via .NET将自动调整行高。调整后的行高可以有效满足文本显示的要求。
<br>
<img src="3.png" width=70% />

## **Python示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
{{< app/cells/assistant language="python-net" >}}
