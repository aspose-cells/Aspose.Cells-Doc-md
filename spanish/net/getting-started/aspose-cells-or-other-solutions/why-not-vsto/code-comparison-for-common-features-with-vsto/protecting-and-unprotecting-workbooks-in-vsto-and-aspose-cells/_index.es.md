---
title: Proteger y desproteger libros de trabajo en VSTO y Aspose.Cells
type: docs
weight: 200
url: /es/net/protecting-and-unprotecting-workbooks-in-vsto-and-aspose-cells/
---
Para abrir un archivo de Excel Microsoft existente, proteja el libro de trabajo con estructura y atributos Windows y guarde el archivo.

continuación se muestran fragmentos de código paralelo para VSTO (C#) y Aspose.Cells for .NET (C#) que muestran cómo proteger un libro de trabajo.
## **VSTO**
**Proteger el libro de trabajo**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

   Excel.Application excelApp = Application;

//Excel.Application excelApp = Application;

//Specify the template excel file path.

  string myPath = "MyBook.xls";

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

**Libro de trabajo de desprotección**

{{< highlight "csharp" >}}

  //Unprotect the workbook specifying its password.

  excelApp.ActiveWorkbook.Unprotect("007");

{{< /highlight >}}
## **Aspose.Cells**
**Proteger el libro de trabajo**

{{< highlight "csharp" >}}

 //Specify the template excel file path.

   string myPath = "Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

   Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.

   workbook.Protect(ProtectionType.All, "007");

//Save As the excel file.

   workbook.Save("MyBook.xls");

{{< /highlight >}}

**Libro de trabajo de desprotección**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

  workbook.Unprotect("007");

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protecting.and.Unprotecting.Workbooks.Aspose.Cells.zip)
- [forjafuente](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip/descargar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).Código Postal)
