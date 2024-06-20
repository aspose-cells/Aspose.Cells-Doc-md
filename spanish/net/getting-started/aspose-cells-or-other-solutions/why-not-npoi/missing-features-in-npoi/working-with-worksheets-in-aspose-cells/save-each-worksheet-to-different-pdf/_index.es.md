---
title: Guardar cada hoja de trabajo en PDFs diferentes
type: docs
weight: 10
url: /es/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - Guardar cada hoja de trabajo en PDFs diferentes**
Aspose.Cells admite la conversión de archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for .NET puede trabajar de forma independiente para convertir una hoja de cálculo a un documento Pdf y ya no es necesario utilizar Aspose.Pdf para .NET para la conversión. La conversión tampoco requiere crear o usar ningún archivo temporal, ya que todo el proceso se puede realizar en la memoria.

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Guardar cada hoja de trabajo en PDFs diferentes** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Para más detalles, visite [Guardar cada hoja de cálculo en un archivo PDF diferente](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
