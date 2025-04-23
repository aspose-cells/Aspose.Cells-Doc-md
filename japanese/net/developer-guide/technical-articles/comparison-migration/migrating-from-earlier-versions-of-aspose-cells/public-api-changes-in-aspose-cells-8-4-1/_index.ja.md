---
title: Aspose.Cells 8.4.1の公開APIの変更
type: docs
weight: 140
url: /ja/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cellsのバージョン8.4.0から8.4.1への変更点について、モジュール/アプリケーション開発者にとって興味深い可能性があるものを記載しています。[追加されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-1/)、[削除されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-1/)に加えて、Aspose.Cells内部での挙動の変更についての記述も含まれます。

{{% /alert %}} 
## **APIの追加**
### **データベース接続の変更メカニズム**
Aspose.Cells.ExternalConnections.ExternalConnection クラスには、スプレッドシートに格納されているデータベース接続の詳細を検査するために使用できるメソッドやプロパティが既に含まれていました。Aspose.Cells.ExternalConnections.ExternalConnection クラスに関連するプロパティのほとんどは、リリースAspose.Cells for .NET 8.4.1まで読み取り専用でした。このリリースにより、APIはデータベース接続設定を操作するためのサポートを提供しました。

次のコードスニペットは、データベース接続設定を動的に変更する方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



Aspose.Cells.ExternalConnections.ExternalConnection クラスで公開されている重要なプロパティの一部です。

|**プロパティ名**|**説明**|
| :- | :- |
|BackgroundRefresh|接続をバックグラウンドでリフレッシュできるかどうかを示します。接続の推奨される使用法がバックグラウンドで非同期にリフレッシュする場合は true。接続の推奨される使用法が前景で同期にリフレッシュする場合は false。|
|ConnectionDescription|この接続のユーザー説明を指定します|
|ConnectionId|この接続の一意の識別子を指定します。|
|Credentials|接続を確立（または再確立）する際に使用する認証メソッドを指定します。|
|IsDeleted|関連するワークブック接続が削除されたかどうかを示します。接続が削除されている場合は true。それ以外の場合は false。|
|IsNew|接続が最初にリフレッシュされていない場合は true。それ以外の場合は false。この状態は、クエリが返ってくる前にユーザーがファイルを保存すると発生する可能性があります。|
|KeepAlive|スプレッドシート アプリケーションが接続を維持する努力をする場合は true。false の場合、情報を取得した後に接続を閉じる必要があります。|
|Name|接続の名前を指定します。各接続には固有の名前が必要です。|
|OdcFile|この接続が作成された外部接続ファイルのフルパスを指定します。接続が再試行Method=1 によってデータの再リフレッシュ中に接続が失敗し、external connection fileによる情報を使用して再度試す場合は、スプレッドシート アプリケーションは、ブック内に埋め込まれている接続オブジェクトではなく、external connection file内の情報を使用して再度試します。|
|OnlyUseConnectionFile|接続がリフレッシュされる際に、常に外部接続ファイルで指示された接続情報のみを使用するかどうかを示します。false の場合、スプレッドシート アプリケーションは、reconnectionMethod 属性によって指示された手順に従う必要があります。|
|Parameters|ODBCまたはWeb QueryのConnectionParameterCollectionを取得します。|
|ReConnectionMethod|再接続Methodのタイプを指定します|
|RefreshInternal|は接続の自動更新間隔を分単位で指定します。
|RefreshOnLoad|ファイルを開く際にこの接続をリフレッシュする必要がある場合は true。それ以外の場合は false。|
|SaveData|接続を通じて取得した外部データをワークブックとともに保存する場合は true。それ以外の場合は false。|
|SavePassword|接続文字列の一環としてパスワードを保存する場合はTrue。それ以外の場合はFalse。|
|SourceFile|外部データソースがファイルベースの場合に使用されます。このようなデータソースへの接続が失敗した場合、スプレッドシートアプリケーションは直接このファイルに接続を試みます。URIまたはシステム固有のファイルパス表記で表すことができます。|
|SSOId|中間のspreadsheetMLサーバーと外部データソース間の認証に使用されるSingle Sign On (SSO)の識別子。|
|Type|データソースのタイプを指定します。|

