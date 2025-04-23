---
title: Aspose.Cells 8.9.1のPublic API変更
type: docs
weight: 320
url: /ja/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

この文書は、Aspose.Cells APIのバージョン8.9.0から8.9.1への変更点をモジュール/アプリケーション開発者に興味を持つ可能性があるものを説明しています。新しいおよび更新されたパブリックメソッド、追加および削除されたクラスなどだけでなく、Aspose.Cellsの内部の挙動の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **設定可能なフォントソース**
Aspose.Cells for Javaは、スプレッドシートのレンダリングに設定可能なフォントソースを提供するためのいくつかのクラスを公開しました。以下に、Aspose.Cells for Java 8.9.1で追加されたクラスのリストがあります。

1. FontConfigsクラスはフォント設定を指定します。
1. FontSourceBaseクラスは、ユーザーがさまざまなフォントソースを指定できるクラスの抽象基本クラスです。
1. FileFontSourceクラスは、ファイルシステムに保存されている単一のTrueTypeフォントファイルを表します。
1. FolderFontSourceクラスは、TrueTypeフォントファイルが含まれているフォルダを表します。
1. MemoryFontSourceクラスは、メモリに保存されている単一のTrueTypeフォントファイルを表します。
1. FontSourceType列挙型は、フォントソースのタイプを指定します。

上記の変更が適用されると、Aspose.Cells for Javaでは以下のようにフォントを設定することができます。

1. FontConfigs.setFontFolderメソッドを使用してカスタムフォントフォルダを1つ設定します。
1. FontConfigs.setFontFoldersメソッドを使用して複数のカスタムフォントフォルダを設定します。
1. FontConfigs.setFontSourcesメソッドを使用してカスタムフォントフォルダ、単一のフォントファイルやバイト配列からのフォントデータを設定します。

上記のメソッドのシンプルな使用シナリオは次のとおりです。

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.setFontFolderおよびFontConfigs.setFontFoldersメソッドの両方は、2番目のパラメーターとしてBoolean型を受け入れます。2番目のパラメーターをtrueとして渡すと、Aspose.Cells APIはフォントファイルのサブフォルダを検索するようになります。 

{{% /alert %}} 

Aspose.Cells for Javaは、フォント置換を設定することも可能であります。これは、変換を行う必要のあるマシンで必要なフォントが利用できない場合に役立ちます。ユーザーは、元のフォント名の代替としてフォント名のリストを提供することができます。Aspose.Cells APIが公開したFontConfigs.setFontSubstitutesメソッドは、2つのパラメーターを受け入れます。1つ目のパラメーターは文字列型で、代替する必要があるフォント名になり、2番目のパラメーターは文字列型の配列です。ユーザーは、元のフォント名（1番目のパラメーターで指定）の代わりに提供するフォント名のリストを指定できます。

FontConfigs.SetFontSubstitutesメソッドのシンプルな使用シナリオは次のとおりです。

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Javaは、設定されたソースと代替の情報を収集する手段も提供しています。

1. FontConfigs.getFontSourcesメソッドは、指定されたフォントソースのリストを含むFontSourceBase型の配列を返します。ソースが設定されていない場合、FontConfigs.getFontSourcesメソッドは空の配列を返します。
1. FontConfigs.getFontSubstitutesメソッドは、フォント置換が設定されているフォント名を指定するstring型のパラメーターを受け入れます。指定されたフォント名に対して置換が設定されていない場合、FontConfigs.getFontSubstitutesメソッドはnullを返します。

{{% alert color="primary" %}} 

FontConfigsの詳細については、[スプレッドシートのレンダリング用フォントの設定](/cells/ja/java/configuring-fonts-for-rendering-spreadsheets/)の記事をご覧ください。

{{% /alert %}} 
### **IFilePathProviderインタフェースとHtmlSaveOptions.FilePathProviderプロパティを追加しました**
Aspose.Cells for Java 8.9.1では、ワークシートを個別のHTMLファイルにエクスポートするためのIFilePathProviderを取得/設定することができます。これらの新しいAPIは、1つのワークシートのハイパーリンクが別のワークシートの場所を指す場合や、アプリケーション要件が各ワークシートを個別のHTMLファイルにレンダリングする場合に役立ちます。IFilePathProviderを実装することで、前述のハイパーリンクが別の結果として得られるHTMLファイル内の場所を指していても、これらのハイパーリンクをそのまま保持することができます。

HtmlSaveOptions.FilePathProviderプロパティのシンプルな使用シナリオは次のとおりです。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

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

この拡張についての詳細については、[IFilePathProviderインタフェースの実装](/cells/ja/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)の記事をご覧ください。

{{% /alert %}} 
### **CopyOptions.ReferToDestinationSheetプロパティとCells.copyRowsメソッドのオーバーロードを追加しました**
Aspose.Cells for Java API は、Boolean 型の CopyOptions.ReferToDestinationSheet プロパティを公開しており、Cells.copyRows メソッドのオーバーロードも含まれているため、コピーする行にチャートとそのデータソースが含まれている場合の行のコピー操作を容易にすることができます。開発者はこれらの新しい API を使用して、チャートのデータソースをソースまたは宛先ワークシートに指示することができます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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

この機能の詳細については、[行のコピー時にチャートのデータソースを制御する](/cells/ja/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)の記事を参照してください。

{{% /alert %}} 
### **CalculationOptions.Recursive プロパティが追加されました**
Aspose.Cells for Java 8.9.1 では、CalculationOptions.Recursive プロパティの Boolean 型を公開しています。CalculationOptions.Recursive プロパティを true に設定し、そのオブジェクトを Workbook.calculateFormula メソッドに渡すことで、Aspose.Cells API は他のセルに依存するセルの計算時に、再帰的に依存セルを計算するように指示されます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

この機能の詳細については、[計算時間の最適化](/cells/ja/java/decrease-the-calculation-time-of-cell-calculate-method/)の記事を参照してください。

{{% /alert %}}
## **非推奨API**
### **非推奨の CellsHelper.FontDir プロパティ**
代わりに、FontConfigs.setFontFolder(String, boolean) メソッドを使用し、再帰を false に設定することを推奨します。
### **非推奨の CellsHelper.FontDirs プロパティ**
代わりに、FontConfigs.setFontFolders(String[], boolean) メソッドを使用し、再帰を false に設定することを推奨します。
### **非推奨の CellsHelper.FontFiles プロパティ**
代わりに、FontConfigs.setFontSources(FontSourceBase[]) メソッドを使用してください。
{{< app/cells/assistant language="java" >}}
