---
title: GridWebの紹介
type: docs
weight: 10
url: /ja/java/introduction-of-gridweb/
---
## **GridWeb Java デモ用に Aspose.Cells を実行する方法**
{{% alert color="primary" %}} 

Aspose.Cells GridWeb Java デモは簡単に実行できます。デプロイするだけです**gridwebdemo.war**あなたのウェブサーバーで。ここからデモをダウンロードしてください[リンク](https://forum.aspose.com/uploads/discourse_instance3/22292).

この記事では、Apache Tomcat サーバーで GridWeb Java デモ用に Aspose.Cells を実行する方法について説明します。

{{% /alert %}} 
### **GridWeb Java デモを実行するためのステップバイステップガイド**
1. エキス**Apache-Tomcat-7.0.52.zip** C:\Tomcat などの任意のディレクトリ

![todo:画像_代替_文章](introduction-of-gridweb_1.png)



次のスナップショットは、Apache Tomcat サーバーの抽出されたディレクトリとファイルを示しています。

![todo:画像_代替_文章](introduction-of-gridweb_2.png)



環境変数を設定する必要がある場合もあります**CATALINA_HOME** 

![todo:画像_代替_文章](introduction-of-gridweb_3.png)

1. 開く**tomcat-users.xml**ファイル。

![todo:画像_代替_文章](introduction-of-gridweb_4.png)

1. このユーザーを追加:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**ここで、ユーザー名は tomcat で、パスワードは secret です** 

![todo:画像_代替_文章](introduction-of-gridweb_5.png)

1. 実行します**スタートアップ.bat**ファイル。
 Apache Tomcat サーバーを実行します。

![todo:画像_代替_文章](introduction-of-gridweb_6.png)



**コマンド ウィンドウで実行されている Tomcat サーバー** 

![todo:画像_代替_文章](introduction-of-gridweb_7.png)

1. ブラウザを開いて入力します**ローカルホスト:8080**.
 Apache Tomcat Web ページが表示されます。

   **Apache Tomcat の Web ページ** 

![todo:画像_代替_文章](introduction-of-gridweb_8.png)

1. クリック**マネージャー アプリ**ユーザー名とパスワードを入力します。 (上記のように: tomcat, secret)

![todo:画像_代替_文章](introduction-of-gridweb_9.png)

1. セクションまでスクロールします**デプロイするWARファイル**を閲覧し、**gridwebdemo.war**ファイル。
1. クリック**配備**. 

![todo:画像_代替_文章](introduction-of-gridweb_10.png)

1. ブラウズ**gridwebdemo.war**ファイル。

![todo:画像_代替_文章](introduction-of-gridweb_11.png)

1. クリック**配備**. 

![todo:画像_代替_文章](introduction-of-gridweb_12.png)

1. 展開したら、クリックします**/gridwebdemo**デモの実行を開始します。

![todo:画像_代替_文章](introduction-of-gridweb_13.png)


 GridWeb デモ ページが表示されます。

**GridWeb デモページ** 

![todo:画像_代替_文章](introduction-of-gridweb_14.png)

1. 任意のデモをクリックして実行します。

   **コンテンツ作成デモ実施中** 

![todo:画像_代替_文章](introduction-of-gridweb_15.png)



**ワークシートのデモの実行** 

![todo:画像_代替_文章](introduction-of-gridweb_16.png)



**HeaderBar と CommandButton のデモの実行中** 

![todo:画像_代替_文章](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb - デモ**
{{% alert color="primary" %}} 

すぐに使いこなせるように、Aspose.Cells.GridWeb API の使用方法を示す多数のコード例とデモを提供しています。

以下のリンクからデモをダウンロードしてください。
[Aspose.Cells.GridWeb デモ](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **ブラウザの機能と Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb は、他の Web コントロールと同様に JSP Web ページに埋め込むことができる GUI ベースの Web コントロールです。 Web コントロールで最も重要なことは、クロスブラウザー サポートを提供することです。 Aspose.Cells.GridWeb は、クロスブラウザー サポートを提供します。
### **比較**
Aspose.Cells.GridWeb は、Microsoft の Internet Explorer (IE) で完全にサポートされています。ただし、他のブラウザーでは、小さな制限があります。このトピックでは、さまざまなブラウザーでサポートされている機能を詳細に比較します。

|**クライアント側の機能**|**Microsoft インターネット エクスプローラー**|**Google クロム**|**モジラ ファイアフォックス**|**オペラ**|
|:- |:- |:- |:- |:- |
|Cellのコンテキストメニュー|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|クライアント側の検証|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ダブルクリックイベント|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ドロップダウンリスト （*コンボボックス モード* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ドロップダウンリスト （*ポップアップ メニュー モード* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|数式入力・編集|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行/列の凍結または凍結解除|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ハイパーリンク (*CellCommand モード* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ハイパーリンク (*URL モード* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|マージまたはマージ解除 Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|複数 Cells コピー/貼り付け|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|複数の Cells 入力/編集、単一のポストバック|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|数値形式|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|シートのページング|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|読み取り専用 Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|読み取り専用の行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|正規表現を使用したデータ検証|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|列幅のサイズ変更|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行の高さのサイズ変更|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|行と列の挿入/削除|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|スクロールコンテンツ|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|シートのタブをスクロール|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cells の境界線を設定|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cellsのフォント設定をする|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}}セルのコンテキスト メニューは、クライアント サイド メニュー ボタンをクリックすることによってのみアクティブ化できます。
