---
title: Save Each Worksheet to Different PDF using Aspose.Cells
type: docs
weight: 80
url: /java/save-each-worksheet-to-different-pdf-using-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
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
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

For more details, visit [Save Each Worksheet to a Different PDF File](/cells/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
