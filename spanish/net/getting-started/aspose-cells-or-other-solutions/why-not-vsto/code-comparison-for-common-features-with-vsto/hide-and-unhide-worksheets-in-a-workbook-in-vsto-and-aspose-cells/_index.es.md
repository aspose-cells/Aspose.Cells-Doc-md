---
title: Ocultar y mostrar hojas de cálculo en un libro en VSTO y Aspose.Cells
type: docs
weight: 140
url: /es/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

Este artículo compara cómo ocultar y mostrar hojas de cálculo con VSTO, utilizando C# o Visual Basic, con la realización de la misma tarea con Aspose.Cells, nuevamente utilizando C# o Visual Basic. Aspose.Cells te permite trabajar sin tener instalado Microsoft Excel.

Los pasos para ocultar una hoja de cálculo son:

1. Abrir un archivo.
1. Obtener una hoja de cálculo.
1. Ocultar la hoja de cálculo.
1. Guarde el archivo.
   Para mostrar una hoja de cálculo nuevamente, simplemente cambie la visibilidad de la hoja oculta.

Las muestras de código a continuación muestran primero como ocultar una hoja de cálculo. Las primeras muestras muestran el proceso con VSTO, utilizando C#, en comparación con el uso de Aspose.Cells, nuevamente utilizando C#.

El segundo conjunto de muestras de código muestra la línea utilizada para mostrar la hoja de cálculo oculta en VSTO o Aspose.Cells.
## **Ocultar Hojas de Cálculo**
A continuación se muestran muestras de código para VSTO y Aspose.Cells que ilustran cómo ocultar una hoja de cálculo en un libro.
### **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **Mostrar Hoja de Cálculo**
A continuación se muestran muestras de código para VSTO y Aspose.Cells que ilustran cómo mostrar una hoja de cálculo en un libro.
### **VSTO**
{{< highlight csharp >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
