---
title: Aspose.Cells 8.7.0の公開API変更
type: docs
weight: 240
url: /ja/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells APIの8.6.3から8.7.0への変更について記載しており、モジュール／アプリケーション開発者に関心がある可能性のある変更を説明しています。新しいおよび更新された公開メソッド、追加および削除されたクラスなどに加えて、Aspose.Cellsの裏側の挙動に変更がある場合も含まれています。

{{% /alert %}} 
## **APIの追加**
### **PDF最適化のサポート**
Aspose.Cells APIは既にスプレッドシートをPDFに変換する機能を提供しています。このAPIのこのリリースでは、結果となるPDFサイズを[最適化](/cells/ja/java/save-excel-into-pdf-with-standard-or-minimum-size/)することができます。Aspose.Cells for Java 8.7.0では、PdfSaveOptions.OptimizationTypeプロパティとPdfOptimizationType列挙型が公開され、スプレッドシートをPDF形式にエクスポートする際に希望の最適化アルゴリズムを選択するための機能をユーザーに提供します。PdfSaveOptions.OptimizationTypeプロパティには以下の2つの可能な値があります。 

1. PdfOptimizationType.MINIMUM_SIZE: 結果ファイルサイズのために品質が犠牲になります。
1. PdfOptimizationType.STANDARD: 品質は犠牲にされず、結果ファイルサイズは大きくなります。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **デジタルに署名されたVBAプロジェクトの検出**
新しく公開されたVbaProject.isSignedプロパティを使用して、ワークブック内のVBAプロジェクトが[デジタルに署名されているかどうかを検出](/cells/ja/java/check-if-vba-code-is-signed/)することができます。VbaProject.isSignedプロパティはBoolean型で、VBAプロジェクトがデジタルに署名されている場合はtrueを返し、それ以外の場合はfalseを返します。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **Protection.verifyPasswordメソッドの追加**
Aspose.Cells APIは、Protectionクラスを改良し、[指定したパスワードを使用してワークシートを保護したかどうかを検証](/cells/ja/java/verify-password-used-to-protect-the-worksheet/)するためのverifyPasswordメソッドを導入しました。Protection.verifyPasswordメソッドは、指定したパスワードが指定されたワークシートを保護するために使用されたパスワードと一致する場合はtrueを返し、一致しない場合はfalseを返します。次のコードはProtection.verifyPasswordメソッドをProtection.isProtectedWithPasswordフィールドと組み合わせて使用してパスワード保護を検出し、パスワードを検証します。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **Added Protection.isProtectedWithPassword Property**
Aspose.Cells for Java のこのリリースでは、Protection.isProtectedWithPassword フィールドが公開されました。これは [Worksheet がパスワードで保護されているかどうかを検出する際に役立ちます](/cells/ja/java/detect-if-worksheet-is-password-protected/)。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **Added ColorScale.Is3ColorScale Property**
Aspose.Cells for Java の 8.7.0 では、ColorScale.Is3ColorScale プロパティが公開されました。これは [2 色尺度の条件付き書式を追加すること](/cells/ja/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/) に使用できます。このプロパティは、既定値が true の Boolean 型であり、これは条件付き書式がデフォルトで 3 色スケールになることを意味します。ただし、ColorScale.Is3ColorScale プロパティを false に切り替えると、2 色尺度の条件付き書式が生成されます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **Added TxtLoadOptions.HasFormula Property**
Aspose.Cells for Java の 8.7.0 では、入力区切りファイルから数式を識別および解析するサポートが提供されました。新しく公開された TxtLoadOptions.HasFormula プロパティは、true に設定すると、API に入力区切りファイルから数式を解析し、関連するセルに設定するよう指示します。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **Added DataLabels.ResizeShapeToFitText Property**
Aspose.Cells for Java の 8.7.0 で公開された便利な機能の1つは、DataLabels.ResizeShapeToFitText プロパティです。これにより、Excel アプリケーションのグラフのデータラベルの[テキストに合わせて形状を調整](/cells/ja/java/resize-chart-s-data-label-shape-to-fit-text/)することができます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **API が削除されました**
### **Removed Workbook.SaveOptions Property**
Workbook.SaveOptions プロパティは以前から非推奨とされていました。このリリースで、これは公開 API から完全に削除されたため、代替として Workbook.save(Stream, SaveOptions) または Workbook.save(string, SaveOptions) メソッドを使用することが推奨されています。
{{< app/cells/assistant language="java" >}}
