---
title: Establecer enlaces externos en fórmulas en Aspose.Cells
type: docs
weight: 90
url: /es/net/set-external-links-in-formulas-in-aspose-cells/
---
{{% alert color="primary" %}} 

A veces, es necesario incluir enlaces a archivos externos en fórmulas, por ejemplo, para evaluar un valor de celda o rango contra ellos. Aspose.Cells proporciona esta función y este documento explica cómo usarla.

{{% /alert %}} 

El siguiente código de ejemplo muestra cómo incluir archivos externos en fórmulas.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Set External Links in Formula.xlsx";

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get first Worksheet

Worksheet sheet = workbook.Worksheets[0];

//Get Cells collection

Aspose.Cells.Cells cells = sheet.Cells;

//Set formula with external links

cells["A1"].Formula = "=SUM('[book1.xls]Sheet1'!A2, '[book1.xls]Sheet1'!A4)";

//Set formula with external links

cells["A2"].Formula = "='[book1.xls]Sheet1'!A8";

//Save the workbook

workbook.Save(FileName);

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **Descargar ejemplo de ejecución**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
