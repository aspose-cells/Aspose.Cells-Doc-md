---
title: Create Workbook (Global) and Worksheet Scoped Named Ranges
type: docs
weight: 10
url: /java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel allows users to define named ranges with two different scopes: workbook (also known as global scope) and worksheet.

- Named ranges with a workbook scope can be accessed from any worksheet within that workbook by simply using its name.
- Worksheet scoped named ranges are accessed with the reference of the particular worksheet in which it was created.

Aspose.Cells provides the same functionality as Microsoft Excel for adding workbook and worksheet scoped named ranges. When creating a worksheet scoped named range, the worksheet reference should be used in the named range to specify it as a worksheet scoped named range.

{{% /alert %}}

The following code samples show how to create workbook and worksheet scoped name ranges by using the [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) class.

## **Adding a Named Range with Workbook Scope**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Adding a Named Range with Worksheet Scope**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
