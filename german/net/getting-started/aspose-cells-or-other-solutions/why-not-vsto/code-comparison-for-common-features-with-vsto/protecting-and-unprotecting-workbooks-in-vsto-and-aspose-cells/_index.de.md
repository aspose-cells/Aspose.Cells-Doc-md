---
title: Schützen und Aufheben des Schutzes von Arbeitsmappen in VSTO und Aspose.Cells
type: docs
weight: 200
url: /de/net/protecting-and-unprotecting-workbooks-in-vsto-and-aspose-cells/
---
Um eine vorhandene Microsoft-Excel-Datei zu öffnen, schützen Sie die Arbeitsmappe mit Struktur- und Windows-Attributen und speichern Sie die Datei.

Nachfolgend finden Sie parallele Codeausschnitte für VSTO (C#) und Aspose.Cells for .NET (C#), die zeigen, wie eine Arbeitsmappe geschützt wird.
## **VSTO**
**Arbeitsmappe schützen**

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

**Schutz der Arbeitsmappe aufheben**

{{< highlight "csharp" >}}

  //Unprotect the workbook specifying its password.

  excelApp.ActiveWorkbook.Unprotect("007");

{{< /highlight >}}
## **Aspose.Cells**
**Arbeitsmappe schützen**

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

**Schutz der Arbeitsmappe aufheben**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

  workbook.Unprotect("007");

{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protecting.and.Unprotecting.Workbooks.Aspose.Cells.zip)
- [Quellenschmiede](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip/herunterladen)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).Postleitzahl)
