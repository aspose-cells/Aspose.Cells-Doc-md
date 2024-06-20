---
title: Aspose.Cells 16.12.0でのパブリックAPIの変更
type: docs
weight: 360
url: /ja/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、バージョン16.11.0から16.12.0へのAspose.Cells APIの変更について説明します。これは、モジュール/アプリケーション開発者にとって興味深い変更だけでなく、新しいメソッドや更新された公開メソッド、追加および削除されたクラスなどを含むものです。

{{% /alert %}} 
## **APIの追加**
### **ロード時のオブジェクトフィルタ**
Aspose.Cells 16.12.0 では、テンプレートファイルからワークブックのインスタンスを初期化する際にロードされるデータの種類を制御する LoadFilter クラスと LoadOptions.LoadFilter プロパティが公開されました

ここには、テンプレートファイルからドキュメントプロパティのみをロードするシンプルな使用シナリオがあります

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



以下のスニペットは、チャートを除く既存のスプレッドシートからすべてをロードします

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



以下のコードは、既存のスプレッドシートからセルデータ（および数式）および書式のみをロードします

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



LoadFilter クラスでは、Worksheet のプロパティに応じて読み込みプロセスをカスタマイズすることも可能です。ワークシートに応じて読み込みプロセスをカスタマイズするには、以下に示すように LoadFilter.StartSheet メソッドをオーバーライドする必要があります。

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



以下のスニペットでは、上記で定義した CustomFilter クラスを使用しています。

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **FileFormatType.OTS 列挙型が追加されました**
Aspose.Cells 16.12.0 では、OTS ファイルの形式を検出するために FileFormatType 列挙型に OTS エントリが追加されました

次のスニペットは FileFormatType.OTS を利用します

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **FontConfigs.PreferSystemFontSubstitutes プロパティを追加しました**
Aspose.Cells 16.12.0 では、FontConfigs クラスの PreferSystemFontSubstitutes プロパティが公開されています。FontConfigs.PreferSystemFontSubstitutes プロパティは、特定のフォントが存在せず、そのフォントの置換が定義されていない場合に、API がまずシステムのフォント置換メカニズムを使用するかどうかを示す Boolean 型のプロパティです。FontConfigs.PreferSystemFontSubstitutes プロパティのデフォルト値は false です。
### **BuiltInDocumentPropertyCollection.ScaleCrop プロパティが追加されました**
Aspose.Cells 16.12.0 では、BuiltInDocumentPropertyCollection クラスに ScaleCrop プロパティが追加されました。ScaleCrop はドキュメントサムネイルの表示モードを示します。この要素を true に設定すると、ドキュメントサムネイルの表示に応じてスケーリングが有効になり、false に設定すると、表示に適合するセクションをトリミングしてドキュメントサムネイルを表示します
### **BuiltInDocumentPropertyCollection.LinksUpToDate プロパティが追加されました**
Aspose.Cells 16.12.0 では、BuiltInDocumentPropertyCollection クラスに LinksUpToDate プロパティも公開されました。LinksUpToDate プロパティは、ドキュメント内のハイパーリンクが最新かどうかを示します
### **Workbook.ExportXml メソッドを追加しました**
Aspose.Cells 16.12.0 では、XML マップデータを指定されたファイルパスに保存するための Workbook.ExportXml メソッドが公開されています。Workbook.ExportXml メソッドは、1 番目のパラメータを文字列型で XML マップ名とし、2 番目のパラメータを XML データを保存するファイルパスとして受け入れます。
### **WorksheetCollection.CreateRange メソッドを追加しました**
Aspose.Cells 16.12.0 では、WorksheetCollection.CreateRange メソッドが追加され、アドレス（セルエリアの参照）とワークシートのインデックスに基づいて範囲を作成できるようになりました。

以下のスニペットでは、最初（デフォルト）のワークシートに A1 から A2 までのセル範囲を作成するために WorksheetCollection.CreateRange メソッドを使用しています。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **非推奨API**
### **LoadOptions.LoadDataOptions プロパティが非推奨になりました**
代替として LoadOptions.LoadFilter プロパティを使用してください
### **LoadOptions.LoadDataFilterOptions プロパティは廃止されました**
代わりに LoadOptions.LoadFilter プロパティを使用してください
### **LoadOptions.OnlyLoadDocumentProperties プロパティは廃止されました**
代替として LoadOptions.LoadFilter プロパティを使用してください
### **LoadOptions.LoadDataAndFormatting プロパティは廃止されました**
代わりに LoadOptions.LoadFilter プロパティを使用してください

{{% alert color="primary" %}} 

廃止されたAPIのコードスニペットが上で共有されています

{{% /alert %}}
## **削除されたAPI**
### **DataLabels.Rotation プロパティは削除されました**
代わりに DataLabels.RotationAngle プロパティを使用してください
### **Title.Rotation プロパティは削除されました**
代替として Title.RotationAngle プロパティを使用してください
### **DataLabels.Background プロパティは削除されました**
代わりに DataLabels.BackgroundMode プロパティを使用することをお勧めします
### **DisplayUnitLabel.Rotation プロパティは削除されました**
同じ目的を達成するために DisplayUnitLabel.RotationAngle プロパティを使用することを検討してください
