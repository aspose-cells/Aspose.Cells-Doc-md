---
title: パブリック API Aspose.Cells 8.4.1 の変更点
type: docs
weight: 150
url: /ja/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.4.0 から 8.4.1 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-1/)と[削除されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-1/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **データベース接続を変更するメカニズム**
com.aspose.cells.ExternalConnection クラスには、スプレッドシートに格納されたデータベース接続の詳細を検査するために使用できるメソッドとプロパティが既に含まれていました。 ExternalConnection クラスに関連付けられたほとんどのプロパティは、Aspose.Cells for Java 8.4.1 のリリースまで読み取り専用でした。このリリースでは、API はデータベース接続設定の操作もサポートしています。

次のコード スニペットは、データベース接続設定を動的に変更する方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{ExternalConnection}} クラスによって公開されるいくつかの最も重要なプロパティを次に示します。

|**プロパティ名** |**説明** |
|:- |:- |
|背景の更新|接続をバックグラウンドで (非同期に) リフレッシュできるかどうかを示します。<br>バックグラウンドで非同期に更新することを優先する接続の使用法である場合は true 。<br>フォアグラウンドで同期的に更新することを優先する接続の使用法である場合は false。|
|接続説明|この接続のユーザーの説明を指定します|
|接続 ID|この接続の一意の識別子を指定します。|
|資格情報|接続を確立 (または再確立) するときに使用する認証方法を指定します。|
|削除済み|関連するワークブック接続が削除されているかどうかを示します。真の場合<br>接続が削除されました。それ以外の場合は false。|
|新しく追加されました|接続が初めて更新されていない場合は true。それ以外の場合は false。この<br>クエリが返される前にユーザーがファイルを保存すると、状態が発生する可能性があります。|
|生き続ける|スプレッドシート アプリケーションが接続を維持するために努力する必要がある場合は True<br>開いた。 false の場合、アプリケーションは、<br>情報。|
|名前|接続の名前を指定します。各接続には一意の名前が必要です。|
| OdcFile|この接続元の外部接続ファイルへのフル パスを指定します。<br>作成した。データの更新中に接続が失敗し、reconnectionMethod=1 の場合、<br>その後、スプレッドシート アプリケーションは、外部接続ファイルからの情報を使用して再試行します。<br>ワークブック内に埋め込まれた接続オブジェクトの代わりに。|
| OnlyUseConnectionFile|スプレッドシート アプリケーションが常に使用する必要があるかどうかを示します。<br> odcFile 属性で示される外部接続ファイル内の接続情報<br>接続が更新されたとき。 false の場合、スプレッドシート アプリケーション<br>reconnectionMethod 属性で示される手順に従う必要があります|
|パラメーター|ODBC または Web クエリの ConnectionParameterCollection を取得します。|
|再接続方法|reconnectionMethod タイプを指定します|
|RefreshInternal|接続の自動リフレッシュ間の分数を指定します。|
| RefreshOnLoad|ファイルを開くときにこの接続を更新する必要がある場合は True。それ以外の場合は false。|
|データの保存|テーブルに入力するために接続を介してフェッチされた外部データを保存する場合は true<br>ワークブックで;それ以外の場合は false。|
|パスワードを保存する|パスワードを接続文字列の一部として保存する場合は True。それ以外の場合は False。|
|ソースファイル|外部データ ソースがファイルベースの場合に使用されます。そのようなデータへの接続時に<br>source が失敗すると、スプレッドシート アプリケーションはこのファイルに直接接続しようとします。多分<br>URI またはシステム固有のファイル パス表記で表されます。|
|SSOID|中間サーバー間の認証に使用されるシングル サインオン (SSO) の識別子。<br>スプレッドシート ML サーバーと外部データ ソース。|
|タイプ|データ ソースの種類を指定します。|

### **DataLabels のテキストの部分文字列をフォーマットする機能**
Aspose.Cells for Java 8.4.1 は DataLabels.characters メソッドを公開して、ChartPoints.DataLabels の部分文字列に対応する FontSetting クラスのインスタンスを取得します。次に、FontSetting クラスのインスタンスを使用して、DataLabels の部分文字列をさまざまなフォント設定と色でフォーマットできます。

次のコード スニペットは、DataLabels.characters メソッドの使用方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **スプレッドシートとチャートのエクスポートに必要な画像サイズを設定する機能**
Aspose.Cells for Java 8.4.1 は、スプレッドシートとチャートを画像にエクスポートする際に、結果の画像の寸法を設定する ImageOrPrintOptions.setDesiredSize メソッドを公開しました。 ImageOrPrintOptions.setDesiredSize メソッドは、2 つの整数型パラメーターを受け入れます。1 つ目は目的の幅、2 つ目は目的の高さです。

次のコード スニペットは、ワークシートを PNG にエクスポートする際に目的の寸法を設定する方法を示しています。

**Java**

{{< highlight "csharp" >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

同じ方法でチャートを画像に変換することもできます。

{{% /alert %}} 

### **PDF へのコメントのレンダリング**
v8.4.1 のリリースにより、Aspose.Cells API は、スプレッドシートを PDF 形式に変換する際にコメントのレンダリングを容易にするために、PageSetup.PrintComments プロパティと PrintCommentsType 列挙を提供しました。 PrintCommentsType 列挙には、次の定数があります。

- PrintCommentsType.PRINT_いいえ_コメント: コメントは表示されません。
- PrintCommentsType.PRINT_の_PLACE: コメントは、配置された場所にレンダリングされます。
- PrintCommentsType.PRINT_シート_END: コメントはワークシートの最後に表示されます。

次のサンプル コードは、PageSetup.PrintComments プロパティを使用して、可能なすべての PrintCommentsType 列挙値を使用してコメントを表示する方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **Workbook.isLicensed プロパティを追加**
Aspose.Cells for Java 8.4.1 は Workbook.isLicensed を公開しました。これは、ライセンスが正常に読み込まれたかどうかを判断するのに非常に役立ちます。ライセンスを設定する前にこのプロパティにアクセスすると false が返され、その逆も同様ですが、ライセンスは有効である必要があります。

次のサンプル コードは、Workbook.isLicensed プロパティの使用方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **ImageOrPrintOptions.SVGFitToViewPort プロパティを追加**
Aspose.Cells for Java 8.4.1 は、スプレッドシートまたはチャートを SVG 形式にエクスポートする際に、SVG ファイル形式の viewBox 属性をオンにするために使用できる ImageOrPrintOptions クラスの SVGFitToViewPort プロパティを公開しました。このプロパティのデフォルト値は false であるため、前述のプロパティを設定せずに生成された SVG ファイルのベース XML には、viewBox 属性が含まれません。

次のサンプル コードは、ImageOrPrintOptions.SVGFitToViewPort プロパティの使用方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **廃止された API**
### **メソッド Workbook.validateFormula 廃止されました**
Cell.Formula プロパティを使用して式を検証します。
