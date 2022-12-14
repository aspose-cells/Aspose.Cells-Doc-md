---
title: Proteger y desproteger libros de trabajo
type: docs
weight: 20
url: /es/net/protecting-and-unprotecting-workbooks/
---
{{% alert color="primary" %}} 

Para evitar que alguien cambie, mueva o elimine hojas de cálculo de forma accidental o deliberada, puede proteger los elementos del libro de trabajo con o sin contraseña. Para proteger la estructura de un libro de trabajo de modo que las hojas de trabajo del libro de trabajo no se puedan mover, eliminar, ocultar, mostrar o renombrar, y no se puedan insertar nuevas hojas de trabajo, especifique ProtectionType como Estructura.

 Para proteger Windows para que tengan el mismo tamaño y posición cada vez que se abre el libro, especifique ProtectionType como Windows. En este artículo, mostramos cómo[proteger](/cells/es/net/protecting-and-unprotecting-workbooks/) y[desproteger](/cells/es/net/protecting-and-unprotecting-workbooks/) libros de trabajo usando VSTO y Aspose.Cells for .NET para permitirle comparar los dos métodos.

Aspose.Cells funciona independientemente de Microsoft Office Automation y está desarrollado para ser fácil de usar y producir un código ordenado.

Proteger un libro de trabajo no impide que los usuarios editen celdas. Para proteger los datos, debe proteger las hojas de trabajo.

{{% /alert %}} 
## **Proteger un libro de trabajo**
Para abrir un archivo de Excel Microsoft existente, proteja el libro de trabajo con estructura y atributos Windows y guarde el archivo.

A continuación se muestran fragmentos de código paralelo para VSTO (C#, VB) y Aspose.Cells for .NET (C#, VB) que muestran cómo proteger un libro de trabajo.
### **VSTO**
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

//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Protect the workbook specifying a password with Structure and Windows attributes.

excelApp.ActiveWorkbook.Protect("007", true, true);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......


//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.

workbook.Protect(ProtectionType.All,"007");

//Save As the excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}
## **Desproteger un libro de trabajo**
Para desproteger un libro de trabajo, use las siguientes líneas de código para VSTO (C#, VB) y Aspose.Cells for .NET (C#, VB).
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
