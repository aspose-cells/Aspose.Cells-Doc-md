---
title: 通过Aspose.Cells在输出PDF中呈现Unicode补充字符
type: docs
weight: 690
url: /zh/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

普通的Unicode字符长为2个字节，而Unicode补充字符长为4个字节。Aspose.Cells现在支持呈现这些4字节Unicode字符。

在Unicode字符标准中，补充字符是指分配的代码点范围从U+10000到U+10FFFF。换句话说，这些是大于U+FFFF的Unicode字符。

- 在UTF-8中，这些字符每个都是4个字节长。
- 在UTF-16中，这些字符需要2个代理对（16位单位）。

{{% /alert %}} 
## **通过Aspose.Cells在输出PDF中呈现Unicode补充字符**
以下屏幕截图显示了Aspose.Cells如何将[源Excel文件](5473390.xlsx)呈现为[输出PDF](5473391.pdf)。您可以看到所有三个Unicode补充字符都与Microsoft Excel所做的完全相同。

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

您可以使用此样本代码将[源Excel文件](5473390.xlsx)转换为[输出PDF](5473391.pdf)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
