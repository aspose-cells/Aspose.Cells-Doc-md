---
title: インポート Microsoft Excel ファイル
type: docs
weight: 40
url: /ja/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop のように、Aspose.Cells.GridWeb コントロールは Microsoft Excel ファイルを開いて読み込むことができます - データ、書式設定、グラフ、画像などを備えていますが、Web アプリケーション内です。このトピックでは、その方法について説明します。

{{% /alert %}} 
## **Excel ファイルのインポート**
### **ファイルからインポート**
Aspose.Cells.GridWeb コントロールを使用して Excel ファイルを開くには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ファイル パスを指定して、Excel ファイルをインポートします。
1. アプリケーションを実行します。

{{% alert color="primary" %}} 

コントロールを Web フォームに追加する方法がわからない場合は、次を参照してください。[GridWeb を Web フォームに追加する](/cells/ja/net/add-gridweb-to-web-form/).

{{% /alert %}} 

Aspose.Cells.GridWeb コントロールが Web フォームに追加されると、コントロールは自動的にインスタンス化され、既定のサイズでフォームに追加されます。 Aspose.Cells.GridWeb コントロール オブジェクトを作成する必要はありません。コントロールをドラッグ アンド ドロップして使用を開始するだけです。

ただし、Excel ファイルから Aspose.Cells.GridWeb コントロールにコンテンツを読み込むには、ImportExcelFile メソッドを呼び出して Excel ファイルのパスを指定する必要があります。その後、Aspose.Cells.GridWeb コントロールは、指定されたパスからファイルを自動的に検索し、その内容を表示します。 Excel ファイルの内容をロードするコード スニペットを以下に示します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


上記のコード スニペットは、任意の方法で使用できます。たとえば、Web フォームの読み込み時に Excel ファイルを自動的に読み込むには、このコードをフォームの Page_Load イベントに追加します。ボタンがクリックされたときにファイルを開く場合は、Web フォームにボタンを追加し、ボタンの Click イベントの下に上記のコードを記述します。

**ボタンをクリックするとExcelファイルが読み込まれます** 

![todo:画像_代替_文章](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

ファイル システムが NTFS の場合は、ASPNET または Everyone ユーザー アカウントに読み取りアクセス許可を付与する必要があります。そうしないと、実行時にアクセス拒否の例外が発生します。

{{% /alert %}} 
### **ストリームからインポート**
Aspose.Cells.GridWeb コントロールは、ファイルから Excel ファイルを開くだけでなく、ストリームから Excel ファイルを読み込むこともできます。ファイルをストリームとして使用することは、ストリームを閉じることによってファイルへのすべての接続を確実に閉じることができるため、あらゆる種類のファイル アクセスまたは共有違反の問題を防止するためのより良い方法です。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
