---
title: 共通のボタンを使用してGridデータを送信する
type: docs
weight: 20
url: /ja/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb,submit,button,custom
description: この記事では、GridWebで送信ボタンの使用について説明します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebには、**Submit**と**Save**のような組み込みコマンドボタンが提供されています。これらのボタンを使用して関連するタスクを実行します。

この記事では、Aspose.Cells.GridWebの組み込みの**Save**コマンドボタンをクリックするだけでなく、一般的なASP.NETボタン(Webコントロール)をクリックしてサーバーにデータを送信する方法を示します。この記事の目的は、Aspose.Cells.GridWebの柔軟性を示すことです。さらに、この記事では、クライアントサイドのスクリプトで使用するAspose.Cells.GridWebによって公開された特別な機能も使用します。

{{% /alert %}} 
## **ASP.NETボタンを使用してGridデータを送信する**
Aspose.Cells.GridWebには、**Submit**、**Save**、**Undo**の3つの組み込みボタンが用意されています。GridWebで編集した後、ユーザーはタブバーの**Submit**または**Save**ボタンをクリックしてデータをサーバーに送信することができます。ユーザーがシートタブをクリックすると、GridWebコントロールは組み込みのコマンドボタンと同じタスクを実行します。Aspose.Cells.GridWebは、この機能を一般的なASP.NETボタンコントロールに追加することもサポートしていますが、アプリケーションにいくつかの追加のコードを追加する必要があります。
### **1. テストアプリケーションの作成**
Visual Studio.NET IDEを開いて、新しいASP.NET Webアプリケーションプロジェクトを作成します。アプリケーションが作成されると、デフォルトのWebForm1.aspxページがプロジェクトに追加されます。ツールボックスからGridWebコントロールをWebフォームにドラッグ＆ドロップします。ツールボックスでGridWebコントロールが見つからない場合は、このページを参照してください：[Visual Studio.NETでAspose.Cells Gridコントロールを統合](/cells/ja/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/)。GridWebコントロールをWebフォームに追加したら、ツールボックスからButtonウェブコントロールをWebフォームに追加します。
### **2. Page_Loadイベントにコードを追加する**
次に、Webフォームをデザインビューでダブルクリックすると、VS.NET IDEが自動的にPage_Loadイベントハンドラに移動し、ButtonのAttributesコレクションを使用してOnClickイベントをオーバーライドする必要があります。

{{% alert color="primary" %}} 

ASP.NET Buttonコントロールはサーバーサイドコントロールです。クリックされると、サーバーサイドイベントがトリガーされますが、このButtonコントロールを使用してクライアントサイドでコードを実行したい場合（通常はjavascriptを使用）、Page_Loadイベントの下でonclick属性を修正する必要があります。Aspose.Cells.GridWebには、クライアントサイドでGridWebコントロールを扱うためのjavascriptを呼び出すことができるいくつかの機能があります。以下の例では、GridWebのupdateDataおよびvalidateAllのクライアントサイド関数（javascriptで使用される関数）を使用して、Gridデータを更新および検証しています。

{{% /alert %}} 
#### **コード例**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. アプリケーションの実行**
Ctrl+F5を押してアプリケーションをコンパイルして実行し、ページが新しいブラウザウィンドウで開きます。GridWebに値を追加し、Submit Grid Data to Serverボタンを押すと、GridWebデータを更新および検証するためのポストバックが発生するのを見ることができます。
## **結論**
{{% alert color="primary" %}} 

Aspose.Cells.GridWebは、サーバーサイドまたはクライアントサイドのどちらからでもGridWebコントロールを使用するための大きな柔軟性を提供します。開発者は、さまざまなシナリオでGridWebコントロールを使用して顧客により良いソリューションを提供するための幅広いオプションを利用できます。

{{% /alert %}}
