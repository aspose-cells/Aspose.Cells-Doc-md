﻿---
title: Spara varje arbetsblad till olika PDF i xlsx4j
type: docs
weight: 50
url: /sv/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---
## **Aspose.Cells - Spara varje arbetsblad till olika PDF**
Aspose.Cells stöder konvertering av XLS-filer (som innehåller bilder, diagram etc.) till PDF-dokument. Aspose.Cells for Java kan arbeta självständigt för att konvertera ett kalkylblad till Pdf-dokument och du behöver inte längre använda Aspose.Pdf for Java för konverteringen. Konverteringen kräver inte att man skapar/använder någon temporär fil(er) också eftersom hela processen kan göras i minnet.

**Java**

{{< highlight "java" >}}

 //Hämta sökvägen till Excel-filen

String filePath = dataDir + "workbook.xlsx";

//Instantiera en ny arbetsbok och öppna Excel

//Fil från sin plats

Workbook workbook = new Workbook(filePath);

//Hämta antalet arbetsblad i arbetsboken

int sheetCount = workbook.getWorksheets().getCount();

//Gör alla ark osynliga utom det första kalkylbladet

 för (int i = 1; i< workbook.getWorksheets().getCount(); i++)

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
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

 För mer information, besök[Spara varje kalkylblad till en annan PDF-fil](/cells/sv/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
