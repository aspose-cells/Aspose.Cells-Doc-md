---
title: 创建工作簿（全局）和工作表范围的命名区域
type: docs
weight: 10
url: /zh/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel 允许用户定义具有两种不同范围（工作簿（也称为全局范围）和工作表）的命名范围。

- 具有工作簿范围的命名范围可以通过简单地使用其名称从工作簿内的任何工作表中访问。
- 具有工作表范围的命名范围是通过在其创建的特定工作表的引用中访问的。

Aspose.Cells 提供了与 Microsoft Excel 相同的功能，用于添加工作簿和工作表范围的命名范围。创建工作表范围的命名范围时，应使用工作表引用来将其指定为工作表范围的命名范围。

{{% /alert %}}

以下代码示例展示了如何通过使用 [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) 类来创建工作簿和工作表范围的名称区域。

## **添加具有工作簿范围的命名区域**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **使用工作表范围添加命名范围**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
{{< app/cells/assistant language="java" >}}
