---
title: Ställ flikfärg i xlsx4j
type: docs
weight: 60
url: /sv/java/set-worksheet-tab-color-in-xlsx4j/
---

## **Aspose.Cells - Ställ in färg för fliken för kalkylblad**
Aspose.Cells låter dig ändra färgen på individuella arbetsbladsflikar för att göra dem framträdande från resten. Till exempel kan du göra Utgifter röda, Försäljning gröna, Tillgångar blå, osv.
### **Ställa in färg på arbetsbladets flik i Microsoft Excel**
1. Högerklicka på en flik i flikarket längst ned på det aktuella arbetsbladet.
1. Välj **Flikens färg**.
1. Välj en färg från paletten.
1. Klicka på **OK**.

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
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

För mer information, besök [Ställ flikfärg](/java/set-worksheet-tab-color).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
