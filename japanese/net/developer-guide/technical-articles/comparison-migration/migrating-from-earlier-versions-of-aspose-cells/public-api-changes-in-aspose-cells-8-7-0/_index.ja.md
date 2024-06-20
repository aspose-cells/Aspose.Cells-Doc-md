---
title: Aspose.Cells 8.7.0の公開API変更
type: docs
weight: 230
url: /ja/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells APIの8.6.3から8.7.0への変更について記載しており、モジュール／アプリケーション開発者に関心がある可能性のある変更を説明しています。新しいおよび更新された公開メソッド、追加および削除されたクラスなどに加えて、Aspose.Cellsの裏側の挙動に変更がある場合も含まれています。

{{% /alert %}} 
## **APIの追加**
### **VBAプロジェクトのデジタル署名、検出、および抽出のサポート**
このリリースのAspose.Cells for .NETでは、ユーザーがVBAプロジェクトにデジタル署名を行ったり、VBAプロジェクトが署名されているかどうかを検出したり、有効かどうかを確認したりするための新しいプロパティやメソッドがいくつか公開されています。さらに、新しいAPIでは、署名されたVBAプロジェクトから証明書を生データとして抽出することもできます。
###### **VBAプロジェクトにデジタル署名**
Aspose.Cells for .NET 8.7.0では、VbaProject.Signメソッドが公開され、[ワークブック内のVBAプロジェクトにデジタル署名](/cells/ja/net/digitally-sign-a-vba-code-project-with-certificate/)するために使用できます。このメソッドは、Aspose.Cells.DigitalSignaturesネームスペースに属するDigitalSignatureクラスのインスタンスを受け入れます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **デジタルに署名されたVBAプロジェクトの検出**
新しく公開されたVbaProject.IsSignedプロパティを使用して、ワークブック内のVBAプロジェクトがデジタルで署名されているかどうかを[検出](/cells/ja/net/check-if-vba-code-is-signed/)できます。VbaProject.IsSignedプロパティはブール型で、VBAプロジェクトがデジタルで署名されている場合はtrueを返し、その逆も同様です。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


###### **VBAプロジェクトからのデジタル署名の抽出**
このAPIのこのリビジョンでは、VbaProject.CertRawDataプロパティも公開されており、VBAプロジェクトからデジタル証明書の生データを[抽出することができます](/cells/ja/net/export-vba-certificate-to-file-or-stream/)。VbaProject.CertRawDataプロパティはバイト配列の型で、VBAプロジェクトがデジタルで署名されている場合は生の証明書データが含まれ、それ以外の場合はnullになります。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **VBAプロジェクトのデジタル署名の検証**
公開APIへのもう1つの追加は、VbaProject.IsValidSignedプロパティです。これは[VBAプロジェクトのデジタル署名を検証するのに役立ちます](/cells/ja/net/check-if-digital-signature-of-vba-code-is-valid/)。該当するプロパティは、デジタル署名が有効な場合はtrueを返し、無効な場合はfalseを返します。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **Protection.VerifyPasswordメソッドの追加**
Aspose.Cells for .NET 8.7.0では、Worksheetを保護するために使用されるパスワードを[検証するメソッドProtection.VerifyPassword](/cells/ja/net/verify-password-used-to-protect-the-worksheet/)が公開されました。このメソッドは、stringのインスタンスをパラメーターとして受け入れ、指定されたパスワードがWorksheetを保護するために使用されたパスワードと一致する場合はtrueを返します。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **Protection.IsProtectedWithPasswordプロパティの追加**
このAspose.Cells for .NET APIのリリースでは、Protection.IsProtectedWithPasswordプロパティも公開され、[ワークシートがパスワードで保護されているかどうかを検出するのに役立ちます](/cells/ja/net/detect-if-worksheet-is-password-protected/)。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **Added ColorScale.Is3ColorScale Property**
Aspose.Cells for .NET 8.7.0では、ColorScale.Is3ColorScaleプロパティも公開され、2-Color Scale条件付き書式を作成するために使用することができます。該当するプロパティはデフォルト値がtrueのBoolean型であり、これは条件付き書式がデフォルトで3-Color Scaleになることを意味します。ただし、ColorScale.Is3ColorScaleプロパティをfalseに切り替えると、[2-Color Scale条件付き書式が生成されます](/cells/ja/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **Added TxtLoadOptions.HasFormula Property**
Aspose.Cells for .NET 8.7.0では、区切られたプレーンデータを含むCSV/TXTファイルをロードする際に、[数式を識別および解析するためのサポート](/cells/ja/net/load-or-import-csv-file-with-formulas/)が提供されました。新たに公開されたTxtLoadOptions.HasFormulaプロパティは、trueに設定されている場合、APIに対して入力区切りファイルから数式を解析し、それらを追加の処理を必要とせずに関連するセルに設定するよう指示します。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **DataLabels.IsResizeShapeToFitTextプロパティの追加**
Aspose.Cells for .NET 8.7.0が公開したもう1つの有用な機能は、DataLabels.IsResizeShapeToFitTextプロパティで、これはExcelアプリケーションの[チャートのデータラベルのテキストに合わせてサイズを調整](/cells/ja/net/resize-chart-s-data-label-shape-to-fit-text/)する機能を有効にすることができます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **PdfSaveOptions.OptimizationTypeプロパティの追加**
Aspose.Cells for .NET 8.7.0では、PdfSaveOptions.OptimizationTypeプロパティとPdfOptimizationType列挙型が公開され、スプレッドシートをPDF形式にエクスポートする際に[希望する最適化アルゴリズムを選択](/cells/ja/net/save-excel-into-pdf-with-standard-or-minimum-size/)できるようになりました。PdfSaveOptions.OptimizationTypeプロパティの可能な値は次の通りです。

1. PdfOptimizationType.MinimumSize: ファイルサイズのために品質が犠牲になります。
1. PdfOptimizationType.Standard: 品質が犠牲にならず、したがってファイルサイズが大きくなります。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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
## **API が削除されました**
### **Workbook.SaveOptionsプロパティが削除されました**
Workbook.SaveOptionsプロパティは以前から廃止されていました。このリリースで、それが公開APIから完全に削除されました。したがって、代替としてWorkbook.Save(Stream、SaveOptions)またはWorkbook.Save(string、SaveOptions)メソッドを使用することが推奨されています。
