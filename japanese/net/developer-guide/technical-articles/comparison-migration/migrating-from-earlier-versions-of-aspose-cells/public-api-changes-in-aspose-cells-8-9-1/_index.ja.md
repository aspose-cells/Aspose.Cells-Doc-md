---
title: パブリック API Aspose.Cells 8.9.1 の変更点
type: docs
weight: 310
url: /ja/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.9.0 から 8.9.1 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **構成可能なフォント ソース**
Aspose.Cells for .NET は、スプレッドシートをレンダリングするための構成可能なフォント ソースのサポートを提供するために、多くのクラスを公開しました。以下は、Aspose.Cells for .NET 8.9.1 で追加されたクラスのリストです。

1. FontConfigs クラスは、フォント設定を指定します。
1. FontSourceBase クラスは、ユーザーがさまざまなフォント ソースを指定できるようにするクラスの抽象基本クラスです。
1. FileFontSource クラスは、ファイル システムに格納されている単一の TrueType フォント ファイルを表します。
1. FolderFontSource クラスは、TrueType フォント ファイルを含むフォルダーを表します。
1. MemoryFontSource クラスは、メモリに格納された単一の TrueType フォント ファイルを表します。
1. FontSourceType 列挙体は、フォント ソースの種類を指定します。

上記の変更により、Aspose.Cells for .NET では、以下に示すようにフォントを設定できます。

1. FontConfigs.SetFontFolder メソッドを使用して、1 つのカスタム フォント フォルダーを設定します。
1. FontConfigs.SetFontFolders メソッドを使用して、複数のカスタム フォント フォルダーを設定します。
1. FontConfigs.SetFontSources メソッドを使用して、カスタム フォント フォルダー、単一のフォント ファイル、またはバイト配列のフォント データからフォント ソースを設定します。

前述の方法の簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.SetFontFolder と FontConfigs.SetFontFolders の両方のメソッドは、ブール型の 2 番目のパラメーターを受け入れます。 2 番目のパラメーターとして true を渡すと、Aspose.Cells API がフォント ファイルのサブフォルダーを検索するように指示されます。

{{% /alert %}} 

Aspose.Cells for .NET では、フォントの置換を構成することもできます。このメカニズムは、変換が必要なマシンで必要なフォントが利用できない場合に役立ちます。ユーザーは、元々必要だったフォントの代わりに、フォント名のリストを提供できます。これを実現するために、Aspose.Cells API は、2 つのパラメーターを受け入れる FontConfigs.SetFontSubstitutes メソッドを公開しました。最初のパラメーターは文字列型で、置換する必要があるフォントの名前にする必要があります。 2 番目のパラメーターは、string 型の配列です。ユーザーは、元のフォント名 (最初のパラメーターで指定) の代わりに、フォント名のリストを提供できます。

FontConfigs.SetFontSubstitutes メソッドの簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET は、どのソースと代替が設定されているかに関する情報を収集する手段も提供しています。

1. FontConfigs.GetFontSources メソッドは、指定されたフォント ソースのリストを含む FontSourceBase 型の配列を返します。ソースが設定されていない場合、FontConfigs.GetFontSources メソッドは空の配列を返します。
1. FontConfigs.GetFontSubstitutes メソッドは文字列型のパラメータを受け入れ、置換が設定されているフォント名を指定できます。指定されたフォント名に代替が設定されていない場合、FontConfigs.GetFontSubstitutes メソッドは null を返します。

{{% alert color="primary" %}} 

 FontConfigs の詳細については、次の記事を参照してください。[スプレッドシートをレンダリングするためのフォントの構成](/cells/ja/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **IFilePathProvider インターフェイスと HtmlSaveOptions.FilePathProvider プロパティを追加**
Aspose.Cells for .NET 8.9.1 では、ワークシートを別の HTML ファイルにエクスポートするための IFilePathProvider を取得/設定できます。これらの新しい API は、あるワークシートのハイパーリンクが別のワークシート内の場所を指しているシナリオで役立ちます。アプリケーションの要件は、各ワークシートを個別の HTML ファイルにレンダリングすることです。 IFilePathProvider を実装すると、別の結果の HTML ファイル内の場所を指しているという事実に関係なく、前述のハイパーリンクをそのまま維持できます。

以下は、HtmlSaveOptions.FilePathProvider プロパティの簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 // Workbook のインスタンスにスプレッドシートをロードします

var book = new Workbook(dir + "sample.xlsx");

// 各ワークシートを個別の HTML ファイルに保存します

for (int i = 0; i< book.Worksheets.Count; i++)

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



IFilePathProvider インターフェイスを実装する方法は次のとおりです。

**C#**

{{< highlight "csharp" >}}

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

この機能強化の詳細については、次の記事を参照してください。[IFilePathProvider インターフェイスの実装](/cells/ja/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **CopyOptions.ReferToDestinationSheet プロパティと Cells.CopyRows メソッドのオーバーロードを追加**
Aspose.Cells for .NET API は、コピーされる行にグラフとそのデータ ソースも含まれている場合に行のコピー操作を容易にするために、ブール型の CopyOptions.ReferToDestinationSheet プロパティを Cells.CopyRows メソッドのオーバーロードと共に公開しました。開発者は、これらの新しい API を利用して、グラフのデータ ソースをソースまたは宛先のワークシートに向けることができます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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

この機能の詳細については、次の記事を参照してください。[行のコピー中にチャートのデータ ソースを制御する](/cells/ja/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **CalculationOptions.Recursive プロパティを追加しました**
Aspose.Cells for .NET 8.9.1 では、ブール型の CalculationOptions.Recursive プロパティが公開されました。 CalculationOptions.Recursive プロパティを true に設定し、オブジェクトを Workbook.CalculateFormula メソッドに渡すと、Aspose.Cells API は、他のセルに依存するセルを計算するときに、依存セルを再帰的に計算するように指示されます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

この機能の詳細については、次の記事を参照してください。[計算時間の最適化](/cells/ja/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **廃止された API**
### **廃止された CellsHelper.FontDir プロパティ**
代わりに、FontConfigs.SetFontFolder(string, bool) メソッドを false に再帰するフォルダーで使用することをお勧めします。
### **廃止された CellsHelper.FontDirs プロパティ**
代わりに、FontConfigs.SetFontFolders(string[], bool) メソッドを false に再帰するフォルダーで使用します。
### **廃止された CellsHelper.FontFiles プロパティ**
代わりに FontConfigs.SetFontSources(FontSourceBase[]) メソッドを使用してください。
