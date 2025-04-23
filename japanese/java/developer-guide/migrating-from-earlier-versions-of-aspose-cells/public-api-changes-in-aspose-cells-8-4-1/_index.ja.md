---
title: Aspose.Cells 8.4.1の公開APIの変更
type: docs
weight: 150
url: /ja/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells APIのバージョン8.4.0から8.4.1への変更を記載し、モジュール/アプリケーション開発者に興味を持つ可能性があるものです。新しく追加された公開メソッド、[追加されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-1/)、[削除されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-1/)だけでなく、Aspose.Cellsの裏側の動作における変更の説明も含まれます。

{{% /alert %}} 
## **APIの追加**
### **データベース接続の変更メカニズム**
com.aspose.cells.ExternalConnectionクラスには、すでにスプレッドシートに保存されているデータベース接続の詳細を調査するために使用できるメソッドとプロパティが含まれていました。ExternalConnectionクラスに関連する大部分のプロパティは、バージョンAspose.Cells for Java 8.4.1のリリースまで読み取り専用でした。このリリースにより、APIはデータベース接続設定を操作するサポートを提供しました。

次のコードスニペットは、データベース接続設定を動的に変更する方法を示しています。

**Java**

{{< highlight csharp >}}

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

以下は、ExternalConnectionクラスによって公開されるいくつかの重要なプロパティです。

|**プロパティ名**|**説明**|
| :- | :- |
|BackgroundRefresh |接続をバックグラウンドで更新できるかどうかを示します。<br>接続の優先使用方法がバックグラウンドで非同期に更新する場合はtrue。 <br>接続の優先使用方法が前景で同期的に更新する場合はfalse。
|ConnectionDescription |この接続のユーザー説明を指定します。
|ConnectionId |この接続の一意の識別子を指定します。
|Credentials |接続を確立（または再確立）する際に使用する認証方法を指定します。
|IsDeleted |関連するワークブックの接続が削除されたかどうかを示します。接続が削除されている場合はtrue。それ以外の場合はfalse。
|IsNew |接続が最初にリフレッシュされていない場合はtrue。それ以外の場合はfalse。クエリの取得が完了する前にユーザーがファイルを保存すると、この状態が発生する可能性があります。
|KeepAlive |スプレッドシートアプリケーションが接続を開いたままにするよう努める場合はtrue。falseの場合、情報を取得した後に接続を閉じる必要があります。
|Name |接続の名前を指定します。各接続には固有の名前が必要です。
|OdcFile |この接続が作成された外部接続ファイルへのフルパスを指定します。接続がデータをリフレッシュしようと試みる際に接続に失敗し、再接続方法が1の場合、スプレッドシートアプリケーションは代わりにワークブックに埋め込まれた接続オブジェクトの代わりに外部接続ファイルからの情報を使用して再試行します。
|OnlyUseConnectionFile |スプレッドシートアプリケーションが接続をリフレッシュする際に、odcFile属性で示される外部接続ファイルの接続情報のみを常に使用するかどうかを示します。falseの場合、スプレッドシートアプリケーションはreconnectionMethod属性で示される手順に従う必要があります。
|Parameters |ODBCまたはWebクエリのConnectionParameterCollectionを取得します。
|ReConnectionMethod |再接続方法タイプを指定します。
|RefreshInternal|接続を自動的にリフレッシュする間隔（分単位）を指定します。
|RefreshOnLoad |ファイルを開く際にこの接続をリフレッシュする必要がある場合はtrue。それ以外の場合はfalse。
|SaveData |表を埋めるために接続経由で取得された外部データをワークブックとともに保存する場合はtrue。それ以外の場合はfalse。
|SavePassword |パスワードを接続文字列の一部として保存する場合はtrue。それ以外の場合はfalse。
|SourceFile |外部データソースがファイルベースの場合に使用されます。このようなデータソースへの接続が失敗した場合、スプレッドシートアプリケーションはこのファイルに直接接続を試みます。URIまたはシステム固有のファイルパス表記で表すことができます。
|SSOId|中間のスプレッドシートMLサーバーと外部データソースの間の認証に使用されるSingle Sign On（SSO）の識別子。
|Type |データソースのタイプを指定します。

