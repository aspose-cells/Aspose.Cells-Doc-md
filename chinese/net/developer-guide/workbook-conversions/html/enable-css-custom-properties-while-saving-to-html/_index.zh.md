---
title: 在保存为HTML时启用CSS自定义属性
type: docs
weight: 320
url: /zh/net/enable-css-custom-properties-while-saving-to-html/
---

## **可能的使用场景**

将Excel文件保存为HTML时，如果存在多个基于base64的图片，并且使用了自定义属性，图片数据只需保存一次，从而可以提高生成的HTML性能。保存为HTML时，请使用 [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/EnableCssCustomProperties) 属性并将其设置为**true**。
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **在保存为HTML时启用CSS自定义属性**

以下示例代码展示了 [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/enablecsscustomproperties) 属性的用法。截图显示了未设置为 true 时该属性的效果。请下载此代码所用的[示例Excel文件](50528260.xlsx) 和生成的[输出HTML](50528261.zip) 作为参考。



## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-EnableCssCustomProperties-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
