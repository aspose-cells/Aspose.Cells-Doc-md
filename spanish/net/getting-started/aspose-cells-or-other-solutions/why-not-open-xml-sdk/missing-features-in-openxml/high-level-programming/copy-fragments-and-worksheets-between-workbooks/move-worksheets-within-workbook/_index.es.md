---
title: Mover hojas de cálculo dentro del libro de trabajo
type: docs
weight: 30
url: /es/net/move-worksheets-within-workbook/
---

Aspose.Cells proporciona un método, Aspose.Cells.Worksheet.MoveTo(), utilizado para mover una hoja de cálculo a otra ubicación en la hoja de cálculo. El método toma el índice de la hoja de cálculo de destino como parámetro.

El siguiente ejemplo muestra cómo mover una hoja de cálculo a otra ubicación dentro del libro.

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Move Worksheet.xlsx";

//Open an existing excel file.

Workbook wb = new Workbook(FileName);

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Get the first worksheet.

Worksheet worksheet = sheets[0];

string test = worksheet.Name;

//Move the first sheet to the third position in the workbook.

worksheet.MoveTo(2);

//Save the excel file.

wb.Save(FileName);

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)
