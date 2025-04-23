---
title: Aspose.Cells 16.12.0でのパブリックAPIの変更
type: docs
weight: 370
url: /ja/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、バージョン16.11.0から16.12.0へのAspose.Cells APIの変更について説明します。これは、モジュール/アプリケーション開発者にとって興味深い変更だけでなく、新しいメソッドや更新された公開メソッド、追加および削除されたクラスなどを含むものです。

{{% /alert %}} 
## **APIの追加**
### **ロード時のオブジェクトフィルタ**
Aspose.Cells 16.12.0 では、テンプレートファイルからワークブックのインスタンスを初期化する際にロードされるデータの種類を制御する LoadFilter クラスと LoadOptions.LoadFilter プロパティが公開されました

ここには、テンプレートファイルからドキュメントプロパティのみをロードするシンプルな使用シナリオがあります

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

以下のスニペットは、チャートを除く既存のスプレッドシートからすべてをロードします

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

以下のコードは、既存のスプレッドシートからセルデータ（および数式）および書式のみをロードします

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **FileFormatType.OTS 列挙型が追加されました**
Aspose.Cells 16.12.0 では、OTS ファイルの形式を検出するために FileFormatType 列挙型に OTS エントリが追加されました

次のスニペットは FileFormatType.OTS を利用します

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **BuiltInDocumentPropertyCollection.ScaleCrop プロパティが追加されました**
Aspose.Cells 16.12.0 では、BuiltInDocumentPropertyCollection クラスに ScaleCrop プロパティが追加されました。ScaleCrop はドキュメントサムネイルの表示モードを示します。この要素を true に設定すると、ドキュメントサムネイルの表示に応じてスケーリングが有効になり、false に設定すると、表示に適合するセクションをトリミングしてドキュメントサムネイルを表示します
### **BuiltInDocumentPropertyCollection.LinksUpToDate プロパティが追加されました**
Aspose.Cells 16.12.0 では、BuiltInDocumentPropertyCollection クラスに LinksUpToDate プロパティも公開されました。LinksUpToDate プロパティは、ドキュメント内のハイパーリンクが最新かどうかを示します 
### **Workbook.exportXml メソッドが追加されました**
Aspose.Cells 16.12.0 では、XML マップデータを指定されたファイルパスに保存するための Workbook.exportXml メソッドが公開されました。Workbook.exportXml メソッドは、第1パラメータとして XML マップ名であるべき文字列型のパラメータと、XML データを保存するファイルパスのパラメータとして2つのパラメータを受け取ります
### **WorksheetCollection.createRange メソッドが追加されました**
Aspose.Cells 16.12.0 では、アドレス（セルエリア参照）およびワークシートインデックスに基づいて範囲を作成するための WorksheetCollection.createRange メソッドが追加されました

次のスニペットは、WorksheetCollection.createRange メソッドを使用して、最初（デフォルト）のワークシートにおいて A1 から A2 までのセルの範囲を作成します

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

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
### **Title.getCharacters メソッドは削除されました**
代わりに Title.characters メソッドを使用してください
{{< app/cells/assistant language="java" >}}