### **データラベルのテキストのサブストリングをフォーマットする機能**
Aspose.Cells for .NET 8.4.1では、DataLabels.Charactersメソッドが公開され、ChartPoints.DataLabelsのサブ文字列に対応するFontSettingクラスのインスタンスを取得するために使用できます。次に、FontSettingクラスのインスタンスを使用して、DataLabelsのサブ文字列をさまざまなフォント設定および色でフォーマットすることができます。

次のコードスニペットは、DataLabels.Charactersメソッドの使用方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **スプレッドシートおよびチャートのエクスポート時に所望の画像サイズを設定する機能**
Aspose.Cells for .NET 8.4.1では、ImageOrPrintOptions.SetDesiredSizeメソッドが公開され、スプレッドシートやチャートを画像にエクスポートする際に、結果の画像のサイズを設定するために使用できます。ImageOrPrintOptions.SetDesiredSizeメソッドは、第1パラメーターが所望の幅であり、第2パラメーターが所望の高さである2つの整数型のパラメーターを受け入れます。

次のコードスニペットは、ワークシートをPNGにエクスポートする際に所望の寸法を設定する方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

同じプロパティは、チャートを画像に変換する際にも使用できます。

{{% /alert %}} 


### **PDFへのコメントのレンダリング**
v8.4.1のリリースにより、Aspose.Cells APIは、スプレッドシートをPDF形式に変換する際にコメントをレンダリングするためのPageSetup.PrintCommentsプロパティとPrintCommentsType列挙体を提供しました。PrintCommentsType列挙体には以下の定数があります。

- PrintCommentsType.PrintNoComments: コメントはレンダリングされません。
- PrintCommentsType.PrintInPlace: コメントが配置されている場所にレンダリングされます。
- PrintCommentsType.PrintSheetEnd: コメントはワークシートの最後にレンダリングされます。

次のサンプルコードは、PageSetup.PrintCommentsプロパティを使用して、すべてのPrintCommentsType列挙体値を使用してコメントをレンダリングする方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **Aspose.Cells.GridDesktopでワークシートを移動する**
Aspose.Cells.GridDesktopは、ワークシートを指定されたインデックスに移動するためのWorksheetCollection.MoveToメソッドを提供しており、前述のメソッドはソースワークシートと宛先ワークシートのインデックス（ゼロベース）をパラメーターとして受け取ります。

次のサンプルコードは、WorksheetCollection.MoveToプロパティの使用方法を示しています。

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Workbook.IsLicensedプロパティを追加**
Aspose.Cells for .NET 8.4.1では、有効なライセンスが正常にロードされたかどうかを判断するのに役立つWorkbook.IsLicensedが公開されています。ライセンスを設定する前にこのプロパティにアクセスするとfalseを返し、その逆もまた然りですが、ライセンスは有効である必要があります。

次のサンプルコードは、Workbook.IsLicensedプロパティの使用方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **ImageOrPrintOptions.SVGFitToViewPortプロパティを追加しました**
Aspose.Cells for .NET 8.4.1では、ImageOrPrintOptionsクラスのSVGFitToViewPortプロパティが公開され、スプレッドシートやチャートをSVG形式にエクスポートする際にviewBox属性を有効にするために使用できます。このプロパティのデフォルト値はfalseです。したがって、前述のプロパティを設定せずに生成されたSVGファイルのベースXMLにはviewBox属性が含まれません。

以下のサンプルコードは、ImageOrPrintOptions.SVGFitToViewPortプロパティの使用方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **非推奨のAPI**
### **廃止されたWorkbook.ValidateFormulaメソッド**
Cell.Formulaメソッドを使用して式を検証してください。
{{< app/cells/assistant language="csharp" >}}
