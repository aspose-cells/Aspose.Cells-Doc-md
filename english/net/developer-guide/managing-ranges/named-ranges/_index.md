---
title: Create Workbook and Worksheet Scoped Named Ranges
linktitle: Named Range
type: docs
weight: 40
url: /net/create-workbook-and-worksheet-scoped-named-ranges/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Microsoft Excel allows users to define named ranges with two different scopes: workbook (also known as global scope) and worksheet.

- Named ranges with a workbook scope can be accessed from any worksheet within that workbook by simply using its name.
- Worksheet‑scoped named ranges are accessed with the reference of the particular worksheet in which they were created.

Aspose.Cells provides the same functionality as Microsoft Excel for adding workbook‑ and worksheet‑scoped named ranges. When creating a worksheet‑scoped named range, the worksheet reference should be used in the named range to specify it as a worksheet‑scoped named range.

{{% /alert %}} 
## **Adding a Named Range with Workbook Scope**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **Adding a Named Range with Worksheet Scope**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **Advanced topics**
- [Create Access and Copy Named Ranges](/cells/net/create-access-and-copy-named-ranges/)
- [Format and Modify Named Ranges](/cells/net/format-and-modify-named-ranges/)
- [Get Range with External Links](/cells/net/get-range-with-external-links/)
- [Implementing Non-Sequential Ranges](/cells/net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="csharp" >}}
