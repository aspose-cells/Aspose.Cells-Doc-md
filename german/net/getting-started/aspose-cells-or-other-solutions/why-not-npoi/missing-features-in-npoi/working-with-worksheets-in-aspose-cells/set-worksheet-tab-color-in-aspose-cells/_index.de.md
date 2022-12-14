---
title: Legen Sie die Farbe des Arbeitsblatt-Registers in Aspose.Cells fest
type: docs
weight: 20
url: /de/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Legen Sie die Farbe der Arbeitsblatt-Registerkarte fest**
Aspose.Cells ermöglicht es Ihnen, die Farbe einzelner Arbeitsblatt-Registerkarten zu ändern, um sie von den anderen abzuheben. Beispielsweise können Sie Ausgaben rot, Verkäufe grün, Vermögenswerte blau usw.
### **Festlegen der Farbe der Arbeitsblattregisterkarte mit Microsoft Excel**
1. Klicken Sie mit der rechten Maustaste auf eine Registerkarte im Registerkartenblatt unten im aktuellen Arbeitsblatt.
1. Auswählen**Registerkartenfarbe**.
1. Wählen Sie eine Farbe aus der Palette aus.
1. Klicken**OK**.

**C#**

{{< highlight "cs" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Legen Sie die Farbe des Arbeitsblatt-Tabs fest** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Legen Sie die Farbe des Arbeitsblatt-Tabs fest](/cells/de/net/set-worksheet-tab-color/).

{{% /alert %}}
