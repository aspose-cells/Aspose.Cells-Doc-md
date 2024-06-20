---
title: Ocultar y Mostrar Hojas de Cálculo en un Libro de Trabajo
type: docs
weight: 80
url: /es/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

Al presentar libros de trabajo a los clientes, o al hacer una presentación, puede ser útil ocultar hojas de cálculo en un libro de trabajo. Un enfoque estructurado para modelar hojas de cálculo sugiere que los datos, las fórmulas y visualizaciones como los gráficos se mantengan en hojas separadas. Este enfoque mantiene el diseño limpio y simple, y hace que el libro de trabajo sea más fácil de navegar. Al presentar resultados, es posible que desee ocultar los datos o las hojas de fórmulas de la vista para evitar distracciones.

Los usuarios que trabajan en Microsoft Excel pueden ocultar y luego mostrar hojas de cálculo fácilmente. Las mismas funciones están disponibles para los desarrolladores que programan con hojas de cálculo de Excel. Hay diferentes formas de trabajar con hojas de cálculo desde aplicaciones de software. Un método es usar VSTO, otro es Aspose.Cells for .NET.

{{% /alert %}}

## **Ocultar y Mostrar Hojas de Cálculo**

Este artículo compara [ocultar](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) y [mostrar](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) hojas de cálculo con [VSTO](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/), utilizando ya sea C# o Visual Basic, con la realización de la misma tarea con [Aspose.Cells](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/), nuevamente utilizando C# o Visual Basic. Aspose.Cells le permite trabajar sin tener Microsoft Excel instalado.

Los pasos para ocultar una hoja de cálculo son:

1. Abrir un archivo.
1. Obtener una hoja de cálculo.
1. Ocultar la hoja de cálculo.
1. Guarde el archivo.

Para [mostrar](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) nuevamente una hoja de cálculo, simplemente cambie la visibilidad de la hoja oculta.

Los ejemplos de código a continuación muestran primero cómo ocultar una hoja de cálculo. Los primeros ejemplos muestran el proceso con [VSTO](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/), utilizando ya sea C# o Visual Basic, en comparación con el uso de [Aspose.Cells](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/), nuevamente utilizando ya sea C# o Visual Basic.

El segundo conjunto de ejemplos de código muestra la línea utilizada para mostrar la hoja de cálculo en [VSTO](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) o [Aspose.Cells](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Ocultar Hojas de Cálculo**

A continuación se muestran muestras de código para VSTO y Aspose.Cells que ilustran cómo ocultar una hoja de cálculo en un libro.

### **Ocultar Hojas de Cálculo con VSTO**

**C#**

{{< highlight csharp >}}



.......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......



//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();



//Specify the template Excel file path.

string myPath=@"d:\test\MyBook.xls";



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

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Ocultar Hojas de Cálculo con Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Mostrar hojas de cálculo**

A continuación se muestran muestras de código para VSTO y Aspose.Cells que ilustran cómo mostrar una hoja de cálculo en un libro.

### **Mostrar una hoja de cálculo con VSTO**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Mostrar una hoja de cálculo con Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
