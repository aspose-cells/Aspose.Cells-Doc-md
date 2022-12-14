---
title: Inserción y eliminación de comentarios Cell en una hoja de trabajo
type: docs
weight: 30
url: /es/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

Generalmente, los comentarios se utilizan para agregar información adicional a las celdas de una hoja de cálculo. Los usamos de vez en cuando y los eliminamos cuando ya no los necesitamos. Los comentarios son útiles si necesita documentar un valor particular o para recordar lo que hace una fórmula. Cuando mueve el puntero del mouse sobre una celda que tiene un comentario, el comentario aparece en un cuadro pequeño.

En este artículo, comparamos cómo agregar y quitar comentarios de celdas usando VSTO y Aspose.Cells for .NET. Aspose.Cells for .NET funciona con archivos de Excel Microsoft independientemente de Office Automation y le brinda herramientas poderosas para crear y manipular hojas de cálculo.

{{% /alert %}}

## **Agregar y eliminar comentarios en Cells**

Para agregar comentarios a las celdas:

1. Abra un archivo de Excel existente.
1. Agregar un comentario a una celda.
1. Guarda el archivo.

Para eliminar los comentarios, el proceso es similar, con la excepción de que se elimina el comentario.

 Los ejemplos de código a continuación ilustran primero cómo[añadir un comentario](/cells/es/net/inserting-and-removing-cell-comments-in-a-worksheet/) y luego como[eliminar un comentario](/cells/es/net/inserting-and-removing-cell-comments-in-a-worksheet/) con VSTO o Aspose.Cells for .NET.

## **Inserción de comentarios**

 Estos fragmentos de código muestran cómo agregar un comentario a una celda primero con[VSTO](/cells/es/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) y luego con[Aspose.Cells for .NET](/cells/es/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB).

### **Insertar un comentario con VSTO**

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

string myPath=@"d:\test\Book1.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the A1 cell.

Excel.Range rng1=excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

rng1.AddComment("This is my comment");

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **Insertar un comentario con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

int commentIndex=workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

Comment comment=workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

comment.Note="This is my comment";

//Save As the excel file.

workbook.Save(@"d:\test\Book1.xls");



{{< /highlight >}}

## **Eliminar comentarios**

 Para eliminar un comentario de una celda, use las siguientes líneas de código para[VSTO](/cells/es/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) y[Aspose.Cells](/cells/es/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET (C#, VB).

### **Eliminación de un comentario con VSTO**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Eliminar un comentario con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
