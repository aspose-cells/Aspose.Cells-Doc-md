---
title: Spara varje arbetsblad i olika PDF filer med Aspose.Cells
type: docs
weight: 80
url: /sv/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
---

## **Aspose.Cells - Spara varje kalkylblad i olika PDF**
Aspose.Cells stöder konvertering av XLS-filer (som innehåller bilder, diagram etc.) till PDF-dokument. Aspose.Cells for Java kan arbeta oberoende för att konvertera en kalkyl till Pdf-dokument och du behöver inte längre använda Aspose.Pdf for Java för konverteringen. Konverteringen kräver inte heller att skapa/använda några tillfälliga filer eftersom hela processen kan göras i minnet.

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **Ladda ned körbar kod**
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

För mer information, besök [Spara varje arbetsblad till en annan PDF-fil](/cells/sv/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
