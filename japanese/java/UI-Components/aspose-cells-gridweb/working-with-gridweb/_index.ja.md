---
title: GridWeb での作業
type: docs
weight: 20
url: /ja/java/working-with-gridweb/
---

## **Microsoft Excelファイルを開く**

Aspose.Cells.GridWebコントロールを使用して、Microsoft Excelファイルをデータ、書式、グラフ、画像などを含めて開きます。このトピックではその方法について説明します。

GridWebコントロールを使用してExcelファイルを開くには:

1. Aspose.Cells.GridWebコントロールをWebフォームまたはページに追加します。
1. ファイルのパスを指定してExcelファイルをインポートします。
1. アプリケーションを実行するか、ページを開きます。

Aspose.Cells.GridWebコントロールにExcelファイルからコンテンツをロードするには、importExcelFileメソッドを呼び出してExcelファイルのパスを指定する必要があります。その後、GridWebコントロールは指定されたパスからファイルを自動的に見つけ、その内容を表示します。Excelファイルの内容をロードするコードの断片が以下に示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

上記のコード断片は任意の方法で使用できます。たとえば、Webフォームが読み込まれるときにExcelファイルを自動的に読み込む場合は、このコードを自分で指定したフォームのPage_Loadイベントに追加します。

GridWebにExcelファイルがロードされます

![todo:image_alt_text](working-with-gridweb_1.png)

## **Microsoft Excelファイルの保存**

Aspose.Cells.GridWebコントロールを使用して、Webサイト上で新しいMicrosoft Excelファイルを作成したり既存のファイルを操作したりし、Excelファイルとして保存することができます。Aspose.Cells.GridWebは、オンラインスプレッドシートエディタとして効果的に機能します。このトピックでは、グリッドの内容をExcelファイルに保存する方法について説明します。

### **ファイルとして保存する**

Aspose.Cells.GridWebコントロールのコンテンツをExcelファイルとして保存するには：

1. Aspose.Cells.GridWebコントロールをWebフォームまたはページに追加します。
1. 指定したパスに作業内容をExcelファイルとして保存します。
1. アプリケーションを実行するか、ページを開きます。

以下のコード例は、グリッドコンテンツをExcelファイルに保存する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

上記のコード断片はいくつかの方法で使用できます。一般的な方法は、バックグラウンドでExcelファイルにグリッドの内容を保存するボタンを追加することです。Aspose.Cells.GridWebはこのタスクのための簡単なアプローチを提供します。Aspose.Cells.GridWebにはSaveCommandというイベントがあります。上記のコード断片はSaveCommandイベントのイベントハンドラに追加することができ、ユーザーはAspose.Cells.GridWebの組み込みの**Save**ボタンをクリックして作業を保存できます。

## **Aspose.Cells.GridWebとそのヘッダーバーのサイズ変更**

この記事では、Aspose.Cells.GridWeb APIを使用してランタイムでGridWebのサイズを変更する方法について説明します。また、Aspose.Cells.GridWebコントロールのヘッダーバーのサイズを変更してデータを読みやすくする方法についても説明します。

### **Aspose.Cells.GridWeb の幅と高さを変更する**

Aspose.Cells.GridWebコントロールの幅と高さを変更することは、単純ながら重要な機能です。Aspose.Cells.GridWebコントロールはAPI内のGridWebクラスで表されます。GridWebコントロールの幅と高さを変更するには、その幅と高さのプロパティを単純に使用します。

{{% alert color="primary" %}}

コントロールの幅と高さはピクセルまたはポイントで定義できます。

{{% /alert %}}

以下のコードスニペットの出力は以下のようになります。

**GridWebコントロールの幅と高さを変更しました**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **ヘッダーバーの幅と高さを変更する**

Aspose.Cells.GridWebコントロールには、次のような2つのヘッダーバーがあります:

- 上部のヘッダーバー、このヘッダーバーはA、B、C、Dなどの列を表します。
- 左側のヘッダーバー、このヘッダーバーは1、2、3、4などの行を表します。

これらのヘッダーバーは以下に示しています。

