---
title: GridWebの紹介
type: docs
weight: 10
url: /ja/java/introduction-of-gridweb/
---
##  **GridWeb の基本**
Aspose.Cells.GridWeb は、JSP Web ページまたは Java サーバーの任意の HTML ページに埋め込むことができる GUI ベースの Web コントロールです。
{{% alert color="primary" %}} 

使い方は簡単です。

スプレッドシート ファイル用のオンライン Web エディタを迅速に構築するのに役立ちます。

また、MS Excel ファイルと 100% 互換性のあるあらゆる種類のスプレッドシート形式ファイルのインポートとエクスポートもサポートしています。

##  **Aspose.Cells.GridWeb - デモ**
{{% alert color="primary" %}} 

すぐに使い始められるように、Aspose.Cells.GridWeb API の使用方法を示すコード例とデモが多数提供されています。

以下のリンクからデモをダウンロードしてください。
[Aspose.Cells.GridWeb デモ](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


##  **GridWeb Java デモで Aspose.Cells を実行する方法**
{{% alert color="primary" %}} 

GridWeb の場合は Aspose.Cells Java のデモは簡単に実行できます。デプロイするだけです**グリッドウェブデモ.war** Webサーバー内で。ここからデモをダウンロードしてください[リンク](https://forum.aspose.com/uploads/discourse_instance3/22292).

この記事では、Apache Tomcat サーバーで GridWeb Java デモの Aspose.Cells を実行する方法について説明します。

{{% /alert %}} 
###  **GridWeb Java デモを実行するためのステップバイステップ ガイド**
1. 抽出する**apache-tomcat-7.0.52.zip**任意のディレクトリ (例: C:\Tomcat)

![todo:image_alt_text](introduction-of-gridweb_1.png)



次のスナップショットは、Apache Tomcat サーバーの抽出されたディレクトリとファイルを示しています。

![todo:image_alt_text](introduction-of-gridweb_2.png)



環境変数の設定が必要な場合もあります**CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. を開きます**tomcat-users.xml**ファイル。

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. このユーザーを追加します。

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**ここでは、ユーザー名は tomcat 、パスワードは Secret です。** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. を実行します。**スタートアップ.bat**ファイル。
 Apache Tomcat サーバーを実行します。

![todo:image_alt_text](introduction-of-gridweb_6.png)



**コマンド ウィンドウで実行される Tomcat サーバー** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. 次に、ブラウザを開いて「*localhost:8080**」と入力します。
 Apache Tomcat Web ページが表示されます。

   **Apache Tomcat Web ページ** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. クリック**マネージャーアプリ**ユーザー名とパスワードを入力します。 (上記と同様: Tomcat、シークレット)

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. セクションまで下にスクロールします**デプロイするWARファイル**そして閲覧してください**グリッドウェブデモ.war**ファイル。
1. [*展開**] をクリックします。

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. ブラウズ**グリッドウェブデモ.war**ファイル。

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. [*展開**] をクリックします。

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. デプロイされたら、クリックします**/gridwebdemo**そしてデモの実行を開始します。

![todo:image_alt_text](introduction-of-gridweb_13.png)


 GridWeb デモ ページが表示されます。

**GridWeb デモ ページ** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. 任意のデモをクリックして実行します。

   **コンテンツ作成デモ実行中** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**ワークシートのデモの実行中** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar と CommandButton のデモの実行中** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
##  **ブラウザの機能と Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb は、他の Web コントロールと同様に JSP Web ページに埋め込むことができる GUI ベースの Web コントロールです。 Web コントロールで最も重要なことは、クロスブラウザーのサポートを提供することです。 Aspose.Cells.GridWeb は、クロスブラウザーのサポートを提供します。
###  **比較**
Aspose.Cells.GridWeb は、Microsoft の Internet Explorer (IE) で完全にサポートされています。ただし、他のブラウザでは若干の制限があります。このトピックでは、さまざまなブラウザーでサポートされている機能を詳細に比較します。

|**クライアント側の機能**|**Microsoft Internet Explorer**|**Google クロム**|**モジラ Firefox**|**オペラ**|
| :- | :- | :- | :- | :- |
|Cellのコンテキストメニュー|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|クライアント側の検証|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ダブルクリックイベント|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ドロップダウンリスト （*コンボボックスモード* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ドロップダウンリスト （*ポップアップメニューモード* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|数式入力・編集|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行/列のフリーズまたはフリーズ解除|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ハイパーリンク (*セルコマンドモード* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ハイパーリンク (*URLモード* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|結合または結合解除 Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|複数の Cells のコピー/ペースト|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|複数の Cells 入力/編集、単一ポストバック|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|数値の形式|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|シートのページング|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|読み取り専用 Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|読み取り専用の行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|正規表現を使用したデータ検証|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|列幅のサイズを変更する|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行の高さのサイズを変更する|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行と列の挿入/削除|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|スクロールコンテンツ|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|シートタブをスクロールする|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cellsの境界線を設定する|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cellsのフォント設定をする|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}}セルのコンテキスト メニューは、[クライアント サイド メニュー] ボタンをクリックすることによってのみアクティブ化できます。
