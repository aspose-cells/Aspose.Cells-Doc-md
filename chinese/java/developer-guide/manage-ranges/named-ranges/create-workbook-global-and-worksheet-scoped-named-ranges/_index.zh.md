---
title: 创建工作簿（全局）和工作表范围命名范围
type: docs
weight: 10
url: /zh/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft Excel 允许用户定义具有两个不同范围的命名范围：工作簿（也称为全局范围）和工作表。

- 只需使用其名称，即可从该工作簿中的任何工作表访问具有工作簿范围的命名范围。
- 使用创建它的特定工作表的引用访问工作表范围内的命名范围。

Aspose.Cells 提供与 Microsoft Excel 相同的功能，用于添加工作簿和工作表范围内的命名范围。创建工作表范围的命名范围时，应在命名范围内使用工作表引用以将其指定为工作表范围的命名范围。

{{% /alert %}}

以下代码示例展示了如何使用[**范围**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)班级。

## **使用工作簿范围添加命名范围**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **添加具有工作表范围的命名范围**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
