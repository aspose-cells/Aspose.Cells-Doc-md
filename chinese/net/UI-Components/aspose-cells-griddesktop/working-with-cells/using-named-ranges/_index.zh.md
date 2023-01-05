---
title: 使用命名范围
type: docs
weight: 110
url: /zh/net/using-named-ranges/
---
{{% alert color="primary" %}} 

通常，您使用工作表上的列和行标签来引用这些列和行中的单元格。但是您可以创建描述性名称来表示单元格、单元格区域、公式或常量值。这个单词**姓名**可以指表示单元格、单元格范围、公式或常量值的字符串。例如，使用易于理解的名称（例如 Products）来指代难以理解的范围，例如 Sales!C20:C30 来表示单元格、单元格区域、公式或常量值。标签可用于引用同一工作表上数据的公式中；如果你想在另一个工作表上表示一个范围，你可以使用一个名称。**命名范围**是 Microsoft 最强大的功能之一。用户可以为命名范围指定一个名称，以便可以在公式中使用其名称引用该单元格范围。**Aspose.Cells.GridDesktop**确实支持此功能。

{{% /alert %}} 
## **在公式中添加/引用命名范围**
GridDesktop 控件确实支持在 Excel 文件中导入/导出命名范围，它提供了两个类（**姓名**和**姓名收藏**以使用命名范围。

以下代码片段将帮助您如何使用它们。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
