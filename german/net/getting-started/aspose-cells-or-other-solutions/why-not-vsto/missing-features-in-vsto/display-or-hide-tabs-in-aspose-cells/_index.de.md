---
title: Registerkarten in Aspose.Cells anzeigen oder ausblenden
type: docs
weight: 80
url: /de/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

Wenn Sie am unteren Rand einer Microsoft Excel-Datei genau hinsehen, sehen Sie eine Reihe von Steuerelementen. Dazu gehören:

- Registerkarten.
- Registerkarten-Scrolltasten.

Registerkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe sind, desto mehr Registerkarten gibt es. Wenn die Excel-Datei eine gute Anzahl von Arbeitsblättern hat, benötigen Sie Tasten, um zwischen ihnen zu navigieren. Daher bietet Microsoft Excel Registerkarten-Scrolltasten zum Scrollen durch die Registerkarten an.

**Registerkarten und Registerkarten-Bildlaufschaltflächen** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

Mit Aspose.Cells können Entwickler die Sichtbarkeit von Registerkarten und Bildlaufschaltflächen für Registerkarten in Excel-Dateien steuern. 

{{% /alert %}} 

Im Folgenden finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die modifizierte Datei als output.xls speichert.

Sie können im folgenden Abbild sehen, dass die Datei Book1.xls Registerkarten enthält. Nach Ausführung des Beispiels werden die Registerkarten ausgeblendet, wie im Screenshot der Datei output.xls unten zu sehen ist.

**book1.xls: Excel-Datei vor jeglicher Änderung** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: Excel-Datei nach der Änderung** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Steuerung der Registerkartenleistenbreite**
**C#**

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
