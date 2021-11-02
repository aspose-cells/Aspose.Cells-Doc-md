---
title: Aspose.Cells for Java 7.3.3 Release Notes
type: docs
weight: 20
url: /java/aspose-cells-for-java-7-3-3-release-notes/
---

{{% alert color="primary" %}} 

This page contains release notes for [Aspose.Cells for Java 7.3.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.3/)

{{% /alert %}} 

We are
happy to announce Aspose.Cells for Java v7.3.3! 

New Features 

- Add Row.getLastDataCell() method to getthe last cell having data in a row
- New APIs added for getting same Styleobject for cells with the same style settings

Enhancements 

- Add quotes to empty cell value(s) whenexporting a CSV with

option 

Exceptions 

- Conditional formatting with Unicodecharacters fails
- Setting formula before adding areas forconditional formatting and then renaming worksheet caused an error when saving workbook
- Re-saving an XLS template file causedNegativeArraySizeException

Bugs 

- Formatted Date value was different fromwhat is shown in MS Excel
- Chart series names are lost ifCellCollection is cleared
- Displaying blank as gaps/zeroes does notwork for XLSX files
- Data label formatting for charts is notfine
- Font underline disappeared in therendered PDF file
- Setting font styles took no effect forXLSX in LightCells mode
- Part of footer was lost when saving to PDF
