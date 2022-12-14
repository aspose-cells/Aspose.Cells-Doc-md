---
title: Guarde cada hoja de trabajo en un PDF diferente
type: docs
weight: 10
url: /es/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - Guardar cada hoja de trabajo en un PDF diferente**
Aspose.Cells admite la conversión de archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for .NET puede funcionar de forma independiente para convertir una hoja de cálculo a un documento PDF y ya no necesita usar Aspose.Pdf for .NET para la conversión. La conversión no requiere crear / usar ningún archivo temporal, ya que todo el proceso se puede realizar en la memoria.

**C#**

{{< highlight "cs" >}}

 //Crear una instancia de un nuevo libro de trabajo y abrir Excel

//Archivo desde su ubicación

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtenga el recuento de las hojas de trabajo en el libro de trabajo

int sheetCount = libro de trabajo.Worksheets.Count;

// Hacer invisibles todas las hojas excepto la primera hoja de trabajo

 para (int i = 1; i< workbook.Worksheets.Count; i++)

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
## **Descargar código de ejecución**
 Descargar**Guarde cada hoja de trabajo en un PDF diferente** formar cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Para más detalles, visite[Guarde cada hoja de trabajo en un archivo PDF diferente](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
