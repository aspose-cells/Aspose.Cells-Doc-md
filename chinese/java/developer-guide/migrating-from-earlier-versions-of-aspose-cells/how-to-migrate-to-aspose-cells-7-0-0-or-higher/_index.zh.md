---
title: 如何迁移到Aspose.Cells 7.0.0或更高版本
type: docs
weight: 10
url: /zh/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

在本文中，我们分享了Aspose.Cells for Java 7.0.0及更高版本中API的显著变化，与Aspose.Cells for Java之前的版本相比。本文将帮助用户通过理解所做的更改并在其应用程序中执行这些更改来快速从旧API迁移到新API。

{{% /alert %}}

## **现有用户的显著变化**

自Aspose.Cells for Java v7.0.0发布以来，我们在API中进行了一些重大修改，并添加了截至目前为止在Aspose.Cells for .NET中存在的所有功能。因此，现在Aspose.Cells for Java和.NET在功能上甚至在方法和属性名称上都是可以比较的。

与旧方法类似，您现在只需在应用程序中导入一条导入语句即可获取所有类、接口等。

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

我们重新命名了某些API集，以清理API结构，使其与Aspose.Cells for .NET匹配。我们现在添加了一些集合类，并用现有的集合类替换了它们。例如，Worksheets类已替换为**WorksheetCollection**。同样，Shapes类已替换为**ShapeCollection**。然而，类的功能没有受到影响，而是增强了。

如果您希望迁移到新的API，则可能需要进行以下更改，以使在您的应用程序中使其正常工作。以下列表包含类及其相应方法的更改。

## **API更改摘要**

1) 在v2.5.4或更早版本中名称以's'结尾的集合已重命名。在v7.0.0或更高版本中，Collection的名称为：
例如，Shapes（旧）-> ShapeCollection（新），Worksheets（旧）-> WorksheetCollection（新），…等。

2) 更改从集合中获取元素。例如，在v2.5.4或之前，我们通常会使用getXXX(int)，在v7.0.0或更高版本中，我们现在将其改为get(int)：
例如，Worksheets.getSheet(int) (旧) -> WorksheetCollection.get(int) (新)，...等。

3) 获取一个集合的大小（元素数量）已更改。在v2.5.4或更早版本中，我们使用size()，在v7.0.0或更高版本中，现在我们使用getCount()：
Worksheets.size() (旧) -> WorksheetCollection.getCount() (新)，...等。

4) 在v2.5.4或更早版本中，以'is'开头的布尔属性的获取方法已更改。在v7.0.0中，这些以'get'开头。
例如，PageSetup.isBlackAndWhite() (旧) -> PageSetup.getBlackAndWhite() (新)，...等。
