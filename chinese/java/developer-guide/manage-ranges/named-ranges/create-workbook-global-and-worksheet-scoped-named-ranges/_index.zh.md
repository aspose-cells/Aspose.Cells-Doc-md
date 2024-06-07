---
title: 创建全局工作簿和工作表级别的命名范围
type: docs
weight: 10
url: /zh/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel允许用户定义具有两种不同范围作用域（工作簿和工作表）的命名范围。

- 具有工作簿范围的命名范围可以通过简单地使用其名称在该工作簿中的任何工作表中访问。
- 使用特定工作表的引用访问具有工作表范围的命名范围，该命名范围是在其中创建的特定工作表。

Aspose.Cells提供了与Microsoft Excel相同的功能，用于添加具有工作簿和工作表范围的命名范围。创建工作表范围的命名范围时，应使用工作表引用以将其指定为工作表范围的命名范围。

{{% /alert %}}

以下代码示例展示了如何使用[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)类创建工作簿和工作表范围命名。

## **使用工作簿范围添加命名范围**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **添加具有工作表范围的命名范围**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
