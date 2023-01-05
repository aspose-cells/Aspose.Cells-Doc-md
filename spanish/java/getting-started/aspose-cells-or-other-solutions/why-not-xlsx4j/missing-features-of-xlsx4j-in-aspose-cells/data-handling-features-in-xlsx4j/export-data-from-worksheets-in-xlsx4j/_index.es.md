---
title: Exportar datos de hojas de trabajo en xlsx4j
type: docs
weight: 20
url: /es/java/export-data-from-worksheets-in-xlsx4j/
---
## **Aspose.Cells - Exportar datos de hojas de trabajo**
Aspose.Cells no solo permite a sus usuarios importar datos a hojas de trabajo desde fuentes de datos externas, sino que también les permite exportar datos de hojas de trabajo a una matriz.

**Java**

{{< highlight "java" >}}

 //Crear un flujo de archivos que contenga el archivo de Excel que se abrirá

FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

// Instanciando un objeto Workbook

Libro de trabajo libro de trabajo = nuevo libro de trabajo (fstream);

//Accediendo a la primera hoja de trabajo en el archivo de Excel

Hoja de trabajo hoja de trabajo = libro de trabajo.getWorksheets().get(0);

//Exportando el contenido de 7 filas y 2 columnas a partir de la primera celda a Array.

Objeto dataTable [][]= hoja de trabajo.getCells().exportArray(4,0,7,8);

 para (int i = 0 ; i< dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Exportación de datos desde hojas de trabajo](/java/exporting-data-from-worksheets).

{{% /alert %}}
