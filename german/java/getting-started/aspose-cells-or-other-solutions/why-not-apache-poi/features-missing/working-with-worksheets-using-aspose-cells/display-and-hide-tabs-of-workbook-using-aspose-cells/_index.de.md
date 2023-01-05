---
title: Anzeigen und Ausblenden von Registerkarten der Arbeitsmappe mit Aspose.Cells
type: docs
weight: 50
url: /de/java/display-and-hide-tabs-of-workbook-using-aspose-cells/
---
## **Aspose.Cells – Registerkarten der Arbeitsmappe anzeigen und ausblenden**
Aspose.Cells stellt eine Klasse Workbook bereit, die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um die Sichtbarkeit von Registerkarten in einer Excel-Datei zu steuern, können Entwickler die setShowTabs-Methode der Workbook-Klasse verwenden.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file

workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

