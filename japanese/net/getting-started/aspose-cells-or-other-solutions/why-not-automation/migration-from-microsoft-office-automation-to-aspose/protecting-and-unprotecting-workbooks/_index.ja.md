---
title: ブックの保護と保護解除
type: docs
weight: 20
url: /ja/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

誤ってもしくは意図的にワークシートの変更、移動、削除を防止するために、ワークブックの要素をパスワード付きもしくはパスワードなしで保護することができます。ワークブックの構造を保護して、ワークブック内のワークシートを移動、削除、非表示、非非表示、名前変更できなくし、新しいワークシートを挿入できないようにするには、ProtectionType を Structure に指定します。

ワークブックが開かれるたびにウィンドウを同じサイズおよび位置に保護するには、ProtectionType を Windows に指定します。この記事では、VSTO と Aspose.Cells for .NET を使用してワークブックを[保護](/cells/ja/net/protecting-and-unprotecting-workbooks/)および[保護解除](/cells/ja/net/protecting-and-unprotecting-workbooks/)する方法を示します。

Aspose.Cells は Microsoft Office Automation とは独立して動作し、使用が簡単で整ったコードを生成するように開発されています。

ワークブックを保護しても、ユーザーがセルを編集するのを止めることはできません。データを保護するためには、ワークシートを保護する必要があります。

{{% /alert %}} 
## **ワークブックの保護**
既存のMicrosoft Excelファイルを開き、ブックの構造とウィンドウ属性でファイルを保護し、ファイルを保存します。

以下に、VSTO (C#、VB) および Aspose.Cells for .NET (C#、VB) 向けの並列コードスニペットを示し、ワークブックを保護する方法を比較する。
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
## **ワークブックの保護解除**
ワークブックの保護解除には、VSTO (C#、VB) および Aspose.Cells for .NET (C#、VB) 向けの次のコードを使用します。
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
{{< app/cells/assistant language="csharp" >}}
