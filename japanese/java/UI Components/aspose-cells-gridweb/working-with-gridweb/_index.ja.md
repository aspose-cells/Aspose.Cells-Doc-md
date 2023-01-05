---
title: GridWeb の操作
type: docs
weight: 20
url: /ja/java/working-with-gridweb/
---
## **Microsoft Excel ファイルを開く**

Aspose.Cells.GridWeb コントロールは Microsoft Excel ファイルを開いて読み込むことができます - データ、書式設定、グラフ、画像などを完備しています。このトピックではその方法を説明します。

GridWeb コントロールを使用して Excel ファイルを開くには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. ファイル パスを指定して、Excel ファイルをインポートします。
1. アプリケーションを実行するか、ページを開きます。

Excel ファイルから Aspose.Cells.GridWeb コントロールにコンテンツをロードするには、importExcelFile メソッドを呼び出して Excel ファイルのパスを指定する必要があります。その後、GridWeb コントロールは指定されたパスからファイルを自動的に検索し、その内容を表示します。 Excel ファイルの内容をロードするコード スニペットを以下に示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

上記のコード スニペットは、任意の方法で使用できます。たとえば、Web フォームの読み込み時に Excel ファイルを自動的に読み込むには、このコードを、自分で指定したフォームの Page_Load イベントに追加します。

**ExcelファイルがGridWebに読み込まれます**

![todo:画像_代替_文章](working-with-gridweb_1.png)

## **Microsoft Excel ファイルの保存**

Aspose.Cells.GridWeb コントロールを使用して、GUI モードの Web サイトで、新しい Microsoft Excel ファイルを作成したり、既存の Microsoft Excel ファイルを操作したりできます。その後、ファイルを Excel ファイルに保存できます。 Aspose.Cells.GridWeb は、オンラインのスプレッドシート エディターとして効果的に機能します。このトピックでは、グリッド コンテンツを Excel ファイルに保存する方法について説明します。

### **ファイルとして保存する**

Aspose.Cells.GridWeb コントロールのコンテンツを Excel ファイルとして保存するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 指定したパスに Excel ファイルとして作業を保存します。
1. アプリケーションを実行するか、ページを開きます。

次のコード例は、グリッド コンテンツを Excel ファイルに保存する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

上記のコード スニペットは、いくつかの方法で使用できます。一般的な方法は、クリックしたときにグリッド コンテンツを Excel ファイルに保存するボタンを追加することです。 Aspose.Cells.GridWeb は、タスクに対するより簡単なアプローチを提供します。 Aspose.Cells.GridWeb には SaveCommand というイベントがあります。上記のコード スニペットを SaveCommand イベントのイベント ハンドラに追加すると、ユーザーは Aspose.Cells.GridWeb の組み込み**セーブ**ボタン。

## **Aspose.Cells.GridWeb とそのヘッダー バーのサイズ変更**

この記事では、実行時に Aspose.Cells.GridWeb API を使用して GridWeb のサイズを変更する方法について説明します。また、Aspose.Cells.GridWeb コントロールのヘッダー バーのサイズを変更して、データを読みやすくする方法についても説明します。

### **Aspose.Cells.GridWeb の幅と高さを変更する**

Aspose.Cells.GridWeb コントロールの幅と高さを変更することは、単純ですが重要な機能です。 Aspose.Cells.GridWeb コントロールは、API の GridWeb クラスによって表されます。GridWeb コントロールの幅と高さを変更するには、幅と高さのプロパティを使用します。

{{% alert color="primary" %}}

コントロールの幅と高さは、ピクセルまたはポイントで定義できます。

{{% /alert %}}

次のコード スニペットの出力を以下に示します。

**GridWeb コントロールの幅と高さを変更**

