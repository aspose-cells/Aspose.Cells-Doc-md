---
title: Tabellenblattfarbe in Aspose.Cells festlegen
type: docs
weight: 20
url: /de/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Registerkartenfarbe des Arbeitsblatts setzen**
Aspose.Cells ermöglicht es Ihnen, die Farbe einzelner Arbeitsblattregisterkarten zu ändern, um sie von anderen hervorzuheben. Zum Beispiel können Sie Ausgaben rot, Verkäufe grün, Vermögenswerte blau usw. machen.
### **Verwenden von Microsoft Excel zur Festlegung der Registerkartenfarbe des Arbeitsblatts**
1. Klicken Sie mit der rechten Maustaste auf eine Registerkarte im Registerblatt am unteren Rand des aktuellen Arbeitsblatts.
1. Wählen Sie **Registerkartenfarbe**.
1. Wählen Sie eine Farbe aus der Palette.
1. Klicken Sie auf **OK**.

**C#**

{{< highlight cs >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Arbeitsblattregisterkarte-Farbe festlegen** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Arbeitsblattregisterkarte-Farbe festlegen](/cells/de/net/set-worksheet-tab-color/).

{{% /alert %}}
