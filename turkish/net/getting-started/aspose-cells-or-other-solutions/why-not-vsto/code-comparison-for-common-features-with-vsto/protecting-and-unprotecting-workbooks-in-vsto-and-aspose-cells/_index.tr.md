---
title: VSTO ve Aspose.Cells te Çalışma Kitaplarının Korunması ve Korumanın Kaldırılması
type: docs
weight: 200
url: /tr/net/protecting-and-unprotecting-workbooks-in-vsto-and-aspose-cells/
---

Var olan bir Microsoft Excel dosyasını açın, çalışma kitabını yapı ve Windows özellikleriyle koruyun ve dosyayı kaydedin.

VSTO (C#) ve Aspose.Cells for .NET (C#) için çalışma kitabını korumanın nasıl yapılacağını gösteren paralel kod parçacıkları aşağıda gösterilmektedir.
## **VSTO**
**Çalışma Kitabını Koruma**

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

**Çalışma Kitabının Korumasını Kaldırma**

{{< highlight csharp >}}

  //Unprotect the workbook specifying its password.

  excelApp.ActiveWorkbook.Unprotect("007");

{{< /highlight >}}
## **Aspose.Cells**
**Çalışma Kitabını Koruma**

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

**Çalışma Kitabının Korumasını Kaldırma**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

  workbook.Unprotect("007");

{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protecting.and.Unprotecting.Workbooks.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
