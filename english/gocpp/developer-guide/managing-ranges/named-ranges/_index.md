---
title: Create Workbook and Worksheet Scoped Named Ranges with Golang via C++
linktitle: Named Range
type: docs
weight: 40
url: /go-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Learn how to create workbook- and worksheet-scoped named ranges with Go via C++ using Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel allows users to define named ranges with two different scopes: workbook (also known as global scope) and worksheet.

- Named ranges with a workbook scope can be accessed from any worksheet within that workbook by simply using its name.
- Worksheet-scoped named ranges are accessed using the reference of the particular worksheet in which they were created.

Aspose.Cells provides the same functionality as Microsoft Excel for adding workbook- and worksheet-scoped named ranges. When creating a worksheet‑scoped named range, the worksheet reference should be used to specify that it is worksheet‑scoped.

{{% /alert %}} 

## **Adding a Named Range with Workbook Scope**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges.go" >}}
## **Adding a Named Range with Worksheet Scope**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges-1.go" >}}
## **Advanced Topics**
- [Create Access and Copy Named Ranges](/cells/cpp/create-access-and-copy-named-ranges/)
- [Format and Modify Named Ranges](/cells/cpp/format-and-modify-named-ranges/)
- [Get Range with External Links](/cells/cpp/get-range-with-external-links/)
- [Implementing Non-Sequential Ranges](/cells/cpp/implementing-non-sequential-ranges/)