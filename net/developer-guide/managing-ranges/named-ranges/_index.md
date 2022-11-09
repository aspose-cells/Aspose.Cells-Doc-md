---
title: Create Workbook and Worksheet Scoped Named Ranges
linktitle: Named Range
type: docs
weight: 40
url: /net/create-workbook-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}} 

Microsoft Excel allows users to define named ranges with two different scopes: workbook (also known as global scope) and worksheet.

- Named ranges with a workbook scope can be accessed from any worksheet within that workbook by simply using its name.
- Worksheet scoped named ranges are accessed with the reference of the particular worksheet in which it was created.

Aspose.Cells provides the same functionality as Microsoft Excel for adding workbook and worksheet scoped named ranges. When creating a worksheet scoped named range, the worksheet reference should be used in the named range to specify it as a worksheet scoped named range.

{{% /alert %}} 
## **Adding a Named Range with Workbook Scoped**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **Adding a Named Range with Worksheet Scope**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}
