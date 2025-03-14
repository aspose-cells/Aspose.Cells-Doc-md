---
title: Managing Page Breaks
type: docs
weight: 30
url: /go-cpp/managing-page-breaks/
---

{{% alert color="primary" %}}

According to the definition, a page break is a place in a flow of text where one page ends and the next begins. Microsoft Excel lets users add page breaks into any selected cell of a worksheet.

The location of the cell where the page break is added, the page is ended and all rest of the data after the page break is printed on the next page while printing. In simple words, page breaks divide your worksheet into multiple pages according to your specifications. You can also add page breaks to your worksheets at runtime using Aspose.Cells. Aspose.Cells allows developers to add two kinds of page breaks:

- Horizontal page break
- Vertical page break

In the rest of the discussion, we will describe how can you add horizontal or vertical page breaks into your worksheets using Aspose.Cells.

{{% /alert %}}

## **Page Breaks**

Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) that represents an Excel file. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) class contains a [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a wide range of methods used to manage a worksheet. To add the page breaks, use the [AddPageBreaks](https://reference.aspose.com/cells/go-cpp/worksheet/addpagebreaks) method of the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class.

### **Adding Page Breaks**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingPageBreaks.go" >}}
