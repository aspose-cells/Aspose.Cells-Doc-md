---
title: Ocultar y mostrar hojas de trabajo en un libro de trabajo en VSTO y Aspose.Cells
type: docs
weight: 140
url: /es/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
Este artículo compara la ocultación y visualización de hojas de trabajo con VSTO, usando C# o Visual Basic, con la realización de la misma tarea con Aspose.Cells, nuevamente usando C# o Visual Basic. Aspose.Cells le permite trabajar sin Microsoft Excel instalado.

Los pasos para ocultar una hoja de trabajo son:

1. Abre un archivo.
1. Consigue una hoja de trabajo.
1. Ocultar la hoja de trabajo.
1. Guarda el archivo.
 Para volver a mostrar una hoja de cálculo, simplemente active la visibilidad de la hoja oculta.

Los ejemplos de código a continuación muestran primero cómo ocultar una hoja de trabajo. Los primeros ejemplos muestran el proceso con VSTO, usando C#, en comparación con el uso de Aspose.Cells, nuevamente usando C#.

El segundo conjunto de ejemplos de código muestra la línea utilizada para mostrar la hoja de trabajo en VSTO o Aspose.Cells.
## **Ocultar hojas de trabajo**
A continuación se muestran ejemplos de código para VSTO y Aspose.Cells que ilustran cómo ocultar una hoja de cálculo en un libro.
### **VSTO**
{{< highlight "csharp" >}}

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
{{< highlight "csharp" >}}

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
## **Hoja de trabajo para mostrar**
A continuación se muestran ejemplos de código para VSTO y Aspose.Cells que ilustran cómo mostrar una hoja de trabajo en un libro.
### **VSTO**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [forjafuente](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/descargar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).Código Postal)
