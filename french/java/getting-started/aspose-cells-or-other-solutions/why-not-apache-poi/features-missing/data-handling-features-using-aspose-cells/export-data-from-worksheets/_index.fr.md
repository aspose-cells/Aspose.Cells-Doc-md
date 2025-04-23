---
title: Exporter des données à partir des feuilles de calcul
type: docs
weight: 40
url: /fr/java/export-data-from-worksheets/
---

## **Aspose.Cells - Exporter des données à partir des feuilles de calcul**
Aspose.Cells permet non seulement à ses utilisateurs d'importer des données dans des feuilles de calcul à partir de sources de données externes, mais leur permet également d'exporter des données de feuille de calcul vers un tableau.

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

//Closing the file stream to free all resources

fstream.close();

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/ExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Exporter des données à partir des feuilles de calcul](/java/exporting-data-from-worksheets).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
