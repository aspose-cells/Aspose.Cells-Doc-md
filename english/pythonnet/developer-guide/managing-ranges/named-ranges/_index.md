---
title: Create Workbook and Worksheet Scoped Named Ranges
linktitle: Named Range
type: docs
weight: 40
url: /python-net/create-workbook-and-worksheet-scoped-named-ranges/
description: This article shows how to Create Workbook and Worksheet Scoped Named Ranges by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Create Workbook and Worksheet Scoped Named Ranges, Python Add a Named Range with Workbook Scoped, Python Add a Named Range with Worksheet Scope.
---

{{% alert color="primary" %}} 

Microsoft Excel allows users to define named ranges with two different scopes: workbook (also known as global scope) and worksheet.

- Named ranges with a workbook scope can be accessed from any worksheet within that workbook by simply using its name.
- Worksheet scoped named ranges are accessed with the reference of the particular worksheet in which it was created.

Aspose.Cells for Python via .NET provides the same functionality as Microsoft Excel for adding workbook and worksheet scoped named ranges. When creating a worksheet scoped named range, the worksheet reference should be used in the named range to specify it as a worksheet scoped named range.


{{% /alert %}} 
## **How to Add a Named Range with Workbook Scoped**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.py" >}}
## **How to Add a Named Range with Worksheet Scope**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-WorksheetNamedRange-1.py" >}}

## **Advance topics**
- [Create Access and Copy Named Ranges](/cells/python-net/create-access-and-copy-named-ranges/)
- [Format and Modify Named Ranges](/cells/python-net/format-and-modify-named-ranges/)
- [Get Range with External Links](/cells/python-net/get-range-with-external-links/)
- [Implementing Non-Sequential Ranges](/cells/python-net/implementing-non-sequential-ranges/)
