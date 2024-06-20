---
title: Daten aus Arbeitsblättern in xlsx4j exportieren
type: docs
weight: 20
url: /de/java/export-data-from-worksheets-in-xlsx4j/
---

## **Aspose.Cells - Daten aus Arbeitsblättern exportieren**
Aspose.Cells ermöglicht es den Benutzern nicht nur, Daten aus externen Datenquellen in Arbeitsblätter zu importieren, sondern auch, Arbeitsblattdaten in ein Array zu exportieren.

**Java**

{{< highlight java >}}

 //Creating a file stream containing the Excel file to be opened

FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

//Instantiating a Workbook object

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Exporting the contents of 7 rows and 2 columns starting from 1st cell to Array.

Object dataTable [][] = worksheet.getCells().exportArray(4,0,7,8);

for (int i = 0 ; i < dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

Für weitere Details, besuchen Sie [Daten aus Arbeitsblättern exportieren](/java/exporting-data-from-worksheets).

{{% /alert %}}