**ヘッダーバー**

![todo:image_alt_text](working-with-gridweb_3.png)

GridWebコントロールのHeaderBarHeightとHeaderBarWidthプロパティを使用して、上部ヘッダーバーの高さと左側ヘッダーバーの幅を変更します。以下のコード例の出力は以下のようになります。

**ヘッダーバーの幅と高さを変更しました**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Aspose.Cells.GridWebイベントの操作**

すべての開発者はイベントとその目的を把握している必要があります。 イベントは、コントロールやクラスで発生する変更の通知を送信するために使用されます。 Aspose.Cells.GridWebには、コントロール内で特定の変更が発生したときに特定のタスクを実行するために使用できるいくつかのイベントがあります。

このトピックでは、Aspose.Cells.GridWebコントロールでサポートされているすべてのイベントについて紹介し、これらのイベントをどのように扱うかについて詳細を提供します。

### **Gridイベントへの導入**

Aspose.Cells.GridWebコントロールは、コントロールで特定のイベントがトリガーされたときに操作をより細かく行うための複数のイベントをサポートしています。Aspose.Cells.GridWebコントロールでサポートされているイベントの完全なリストは以下で見つけることができます。

|**イベント**|**説明**|
| :- | :- |
|CellCommand|セルのコマンドハイパーリンクがクリックされたときに発生します。このイベントが発生すると、そのパラメータe.Argumentがコマンドの名前を提供します。
|CellDoubleClick|セルがダブルクリックされたときに発生します。
|ColumnDeleted|クライアント側のメニューを使用してワークシートから列を削除するユーザーがいる場合に発生します。
クライアント側のメニューを使用してワークシートから列を削除しようとする場合に発生します。
列ヘッダーがダブルクリックされたときに発生します。
クライアント側のメニューを使用してワークシートに列を挿入しようとする際に発生します。
ユーザーがカスタムコマンドボタンをクリックしたときに発生します。
コントロールのEnableSessionプロパティがfalseに設定されており、セッションレスモードでワークシートデータをロードする必要がある場合に発生します。セッションレスモードで、ファイルやデータベースからワークシートデータをロードするためにこのイベントを処理できます。
コントロールのシートページインデックスが変更されたときに発生します。
クライアント側のメニューを使用してワークシートから行を削除しようとする場合に発生します。
クライアント側のメニューを使用してワークシートから行を削除しようとする場合に発生します。
行ヘッダーがダブルクリックされたときに発生します。
|RowInserted|クライアント側のメニューを使用してワークシートに行を挿入したときに発生します。
|SaveCommand|**保存**ボタンがクリックされたときに発生します。
|SheetTabClick|シートタブがクリックされたときに発生します。
|SubmitCommand|**送信**ボタンがクリックされたときに発生します。
|UndoCommand|**元に戻す**ボタンがクリックされたときに発生します。
|AjaxCallFinished|コントロールのAJAX更新が終了したときに発生します。(EnableAJAXがtrueに設定されている必要があります)。
|CellModifiedOnAjax|AJAX呼び出しでセルが変更されたときに発生します。
|AfterColumnFilter|列にフィルターが適用されたときに発生します。

### **グリッドイベントの処理**

特定のイベントをトリガーとして特定の操作を行うには、イベントハンドラを作成する必要があります。 イベントハンドラは、特定のイベントがトリガーされたときに必要なタスクを実行します。 以下の例では、シンプルなグリッドイベントの処理方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **ダブルクリックイベントの操作**

Aspose.Cells.GridWeb には、3種類のダブルクリックイベントが含まれています:

- CellDoubleClick: セルがダブルクリックされたときに発生します。
- ColumnDoubleClick: 列ヘッダがダブルクリックされたときに発生します。
- RowDoubleClick: 行ヘッダがダブルクリックされたときに発生します。

このトピックでは、Aspose.Cells.GridWeb でのダブルクリックイベントの有効化と、これらのイベントのためのイベントハンドラの作成について説明します。

### **ダブルクリックイベントの有効化**

