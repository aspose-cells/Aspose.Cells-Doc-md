---
title: Ställ in färg för kalkylblad i Aspose.Cells
type: docs
weight: 20
url: /sv/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Ställ in färg för fliken för kalkylblad**
Aspose.Cells låter dig ändra färgen på individuella arbetsbladsflikar för att göra dem framträdande från resten. Till exempel kan du göra Utgifter röda, Försäljning gröna, Tillgångar blå, osv.
### **Ställa in färg på arbetsbladets flik i Microsoft Excel**
1. Högerklicka på en flik i flikarket längst ned på det aktuella arbetsbladet.
1. Välj **Flikens färg**.
1. Välj en färg från paletten.
1. Klicka på **OK**.

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
## **Ladda ned körbar kod**
Ladda ner **Ställ in färg för kalkylblad** från någon av nedanstående sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

För mer detaljer, besök [Ställ in färg för kalkylblad](/cells/sv/net/set-worksheet-tab-color/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
