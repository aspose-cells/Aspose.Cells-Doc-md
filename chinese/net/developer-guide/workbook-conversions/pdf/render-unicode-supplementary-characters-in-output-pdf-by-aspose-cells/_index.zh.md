---
title: 通过Aspose.Cells在输出PDF中呈现Unicode补充字符
type: docs
weight: 350
url: /zh/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}}

普通的Unicode字符长为2个字节，而Unicode补充字符长为4个字节。Aspose.Cells现在支持呈现这些4字节Unicode字符。

在Unicode字符标准中，补充字符是指分配的代码点范围从U+10000到U+10FFFF。换句话说，这些是大于U+FFFF的Unicode字符。

- 在UTF-8中，这些字符每个都是4个字节长。
- 在UTF-16中，这些字符需要2个代理对（16位单位）。

{{% /alert %}}

## 通过Aspose.Cells在输出PDF中渲染Unicode补充字符

以下屏幕截图显示了Aspose.Cells如何将[源Excel文件](5115563.xlsx)渲染成[输出PDF](5115564.pdf)。您可以看到，所有三个Unicode补充字符都与由Microsoft Excel执行的渲染完全相同。

![todo:image_alt_text](output.png)

## 示例代码

您可以使用此示例代码将[源Excel文件](5115563.xlsx)转换为[输出PDF](5115564.pdf)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
{{< app/cells/assistant language="csharp" >}}
