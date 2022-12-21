---
title: パブリック API Aspose.Cells 8.7.0 の変更点
type: docs
weight: 230
url: /ja/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.6.3 から 8.7.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **VBA プロジェクトのデジタル署名、検出、抽出のサポート**
Aspose.Cells for .NET のこのリリースでは、VBA プロジェクトのデジタル署名、VBA プロジェクトが署名済みで有効かどうかの検出などのタスクでユーザーを支援するいくつかの新しいプロパティとメソッドが公開されています。さらに、新しい API を使用すると、Workbook でデジタル署名された VBA プロジェクトから生データとして証明書を抽出できます。
###### **VBA プロジェクトにデジタル署名する**
Aspose.Cells for .NET 8.7.0 で使用できる VbaProject.Sign メソッドが公開されました。[ワークブックで VBA プロジェクトにデジタル署名する](/cells/ja/net/digitally-sign-a-vba-code-project-with-certificate/).上記のメソッドは、Aspose.Cells.DigitalSignatures 名前空間に存在する DigitalSignature クラスのインスタンスを受け入れます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **デジタル署名された VBA プロジェクトの検出**
新しく公開された VbaProject.IsSigned プロパティは、[ワークブック内の VBA プロジェクトがデジタル署名されているかどうかを検出する](/cells/ja/net/check-if-vba-code-is-signed/). VbaProject.IsSigned プロパティはブール型で、VBA プロジェクトがデジタル署名されている場合は true を返し、その逆の場合も同様です。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **VBA プロジェクトからのデジタル署名の抽出**
API のこのリビジョンでは、VbaProject.CertRawData プロパティも公開されています。[VBA プロジェクトからデジタル証明書の生データを抽出する](/cells/ja/net/export-vba-certificate-to-file-or-stream/)VbaProject.CertRawData プロパティはバイト配列型で、VBA プロジェクトがデジタル署名されている場合は未加工の証明書データが含まれます。それ以外の場合、前述のプロパティは null になります。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **VBA プロジェクトのデジタル署名を検証する**
public API へのもう 1 つの追加は、VbaProject.IsValidSigned プロパティです。[VBA プロジェクトのデジタル署名の検証](/cells/ja/net/check-if-digital-signature-of-vba-code-is-valid/).上記のプロパティは、デジタル署名が有効な場合は true を返し、署名が無効な場合は false を返します。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **メソッド Protection.VerifyPassword が追加されました**
Aspose.Cells for .NET 8.7.0 では、次の目的で使用できる Protection.VerifyPassword メソッドが公開されました。[ワークシートを保護するために使用されるパスワードを確認してください](/cells/ja/net/verify-password-used-to-protect-the-worksheet/).このメソッドは文字列のインスタンスをパラメーターとして受け取り、指定されたパスワードがワークシートの保護に使用されているパスワードと一致する場合に true を返します。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **プロパティ Protection.IsProtectedWithPassword が追加されました**
Aspose.Cells for .NET API のこのリリースでは、次の場合に役立つ Protection.IsProtectedWithPassword プロパティも公開されています。[ワークシートがパスワードで保護されているかどうかを検出する](/cells/ja/net/detect-if-worksheet-is-password-protected/).

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **プロパティ ColorScale.Is3ColorScale が追加されました**
 Aspose.Cells for .NET 8.7.0 では、2 色スケールの条件付き書式の作成に使用できる ColorScale.Is3ColorScale プロパティが公開されています。上記のプロパティはブール型で、デフォルト値は true です。これは、条件付き書式がデフォルトで 3 色スケールになることを意味します。ただし、ColorScale.Is3ColorScale プロパティを false に切り替えると、[2 色スケールの条件付き書式を生成する](/cells/ja/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **プロパティ TxtLoadOptions.HasFormula が追加されました**
Aspose.Cells for .NET 8.7.0 は[区切られたプレーンデータを含む CSV/TXT ファイルを読み込みながら、数式を識別して解析します](/cells/ja/net/load-or-import-csv-file-with-formulas/).新しく公開された TxtLoadOptions.HasFormula プロパティを true に設定すると、API が入力区切りファイルから数式を解析し、追加の処理を必要とせずに関連するセルに設定するように指示されます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **プロパティ DataLabels.IsResizeShapeToFitText が追加されました**
Aspose.Cells for .NET 8.7.0 が公開したもう 1 つの便利な機能は、DataLabels.IsResizeShapeToFitText プロパティです。[テキストに合わせて図形のサイズを変更する](/cells/ja/net/resize-chart-s-data-label-shape-to-fit-text/)グラフのデータ ラベル用の Excel アプリケーションの機能。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **プロパティ PdfSaveOptions.OptimizationType が追加されました**
8.7.0 は、ユーザーが容易に[スプレッドシートを PDF 形式にエクスポートする際に、目的の最適化アルゴリズムを選択します](/cells/ja/net/save-excel-into-pdf-with-standard-or-minimum-size/).以下に詳述するように、PdfSaveOptions.OptimizationType プロパティには 2 つの可能な値があります。

1. PdfOptimizationType.MinimumSize: 結果のファイル サイズに対して品質が低下します。
1. PdfOptimizationType.Standard: 品質が損なわれないため、結果のファイル サイズが大きくなります。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **削除された API**
### **プロパティ Workbook.SaveOptions が削除されました**
Workbook.SaveOptions プロパティは、しばらく前に廃止されました。このリリースでは、パブリック API から完全に削除されたため、代わりに Workbook.Save(Stream, SaveOptions) または Workbook.Save(string, SaveOptions) メソッドを使用することをお勧めします。