### **データラベルのテキストのサブストリングをフォーマットする機能**
Aspose.Cells for Java 8.4.1では、DataLabels.charactersメソッドが公開され、ChartPoints.DataLabelsのサブストリングに対応するFontSettingクラスのインスタンスを取得できるようになりました。その後、FontSettingクラスのインスタンスを使用して、DataLabelsのサブストリングを異なるフォント設定や色でフォーマットすることができます。

次のコードスニペットは、DataLabels.charactersメソッドの使用方法を示しています。

**Java**

{{< highlight csharp >}}

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

### **スプレッドシートおよびチャートのエクスポート時に所望の画像サイズを設定する機能**
Aspose.Cells for Java 8.4.1では、ImageOrPrintOptions.setDesiredSizeメソッドが公開され、スプレッドシートやチャートを画像にエクスポートする際の出力画像の寸法を設定することができるようになりました。ImageOrPrintOptions.setDesiredSizeメソッドは、最初のパラメーターに所望の幅、2番目のパラメーターに所望の高さの整数型の値を受け入れます。

次のコードスニペットは、ワークシートをPNGにエクスポートする際に所望の寸法を設定する方法を示しています。

**Java**

{{< highlight csharp >}}

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

同じ方法は、チャートを画像に変換する際にも使用できます。 

{{% /alert %}} 

### **PDFへのコメントのレンダリング**
v8.4.1のリリースにより、Aspose.Cells APIは、スプレッドシートをPDF形式に変換する際にコメントをレンダリングするためのPageSetup.PrintCommentsプロパティとPrintCommentsType列挙体を提供しました。PrintCommentsType列挙体には以下の定数があります。 

- PrintCommentsType.PRINT_NO_COMMENTS: コメントはレンダリングされません。
- PrintCommentsType.PRINT_IN_PLACE: コメントは配置された場所でレンダリングされます。
- PrintCommentsType.PRINT_SHEET_END: コメントはワークシートの末尾にレンダリングされます。

次のサンプルコードは、PageSetup.PrintCommentsプロパティを使用して、すべてのPrintCommentsType列挙体値を使用してコメントをレンダリングする方法を示しています。

**Java**

{{< highlight csharp >}}

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

### **Workbook.isLicensedプロパティが追加されました**
Aspose.Cells for Java 8.4.1はWorkbook.isLicensedを公開しました。このプロパティは、ライセンスが正常にロードされたかどうかを判断するのに役立ちます。ライセンスを設定する前にこのプロパティにアクセスするとfalseを返し、その逆もまた然りです。ただし、ライセンスは有効である必要があります。

以下のサンプルコードは、Workbook.isLicensedプロパティの使用方法を示しています。

**Java**

{{< highlight csharp >}}

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

### **ImageOrPrintOptions.SVGFitToViewPortプロパティを追加しました**
Aspose.Cells for Java 8.4.1では、ImageOrPrintOptionsクラスのSVGFitToViewPortプロパティを公開しました。これは、スプレッドシートやチャートをSVG形式にエクスポートする際にviewBox属性を有効にするために使用できます。このプロパティのデフォルト値はfalseです。したがって、上記のプロパティを設定せずに生成されたSVGファイルの基本XMLにはviewBox属性が含まれません。

以下のサンプルコードは、ImageOrPrintOptions.SVGFitToViewPortプロパティの使用方法を示しています。

**Java**

{{< highlight csharp >}}

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
## **非推奨API**
### **廃止されたWorkbook.validateFormulaメソッド**
Cell.Formulaプロパティを使用して、式を検証します。
{{< app/cells/assistant language="java" >}}
