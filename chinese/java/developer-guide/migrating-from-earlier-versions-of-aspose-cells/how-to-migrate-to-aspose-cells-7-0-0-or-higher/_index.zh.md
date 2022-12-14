---
title: 如何迁移到 Aspose.Cells 7.0.0 或更高版本
type: docs
weight: 10
url: /zh/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---
{{% alert color="primary" %}}

在本文中，我们分享了 Aspose.Cells for Java 7.0.0 及更高版本中的 API 与之前版本的 Aspose.Cells for Java 相比的显着变化。本文将帮助用户快速从旧版本 API 迁移到新版本API 通过了解所做的更改并在其应用程序中执行这些更改。

{{% /alert %}}

## **现有用户的显着变化**

自 Aspose.Cells for Java v7.0.0 发布以来，我们对 API 进行了一些重大修改，并添加了迄今为止 Aspose.Cells for .NET 中存在的所有功能。因此，Aspose.Cells for Java 和 .NET 现在在功能方面甚至在方法和属性名称方面都具有可比性。

与旧方法类似，您只需在应用程序中导入一条导入语句即可获取所有类、接口等。

[**Java**]{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

我们重命名了某些 API 的集合以清理 API 结构以将其与 Aspose.Cells for .NET 匹配。我们现在添加了一些集合类并将它们替换为现有集合类。就像 Worksheets 类已被替换为**工作表集合**.同样，Shapes 类已替换为**形状集合**.但是，这些类的功能并没有受到影响，而是得到了增强。

如果您希望迁移到新的 API，那么您可能需要在您的应用程序中执行以下更改，以使一切正常进行。以下列表包含对类及其各自方法所做的更改。

## **API 变更汇总**

1) v2.5.4 及之前版本名称以's'结尾的集合重命名。在 v7.0.0 或更高版本中，集合被命名为：
例如，Shapes（旧）-> ShapeCollection（新），Worksheets（旧）-> WorksheetCollection（新），...等。

2) 从集合中获取元素已更改。例如，在v2.5.4或之前我们使用getXXX(int)，在v7.0.0或更高版本，现在我们使用get(int)：
例如，Worksheets.getSheet(int)（旧）-> WorksheetCollection.get(int)（新），...等。

3) 更改了获取一个集合的大小（元素数）。在 v2.5.4 或之前，我们使用 size() 来完成，在 v7.0.0 或更高版本中，我们现在使用 getCount() 来完成：
Worksheets.size()（旧）-> WorksheetCollection.getCount()（新），...等。

4) 更改了v2.5.4 及之前以'is' 开头的名称的布尔属性的getter 方法。在 v7.0.0 中，这些以“get”开头：
例如，PageSetup.isBlackAndWhite()（旧）-> PageSetup.getBlackAndWhite()（新），...等。
