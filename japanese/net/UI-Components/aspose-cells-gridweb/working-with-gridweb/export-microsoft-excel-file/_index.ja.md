---
title: Microsoft Excelファイルをエクスポート
type: docs
weight: 50
url: /ja/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb、エクスポート
description: この記事では、GridWebでファイルをエクスポートする方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebコントロールを使用してGUIモードでWebサイト上で新しいまたは既存のMicrosoft Excelファイルを作成したり操作したり、ファイルをExcelファイルとして保存することができます。 Aspose.Cells.GridWebはオンラインスプレッドシートエディタとして効果的に機能します。 このトピックでは、グリッドコンテンツをExcelファイルに保存する方法について説明します。

{{% /alert %}} 
## **Excelファイルをエクスポート**
### **ファイルとしてエクスポート**
Aspose.Cells.GridWebコントロールのコンテンツをExcelファイルとして保存するには：

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. 指定したパスに作業内容をExcelファイルとして保存します。
1. アプリケーションを実行します。

{{% alert color="primary" %}} 

Aspose.Cells.GridWebコントロールをWebフォームに追加する方法がわからない場合は、[WebフォームにGridWebを追加](/cells/ja/net/aspose-cells-gridweb/add-gridweb-to-web-form/)を参照してください。

{{% /alert %}} 

Aspose.Cells.GridWebコントロールがウィンドウフォームに追加されると、デフォルトのサイズで自動的にインスタンス化され、フォームに追加されます。 Aspose.Cells.GridWebコントロールオブジェクトを作成する必要はありません。 コントロールをドラッグアンドドロップして使用を開始するだけです。

以下のコード例は、グリッドコンテンツをExcelファイルに保存する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

ファイルシステムがNTFSである場合、ASPNETまたはEveryoneユーザーアカウントに読み取り/書き込みアクセスを付与するか、実行時にアクセスが拒否される例外が発生します。

{{% /alert %}} 

上記のコードスニペットは、いくつかの方法で使用できます。 一般的な方法は、クリック時にグリッドコンテンツをExcelファイルに保存するボタンを追加することです。 Aspose.Cells.GridWebはそのタスクのためのより簡単なアプローチを提供しています。 Aspose.Cells.GridWebにはSaveCommandというイベントがあります。 上記のコードスニペットをSaveCommandイベントのイベントハンドラに追加することで、Aspose.Cells.GridWebの組み込み**保存**ボタンをクリックして作業を保存できます。

**GridWebのSaveCommandイベント** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**GridWebの組み込みSaveボタンをクリックしてグリッドのコンテンツをExcelに保存** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Visual Studioで作業している場合は、**プロパティ**ペインでイベントをダブルクリックしてSaveCommandイベントのイベントハンドラを簡単に作成できます。 詳細については、[GridWebイベントの使用](/cells/ja/net/aspose-cells-gridweb/working-with-gridweb-events/)を参照してください。

{{% /alert %}} 
### **ストリームとしてエクスポート**
また、グリッドのコンテンツをストリーム（たとえばMemoryStream）に保存することも可能です。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
