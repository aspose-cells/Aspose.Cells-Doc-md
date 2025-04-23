---
title: 在加载文件时自动调整行高
type: docs
weight: 120
url: /zh/net/autofit-row-height/
description: 了解如何调整行高没有自定义高度。
keywords: 在加载文件时自动调整行高，打开Excel文件时自动调整行高。 
---

## **可能的使用场景**
行高将自动与内容的字体匹配，但是当缓存行的高度与文件中的内容高度不匹配时，MS Excel将在加载文件时自动调整行高，而Aspose.Cells不会自动调整行高以提高性能。如果需要使用Aspose.Cells程序在加载文件时自动匹配行高，可以通过参数[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/)来实现目标。

请参考以下图像数据。我们可以观察到第11行的缓存行高为15，但是Excel在加载文件时会自动调整行高。
<br>
<img src="1.png" width=70% />

## **使用Aspose.Cells调整行高**
如果直接加载文件并将其保存为PDF，那么数据在PDF中将无法完全显示，因为其缓存行高仅为15。
<br>
<img src="2.png" width=70% />
<br>
如果在加载文件时将参数[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/)设置为true，则Aspose.Cells将自动调整行高。调整后的行高可以有效满足文本显示要求。
<br>
<img src="3.png" width=70% />

## **C# 示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
