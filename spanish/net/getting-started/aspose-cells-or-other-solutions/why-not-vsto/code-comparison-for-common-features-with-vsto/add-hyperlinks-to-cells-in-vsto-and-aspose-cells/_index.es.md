---
title: Agregar hipervínculos a Cells en VSTO y Aspose.Cells
type: docs
weight: 20
url: /es/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---
Para agregar hipervínculos a las celdas de una hoja de cálculo, siga los siguientes pasos:

1.  Configure la hoja de trabajo:
 1. Cree una instancia de un objeto de aplicación (solo VSTO).
 1. Agregue un libro de trabajo.
 1. Obtenga la primera hoja.
 1. Agregue texto a las celdas a las que agregará un hipervínculo.
1. Añadir hipervínculo.
1. Guarde el documento.

Estos pasos se muestran en los ejemplos de código a continuación. Los primeros ejemplos muestran cómo usar VSTO con C# para agregar un hipervínculo a una celda. Los ejemplos que siguen muestran cómo hacer lo mismo usando Aspose.Cells for .NET, nuevamente usando C#.

Los ejemplos de código generan un archivo de Excel que tiene un hipervínculo en la celda A1 de la primera hoja de trabajo.

![todo:imagen_alternativa_texto](picture1.png)

Se agrega un hipervínculo a la celda A1.

## **VSTO**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **Descargar código de muestra**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [forjafuente](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/descargar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).Código Postal)
