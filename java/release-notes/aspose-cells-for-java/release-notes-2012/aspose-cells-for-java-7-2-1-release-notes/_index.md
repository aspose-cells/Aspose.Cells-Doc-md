---
title: Aspose.Cells for Java 7.2.1 Release Notes
type: docs
weight: 70
url: /java/aspose-cells-for-java-7-2-1-release-notes/
---

{{% alert color="primary" %}} 

This page contains release notes for [Aspose.Cells for Java 7.2.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.2.1/)

{{% /alert %}} 

We are
happy to announce Aspose.Cells for Java v7.2.1! 

New Features 

- Format Pivot Table with custom styles fordifferent categories (Modify Pivot Table’s Quick Style)

Enhancements 

- Cells.findString()/find() supports to search RegExand in specific range
- Support Picture.setTitle()/getTitle()
- Save MS Excel charts in ODS file
- Make Aspose.Cells created XLS filecompatible with POI

Exceptions 

- Reading XLSX file produces: “java.lang.ClassCastException:org.dom4j.Namespace”

Bugs 

- Saved XLSX file gives error: "Datamay has been lost"
- Formatted number was incorrect in thegenerated PDF (Thousand group characters were lost)
- Bar chart was not appearing in the generatedPDF for JDK6 version
- References are not updated when expandinga range
