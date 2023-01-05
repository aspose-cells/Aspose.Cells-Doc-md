---
title: GridWeb を Web フォームに追加する
type: docs
weight: 10
url: /ja/net/add-gridweb-to-web-form/
---
{{% alert color="primary" %}} 

このトピックでは、初心者が Web アプリケーションで Aspose.Cells.GridWeb コントロールを作成して使用するのに役立つ基本的なステップ バイ ステップ ガイドを提供します。

{{% /alert %}} 
## **Aspose.Cells.GridWeb コントロールの作成と使用**
### **ステップ 1: Web アプリケーション プロジェクトの作成**
最初に、Aspose.Cells.GridWeb コントロールを使用する Web アプリケーション プロジェクトを作成します。

1. Visual Studio を開きます。
1. から**ファイル**メニュー、選択**新しい**に続く**計画**. 

![todo:画像_代替_文章](add-gridweb-to-web-form_1.png)



[新しいプロジェクト] ダイアログが表示されます。

1. 選択する**ASP.NET Web アプリケーション**希望の言語に。

![todo:画像_代替_文章](add-gridweb-to-web-form_2.png)

1. 選択する**Web フォーム**テンプレート。

![todo:画像_代替_文章](add-gridweb-to-web-form_3.png)

1. プロジェクトに新しい Web フォームを追加します。
### **手順 2: コントロールを Web フォームに埋め込む**
Aspose.Cells.GridWeb コントロールを Visual Studio ツールボックスから Web フォームにドラッグ アンド ドロップします。

![todo:画像_代替_文章](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

 Aspose.Cells グリッド コントロールを Visual Studio ツールボックスに追加する方法については、以下をお読みください。[Aspose.Cells.Grid コントロールを Visual Studio.NET と統合する](/cells/ja/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

コントロールがフォームに追加されると、次のようにレンダリングされます。

![todo:画像_代替_文章](add-gridweb-to-web-form_5.png)
### **ステップ 3: コントロールのサイズ変更**
フォームはデフォルトのサイズで表示されます。境界線または角をドラッグしてサイズを調整します。

![todo:画像_代替_文章](add-gridweb-to-web-form_6.png)
### **ステップ 4: コントロール プロパティの設定**
Aspose.Cells.GridWeb コントロールは、さまざまなプロパティを使用して構成することもできます。

![todo:画像_代替_文章](add-gridweb-to-web-form_7.png)

[プロパティ] ダイアログを使用して、コントロールの多くのプロパティを調整できます。基本的なプロパティには、高さ、幅、色、およびビジュアル スタイルが含まれます。詳細プロパティには、編集モード、セッション モード、およびダブルクリック モードが含まれます。さらに、[プロパティ] ダイアログでカスタマイズされたイベント ハンドラーを設定することができます。

Aspose.Cells.GridWeb 用の追加の構成ツールもいくつかあります。これらは [プロパティ] ダイアログの下部にハイパーリンクとして表示されるか、GridWeb コントロールを右クリックして検索します。これらの構成ツールには次のものがあります。

- カスタム コマンド ボタン
#### **カスタム コマンド ボタン**
カスタム コマンド ボタン エディターを開くには:
 GridWeb コントロールを右クリックして、**カスタム コマンド ボタン**. 

![todo:画像_代替_文章](add-gridweb-to-web-form_8.png)



 CustomCommandButton Collection Editor ダイアログが表示されます。

![todo:画像_代替_文章](add-gridweb-to-web-form_9.png)

このダイアログを使用すると、開発者は GridWeb コントロールのカスタム コマンド ボタンを追加および削除できます。


### **重要**
Aspose.Cells.GridWeb は、そのリソース ファイルにもコントロールを提供します。 「acw_client" は、ファイルを含むフォルダー (@ インストール ディレクトリ) であり、Aspose.Cells.GridWeb は、このフォルダーを使用して内部構成およびその他の機能を管理します。GridWeb の動作を指定し、その他の操作を設定するためのスクリプト ファイル、画像ファイル、およびその他のファイルがあります。 config ファイルは、埋め込まれたクライアント リソース (イメージ、スクリプトなど) を管理するために使用されます。さらに、GridWeb コントロールを持つ Web アプリケーションをデプロイする必要がある場合は、「acw」もコピーします。_client" ディレクトリをプロジェクト フォルダーに追加する必要があります。少なくとも、Web アプリケーション (サーバー上にデプロイされた) はそれを見つけることができませんでした。 次のコード行を構成セクション (たとえば、 VS.NET プロジェクト):



|<p>{{< highlight "java" >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
|:- |


{{% alert color="primary" %}}

パスは常にプロジェクトのディレクトリに関連しています。プロジェクトのディレクトリ以外のディレクトリは使用しないでください。そのため、「acw_client」ディレクトリ (@GridWeb インストール フォルダー) をプロジェクトのディレクトリ/サブディレクトリにコピーする必要があります。

{{% /alert %}}
### **ステップ 5: Web アプリケーションの実行**
Ctrl+F5 を押すか、**始める**ボタン。

アプリケーションがブラウザーで実行されると、空の Aspose.Cells.GridWeb コントロールを含む WebForm1.aspx ページが表示されます。セルをクリックして値を追加します。行の高さや列の幅の変更、クリップボードへのセル データのコピー (Ctrl+C) または切り取り (Ctrl+X)、セルへのデータの貼り付け (Ctrl+V) など、他のタスクを実行することもできます。 .さらに操作を実行するには、コントロールを右クリックして、オプションの完全なリストを表示します。

**GridWeb コントロールのコンテキスト メニュー** 

![todo:画像_代替_文章](add-gridweb-to-web-form_10.png)
