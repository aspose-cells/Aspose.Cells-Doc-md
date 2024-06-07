---
title: 如何迁移到Aspose.Cells 7.0.0或更高版本
type: docs
weight: 10
url: /zh/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

在本文中，我们分享了Aspose.Cells for Java 7.0.0及更高版本中与Aspose.Cells for Java前身版本相比所做的重要更改。本文将帮助用户通过了解和在应用程序中实施所做的更改，快速从旧API迁移到新API。

{{% /alert %}}

## **现有用户的显著变化**

自Aspose.Cells for Java v7.0.0发布以来，我们对API进行了一些重大修改，并添加了截至目前在Aspose.Cells for .NET中存在的所有功能。因此，现在Aspose.Cells for Java和.NET在功能上甚至在方法和属性名称上都是可比较的。

与较旧的方法类似，您可以在应用程序中仅导入一个导入语句即可获取所有类、接口等。

【**Java**】

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

我们已将某些API的集合重命名以清理API结构，使其与Aspose.Cells for .NET匹配。我们现在添加了一些集合类，并用现有的集合类替换了它们。例如，Worksheets类已替换为**WorksheetCollection**。同样，Shapes类已替换为**ShapeCollection**。但是，类的功能没有受到影响，而是得到了增强。

如果您希望迁移到新的API，则可能需要在应用程序中进行以下更改，以使事情在您的端上正常工作。以下列表包含了类及其相应方法中的更改。

## **API更改摘要**

1） v2.5.4或更早版本中以's'结尾的集合已更名。在v7.0.0或更高版本中，集合被命名为：
例如，Shapes（旧）-> ShapeCollection（新），Worksheets（旧）-> WorksheetCollection（新），...等。

2）从集合获取元素已更改。例如，在v2.5.4或更早版本中，我们通常使用getXXX(int)，在v7.0.0或更高版本中，我们现在使用get(int)：
例如，Worksheets.getSheet(int)（旧）-> WorksheetCollection.get(int)（新），...等。

3）获取一个集合的大小（元素计数）已更改。在v2.5.4或更早版本中，我们使用size()，在v7.0.0或更高版本中，我们现在使用getCount()：
Worksheets.size()（旧）-> WorksheetCollection.getCount()（新），...等。

4）以'is'开头的布尔属性的getter方法在v2.5.4或更早版本中已更改。在v7.0.0中，这些方法以“get”开头：
例如，PageSetup.isBlackAndWhite()（旧）-> PageSetup.getBlackAndWhite()（新），...等。
