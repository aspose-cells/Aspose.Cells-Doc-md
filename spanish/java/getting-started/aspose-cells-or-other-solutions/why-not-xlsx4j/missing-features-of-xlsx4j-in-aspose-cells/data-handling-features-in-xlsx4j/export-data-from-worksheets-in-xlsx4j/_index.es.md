---
title: Exportar Datos desde Hojas de Cálculo en xlsx4j
type: docs
weight: 20
url: /es/java/export-data-from-worksheets-in-xlsx4j/
---

## **Aspose.Cells - Exportar Datos desde Hojas de Cálculo**
Aspose.Cells no solo permite a sus usuarios importar datos a las hojas de cálculo desde fuentes de datos externas, sino que también les permite exportar datos de la hoja de cálculo a un array.

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
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

Para más detalles, visite [Exportar Datos desde Hojas de Cálculo](/java/exporting-data-from-worksheets).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
