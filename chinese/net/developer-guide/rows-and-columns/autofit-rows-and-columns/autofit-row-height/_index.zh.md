---
title: 加载文件时自动调整行高
type: docs
weight: 120
url: /zh/net/autofit-row-height/
description: 了解如何调整未自定义高度的行。
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **可能的使用场景**
行高自动匹配内容的字体，但是当缓存的行高与文件中内容的高度不匹配时，MS Excel在加载文件时会自动调整行高，而Aspose.Cells则不会自动调整它以提高性能。如果需要使用Aspose.Cells程序在加载文件时自动匹配行高，可以通过参数来达到目的[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

请参考以下图像数据。我们可以观察到第11行的缓存行高是15，但是Excel在加载文件时自动调整了行高。
<br>
<img src="1.png" width=70% />

##  **使用 Aspose.Cells 调整行高**
如果直接加载文件并保存到PDF，PDF中的数据将无法完全显示，因为它的缓存行高度只有15。
<br>
<img src="2.png" width=70% />
<br>
如果你设置了参数[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/)加载文件时设置为true，则Aspose.Cells会自动调整行高。调整后的行高可以有效满足文本显示要求。
<br>
<img src="3.png" width=70% />

##  **C# 示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}