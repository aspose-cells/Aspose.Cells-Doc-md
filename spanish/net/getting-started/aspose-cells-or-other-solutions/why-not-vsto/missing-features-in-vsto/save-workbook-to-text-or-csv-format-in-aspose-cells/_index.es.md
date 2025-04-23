---
title: Guardar libro de trabajo en formato de texto o CSV en Aspose.Cells
type: docs
weight: 110
url: /es/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---

{{% alert color="primary" %}} 

A veces, es posible que desee convertir o guardar un libro de trabajo con varias hojas de cálculo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), tanto Microsoft Excel como Aspose.Cells guardan por defecto el contenido de la hoja de cálculo activa únicamente.

{{% /alert %}} 

El siguiente ejemplo de código explica cómo guardar un libro de trabajo completo en formato de texto. Cargue el libro de trabajo fuente que podría ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando el código se ejecuta, convierte los datos de todas las hojas en el libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en CSV. Por defecto, TxtSaveOptions.Separator es la coma, así que no especifique un separador al guardar en formato CSV.

**C#**

{{< highlight csharp >}}

 string filePath = "source.xlsx";

//Load your source workbook

Workbook workbook = new Workbook(filePath);

//0-byte array

byte[] workbookData = new byte[0];

//Text save options. You can use any type of separator

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//Copy each worksheet data in text format inside workbook data array

for (int idx = 0; idx < workbook.Worksheets.Count; idx++)

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

File.WriteAllBytes(filePath + ".out.txt", workbookData);


{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
