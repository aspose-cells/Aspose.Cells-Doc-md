---
title: 在 Aspose.Cells 中使用自定义 XML 部件
type: docs
weight: 390
url: /zh/net/use-custom-xml-parts-in-aspose-cells/
---
## 在 Aspose.Cells 中使用自定义 XML 部件

自定义 XML 部件是由不同应用程序（如 SharePoint 等）存储在 excel 文件中的 XML 数据。此数据由需要它的不同应用程序使用。 Microsoft Excel 不使用此数据，因此没有用于添加它的 GUI。您可以通过更改扩展名来查看此数据**.xlsx**进入**。压缩**然后使用打开它**压缩包**.您还可以使用任何第 3 部分 Windows 压缩实用程序（例如 WinRAR 或 WinZip 等）打开 ZIP 文件。数据位于**自定义XML**文件夹。

您可以使用 Aspose.Cells 通过[**工作簿.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)方法。

下面的示例代码使用了[**工作簿.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)方法并添加**图书目录 XML**它的名字是**书店**.下图显示了这段代码的结果。如您所见，Book Catalog XML 添加到 BookStore 节点中，这是该属性的名称。

![待办事项：图像_替代_文本](use-custom-xml-parts-in-aspose-cells_1.png)

![待办事项：图像_替代_文本](use-custom-xml-parts-in-aspose-cells_2.png)

## C# 使用自定义 XML 部件的代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## 相关文章

- [添加在文档信息面板内可见的自定义属性](/cells/zh/net/adding-custom-properties-visible-inside-document-information-panel/)
