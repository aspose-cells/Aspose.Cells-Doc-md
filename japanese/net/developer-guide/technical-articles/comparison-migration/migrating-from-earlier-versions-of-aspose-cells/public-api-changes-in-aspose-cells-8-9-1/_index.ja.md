---
title: Aspose.Cells 8.9.1のPublic API変更
type: docs
weight: 310
url: /ja/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

この文書は、Aspose.Cells APIのバージョン8.9.0から8.9.1への変更点をモジュール/アプリケーション開発者に興味を持つ可能性があるものを説明しています。新しいおよび更新されたパブリックメソッド、追加および削除されたクラスなどだけでなく、Aspose.Cellsの内部の挙動の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **設定可能なフォントソース**
Aspose.Cells for .NETは、スプレッドシートのレンダリングに設定可能なフォントソースをサポートするためのクラス群を公開しました。以下は、Aspose.Cells for .NET 8.9.1で追加されたクラスのリストです。

1. FontConfigsクラスはフォント設定を指定します。
1. FontSourceBaseクラスは、ユーザーがさまざまなフォントソースを指定できるクラスの抽象基本クラスです。
1. FileFontSourceクラスは、ファイルシステムに保存されている単一のTrueTypeフォントファイルを表します。
1. FolderFontSourceクラスは、TrueTypeフォントファイルが含まれているフォルダを表します。
1. MemoryFontSourceクラスは、メモリに保存されている単一のTrueTypeフォントファイルを表します。
1. FontSourceType列挙型は、フォントソースのタイプを指定します。

上記の変更により、Aspose.Cells for .NETでは以下のようにフォントを設定することができます。

1. FontConfigs.SetFontFolderメソッドを使用して、カスタムフォントフォルダを1つ設定します。
1. FontConfigs.SetFontFoldersメソッドを使用して、複数のカスタムフォントフォルダを設定します。
1. FontConfigs.SetFontSourcesメソッドを使用して、カスタムフォントフォルダ、単一のフォントファイル、またはバイト配列からフォントソースを設定します。

上記のメソッドのシンプルな使用シナリオは次のとおりです。

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.SetFontFolderおよびFontConfigs.SetFontFoldersメソッドは、第2パラメータとしてBoolean型を受け入れます。第2パラメータにtrueを渡すと、Aspose.Cells APIはフォントファイルのサブフォルダを検索します。

{{% /alert %}} 

Aspose.Cells for .NETはまた、フォントの置換を設定することができます。これは、必要なフォントが変換を行うマシンに存在しない場合に役立ちます。ユーザーは、元々必要とされているフォントの代替として、フォント名のリストを提供できます。これを実現するために、Aspose.Cells APIはFontConfigs.SetFontSubstitutesメソッドを公開しており、2つのパラメータを受け入れます。第1パラメータはstring型であり、代替にする必要のあるフォントの名前でなければなりません。第2パラメータはstring型の配列です。ユーザーは、元のフォント名（第1パラメータで指定された名前）の代替として、フォント名のリストを提供できます。

FontConfigs.SetFontSubstitutesメソッドのシンプルな使用シナリオは次のとおりです。

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NETは、設定されたソースと置換の情報を収集する手段も提供しています。

1. FontConfigs.GetFontSourcesメソッドは、指定されたフォントソースのリストを含むFontSourceBase型の配列を返します。ソースが設定されていない場合、FontConfigs.GetFontSourcesメソッドは空の配列を返します。
1. FontConfigs.GetFontSubstitutesメソッドは、指定されたフォント名の代替が設定されている場合に、nullを返します。代替が指定されていない場合はnullを返します。

{{% alert color="primary" %}} 

FontConfigsの詳細については、[スプレッドシートのレンダリング用フォントの構成](/cells/ja/net/configuring-fonts-for-rendering-spreadsheets/)の記事を参照してください。

{{% /alert %}} 
### **IFilePathProviderインタフェースとHtmlSaveOptions.FilePathProviderプロパティを追加しました**
Aspose.Cells for .NET 8.9.1では、ワークシートを別々のHTMLファイルにエクスポートするために IFilePathProvider の取得/設定を可能にします。これらの新しいAPIは、1つのワークシート内のハイパーリンクが他のワークシート内の場所を指しているシナリオで有用であり、ワークシートを別々のHTMLファイルにレンダリングするアプリケーション要件がある場合に役立ちます。IFilePathProviderを実装することで、前述のハイパーリンクを保持することができます。

HtmlSaveOptions.FilePathProviderプロパティのシンプルな使用シナリオは次のとおりです。

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



IFilePathProvider インターフェースの実装方法については、[IFilePathProvider インターフェースの実装](/cells/ja/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)の記事を参照してください。

**C#**

{{< highlight csharp >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

この拡張機能の詳細については、[IFilePathProviderインタフェースの実装](/cells/ja/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)の記事をご確認ください。

{{% /alert %}} 
### **CopyOptions.ReferToDestinationSheet プロパティ & Cells.CopyRows メソッドのオーバーロードの追加**
Aspose.Cells for .NET APIは、行をコピーする際に、コピーされる行にチャートとそのデータソースが含まれる場合に、Boolean型のCopyOptions.ReferToDestinationSheetプロパティと、Cells.CopyRowsメソッドのオーバーロードを公開しました。これらの新しいAPIを使用することで、チャートのデータソースをソースまたは宛先ワークシートに指定できます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

この機能の詳細については、[行をコピーする際のチャートのデータソースの制御](/cells/ja/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)の記事を参照してください。

{{% /alert %}} 
### **CalculationOptions.Recursive プロパティが追加されました**
Aspose.Cells for .NET 8.9.1 でブール型の CalculationOptions.Recursive プロパティが公開されました。CalculationOptions.Recursive プロパティを true に設定し、オブジェクトを Workbook.CalculateFormula メソッドに渡すと、Aspose.Cells API は依存するセルを再帰的に計算するように指示されます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

この機能の詳細については、[計算時間の最適化](/cells/ja/net/decrease-the-calculation-time-of-cell-calculate-method/)の記事をご覧ください。

{{% /alert %}}
## **非推奨API**
### **非推奨の CellsHelper.FontDir プロパティ**
代わりにフォルダ再帰を false に設定した FontConfigs.SetFontFolder(string, bool) メソッドを使用することをお勧めします。
### **非推奨の CellsHelper.FontDirs プロパティ**
フォルダ再帰を false に設定した FontConfigs.SetFontFolders(string[], bool) メソッドを使用してください。
### **非推奨の CellsHelper.FontFiles プロパティ**
代わりに FontConfigs.SetFontSources(FontSourceBase[]) メソッドを使用してください。
