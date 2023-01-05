---
title: パブリック API Aspose.Cells 16.12.0 の変更点
type: docs
weight: 360
url: /ja/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 16.11.0 から 16.12.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **読み込み時にオブジェクトをフィルタリングする**
Aspose.Cells 16.12.0 は、テンプレート ファイルから Workbook のインスタンスを初期化する際にロードするデータのタイプを一緒に制御できる LoadOptions.LoadFilter プロパティと共に LoadFilter クラスを公開しました。

テンプレート ファイルからドキュメント プロパティのみを読み込む簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



次のスニペットは、チャートを除く既存のスプレッドシートからすべてを読み込みます。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



次のコードは、既存のスプレッドシートからセル データ (数式と共に) と書式設定のみを読み込みます。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



LoadFilter クラスでは、ワークシートのプロパティに従って読み込みプロセスをカスタマイズすることもできます。ワークシートごとに読み込みプロセスをカスタマイズするには、以下に示すように LoadFilter.StartSheet メソッドをオーバーライドする必要があります。

**C#**

{{< highlight "csharp" >}}

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



次のスニペットは、上で定義した CustomFilter クラスを利用しています。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **FileFormatType.OTS 列挙を追加**
Aspose.Cells 16.12.0 では、OTS ファイルの形式を検出するために、FileFormatType 列挙に OTS エントリが追加されました。

次のスニペットは、FileFormatType.OTS を利用しています。

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **FontConfigs.PreferSystemFontSubstitutes プロパティを追加**
Aspose.Cells 16.12.0 では、FontConfigs クラスの PreferSystemFontSubstitutes プロパティが公開されました。 FontConfigs.PreferSystemFontSubstitutes プロパティはブール型で、必要なフォントが存在せず、特定のフォントの代替が定義されていない場合に、API が最初にシステムのフォント代替メカニズムを使用する必要があるかどうかを示します。 FontConfigs.PreferSystemFontSubstitutes プロパティのデフォルト値は false です。
### **BuiltInDocumentPropertyCollection.ScaleCrop プロパティを追加**
Aspose.Cells 16.12.0 では、ScaleCrop プロパティが BuiltInDocumentPropertyCollection クラスに追加されました。 ScaleCrop は、ドキュメント サムネイルの表示モードを示します。この要素を true に設定すると、ディスプレイごとにドキュメント サムネイルのスケーリングが有効になります。false に設定すると、ドキュメント サムネイルのトリミングが有効になり、ディスプレイに合わせてセクションが表示されます。
### **BuiltInDocumentPropertyCollection.LinksUpToDate プロパティを追加**
Aspose.Cells 16.12.0 では、BuiltInDocumentPropertyCollection クラスの LinksUpToDate プロパティも公開されています。 LinksUpToDate プロパティは、ドキュメント内のハイパーリンクが最新かどうかを示します。
### **Workbook.ExportXml メソッドを追加**
Aspose.Cells 16.12.0 では、指定したファイル パスに XML マップ データを保存できる Workbook.ExportXml メソッドが公開されました。 Workbook.ExportXml メソッドは 2 つのパラメーターを受け入れます。最初の文字列型のパラメーターは XML マップ名で、2 番目のパラメーターは XML データを保存するファイル パスの場所である必要があります。
### **WorksheetCollection.CreateRange メソッドを追加**
Aspose.Cells 16.12.0 では、アドレス (セル領域参照) とワークシート インデックスに基づいて範囲を作成できる WorksheetCollection.CreateRange メソッドが追加されました。

次のスニペットでは、WorksheetCollection.CreateRange メソッドを使用して、最初の (既定の) ワークシートで A1 から A2 にまたがるセル範囲を作成します。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **廃止された API**
### **廃止された LoadOptions.LoadDataOptions プロパティ**
代わりに LoadOptions.LoadFilter プロパティを使用してください。
### **廃止された LoadOptions.LoadDataFilterOptions プロパティ**
代わりに LoadOptions.LoadFilter プロパティを使用してください。
### **廃止された LoadOptions.OnlyLoadDocumentProperties プロパティ**
代わりに LoadOptions.LoadFilter プロパティを使用してください。
### **廃止された LoadOptions.LoadDataAndFormatting プロパティ**
代わりに LoadOptions.LoadFilter プロパティを使用してください。

{{% alert color="primary" %}} 

廃止されたすべての API のコード スニペットは上記で共有されています。

{{% /alert %}}
## **削除された API**
### **削除された DataLabels.Rotation プロパティ**
代わりに DataLabels.RotationAngle プロパティを使用してください。
### **削除された Title.Rotation プロパティ**
代わりに Title.RotationAngle プロパティを使用してください。
### **削除された DataLabels.Background プロパティ**
代わりに DataLabels.BackgroundMode プロパティを使用することをお勧めします。
### **DisplayUnitLabel.Rotation プロパティを削除**
同じ目標を達成するために DisplayUnitLabel.RotationAngle プロパティの使用を検討してください。
