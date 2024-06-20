---
title: Proteger y desproteger libros de trabajo
type: docs
weight: 20
url: /es/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

Para evitar que alguien cambie, mueva o elimine hojas de cálculo accidental o deliberadamente, puedes proteger elementos del libro de trabajo con o sin contraseña. Para proteger la estructura de un libro de trabajo de modo que las hojas de cálculo del libro no se puedan mover, eliminar, ocultar, mostrar, desocultar o cambiar el nombre, y no se puedan insertar nuevas hojas de cálculo, especifica el ProtectionType como Estructura.

Para proteger las ventanas de modo que tengan el mismo tamaño y la misma posición cada vez que se abre el libro de trabajo, especifica el ProtectionType como Ventanas. En este artículo, mostramos cómo [proteger](/cells/es/net/protecting-and-unprotecting-workbooks/) y [desproteger](/cells/es/net/protecting-and-unprotecting-workbooks/) libros de trabajo utilizando VSTO y Aspose.Cells for .NET para que puedas comparar ambos métodos.

Aspose.Cells funciona de forma independiente de la Automatización de Microsoft Office y está diseñado para ser fácil de usar y generar un código ordenado.

Proteger un libro de trabajo no impide que los usuarios editen celdas. Para proteger los datos, debes proteger las hojas de cálculo.

{{% /alert %}} 
## **Proteger un libro de trabajo**
Para abrir un archivo de Microsoft Excel existente, proteger el libro con atributos de estructura y de Windows y guardar el archivo.

A continuación se muestran fragmentos de código paralelos para VSTO (C#, VB) y Aspose.Cells for .NET (C#, VB) que muestran cómo proteger un libro.
### **VSTO**
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

{{< highlight csharp >}}

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
## **Desproteger un Libro**
Para desproteger un libro, use las siguientes líneas de código para VSTO (C#, VB) y Aspose.Cells for .NET (C#, VB).
### **VSTO**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
