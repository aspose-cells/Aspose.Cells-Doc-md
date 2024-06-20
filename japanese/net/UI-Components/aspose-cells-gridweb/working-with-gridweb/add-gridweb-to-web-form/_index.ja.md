---
title: WebフォームにGridWebを追加
type: docs
weight: 10
url: /ja/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: この記事では、GridWebでWebフォームを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridWebコントロールをWebアプリケーションで作成および使用する初心者向けの基本的なステップバイステップガイドを提供します。

{{% /alert %}} 
## **Aspose.Cells.GridWebコントロールの作成と使用**
### **ステップ1：Webアプリケーションプロジェクトの作成**
まず、Aspose.Cells.GridWebコントロールを使用するWebアプリケーションプロジェクトを作成します:

1. Visual Studioを開きます。
1. **ファイル**メニューから**新規**を選択し、**プロジェクト**を選択します。 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



新しいプロジェクトダイアログが表示されます。

1. 望ましい言語として**ASP.NET Webアプリケーション**を選択します。 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. **Webフォーム**テンプレートを選択します。 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. 新しいWebフォームをプロジェクトに追加します。
### **ステップ2：Webフォームにコントロールを埋め込む**
Visual StudioツールボックスからAspose.Cells.GridWebコントロールをドラッグアンドドロップしてWebフォームに追加します。 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

Visual Studio ToolboxにAspose.Cells Gridコントロールを追加する方法については、[Visual Studio.NETとAspose.Cells.Grid Controlsの統合](/cells/ja/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/)を参照してください。

{{% /alert %}} 

コントロールがフォームに追加されると、次のようにレンダリングされます: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **ステップ3：コントロールのサイズ変更**
フォームはデフォルトのサイズでレンダリングされます。境界や角をドラッグしてサイズを調整します。 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **ステップ4：コントロールのプロパティ設定**
Aspose.Cells.GridWebコントロールは、さまざまなプロパティを使用して設定することも可能です。 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

プロパティのダイアログでコントロールの多くのプロパティを調整することができます。基本的なプロパティには、高さ、幅、色、視覚スタイルが含まれます。高度なプロパティには、編集モード、セッションモード、ダブルクリックモードが含まれます。また、プロパティのダイアログでカスタムイベントハンドラーを設定することも可能です。

また、プロパティのダイアログの下部には、ハイパーリンクとして表示されるAspose.Cells.GridWebの追加設定ツールや、右クリックして見つけることができる追加の設定ツールがあります:

- カスタムコマンドボタン
#### **カスタムコマンドボタン**
カスタムコマンドボタンエディタを開くには:
GridWebコントロールを右クリックし、**カスタムコマンドボタン**を選択します。 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



カスタムコマンドボタンコレクションエディタダイアログが表示されます。 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

このダイアログでは、開発者がGridWebコントロールにカスタムコマンドボタンを追加および削除することができます。


### **重要**
Aspose.Cells.GridWebは、そのコントロールと共にリソースファイルを提供しています。"acw_client"はフォルダで、Aspose.Cells.GridWebはその内部構成やその他の機能を管理するためにこのフォルダを使用し、スクリプトファイル、画像ファイル、その他のファイルが含まれています。また、Webアプリケーションをデプロイする際には、"acw_client"ディレクトリをプロジェクトフォルダにコピーする必要があります。これにより、Webアプリケーションがこのフォルダを見つけられるようになります。



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

ステップ5：Webアプリケーションの実行

{{% /alert %}}
### **ステップ5：Webアプリケーションの実行**
「Ctrl+F5」を押すか、「Start」ボタンをクリックしてアプリケーションを実行します。 

アプリケーションがブラウザで実行されると、WebForm1.aspxページが表示され、空のAspose.Cells.GridWebコントロールが含まれています。セルに値を追加するには、それらをクリックします。また、行の高さや列の幅を変更したり、セルのデータをクリップボードにコピーしたり切り取ったりして、データをセルに貼り付けたりすることも可能です。さらに多くの操作を行うには、コントロールを右クリックして完全なオプションのリストを表示します。 

「GridWebコントロールのコンテキストメニュー」 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
