---
title: 在Aspose.Cells中使用自定义XML部件
type: docs
weight: 390
url: /zh/net/use-custom-xml-parts-in-aspose-cells/
---

## 在Aspose.Cells中使用自定义XML部件

自定义XML部件是由不同应用程序（如SharePoint等）存储在Excel文件中的XML数据。这些数据由需要的不同应用程序使用。Microsoft Excel不使用此数据，因此没有GUI来添加它。您可以通过将**.xlsx**的扩展名更改为**.zip**，然后使用**WinZip**打开它来查看此数据。您还可以使用任何第三方Windows zip实用程序（如WinRAR或WinZip等）打开ZIP文件。数据位于**customXml**文件夹中。

您可以通过[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)方法向Aspose.Cells添加自定义XML部件。

以下示例代码利用[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)方法并添加了**Book Catalog XML**，其名称为**BookStore**。以下图像显示了此代码的结果。正如您所看到的，Book Catalog XML添加在BookStore节点内，该节点是此属性的名称。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## 使用自定义XML部件的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## 相关文章

- [在文档信息面板中可见的自定义属性](/cells/zh/net/adding-custom-properties-visible-inside-document-information-panel/)
