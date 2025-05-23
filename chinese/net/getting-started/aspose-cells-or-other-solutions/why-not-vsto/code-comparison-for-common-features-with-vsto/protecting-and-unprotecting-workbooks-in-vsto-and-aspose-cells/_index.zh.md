---
title: 在VSTO和Aspose.Cells中保护和取消保护工作簿
type: docs
weight: 200
url: /zh/net/protecting-and-unprotecting-workbooks-in-vsto-and-aspose-cells/
---

要打开现有的 Microsoft Excel 文件，请保护工作簿的结构和 Windows 属性，并保存文件。

下面是VSTO（C＃）和Aspose.Cells for .NET（C#）的并行代码片段，演示了如何保护工作簿。
## **VSTO**
**保护工作簿**

{{< highlight csharp >}}

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

**取消保护工作簿**

{{< highlight csharp >}}

  //Unprotect the workbook specifying its password.

  excelApp.ActiveWorkbook.Unprotect("007");

{{< /highlight >}}
## **Aspose.Cells**
**保护工作簿**

{{< highlight csharp >}}

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

**取消保护工作簿**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

  workbook.Unprotect("007");

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protecting.and.Unprotecting.Workbooks.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
