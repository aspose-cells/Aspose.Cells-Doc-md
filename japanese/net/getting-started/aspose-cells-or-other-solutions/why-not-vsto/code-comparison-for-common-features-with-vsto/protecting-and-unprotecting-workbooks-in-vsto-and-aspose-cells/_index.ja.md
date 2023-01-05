---
title: VSTO および Aspose.Cells でブックを保護および保護解除する
type: docs
weight: 200
url: /ja/net/protecting-and-unprotecting-workbooks-in-vsto-and-aspose-cells/
---
既存の Microsoft Excel ファイルを開くには、ワークブックを構造と Windows 属性で保護し、ファイルを保存します。

以下は、ワークブックを保護する方法を示す VSTO (C#) および Aspose.Cells for .NET (C#) の並列コード スニペットです。
## **VSTO**
**ブックの保護**

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

**ブックの保護を解除しています**

{{< highlight "csharp" >}}

  //Unprotect the workbook specifying its password.

  excelApp.ActiveWorkbook.Unprotect("007");

{{< /highlight >}}
## **Aspose.Cells**
**ブックの保護**

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

**ブックの保護を解除しています**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

  workbook.Unprotect("007");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protecting.and.Unprotecting.Workbooks.Aspose.Cells.zip)
- [ソースフォージ](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip/ダウンロード)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\)。ジップ）
