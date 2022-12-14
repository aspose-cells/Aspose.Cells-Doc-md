---
title: 创建工作簿和工作表范围命名范围
linktitle: 命名范围
type: docs
weight: 40
url: /zh/net/create-workbook-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}} 

Microsoft Excel 允许用户定义具有两个不同范围的命名范围：工作簿（也称为全局范围）和工作表。

- 只需使用其名称，即可从该工作簿中的任何工作表访问具有工作簿范围的命名范围。
- 使用创建它的特定工作表的引用访问工作表范围内的命名范围。

Aspose.Cells 提供与 Microsoft Excel 相同的功能，用于添加工作簿和工作表范围内的命名范围。创建工作表范围的命名范围时，应在命名范围内使用工作表引用以将其指定为工作表范围的命名范围。

{{% /alert %}} 
## **添加带工作簿作用域的命名范围**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **添加具有工作表范围的命名范围**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **推进主题**
- [创建访问和复制命名范围](/cells/zh/net/create-access-and-copy-named-ranges/)
- [格式化和修改命名范围](/cells/zh/net/format-and-modify-named-ranges/)
- [使用外部链接获取范围](/cells/zh/net/get-range-with-external-links/)
- [实现非顺序范围](/cells/zh/net/implementing-non-sequential-ranges/)