すべての種類のダブルクリックイベントをクライアント側で有効にするには、GridWeb コントロールの EnableDoubleClickEvent プロパティを true に設定します。

{{% alert color="primary" %}}

デフォルトでは、EnableDoubleClickEvent プロパティは false に設定されています。 これは、ダブルクリックイベントがデフォルトで有効になっていないことを意味します。 このようなイベントを実装するには、まずこの機能を有効にする必要があります。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

ダブルクリックイベントが有効になると、任意のダブルクリックイベントのためのイベントハンドラを作成できます。 これらのイベントハンドラは、特定のダブルクリックイベントが発生したときに特定のタスクを実行します。

### **ダブルクリックイベントの処理**

#### **セルのダブルクリック**

CellDoubleClick イベントのイベントハンドラは、CellEventArgs タイプの引数を提供します。 これにより、ダブルクリックされたセルの完全な情報が提供されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **列ヘッダのダブルクリック**

ColumnDoubleClick イベントのイベントハンドラは、ColumnDoubleClick イベントのイベントハンドラは、RowColumnEventArgs タイプの引数を提供し、ダブルクリックされたヘッダの列のインデックス番号などの情報が提供されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **行ヘッダのダブルクリック**

RowDoubleClick イベントのイベントハンドラは、RowColumnEventArgs タイプの引数を提供し、ダブルクリックされたヘッダの行のインデックス番号などの情報が提供されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Aspose.Cells.GridWebのスタイルまたは外観の設定**

Aspose.Cells.GridWebにはデフォルトの外観がありますが、外観を変更することも可能です。Aspose.Cells.GridWebは、開発者が外観を完全に制御するためにいくつかのプロパティを提供しています。このトピックでは、その中のいくつかのプロパティについて説明します。

### **Aspose.Cells.GridWebのスタイルまたは外観の設定**

#### **プリセットスタイル**

開発者の手間を省くために、Aspose.Cells.GridWebはいくつかのプリセットスタイルを提供しています。リストからスタイルを選択して適用するだけです。

|**スタイル**|**色の配色**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
特定のスタイルが選択されると、GridWebコントロール全体の外観が変更されます。 開発者は、柔軟なAspose.Cells.GridWebのAPIを使用して、ランタイムでプリセットスタイルを選択して適用することができます。

GridWebコントロールは、開発者が任意のプリセットスタイルを割り当てることができるPresetStyleプロパティを提供します。

以下のコードスニペットの出力は以下に示されています。

Colorful1スタイルが適用されたGridWebコントロール

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **ヘッダーバースタイル**

GridWebコントロールを見ると、2つのヘッダーバーがあることに気付くでしょう。 列用のもの（A、B、C、Dなど）と行用のもの（1、2、3、4など）です。 Aspose.Cells.GridWebでは、これらのヘッダーバーの外観を制御することが可能です。 開発者は、ランタイムでヘッダーバーのスタイルを設定することができます。

{{% alert color="primary" %}}

GridWebコントロールは、コントロールの両方のヘッダーバーにスタイルを適用するHeaderBarStyleプロパティを提供します。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **タブバースタイル**

タブバーのスタイルを設定することができます。次のコードを参照してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **スタイルファイルの読み込み**

開発者は、既存のスタイルファイルからGridWebコントロールにスタイル設定を適用するために、コントロールのCustomStyleFileNameプロパティにスタイルファイルのパスを設定することができます。ただし、その前に、コントロールのPresetStyleプロパティをCustomに設定する必要があります。なぜなら、スタイルファイルには、すでに開発者によって定義されたカスタムスタイル情報が含まれているためです。

カスタムスタイルが適用されたGridWebを示す次の画像をご覧ください。

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

重要：GridWebコントロールにスタイルファイルを読み込んでも、コントロールのセルの書式設定には影響しません。

{{% /alert %}}

#### **サンプルカスタムスタイルテンプレート**

以下はサンプルのカスタムスタイルテンプレートです。必要に応じて変更することができます。

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Webフォームでコントロールを作成する**

この記事では、GridWebコントロールを含むシンプルなWebフォームJSP（Java Server Page）を作成する方法について説明します。

