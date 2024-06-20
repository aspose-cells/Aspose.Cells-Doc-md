---
title: Guardar cada hoja de cálculo en un PDF diferente usando Aspose.Cells
type: docs
weight: 80
url: /es/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
---

## **Aspose.Cells - Guardar cada hoja de trabajo en PDFs diferentes**
Aspose.Cells admite la conversión de archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for Java puede trabajar de forma independiente para convertir una hoja de cálculo a un documento PDF y ya no necesita usar Aspose.Pdf for Java para la conversión. La conversión tampoco requiere crear/usar ningún archivo temporal ya que todo el proceso se puede realizar en la memoria.

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
## **Descargar Código en Ejecución**
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Guardar cada hoja de trabajo en un archivo PDF diferente](/cells/es/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
