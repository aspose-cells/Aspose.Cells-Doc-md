---
title: 在 Aspose.Cells 中使用自定义 XML 部件
type: docs
weight: 570
url: /zh/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

自定义 XML 部分是 XML 数据，由不同的应用程序（如 SharePoint 等）存储在 excel 文件中。此数据由需要它的不同应用程序使用。 Microsoft Excel 不使用此数据，因此没有用于添加它的 GUI。您可以通过更改扩展名来查看此数据**.xlsx**进入**。压缩**然后使用打开它**WinRAR** .数据存在于**自定义XML**文件夹，如图所示。

![待办事项：图片_替代_文本](using-custom-xml-parts-in-aspose-cells_1.png)

您可以使用 Aspose.Cells 通过[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)） 方法。

{{% /alert %}} 
## **在 Aspose.Cells 中使用自定义 Xml 部件**
下面的示例代码使用了[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) 方法并添加**图书目录 Xml**它的名字是**书店**.下图显示了这段代码的结果。如您所见，Book Catalog Xml 添加到 BookStore 节点中，这是此属性的名称。

![待办事项：图片_替代_文本](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **相关文章**
{{% alert color="primary" %}} 

- [添加在文档信息面板内可见的自定义属性](/cells/zh/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
