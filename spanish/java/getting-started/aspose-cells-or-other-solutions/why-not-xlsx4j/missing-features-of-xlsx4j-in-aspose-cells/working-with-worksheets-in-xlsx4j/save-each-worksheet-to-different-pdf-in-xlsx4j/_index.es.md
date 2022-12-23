---
title: Guarde cada hoja de trabajo en diferentes PDF en xlsx4j
type: docs
weight: 50
url: /es/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---
## **Aspose.Cells - Guarde cada hoja de trabajo en diferentes PDF**
Aspose.Cells admite la conversión de archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for Java puede funcionar de forma independiente para convertir una hoja de cálculo a un documento PDF y ya no necesita usar Aspose.Pdf for Java para la conversión. La conversión no requiere crear / usar ningún archivo temporal, ya que todo el proceso se puede realizar en la memoria.

**Java**

{{< highlight "java" >}}

 //Obtenga la ruta del archivo de Excel

String filePath = dataDir + "workbook.xlsx";

//Crear una instancia de un nuevo libro de trabajo y abrir Excel

//Archivo desde su ubicación

Libro de trabajo libro de trabajo = nuevo libro de trabajo (filePath);

//Obtenga el recuento de las hojas de trabajo en el libro de trabajo

int sheetCount = libro de trabajo.getWorksheets().getCount();

// Hacer invisibles todas las hojas excepto la primera hoja de trabajo

 para (int i = 1; i< workbook.getWorksheets().getCount(); i++)

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
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Guarde cada hoja de trabajo en un archivo PDF diferente](/cells/es/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
