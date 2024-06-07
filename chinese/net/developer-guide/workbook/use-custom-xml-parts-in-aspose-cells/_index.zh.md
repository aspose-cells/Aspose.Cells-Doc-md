---
title: 在 Aspose.Cells 中使用自定义 XML 部件
type: docs
weight: 390
url: /zh/net/use-custom-xml-parts-in-aspose-cells/
---

## 在 Aspose.Cells 中使用自定义 XML 部件

自定义 XML 部件是由不同应用程序（如 SharePoint 等）存储在 Excel 文件中的 XML 数据。这些数据由需要的不同应用程序消耗。Microsoft Excel 不使用此数据，因此没有 GUI 来添加它。您可以通过更改 **.xlsx** 的扩展名为 **.zip**，然后使用 **WinZip** 打开来查看此数据。您还可以使用任何第三方 Windows 压缩实用程序（如 WinRAR 或 WinZip 等）打开 ZIP 文件。数据存在于 **customXml** 文件夹中。

您可以通过 [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) 方法使用 Aspose.Cells 添加自定义 XML 部件。

以下示例代码使用 [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) 方法，并添加了 **图书目录 XML**，其名称为 **BookStore**。如下图显示此代码的结果。您可以看到，图书目录 XML 添加到了名为 BookStore 的节点内，这是此属性的名称。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## 用于使用自定义 XML 部件的 C# 代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## 相关文章

- [在文档信息面板中显示的添加自定义属性](/cells/zh/net/adding-custom-properties-visible-inside-document-information-panel/)
