---
title: パブリック API Aspose.Cells 8.9.1 の変更点
type: docs
weight: 320
url: /ja/java/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.9.0 から 8.9.1 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **構成可能なフォント ソース**
Aspose.Cells for Java は、スプレッドシートをレンダリングするための構成可能なフォント ソースのサポートを提供するために、多くのクラスを公開しました。以下は、Aspose.Cells for Java 8.9.1 で追加されたクラスのリストです。

1. FontConfigs クラスは、フォント設定を指定します。
1. FontSourceBase クラスは、ユーザーがさまざまなフォント ソースを指定できるようにするクラスの抽象基本クラスです。
1. FileFontSource クラスは、ファイル システムに格納されている単一の TrueType フォント ファイルを表します。
1. FolderFontSource クラスは、TrueType フォント ファイルを含むフォルダーを表します。
1. MemoryFontSource クラスは、メモリに格納された単一の TrueType フォント ファイルを表します。
1. FontSourceType 列挙体は、フォント ソースの種類を指定します。

上記の変更により、Aspose.Cells for Java では、以下に示すようにフォントを設定できます。

1. FontConfigs.setFontFolder メソッドを使用して、1 つのカスタム フォント フォルダーを設定します。
1. FontConfigs.setFontFolders メソッドを使用して、複数のカスタム フォント フォルダーを設定します。
1. FontConfigs.setFontSources メソッドを使用して、カスタム フォント フォルダー、単一のフォント ファイル、またはバイト配列のフォント データからフォント ソースを設定します。

前述の方法の簡単な使用シナリオを次に示します。

**Java**

{{< highlight "csharp" >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[]{ fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[]bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

 FontConfigs.setFontFolder と FontConfigs.setFontFolders の両方のメソッドは、ブール型の 2 番目のパラメーターを受け入れます。 2 番目のパラメーターとして true を渡すと、Aspose.Cells API がフォント ファイルのサブフォルダーを検索するように指示されます。

{{% /alert %}} 

Aspose.Cells for Java では、フォントの置換を構成することもできます。このメカニズムは、変換が必要なマシンで必要なフォントが利用できない場合に役立ちます。ユーザーは、元々必要だったフォントの代わりに、フォント名のリストを提供できます。これを実現するために、Aspose.Cells API は、2 つのパラメーターを受け入れる FontConfigs.setFontSubstitutes メソッドを公開しました。最初のパラメーターは文字列型で、置換する必要があるフォントの名前にする必要があります。 2 番目のパラメーターは、string 型の配列です。ユーザーは、元のフォント名 (最初のパラメーターで指定) の代わりに、フォント名のリストを提供できます。

FontConfigs.SetFontSubstitutes メソッドの簡単な使用シナリオを次に示します。

**Java**

{{< highlight "csharp" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java は、どのソースと代替が設定されているかに関する情報を収集する手段も提供しています。

1. FontConfigs.getFontSources メソッドは、指定されたフォント ソースのリストを含む FontSourceBase タイプの配列を返します。ソースが設定されていない場合、FontConfigs.getFontSources メソッドは空の配列を返します。
1. FontConfigs.getFontSubstitutes メソッドは文字列型のパラメータを受け入れ、置換が設定されているフォント名を指定できます。指定されたフォント名に代替が設定されていない場合、FontConfigs.getFontSubstitutes メソッドは null を返します。

{{% alert color="primary" %}} 

 FontConfigs の詳細については、次の記事を参照してください。[スプレッドシートをレンダリングするためのフォントの構成](/cells/ja/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **IFilePathProvider インターフェイスと HtmlSaveOptions.FilePathProvider プロパティを追加**
Aspose.Cells for Java 8.9.1 では、ワークシートを個別の HTML ファイルにエクスポートするための IFilePathProvider を取得/設定できます。これらの新しい API は、あるワークシートのハイパーリンクが別のワークシート内の場所を指しているシナリオで役立ちます。アプリケーションの要件は、各ワークシートを個別の HTML ファイルにレンダリングすることです。 IFilePathProvider を実装すると、別の結果の HTML ファイル内の場所を指しているという事実に関係なく、前述のハイパーリンクをそのまま維持できます。

以下は、HtmlSaveOptions.FilePathProvider プロパティの簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 // Workbook のインスタンスにスプレッドシートをロードします

Workbook book = new Workbook(dir + "sample.xlsx");

//各ワークシートを個別の HTML ファイルに保存します

for (int i = 0; i< book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

この機能強化の詳細については、次の記事を参照してください。[IFilePathProvider インターフェイスの実装](/cells/ja/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **CopyOptions.ReferToDestinationSheet プロパティと Cells.copyRows メソッドのオーバーロードを追加**
Aspose.Cells for Java API は、コピーされる行にグラフとそのデータ ソースも含まれている場合に行のコピー操作を容易にするために、Cells.copyRows メソッドのオーバーロードと共にブール型の CopyOptions.ReferToDestinationSheet プロパティを公開しました。開発者は、これらの新しい API を利用して、グラフのデータ ソースをソースまたは宛先のワークシートに向けることができます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

この機能の詳細については、次の記事を参照してください。[行のコピー中にチャートのデータ ソースを制御する](/cells/ja/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **CalculationOptions.Recursive プロパティを追加しました**
Aspose.Cells for Java 8.9.1 では、ブール型の CalculationOptions.Recursive プロパティが公開されました。 CalculationOptions.Recursive プロパティを true に設定し、オブジェクトを Workbook.calculateFormula メソッドに渡すと、Aspose.Cells API は、他のセルに依存するセルを計算するときに、依存セルを再帰的に計算するように指示されます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

この機能の詳細については、次の記事を参照してください。[計算時間の最適化](/cells/ja/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **廃止された API**
### **廃止された CellsHelper.FontDir プロパティ**
代わりに、FontConfigs.setFontFolder(String, boolean) メソッドを false に再帰するフォルダーで使用することをお勧めします。
### **廃止された CellsHelper.FontDirs プロパティ**
代わりに、FontConfigs.setFontFolders(String[], boolean) メソッドを false に再帰するフォルダーで使用します。
### **廃止された CellsHelper.FontFiles プロパティ**
代わりに FontConfigs.setFontSources(FontSourceBase[]) メソッドを使用してください。
