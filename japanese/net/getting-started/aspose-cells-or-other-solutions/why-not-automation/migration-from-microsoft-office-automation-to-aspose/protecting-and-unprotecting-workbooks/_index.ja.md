---
title: ワークブックの保護と保護解除
type: docs
weight: 20
url: /ja/net/protecting-and-unprotecting-workbooks/
---
{{% alert color="primary" %}} 

誰かが誤ってまたは故意にワークシートを変更、移動、または削除するのを防ぐために、パスワードを使用して、または使用せずにブック要素を保護できます。ブック内のワークシートを移動、削除、非表示、再表示、または名前変更したり、新しいワークシートを挿入したりできないようにブックの構造を保護するには、ProtectionType を Structure として指定します。

ワークブックを開くたびに同じサイズと位置になるように Windows を保護するには、ProtectionType を Windows として指定します。この記事では、その方法を示します。[守る](/cells/ja/net/protecting-and-unprotecting-workbooks/)と[保護を解除する](/cells/ja/net/protecting-and-unprotecting-workbooks/)VSTO と Aspose.Cells for .NET を使用するワークブックで、2 つの方法を比較できます。

Aspose.Cells は Microsoft Office Automation とは独立して動作し、使いやすく、きちんとしたコードを生成するように開発されています。

ワークブックを保護しても、ユーザーがセルを編集できなくなるわけではありません。データを保護するには、ワークシートを保護する必要があります。

{{% /alert %}} 
## **ワークブックの保護**
既存の Microsoft Excel ファイルを開くには、ワークブックを構造と Windows 属性で保護し、ファイルを保存します。

以下は、ワークブックを保護する方法を示す VSTO (C#、VB) および Aspose.Cells for .NET (C#、VB) の並列コード スニペットです。
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
## **ワークブックの保護解除**
ブックの保護を解除するには、VSTO (C#、VB) および Aspose.Cells for .NET (C#、VB) の次のコード行を使用します。
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
