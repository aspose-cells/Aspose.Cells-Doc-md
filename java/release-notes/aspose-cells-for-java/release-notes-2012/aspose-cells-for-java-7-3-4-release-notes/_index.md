---
title: Aspose.Cells for Java 7.3.4 Release Notes
type: docs
weight: 10
url: /java/aspose-cells-for-java-7-3-4-release-notes/
---

{{% alert color="primary" %}} 

This page contains release notes for [Aspose.Cells for Java 7.3.4](http://www.aspose.com/downloads/cells/java/new-releases/aspose.cells-for-java-7.3.4/)

{{% /alert %}} 

We are
happy to announce Aspose.Cells for Java v7.3.4! 

New Features 

- Support for TIFF format in Sheet-to-Imagefeature

Enhancements 

- Right footer is not above the centerfooter as in MS Excel

Exceptions 

- Out of Memory exception while converting Excelto PDF
- Setting "+100" as the conditionalformula caused an exception
- Exception: “StackOverflowError” whencalculating formulas
- “IllegalArgumentException” is thrown whenWorkbook.copy() is called

Bugs 

- Arabic text became junk characters in thesaved CSV file with UTF-8
- "Data may have been lost" errorfor the re-saved XLS file by Aspose.Cells
- "Excel found unreadable content….."error for Aspose.Cells’ generated report
- Cell.getFormula() did not distinguish differentnamed ranges with the same name but different scope
- Automatic title for PIE chart issue
- Cell.getR1C1Formula() did not distinguishdifferent named ranges with the same name but different scope
