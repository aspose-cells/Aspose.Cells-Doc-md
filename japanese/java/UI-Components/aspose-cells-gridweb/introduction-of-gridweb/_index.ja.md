---
title: GridWebの紹介
type: docs
weight: 10
url: /ja/java/introduction-of-gridweb/
---
## **GridWebの基本**
Aspose.Cells.GridWebは、JSPウェブページまたはjavaサーバの任意のhtmlページに埋め込むことができるGUIベースのウェブコントロールです。 
{{% alert color="primary" %}} 

使いやすくシンプルです。

スプレッドシートファイルのオンライン Web エディタを素早く構築できます。

MS Excel ファイルと完全に互換性のあるあらゆるスプレッドシート形式ファイルのインポートとエクスポートもサポートします。

## **Aspose.Cells.GridWeb - デモ**
{{% alert color="primary" %}} 

すばやく始めるために、Aspose.Cells.GridWeb APIの使用方法を示すいくつかのコード例とデモを提供しています。

以下のリンクからデモをダウンロードしてください。
[Aspose.Cells.GridWeb デモ](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **Aspose.Cells for GridWeb Javaデモの実行方法**
{{% alert color="primary" %}} 

Aspose.Cells for GridWeb Javaデモは簡単に実行できます。ウェブサーバに**gridwebdemo.war**を展開するだけです。この[リンク](https://forum.aspose.com/uploads/discourse_instance3/22292)からデモをダウンロードしてください。

この記事では、Apache TomcatサーバーでAspose.Cells for GridWeb Javaデモを実行する方法について説明しています。

{{% /alert %}} 
### **GridWeb Javaデモのステップバイステップガイド**
1. 任意のディレクトリに**apache-tomcat-7.0.52.zip**を解凍します（例：C:\Tomcat） 

![todo:image_alt_text](introduction-of-gridweb_1.png)



以下のスナップショットは、Apache Tomcatサーバーの展開されたディレクトリとファイルを示しています。 

![todo:image_alt_text](introduction-of-gridweb_2.png)



環境変数**CATALINA_HOME**を設定する必要がある場合もあります 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. **tomcat-users.xml**ファイルを開きます。 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. このユーザーを追加します：

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**ここでのユーザー名はtomcatであり、パスワードはsecretです** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. **startup.bat**ファイルを実行します。
   Apache Tomcatサーバーが実行されます。 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**コマンドウィンドウで実行中のTomcatサーバー** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. ブラウザを開いて**localhost:8080**と入力します。
   Apache Tomcatのウェブページが表示されます。 

   **Apache Tomcatのウェブページ** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. **Manager App**をクリックしてユーザー名とパスワードを入力します（上記のように、tomcat、secret） 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. **WAR file to deploy**セクションまでスクロールして**gridwebdemo.war**ファイルを参照します。
1. **デプロイ** をクリックします。 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. **gridwebdemo.war** ファイルを参照します。 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. **デプロイ** をクリックします。 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. デプロイされたら、**/gridwebdemo** をクリックしてデモを実行します。 

![todo:image_alt_text](introduction-of-gridweb_13.png)


GridWeb デモページが表示されます。 

**GridWeb デモページ** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. 任意のデモをクリックして実行します。 

   **コンテンツの作成デモが実行中** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**ワークシートデモが実行中** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**ヘッダーバーとコマンドボタンデモが実行中** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
## **ブラウザの機能と Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb は、他の Web コントロールと同様に JSP Web ページに埋め込むことができる GUI ベースの Web コントロールです。Web コントロールの最も重要な点は、クロスブラウザ対応を提供することです。Aspose.Cells.GridWeb は、クロスブラウザ対応を提供します。
### **比較**
Aspose.Cells.GridWeb は Microsoft の Internet Explorer (IE) で完全にサポートされています。ただし、他のブラウザではわずかな制限があります。このトピックでは、異なるブラウザでサポートされている機能の詳細な比較を提供します。

|**クライアント側の機能**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|セルのコンテキストメニュー|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|クライアント側の検証|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ダブルクリックイベント|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDownList（ *コンボボックスモード* ）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDownList（ *ポップアップメニューモード* ）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|式の入力/編集|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行/列の凍結または解凍|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ハイパーリンク（ *セルコマンドモード* ）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ハイパーリンク（ *URLモード* ）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|セルの結合または解除|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|複数のセルのコピー/貼り付け|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|複数のセルの入力/編集、単一のポストバック|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|数値書式|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|シートのページ送り|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|読み取り専用セル|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|読み取り専用行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|正規表現を使用したデータ検証|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|列幅の変更|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行の高さの変更|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行/列の挿入/削除|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|コンテンツのスクロール|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|シートタブのスクロール|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|セルの境界線の設定|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|セルのフォント設定の設定|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
