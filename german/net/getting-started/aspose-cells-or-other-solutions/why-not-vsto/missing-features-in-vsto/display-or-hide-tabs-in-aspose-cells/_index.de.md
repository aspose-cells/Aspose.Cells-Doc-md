---
title: Tabs anzeigen oder ausblenden in Aspose.Cells
type: docs
weight: 80
url: /de/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

Wenn Sie sich das Ende einer Microsoft-Excel-Datei genau ansehen, sehen Sie eine Reihe von Steuerelementen. Diese beinhalten:

- Blattregisterkarten.
- Tab-Scroll-Schaltflächen.

Blattregisterkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe vorhanden sind, desto mehr Blattregisterkarten gibt es. Wenn die Excel-Datei eine große Anzahl von Arbeitsblättern enthält, benötigen Sie Schaltflächen, um durch sie zu navigieren. So stellt Microsoft Excel Schaltflächen zum Scrollen von Registerkarten bereit, um durch die Blattregisterkarten zu scrollen.

**Blattregisterkarten und Schaltflächen zum Scrollen von Registerkarten** 

![todo: Bild_alt_Text](display-or-hide-tabs-in-aspose-cells_1.png)

Mit Aspose.Cells können Entwickler die Sichtbarkeit von Blattregisterkarten und Schaltflächen zum Scrollen von Registerkarten in Excel-Dateien steuern.

{{% /alert %}} 

Nachfolgend finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die geänderte Datei als output.xls speichert.

In der Abbildung unten sehen Sie, dass die Datei Book1.xls Registerkarten enthält. Nachdem der Beispielcode ausgeführt wurde, werden die Registerkarten ausgeblendet, wie Sie auf dem Screenshot der Datei output.xls unten sehen können.

**book1.xls: Excel-Datei vor jeder Änderung** 

![todo: Bild_alt_Text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: Excel-Datei nach der Änderung** 

![todo: Bild_alt_Text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Steuern der Breite der Registerkartenleiste**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