![todo:画像_代替_文章](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **ヘッダーバーの幅と高さを変更する**

Aspose.Cells.GridWeb コントロールには、次の 2 つのヘッダー バーが含まれています。

- 上部のヘッダー バー。このヘッダー バーは列を A、B、C、D などで表します。
- 左のヘッダー バー。このヘッダー バーは行を 1、2、3、4 などで表します。

これらのヘッダー バーの両方を以下に示します。

**ヘッダーバー**

![todo:画像_代替_文章](working-with-gridweb_3.png)

GridWeb コントロールの HeaderBarHeight プロパティと HeaderBarWidth プロパティをそれぞれ使用して、上部のヘッダー バーの高さと左側のヘッダー バーの幅を変更します。次の図は、次のコード例の出力を示しています。

**ヘッダーバーの幅と高さを変更**

![todo:画像_代替_文章](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Aspose.Cells.GridWeb イベントの操作**

すべての開発者は、イベントとその目的に精通している必要があります。イベントは、コントロールまたはクラスで発生する可能性のある変更の通知を送信するために使用されます。 Aspose.Cells.GridWeb には、コントロールで特定の変更が発生したときに特定のタスクを実行するために使用できるいくつかのイベントがあります。

このトピックでは、Aspose.Cells.GridWeb コントロールでサポートされているすべてのイベントの概要と、これらのイベントの処理方法の詳細について説明します。

### **グリッド イベントの概要**

Aspose.Cells.GridWeb コントロールは、特定のイベントがコントロールでトリガーされたときに操作を実行するためのより詳細な制御を提供するいくつかのイベントをサポートします。 Aspose.Cells.GridWeb コントロールでサポートされているイベントの完全なリストを以下に示します。

|**イベント**|**説明**|
|:- |:- |
|セルコマンド|セルのコマンド ハイパーリンクがクリックされたときに発生します。このイベントが発生すると、そのパラメーター e.Argument がコマンドの名前を提供します。|
|セルダブルクリック|セルがダブルクリックされたときに発生します。|
|列が削除されました|ユーザーがクライアント側メニューを使用してワークシートから列を削除すると発生します。|
|列の削除|ユーザーがクライアント側メニューを使用してワークシートから列を削除しようとすると発生します。|
|列のダブルクリック|列ヘッダーがダブルクリックされたときに発生します。|
|挿入された列|ユーザーがクライアント側メニューを使用してワークシートに列を挿入すると発生します。|
|カスタムコマンド|ユーザーがカスタム コマンド ボタンをクリックすると発生します。|
|LoadCustomData|コントロールの EnableSession プロパティが false に設定され、ワークシート データを読み込む必要がある場合に発生します。このイベントをセッションレス モードで処理して、ファイルまたはデータベースからワークシート データをロードできます。|
|ページインデックスが変更されました|コントロールのシート ページ インデックスが変更されたときに発生します。|
|行が削除されました|ユーザーがクライアント側メニューを使用してワークシートから行を削除すると発生します。|
|行の削除|ユーザーがクライアント側メニューを使用してワークシートから行を削除しようとすると発生します。|
|行ダブルクリック|行ヘッダーがダブルクリックされたときに発生します。|
|行が挿入されました|ユーザーがクライアント側メニューを使用してワークシートに行を挿入すると発生します。|
|保存コマンド|次の場合に発生します。**セーブ**ボタンがクリックされます。|
|シートタブクリック|シート タブがクリックされると発生します。|
|SubmitCommand|次の場合に発生します。**送信**ボタンがクリックされます。|
|元に戻すコマンド|次の場合に発生します。**元に戻す**ボタンがクリックされます。|
|AjaxCallFinished|コントロールの AJAX 更新が完了したときに発生します。 (EnableAJAX は true に設定されます)。|
|CellModifiedOnAjax|AJAX 呼び出しでセルが変更されたときに発生します。|
|AfterColumnFilter|フィルターが列に適用されると発生します。|

### **グリッド イベントの処理**

特定のイベントをトリガーして特定の操作を実行するには、イベント ハンドラーを作成する必要があります。イベント ハンドラーは、特定のイベントがトリガーされたときに目的のタスクを実行します。次の例は、単純なグリッド イベントを処理する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **ダブルクリック イベントの操作**

Aspose.Cells.GridWeb には、次の 3 種類のダブルクリック イベントが含まれています。

- CellDoubleClick は、セルがダブルクリックされたときに発生します。
- ColumnDoubleClick は、列ヘッダーがダブルクリックされたときに発生します。
- RowDoubleClick、行ヘッダーがダブルクリックされたときに発生します。

このトピックでは、Aspose.Cells.GridWeb でダブルクリック イベントを有効にする方法について説明します。また、これらのイベントのイベント ハンドラーの作成についても説明します。

### **ダブルクリック イベントの有効化**

GridWeb コントロールの EnableDoubleClickEvent プロパティを true に設定することにより、すべてのタイプのダブルクリック イベントをクライアント側で有効にすることができます。

{{% alert color="primary" %}}

デフォルトでは、EnableDoubleClickEvent プロパティは false に設定されています。これは、デフォルトではダブルクリック イベントが有効になっていないことを意味します。このようなイベントを実装するには、まず機能を有効にします。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

ダブルクリック イベントを有効にすると、任意のダブルクリック イベントのイベント ハンドラーを作成できます。これらのイベント ハンドラーは、特定のダブルクリック イベントが発生したときに特定のタスクを実行します。

### **ダブルクリック イベントの処理**

#### **ダブルクリック Cell**

CellDoubleClick イベントのイベント ハンドラーは、ダブルクリックされたセルの完全な情報を提供する CellEventArgs 型の引数を提供します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **列ヘッダーをダブルクリック**

ColumnDoubleClick イベントのイベント ハンドラーは、ダブルクリックされたヘッダーの列のインデックス番号とその他の情報を提供する RowColumnEventArgs 型の引数を提供します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **行ヘッダーをダブルクリック**

RowDoubleClick イベントのイベント ハンドラーは、ダブルクリックされたヘッダーの行のインデックス番号とその他の関連情報を提供する RowColumnEventArgs 型の引数を提供します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Aspose.Cells.GridWeb のスタイルまたは外観の設定**

Aspose.Cells.GridWeb には独自のデフォルトのルック アンド フィールがありますが、外観を変更することができます。 Aspose.Cells.GridWeb は、開発者がその外観を完全に制御できるように、いくつかのプロパティを提供します。このトピックでは、これらのプロパティのいくつかについて説明します。

### **Aspose.Cells.GridWeb のスタイルまたは外観の設定**

#### **プリセット スタイル**

開発者の労力を節約するために、Aspose.Cells.GridWeb にはいくつかのプリセット スタイルが用意されています。スタイルを適用するには、リストからスタイルを選択するだけです。

|**スタイル**|**カラースキーム**|
|:- |:- |
|標準|銀|
|カラフル1|ローズ|
|カラフル2|青い|
|プロフェッショナル1|シアン|
|プロフェッショナル2|シアン再び|
|トラディショナル1|暗い|
|トラディショナル2|グレー|
|カスタム|カスタマイズされた|
特定のスタイルが選択されると、GridWeb コントロールの全体的な外観が変更されます。開発者は、Aspose.Cells.GridWeb の柔軟な API を使用して、実行時に適用されるプリセット スタイルを選択できます。

GridWeb コントロールは、開発者が任意のプリセット スタイルを割り当てることができる PresetStyle プロパティを提供します。

以下のコード スニペットの出力を以下に示します。

**Colorful1 スタイルが適用された GridWeb コントロール**

![todo:画像_代替_文章](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **ヘッダー バーのスタイル**

GridWeb コントロールを見ると、2 つのヘッダー バーがあることがわかります。 1 つは列 (A、B、C、D など) 用で、もう 1 つは行 (1、2、3、4 など) 用です。 Aspose.Cells.GridWeb を使用すると、開発者はこれらのヘッダー バーの外観を制御できます。開発者は、実行時にヘッダー バーのスタイルを設定できます。

{{% alert color="primary" %}}

GridWeb コントロールは、コントロールの両方のヘッダー バーにスタイルを適用する HeaderBarStyle プロパティを提供します。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **タブバーのスタイル**

タブバーのスタイルも設定できます。次のコードを参照してください

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **スタイルファイルを読み込んでいます**

既存のスタイル ファイルから GridWeb コントロールにスタイル設定を適用するために、開発者はスタイル ファイルのパスをコントロールの CustomStyleFileName プロパティに設定できます。ただし、それを行う前に、コントロールの PresetStyle プロパティを Custom に設定する必要があります。そのスタイル ファイルには、開発者によって既に定義されているカスタム スタイル情報が含まれているためです。

カスタム スタイルが適用された GridWeb を示す次の画像を参照してください。

![todo:画像_代替_文章](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

重要: スタイル ファイルを GridWeb コントロールにロードしても、コントロールのセルの書式設定には影響しません。

{{% /alert %}}

#### **カスタム スタイル テンプレートのサンプル**

カスタム スタイル テンプレートのサンプルを次に示します。要件に応じて変更できます。

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Web フォームでのコントロールの作成**

この記事では、GridWeb コントロールを持つ単純な Web フォーム JSP (Java サーバー ページ) を作成する方法について説明します。

**ステップ 1 - ディレクトリ構造を作成する**

に次のディレクトリ構造を作成する必要があります。**ウェブアプリ**Tomcat サーバーのディレクトリ

![todo:画像_代替_文章](working-with-gridweb_7.png)

これらは、作成する必要があるディレクトリとファイルです。コメントを読んでフォローしてください。から最新の Aspose.Cells.GridWeb for Java リリース アーカイブを入手できます。[このリンク](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

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

**ステップ 2 - 作成したファイルにコードを追加する**

このセクションでは、上記のディレクトリ構造で作成されるさまざまなファイルのコードを示します。これらのコードを取得し、メモ帳で開いてコピーして貼り付け、ファイルに追加してください。

**Web.xml**

{{< highlight "java" >}}

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

{{< highlight "java" >}}

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

**ステップ 3 - サンプル JSP Web ページの実行**

これですべて完了です。 Web ページを実行する時が来ました。 Tomcat サーバーを起動し、次の URL を Web ブラウザーに貼り付けてください。

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

次のスクリーンショットのようなものが表示されます。おめでとうございます。JSP ページで GridWeb コントロールを正常に使用できました。

![todo:画像_代替_文章](working-with-gridweb_8.png)

## **GridWeb の印刷**

開発者は、Microsoft Excel ファイルを保存せずに、Web ページに含まれる GridWeb コンテンツを印刷する必要がある場合があります。 Aspose.Cells.GridWeb コントロールは、この機能をサポートしています。

### **GridWeb の印刷**

別のファイルを保存せずに印刷するには、クライアント側で GridWeb クラスの print() メソッドを呼び出してグリッドを印刷します。適切なイベントを選択することもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

クライアント側から呼び出すため、最初に gridweb クライアント ID を取得する必要があります。 gridweb.getClientID() メソッドを使用してクライアント ID を取得できます。

### **クライアント側のサンプル コード**

クライアント側から gridweb.print() メソッドを呼び出す次のリンクを参照してください。

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **さまざまなグリッド モードの紹介**

この記事では、Aspose.Cells.GridWeb のさまざまなモードについて説明します。これらのモードは、機能と動作が異なるため、論理的に区別されます。さまざまなタイプのモードを次のように識別しました。

- 編集モード
- ビューモード

これらのモードにはすべて独自の特徴があります。開発者は、要件に応じて任意のモードで Aspose.Cells.GridWeb を操作できます。以下、各モードについて見ていきます。

### **編集モード**

デフォルトでは、Aspose.Cells.GridWeb コントロールは編集モードになっています。編集モードでは、Aspose.Cells.GridWeb コントロールによって提供されるすべての機能を使用して、グリッド コンテンツを完全に編集または変更できます。これらの機能は次のとおりです。

- グリッド コンテンツを Microsoft Excel ファイルに保存します。
- サーバーへのデータの送信。
- 数式の計算。
- 以前のアクションを元に戻すまたは破棄する。
- 行と列の管理。
- データの切り取り、コピー、または貼り付け。
- セルの書式設定など

**編集モードの GridWeb コントロール**

![todo:画像_代替_文章](working-with-gridweb_9.png)

開発者は、GridWeb コントロールの EditMode プロパティを true に設定することにより、プログラムで編集モードに切り替えることもできます。

### **コード例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **ビューモード**

GridWeb コントロールが表示モードの場合、ユーザーはグリッド コンテンツを編集または変更できません。つまり、ユーザーはグリッド コンテンツのみを表示できます。そのため、このモードはビュー モードと呼ばれます。表示モードでは、いくつかのボタン (**送信**, **セーブ**と**元に戻す** ) が非表示になり、右クリックしたときに表示されるメニューには**コピー**と**探す**オプション。

**表示モードの GridWeb コントロール** 

![todo:画像_代替_文章](working-with-gridweb_10.png)

開発者がユーザーにデータの表示のみを許可したい場合は、GridWeb コントロールの EditMode プロパティを**間違い**.

### **コード例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

表示モードでも、ユーザーは行と列の高さと幅を変更できます。

{{% /alert %}}
