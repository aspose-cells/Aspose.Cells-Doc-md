---
title: Registerkartenfarbe des Arbeitsblatts in xlsx4j setzen
type: docs
weight: 60
url: /de/java/set-worksheet-tab-color-in-xlsx4j/
---

## **Aspose.Cells - Registerkartenfarbe des Arbeitsblatts setzen**
Aspose.Cells ermöglicht es Ihnen, die Farbe einzelner Arbeitsblattregisterkarten zu ändern, um sie von anderen hervorzuheben. Zum Beispiel können Sie Ausgaben rot, Verkäufe grün, Vermögenswerte blau usw. machen.
### **Verwenden von Microsoft Excel zur Festlegung der Registerkartenfarbe des Arbeitsblatts**
1. Klicken Sie mit der rechten Maustaste auf eine Registerkarte im Registerblatt am unteren Rand des aktuellen Arbeitsblatts.
1. Wählen Sie **Registerkartenfarbe**.
1. Wählen Sie eine Farbe aus der Palette.
1. Klicken Sie auf **OK**.

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

Besuchen Sie für weitere Details [Registerkartenfarbe festlegen](/java/set-worksheet-tab-color).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
