---
title: パブリック API Aspose.Cells 8.7.0 の変更点
type: docs
weight: 240
url: /ja/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.6.3 から 8.7.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **PDF 最適化のサポート**
Aspose.Cells API は、スプレッドシートを PDF に変換する機能を既に提供しています。[結果の PDF サイズを最適化する](/cells/ja/java/save-excel-into-pdf-with-standard-or-minimum-size/)同じように。 Aspose.Cells for Java 8.7.0 では、スプレッドシートを PDF 形式にエクスポートする際に、ユーザーが目的の最適化アルゴリズムを簡単に選択できるように、PdfOptimizationType 列挙とともに PdfSaveOptions.OptimizationType プロパティが公開されています。以下に詳述するように、PdfSaveOptions.OptimizationType プロパティには 2 つの可能な値があります。

1. PdfOptimizationType.MINIMUM_SIZE: 結果のファイル サイズに対して品質が低下します。
1. PdfOptimizationType.STANDARD: 品質が損なわれないため、結果のファイル サイズが大きくなります。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **デジタル署名された VBA プロジェクトの検出**
新しく公開された VbaProject.isSigned プロパティは、[ワークブック内の VBA プロジェクトがデジタル署名されているかどうかを検出する](/cells/ja/java/check-if-vba-code-is-signed/)VbaProject.isSigned プロパティはブール型で、VBA プロジェクトがデジタル署名されている場合は true を返し、その逆の場合も同様です。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **メソッド Protection.verifyPassword が追加されました**
Aspose.Cells API は、文字列のインスタンスとしてパスワードを指定できるようにする verifyPassword メソッドを導入することにより、Protection クラスを強化しました。[ワークシートを保護するために同じパスワードが使用されているかどうかを確認します](/cells/ja/java/verify-password-used-to-protect-the-worksheet/)Protection.verifyPassword メソッドは、指定されたパスワードが指定されたワークシートを保護するために使用されるパスワードと一致する場合は true を返し、指定されたパスワードが一致しない場合は false を返します。次のコードは、Protection.isProtectedWithPassword フィールドと組み合わせて Protection.verifyPassword メソッドを使用して、パスワード保護を検出し、パスワードを検証します。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **プロパティ Protection.isProtectedWithPassword が追加されました**
Aspose.Cells for Java のこのリリースでは、次の場合に役立つ Protection.isProtectedWithPassword フィールドも公開されています。[ワークシートがパスワードで保護されているかどうかを検出する](/cells/ja/java/detect-if-worksheet-is-password-protected/).

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **プロパティ ColorScale.Is3ColorScale が追加されました**
Aspose.Cells for Java 8.7.0 では、ColorScale.Is3ColorScale プロパティが公開されました。[色スケールの条件付き書式を作成する](/cells/ja/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/).上記のプロパティはブール型で、デフォルト値は true です。これは、条件付き書式がデフォルトで 3 色スケールになることを意味します。ただし、ColorScale.Is3ColorScale プロパティを false に切り替えると、2 色スケールの条件付き書式が生成されます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **プロパティ TxtLoadOptions.HasFormula が追加されました**
Aspose.Cells for Java 8.7.0 は[区切られたプレーンデータを含むCSV/TXTファイルをロードしながら、式を識別して解析します](/cells/ja/java/load-or-import-csv-file-with-formulas/).新しく公開された TxtLoadOptions.HasFormula プロパティを true に設定すると、API が入力区切りファイルから数式を解析し、追加の処理を必要とせずに関連するセルに設定するように指示されます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **プロパティ DataLabels.ResizeShapeToFitText が追加されました**
Aspose.Cells for Java 8.7.0 が公開したもう 1 つの便利な機能は、DataLabels.ResizeShapeToFitText プロパティです。[テキストに合わせて図形のサイズを変更する](/cells/ja/java/resize-chart-s-data-label-shape-to-fit-text/)グラフのデータ ラベル用の Excel アプリケーションの機能。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
## **削除された API**
### **プロパティ Workbook.SaveOptions が削除されました**
Workbook.SaveOptions プロパティは、しばらく前に廃止されました。このリリースでは、パブリック API から完全に削除されたため、代わりに Workbook.save(Stream, SaveOptions) または Workbook.save(string, SaveOptions) メソッドを使用することをお勧めします。
