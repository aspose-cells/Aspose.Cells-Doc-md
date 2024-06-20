---
title: Esporta i dati dalle pagine di lavoro in xlsx4j
type: docs
weight: 20
url: /it/java/export-data-from-worksheets-in-xlsx4j/
---

## **Aspose.Cells - Esporta i Dati dalle Pagine di Lavoro**
Aspose.Cells non solo consente ai suoi utenti di importare dati nei fogli di lavoro da origini di dati esterne ma consente anche di esportare i dati del foglio di lavoro in un array.

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
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Esportazione dei Dati dalle Pagine di Lavoro](/java/exporting-data-from-worksheets).

{{% /alert %}}
