---
title: Ställ in kalkylbladsflikfärg i Aspose.Cells
type: docs
weight: 20
url: /sv/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Ställ in kalkylbladsflikfärg**
Aspose.Cells låter dig ändra färgen på enskilda kalkylbladsflikar för att göra dem framträdande från resten. Du kan till exempel göra utgifter röda, försäljningsgröna, tillgångar blå osv.
### **Ställa in kalkylbladsflikfärg med Microsoft Excel**
1. Högerklicka på en flik i flikarket längst ned i det aktuella kalkylbladet.
1. Välj**Flikfärg**.
1. Välj en färg från paletten.
1. Klick**OK**.

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
## **Ladda ner Running Code**
 Ladda ner**Ställ in kalkylbladsflikfärg** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Ställ in kalkylbladsflikfärg](/cells/sv/net/set-worksheet-tab-color/).

{{% /alert %}}
