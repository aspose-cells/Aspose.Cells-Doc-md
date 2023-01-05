---
title: パブリック API Aspose.Cells 8.4.1 の変更点
type: docs
weight: 140
url: /ja/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.4.0 から 8.4.1 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-1/)と[削除されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-1/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **データベース接続を変更するメカニズム**
Aspose.Cells.ExternalConnections.ExternalConnection クラスには、スプレッドシートに保存されているデータベース接続の詳細を検査するために使用できるメソッドとプロパティが既に含まれていました。 Aspose.Cells.ExternalConnections.ExternalConnection クラスに関連付けられたプロパティのほとんどは、Aspose.Cells for .NET 8.4.1 のリリースまで読み取り専用でした。このリリースでは、API はデータベース接続設定の操作もサポートしています。

次のコード スニペットは、データベース接続設定を動的に変更する方法を示しています。

**C#**

{{< highlight "csharp" >}}

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



{Aspose.Cells.ExternalConnections.ExternalConnection}} クラスによって公開されるいくつかの最も重要なプロパティを次に示します。

|**プロパティ名**|**説明**|
|:- |:- |
|背景の更新|接続をバックグラウンドで (非同期に) リフレッシュできるかどうかを示します。<br>バックグラウンドで非同期に更新することを優先する接続の使用法である場合は true 。<br>フォアグラウンドで同期的に更新することを優先する接続の使用法である場合は false。|
|接続説明|この接続のユーザーの説明を指定します|
|接続 ID|この接続の一意の識別子を指定します。|
|資格情報|接続を確立 (または再確立) するときに使用する認証方法を指定します。|
|削除済み|関連するワークブック接続が削除されているかどうかを示します。真の場合<br>接続が削除されました。それ以外の場合は false。|
|新しく追加されました|接続が初めて更新されていない場合は true。それ以外の場合は false。この<br>クエリが返される前にユーザーがファイルを保存すると、状態が発生する可能性があります。|
|生き続ける|スプレッドシート アプリケーションが接続を維持するために努力する必要がある場合は True<br>開いた。 false の場合、アプリケーションは、<br>情報。|
|名前|接続の名前を指定します。各接続には一意の名前が必要です。|
|OdcFile|この接続元の外部接続ファイルへのフル パスを指定します。<br>作成した。データの更新中に接続が失敗し、reconnectionMethod=1 の場合、<br>その後、スプレッドシート アプリケーションは、外部接続ファイルからの情報を使用して再試行します。<br>ワークブック内に埋め込まれた接続オブジェクトの代わりに。|
|OnlyUseConnectionFile|スプレッドシート アプリケーションが常に使用する必要があるかどうかを示します。<br> odcFile 属性で示される外部接続ファイル内の接続情報<br>接続が更新されたとき。 false の場合、スプレッドシート アプリケーション<br>reconnectionMethod 属性で示される手順に従う必要があります|
|パラメーター|ODBC または Web クエリの ConnectionParameterCollection を取得します。|
|再接続方法|reconnectionMethod タイプを指定します|
|RefreshInternal|接続の自動リフレッシュ間の分数を指定します。|
|RefreshOnLoad|ファイルを開くときにこの接続を更新する必要がある場合は True。それ以外の場合は false。|
|データの保存|テーブルに入力するために接続を介してフェッチされた外部データを保存する場合は true<br>ワークブックで;それ以外の場合は false。|
|パスワードを保存する|パスワードを接続文字列の一部として保存する場合は True。それ以外の場合は False。|
|ソースファイル|外部データ ソースがファイルベースの場合に使用されます。そのようなデータへの接続時に<br>source が失敗すると、スプレッドシート アプリケーションはこのファイルに直接接続しようとします。多分<br>URI またはシステム固有のファイル パス表記で表されます。|
|SSOId|中間サーバー間の認証に使用されるシングル サインオン (SSO) の識別子。<br>スプレッドシート ML サーバーと外部データ ソース。|
|タイプ|データ ソースの種類を指定します。|

### **DataLabels のテキストの部分文字列をフォーマットする機能**
Aspose.Cells for .NET 8.4.1 は DataLabels.Characters メソッドを公開して、ChartPoints.DataLabels の部分文字列に対応する FontSetting クラスのインスタンスを取得します。次に、FontSetting クラスのインスタンスを使用して、DataLabels の部分文字列をさまざまなフォント設定と色でフォーマットできます。

次のコード スニペットは、DataLabels.Characters メソッドの使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

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


### **スプレッドシートとチャートのエクスポートに必要な画像サイズを設定する機能**
Aspose.Cells for .NET 8.4.1 は、ImageOrPrintOptions.SetDesiredSize メソッドを公開して、スプレッドシートとチャートを画像にエクスポートする際に結果の画像の寸法を設定します。 ImageOrPrintOptions.SetDesiredSize メソッドは、2 つの整数型パラメーターを受け入れます。1 つ目は目的の幅、2 つ目は目的の高さです。

次のコード スニペットは、ワークシートを PNG にエクスポートする際に目的のディメンションを設定する方法を示しています。

**C#**

{{< highlight "csharp" >}}

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

グラフを画像に変換するためにも同じプロパティを使用できます。

{{% /alert %}} 


### **PDF へのコメントのレンダリング**
v8.4.1 のリリースにより、Aspose.Cells API は、スプレッドシートを PDF 形式に変換する際のコメントのレンダリングを容易にするために、PageSetup.PrintComments プロパティと PrintCommentsType 列挙を提供しました。 PrintCommentsType 列挙には、次の定数があります。

- PrintCommentsType.PrintNoComments: コメントは表示されません。
- PrintCommentsType.PrintInPlace: コメントは、配置された場所にレンダリングされます。
- PrintCommentsType.PrintSheetEnd: コメントはワークシートの最後に表示されます。

次のサンプル コードは、PageSetup.PrintComments プロパティを使用して、可能なすべての PrintCommentsType 列挙値を使用してコメントを表示する方法を示しています。

**C#**

{{< highlight "csharp" >}}

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


### **Aspose.Cells.GridDesktop のワークシートを移動**
Aspose.Cells.GridDesktop は、指定したインデックスにワークシートを移動するために使用できる WorksheetCollection.MoveTo メソッドを提供します。前述のメソッドは、ソース ワークシートと宛先ワークシートのインデックス (0 から始まる) をパラメーターとして受け取ります。

次のサンプル コードは、WorksheetCollection.MoveTo プロパティの使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Workbook.IsLicensed プロパティを追加**
Aspose.Cells for .NET 8.4.1 は Workbook.IsLicensed を公開しました。これは、ライセンスが正常に読み込まれたかどうかを判断するのに非常に役立ちます。ライセンスを設定する前にこのプロパティにアクセスすると false が返され、その逆も同様ですが、ライセンスは有効である必要があります。

次のサンプル コードは、Workbook.IsLicensed プロパティの使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

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


### **ImageOrPrintOptions.SVGFitToViewPort プロパティを追加**
Aspose.Cells for .NET 8.4.1 は、スプレッドシートまたはチャートを SVG 形式にエクスポートする際に、SVG ファイル形式の viewBox 属性をオンにするために使用できる ImageOrPrintOptions クラスの SVGFitToViewPort プロパティを公開しました。このプロパティのデフォルト値は false であるため、前述のプロパティを設定せずに生成された SVG ファイルのベース XML には、viewBox 属性が含まれません。

次のサンプル コードは、ImageOrPrintOptions.SVGFitToViewPort プロパティの使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

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
## **廃止された API**
### **メソッド Workbook.ValidateFormula 廃止されました**
Cell.Formula メソッドを使用して式を検証します。
