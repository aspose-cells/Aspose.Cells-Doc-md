---
title: Save Each Worksheet to Different PDF in xlsx4j
type: docs
weight: 50
url: /java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---

## **Aspose.Cells - Save Each Worksheet to Different PDF**
Aspose.Cells supports converting XLS files (that contain images, charts etc.) to PDF documents. Aspose.Cells for Java can work independently to convert a spreadsheet to Pdf document and you do not need to use Aspose.Pdf for Java for the conversion any longer. The conversion does not require to create / use any temporary file(s) too as the whole process can be done in the memory.

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
## **Download Running Code**
- [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://archive.codeplex.com/?p=asposecellsjavaxlsx4j)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

For more details, visit [Save Each Worksheet to a Different PDF File](http://docs.aspose.com:8082/docs/display/cellsjava/Save+Each+Worksheet+to+a+Different+PDF+File).

{{% /alert %}}
