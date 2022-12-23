---
title: Legen Sie die Farbe des Arbeitsblatt-Registers in Aspose.Cells fest
type: docs
weight: 90
url: /de/java/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Legen Sie die Farbe der Arbeitsblatt-Registerkarte fest**
Aspose.Cells ermöglicht es Ihnen, die Farbe einzelner Arbeitsblatt-Registerkarten zu ändern, um sie von den anderen abzuheben. Beispielsweise können Sie Ausgaben rot, Verkäufe grün, Vermögenswerte blau usw.
#### **Festlegen der Farbe der Arbeitsblattregisterkarte mit Microsoft Excel**
1. Klicken Sie mit der rechten Maustaste auf eine Registerkarte im Registerkartenblatt unten im aktuellen Arbeitsblatt.
1. Wählen**Registerkartenfarbe**.
1. Wählen Sie eine Farbe aus der Palette aus.
1. Klicken**OK**.

**Java**

{{< highlight "java" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataPath + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Laufcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Legen Sie die Farbe des Arbeitsblatt-Tabs fest](/java/set-worksheet-tab-color).

{{% /alert %}}
