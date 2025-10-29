---
title: 创建工作簿和工作表范围命名范围
linktitle: 命名范围
type: docs
weight: 40
url: /zh/python-net/create-workbook-and-worksheet-scoped-named-ranges/
description: 本文介绍了如何使用Aspose.Cells for Python via .NET API创建工作簿和工作表作用域的命名区域。
keywords: Python Excel 库，Python 创建工作簿和工作表作用域的命名区域，Python 使用工作簿作用域添加命名区域，Python 使用工作表作用域添加命名区域。
---

{{% alert color="primary" %}} 

Microsoft Excel 允许用户定义具有两种不同范围（工作簿（也称为全局范围）和工作表）的命名范围。

- 具有工作簿范围的命名范围可以通过简单地使用其名称从工作簿内的任何工作表中访问。
- 具有工作表范围的命名范围是通过在其创建的特定工作表的引用中访问的。

Aspose.Cells for Python via .NET 提供了与 Microsoft Excel 相同的功能，用于添加工作簿和工作表作用域的命名区域。 在创建工作表作用域的命名区域时，应在命名区域中使用工作表引用以指定其为工作表作用域的命名区域。


{{% /alert %}} 
## **如何添加具有工作簿作用域的命名区域**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.py" >}}
## **如何添加具有工作表作用域的命名区域**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-WorksheetNamedRange-1.py" >}}

## **高级主题**
- [创建访问和复制命名区域](/cells/zh/python-net/create-access-and-copy-named-ranges/)
- [格式和修改命名区域](/cells/zh/python-net/format-and-modify-named-ranges/)
- [获取带有外部链接的范围](/cells/zh/python-net/get-range-with-external-links/)
- [实现非连续范围](/cells/zh/python-net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="python-net" >}}
