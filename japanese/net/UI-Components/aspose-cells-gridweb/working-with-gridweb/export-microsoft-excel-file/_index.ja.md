---
title: Microsoft Excel ファイルのエクスポート
type: docs
weight: 50
url: /ja/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb コントロールを使用して、GUI モードの Web サイトで新しい Microsoft Excel ファイルを作成したり、既存の Microsoft Excel ファイルを操作したりできます。その後、ファイルを Excel ファイルに保存できます。 Aspose.Cells.GridWeb は、オンラインのスプレッドシート エディターとして効果的に機能します。このトピックでは、グリッド コンテンツを Excel ファイルに保存する方法について説明します。

{{% /alert %}} 
## **Excel ファイルのエクスポート**
### **ファイルとしてエクスポート**
Aspose.Cells.GridWeb コントロールのコンテンツを Excel ファイルとして保存するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. 指定したパスに Excel ファイルとして作業を保存します。
1. アプリケーションを実行します。

{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb コントロールを Web フォームに追加する方法がわからない場合は、以下を参照してください。[GridWeb を Web フォームに追加する](/cells/ja/net/add-gridweb-to-web-form/)

{{% /alert %}} 

Aspose.Cells.GridWeb コントロールが Windows フォームに追加されると、コントロールは自動的にインスタンス化され、既定のサイズでフォームに追加されます。 Aspose.Cells.GridWeb コントロール オブジェクトを作成する必要はありません。コントロールをドラッグ アンド ドロップして使用を開始するだけです。

次のコード例は、グリッド コンテンツを Excel ファイルに保存する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

ファイル システムが NTFS の場合、ASPNET または Everyone ユーザー アカウントに読み取り/書き込みアクセスを許可しないと、実行時にアクセス拒否の例外が発生します。

{{% /alert %}} 

上記のコード スニペットは、いくつかの方法で使用できます。一般的な方法は、クリックしたときにグリッド コンテンツを Excel ファイルに保存するボタンを追加することです。 Aspose.Cells.GridWeb は、タスクに対するより簡単なアプローチを提供します。 Aspose.Cells.GridWeb には SaveCommand というイベントがあります。上記のコード スニペットを SaveCommand イベントのイベント ハンドラに追加すると、ユーザーは Aspose.Cells.GridWeb の組み込み**セーブ**ボタン。

**GridWeb の SaveCommand イベント** 

![todo:画像_代替_文章](export-microsoft-excel-file_1.jpg)

**GridWeb の組み込みの [保存] ボタンをクリックして、グリッド コンテンツを Excel に保存する** 

![todo:画像_代替_文章](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Visual Studio で作業している場合は、SaveCommand イベントのイベント ハンドラーを簡単に作成できます。**プロパティ**ペイン。詳細については、次を参照してください。[GridWeb イベントの操作](/cells/ja/net/working-with-gridweb-events/)

{{% /alert %}} 
### **ストリームとしてエクスポート**
グリッド コンテンツをストリーム (たとえば、MemoryStream) に保存することもできます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
