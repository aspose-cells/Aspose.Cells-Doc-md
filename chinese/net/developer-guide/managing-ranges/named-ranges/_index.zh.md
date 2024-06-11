---
title: 创建工作簿和工作表范围命名范围
linktitle: 命名范围
type: docs
weight: 40
url: /zh/net/create-workbook-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}} 

Microsoft Excel 允许用户定义具有两种不同范围（工作簿（也称为全局范围）和工作表）的命名范围。

- 具有工作簿范围的命名范围可以通过简单地使用其名称从工作簿内的任何工作表中访问。
- 具有工作表范围的命名范围是通过在其创建的特定工作表的引用中访问的。

Aspose.Cells 提供了与 Microsoft Excel 相同的功能，用于添加工作簿和工作表范围的命名范围。创建工作表范围的命名范围时，应使用工作表引用来将其指定为工作表范围的命名范围。

{{% /alert %}} 
## **使用工作簿范围添加命名范围**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **使用工作表范围添加命名范围**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **高级主题**
- [创建访问和复制命名区域](/cells/zh/net/create-access-and-copy-named-ranges/)
- [格式和修改命名区域](/cells/zh/net/format-and-modify-named-ranges/)
- [获取带有外部链接的范围](/cells/zh/net/get-range-with-external-links/)
- [实现非连续范围](/cells/zh/net/implementing-non-sequential-ranges/)
