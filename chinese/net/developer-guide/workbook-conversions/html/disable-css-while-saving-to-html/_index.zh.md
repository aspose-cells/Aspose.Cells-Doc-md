---
title: 禁用CSS在保存为HTML时
type: docs
weight: 320
url: /zh/net/disable-css-while-saving-to-html/
---

## **可能的使用场景**

当将Excel文件保存为单页HTML时，通常CSS元素会嵌入到HTML文件中，并位于HEAD部分。如果将此文件作为电子邮件的内容/正文附件，大多数电子邮件客户端会剥离CSS元素，导致渲染不正常。Aspose.Cells 24.12版本引入了一个选项，可以选择性地禁用CSS，允许将样式直接应用于HTML元素本身。如果希望将HTML设置为电子邮件的内容/正文，请使用 [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss) 属性并将其设置为**true**。



## ** 禁用CSS在保存为HTML时**

以下示例代码展示了 [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss) 属性的用法。 



## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-DisableCss-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