ステップ1 - ディレクトリ構造の作成

Tomcat Serverの**webapps**ディレクトリに、以下のディレクトリ構造を作成する必要があります

![todo:image_alt_text](working-with-gridweb_7.png)

これらが作成する必要のあるディレクトリとファイルです。コメントを読んでそれに従ってください。最新のAspose.Cells.GridWeb for Javaのリリースアーカイブは、[このリンク](https://downloads.aspose.com/cells/java)から入手できます。

{{< highlight java >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

ステップ2 - 作成したファイルにコードを追加

このセクションでは、上記のディレクトリ構造で作成されたさまざまなファイルのコードを示しています。これらのコードを取得し、メモ帳でファイルを開いてコピー/貼り付けしてください。

**Web.xml**

{{< highlight java >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight java >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

ステップ3 - サンプルJSPウェブページの実行

これで作業はすべて完了しました。ウェブページを実行する準備が整いました。Tomcatサーバーを起動して、次のURLをWebブラウザに貼り付けてください。

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

次のスクリーンショットのようなものが表示されます。おめでとうございます、JSPページでGridWebコントロールを正常に使用しました。

![todo:image_alt_text](working-with-gridweb_8.png)

## **GridWeb の印刷**

開発者がMicrosoft Excelファイルを保存せずにWebページからGridWebのコンテンツを印刷する必要がある場合があります。Aspose.Cells.GridWebコントロールは、この機能をサポートしています。

### **GridWeb の印刷**

別のファイルを保存せずに印刷するには、クライアント側でGridWebクラスのprint()メソッドを呼び出します。適切なイベントを選択することもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

クライアント側のサンプルコード

### **クライアントサイドのサンプルコード**

次のリンクをご覧ください。これは、クライアント側からgridweb.print()メソッドを呼び出すリンクです。

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **異なるグリッドモードの紹介**

この記事では、Aspose.Cells.GridWebの異なるモードについて説明しています。これらのモードは、異なる機能や動作を持つため、論理的に区別されています。私たちは、次の種類のモードを特定しました。

- Edit モード
- View モード

これらのモードはそれぞれ独自の特性を持ちます。開発者は、必要に応じて任意のモードで Aspose.Cells.GridWeb と連携できます。以下で各モードを見ていきます。

### **Edit モード**

デフォルトでは、Aspose.Cells.GridWeb コントロールは Edit モードになっています。Edit モードでは、Aspose.Cells.GridWeb コントロールが提供するすべての機能を使用して、グリッドコンテンツを完全に編集したり修正したりできます。これらの機能には次のものが含まれます:

- グリッドのコンテンツを Microsoft Excel ファイルに保存する。
- サーバーにデータを送信する。
- 数式の計算。
- 前のアクションを取り消す、または破棄する。
- 行と列を管理する。
- データを切り取り、コピー、または貼り付ける。
- セルなどの書式を設定する。

**編集モードのGridWebコントロール**

![todo:image_alt_text](working-with-gridweb_9.png)

開発者は、GridWebコントロールのEditModeプロパティをtrueに設定することでプログラムで編集モードに切り替えることもできます。

### **コード例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **ビューモード**

GridWebコントロールが表示モードになっている場合、ユーザーはグリッドの内容を編集したり変更したりすることはできません。つまり、ユーザーはグリッドの内容を表示するだけです。それがこのモードが表示モードと呼ばれる理由です。表示モードでは、いくつかのボタン(**送信**、**保存**、**元に戻す**)が非表示になり、右クリックした際に表示されるメニューには**コピー**と**検索**のオプションしか含まれません。

**ビューモードのGridWebコントロール** 

![todo:image_alt_text](working-with-gridweb_10.png)

開発者がユーザーにデータを表示のみで表示させたい場合は、GridWebコントロールのEditModeプロパティを**false**に設定することで、プログラム上でも表示モードに切り替えることができます。

### **コード例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

ビューモードでも、ユーザーは行と列の高さと幅を変更することができます。

{{% /alert %}}
