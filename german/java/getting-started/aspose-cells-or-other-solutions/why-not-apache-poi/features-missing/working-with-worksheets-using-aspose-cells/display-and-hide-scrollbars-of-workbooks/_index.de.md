---
title: Anzeigen und Ausblenden von Bildlaufleisten in Arbeitsmappen
type: docs
weight: 40
url: /de/java/display-and-hide-scrollbars-of-workbooks/
---

## **Aspose.Cells - Anzeigen und Ausblenden von Bildlaufleisten von Arbeitsmappen**
Aspose.Cells bietet eine Klasse, **Workbook**, die eine Excel-Datei repräsentiert. Die Klasse **Workbook** bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um jedoch die Sichtbarkeit der Bildlaufleisten in der Excel-Datei zu steuern, können Entwickler die Methoden **setVScrollBarVisible** und **setHScrollBarVisible** der Klasse **Workbook** verwenden.

**Java**

{{< highlight java >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
{{< app/cells/assistant language="java" >}}
