---
title: Ställ in kalkylbladsflikfärg i Aspose.Cells
type: docs
weight: 90
url: /sv/java/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Ställ in kalkylbladsflikfärg**
Aspose.Cells låter dig ändra färgen på enskilda kalkylbladsflikar för att göra dem framträdande från resten. Du kan till exempel göra utgifter röda, försäljningsgröna, tillgångar blå osv.
#### **Ställa in kalkylbladsflikfärg med Microsoft Excel**
1. Högerklicka på en flik i flikarket längst ned i det aktuella kalkylbladet.
1. Välj**Flikfärg**.
1. Välj en färg från paletten.
1. Klick**OK**.

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
## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

 För mer information, besök[Ställ in kalkylbladsflikfärg](/java/set-worksheet-tab-color).

{{% /alert %}}
