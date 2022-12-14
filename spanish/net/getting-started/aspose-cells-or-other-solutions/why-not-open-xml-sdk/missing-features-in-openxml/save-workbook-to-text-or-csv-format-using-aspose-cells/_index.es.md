---
title: Guarde el libro de trabajo en formato de texto o CSV usando Aspose.Cells
type: docs
weight: 80
url: /es/net/save-workbook-to-text-or-csv-format-using-aspose-cells/
---
{{% alert color="primary" %}} 

A veces, desea convertir o guardar un libro de trabajo con varias hojas de trabajo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), de forma predeterminada, tanto Microsoft Excel como Aspose.Cells guardan solo el contenido de la hoja de trabajo activa.

{{% /alert %}} 

El siguiente ejemplo de código explica cómo guardar un libro completo en formato de texto. Cargue el libro de origen, que podría ser cualquier archivo de hoja de cálculo de Excel u OpenOffice Microsoft (es decir, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en CSV. De forma predeterminada, TxtSaveOptions.Separator es una coma, así que no especifique un separador si guarda en formato CSV.

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Archivos de muestra\";

string FileName = FilePath + "Guardar libro de trabajo en formato de texto o CSV.xlsx";

string destFileName = FilePath + "Guardar libro de trabajo en formato de texto o CSV.txt";

// Cargue su libro de trabajo de origen

Libro de trabajo libro de trabajo = nuevo libro de trabajo (nombre de archivo);

//matriz de 0 bytes

byte[]workbookData = nuevo byte[0];

//Opciones para guardar texto. Puedes usar cualquier tipo de separador

TxtSaveOptions opts = new TxtSaveOptions();

opciones.Separador = '\t';

// Copie cada dato de la hoja de trabajo en formato de texto dentro de la matriz de datos del libro de trabajo

 para (int idx = 0; idx< workbook.Worksheets.Count; idx++)

{

    //Save the active worksheet into text format

    MemoryStream ms = new MemoryStream();

    workbook.Worksheets.ActiveSheetIndex = idx;

    workbook.Save(ms, opts);

    //Save the worksheet data into sheet data array

    ms.Position = 0;

    byte[] sheetData = ms.ToArray();

    //Combine this worksheet data into workbook data array

    byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];

    Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);

    Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);

    workbookData = combinedArray;

}

//Save entire workbook data into file

File.WriteAllBytes(destFileName, workbookData);

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Save%20Workbook%20to%20Text%20or%20CSV%20Format)

## **Descargar ejemplo de ejecución**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
