---
title: Ocultar y mostrar hojas de trabajo en un libro de trabajo
type: docs
weight: 80
url: /es/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

Al presentar libros de trabajo a clientes o hacer una presentación, puede ser útil ocultar hojas de trabajo en un libro de trabajo. Un enfoque estructurado para el modelado de hojas de cálculo sugiere que los datos, las fórmulas y las visualizaciones, como los gráficos, se mantengan en hojas separadas. Este enfoque mantiene el diseño limpio y simple y hace que el libro de trabajo sea más fácil de navegar. Al presentar los resultados, es posible que desee ocultar los datos o las hojas de fórmulas para evitar distracciones.

Los usuarios que trabajan en Microsoft Excel pueden ocultar fácilmente y luego mostrar (mostrar) hojas de trabajo. Las mismas funciones están disponibles para los desarrolladores que programan con hojas de cálculo de Excel. Hay diferentes formas de trabajar con hojas de cálculo desde dentro de las aplicaciones de software. Un método es usar VSTO, otro es Aspose.Cells for .NET.

{{% /alert %}}

## **Ocultar y mostrar hojas de trabajo**

 Este artículo compara[ocultación](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) y[desocultar](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) hojas de trabajo con[VSTO](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) , utilizando C# o Visual Basic, para realizar la misma tarea con[Aspose.Cells](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/), nuevamente usando C# o Visual Basic. Aspose.Cells le permite trabajar sin Microsoft Excel instalado.

Los pasos para ocultar una hoja de trabajo son:

1. Abre un archivo.
1. Consigue una hoja de trabajo.
1. Ocultar la hoja de trabajo.
1. Guarda el archivo.

 A[mostrar](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) una hoja de trabajo nuevamente, simplemente active la visibilidad de la hoja oculta.

 Los ejemplos de código a continuación muestran primero cómo ocultar una hoja de trabajo. Las primeras muestras muestran el proceso con[VSTO](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) , utilizando C# o Visual Basic, en comparación con el uso[Aspose.Cells](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/), nuevamente usando C# o Visual Basics.

 El segundo conjunto de ejemplos de código muestra la línea utilizada para mostrar la hoja de trabajo en[VSTO](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/) o[Aspose.Cells](/cells/es/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Ocultar hojas de trabajo**

A continuación se muestran ejemplos de código para VSTO y Aspose.Cells que ilustran cómo ocultar una hoja de cálculo en un libro.

### **Ocultar hojas de trabajo con VSTO**

**C#**

{{< highlight "csharp" >}}



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


### **Ocultar hojas de trabajo con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}



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

## **Mostrar hojas de trabajo**

A continuación se muestran ejemplos de código para VSTO y Aspose.Cells que ilustran cómo mostrar una hoja de trabajo en un libro.

### **Mostrar una hoja de trabajo con VSTO**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Mostrar una hoja de trabajo con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
