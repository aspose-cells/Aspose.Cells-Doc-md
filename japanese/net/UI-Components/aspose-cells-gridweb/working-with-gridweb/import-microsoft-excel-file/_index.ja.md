---
title: Microsoft Excelファイルをインポートする
type: docs
weight: 40
url: /ja/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb、インポート
description: この記事ではGridWebでファイルをインポートする方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktopと同様に、Aspose.Cells.GridWebコントロールはWebアプリケーションでMicrosoft Excelファイルを開いてロードできます。データ、書式、チャート、画像などが含まれます。このトピックはその方法について説明します。

{{% /alert %}} 
## **Excelファイルをインポート**
### **ファイルからインポート**
Aspose.Cells.GridWebコントロールを使用してExcelファイルを開くには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ファイルのパスを指定してExcelファイルをインポートします。
1. アプリケーションを実行します。

{{% alert color="primary" %}} 

コントロールをWebフォームに追加する方法がわからない場合は、[WebフォームにGridWebを追加](/cells/ja/net/aspose-cells-gridweb/add-gridweb-to-web-form/)を参照してください。

{{% /alert %}} 

Aspose.Cells.GridWebコントロールをWebフォームに追加すると、コントロールが自動的にインスタンス化され、既定のサイズでフォームに追加されます。Aspose.Cells.GridWebコントロールオブジェクトを作成する必要はありません。コントロールをドラッグして場所を選び、使用を開始するだけです。

ただし、Excelファイルの内容をAspose.Cells.GridWebコントロールにロードするには、ImportExcelFileメソッドを呼び出してExcelファイルのパスを指定する必要があります。その後、Aspose.Cells.GridWebコントロールは指定されたパスからファイルを自動的に見つけてその内容を表示します。Excelファイルの内容をロードするコードスニペットが以下に提供されています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


上記のコードスニペットは自由に使用できます。たとえば、WebフォームがロードされるときにExcelファイルを自動的にロードする場合は、このコードをフォームのPage_Loadイベントに追加します。ボタンがクリックされたときにファイルを開く場合は、Webフォームにボタンを追加し、上記のコードをボタンのClickイベントの下に記述します。

**ボタンがクリックされたときにExcelファイルがロードされます** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

ファイルシステムがNTFSの場合、ASPNETまたはEveryoneユーザーアカウントに読み取りアクセス権限を付与する必要があります。そうしないと、実行時にアクセスが拒否される例外が発生します。

{{% /alert %}} 
### **ストリームからインポート**
Aspose.Cells.GridWebコントロールを使用してExcelファイルをファイルから開くだけでなく、ストリームからもロードできます。ファイルをストリームとして使用することは、ファイルへのアクセスまたは共有の違反問題を防ぐためにはより良いアプローチです。なぜなら、この方法ではストリームを閉じることでファイルへのすべての接続が確実に閉じられるからです。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
