---
title: 共通ボタンを使用してグリッド データを送信する
type: docs
weight: 20
url: /ja/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb には、次のような組み込みコマンド ボタンがいくつか用意されています。**送信**と**セーブ**.これらのボタンを使用して、関連するタスクを実行します。

この記事では、GridWeb の組み込みをクリックするだけでなく、サーバーにデータを送信する方法を示します。**セーブ**コマンド ボタンですが、一般的な ASP.NET ボタン (Web コントロール) をクリックします。この記事の目的は、Aspose.Cells.GridWeb の柔軟性を示すことです。さらに、この記事では、Aspose.Cells.GridWeb によって公開されている特別な関数も使用して、クライアント サイド スクリプトで使用します。

{{% /alert %}} 
## **ASP.NET ボタンを使用したグリッド データの送信**
Aspose.Cells.GridWeb には 3 つの組み込みボタン (**送信**, **セーブ**と**元に戻す** ）。 GridWeb で編集した後、ユーザーは**送信**また**セーブ**タブ バーの ボタンをクリックして、GridWeb がサーバーにデータを送信できるようにします。ユーザーがシート タブをクリックすると、GridWeb コントロールは組み込みコマンド ボタンと同じタスクを実行します。 Aspose.Cells.GridWeb は、この機能を一般的な ASP.NET Button コントロールに追加することもサポートしていますが、アプリケーションにコードを追加する必要があります。
### **1. テスト アプリケーションの作成**
Visual Studio.NET IDE を開き、新しい ASP.NET Web アプリケーション プロジェクトを作成します。アプリケーションが作成されると、既定の WebForm1.aspx ページがプロジェクトに追加されます。 Toolbox から GridWeb コントロールを Web Form にドラッグ アンド ドロップします。ツールボックスに GridWeb コントロールが見つからない場合は、次のページを参照してください。[Aspose.Cells グリッド コントロールを Visual Studio.NET と統合する](/cells/ja/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/)詳細については、GridWeb コントロールを Web フォームに追加した後、Toolbox から Button Web コントロールを Web フォームに追加します。
### **2. Page_Load イベントへのコードの追加**
次に、ページにコードを追加します。_Web フォームの Load イベント。デザイン ビューで Web フォームをダブルクリックすると、VS.NET IDE が自動的にページに移動します。_OnClick イベントをオーバーライドするために Button の Attributes コレクションを使用する必要があるイベント ハンドラーを読み込みます。

{{% alert color="primary" %}} 

ASP.NET ボタン コントロールはサーバー側のコントロールです。クリックされるたびにサーバー側のイベントがトリガーされますが、この Button コントロールを使用してクライアント側でコードを実行する場合 (通常は JavaScript を使用)、Page_Load イベントの下の onclick 属性を変更する必要があります。 Aspose.Cells.GridWeb は、クライアント側から GridWeb コントロールを処理するために JavaScript で呼び出すことができるいくつかの関数を提供します。以下の例では、GridWeb の updateData および validateAll 関数 (クライアント側関数) を使用して、グリッド データを更新および検証しています。

{{% /alert %}} 
#### **コード例**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. アプリケーションの実行**
ここで、Ctrl+F5 を押してアプリケーションをコンパイルして実行すると、ページが新しいブラウザー ウィンドウで開かれます。いくつかの値を GridWeb に追加して [Submit Grid Data to Server] ボタンをクリックすると、GridWeb データを更新および検証するためのポストバックが発生することがわかります。
## **結論**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb は、サーバー側またはクライアント側から GridWeb コントロールを操作するための優れた柔軟性を提供します。開発者には、さまざまな種類のシナリオで GridWeb コントロールを使用して、より優れたソリューションを顧客に提供するための多数のオプションがあります。

{{% /alert %}}
