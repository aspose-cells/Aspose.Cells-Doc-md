---
title: ワークシートを画像に変換し、ページごとにワークシートを画像に変換
type: docs
weight: 80
url: /ja/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

このドキュメントは、開発者に、ワークシートを画像ファイルに変換する方法と、複数のページを持つワークシートを1ページごとに画像ファイルに変換する方法についての詳細な理解を提供するように設計されています。

時には、ワークシートを画像として表示し、それをアプリケーションやWebページで使用したい場合があります。画像をWord文書やPDF、PowerPointなどに挿入したり、他のシナリオで使用したりできます。簡単に言うと、ワークシートを画像としてレンダリングしたいのです。Aspose.Cells for Python via .NETは、Excelファイルのワークシートを画像に変換する機能をサポートしています。また、ワークブックを複数の画像ファイルに変換し、1ページごとに出力することもできます。

これを達成するためには、Office Automationを使用することができますが、Office Automationには独自の欠点があります。セキュリティ、安定性、拡張性/処理速度、価格、機能など、いくつかの理由や問題があります。簡単に言えば、多くの理由がありますが、その中でも主な理由の1つは、Microsoft自体がOffice Automationを強く推奨していないことです。

{{% /alert %}}

## **Aspose.Cellsを使用してワークシートを画像ファイルに変換する方法**

この資料では、Visual Studioでコンソールアプリケーションを作成し、ワークシートを画像に変換し、複数のワークシートをそれぞれ1つの画像に変換する方法を、最も簡潔なコード例とともに紹介します。Aspose.Cells for Python via .NET APIを使用します。

プログラム/プロジェクトに[**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering)ネームスペースをインポートする必要があります。[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)などの貴重なクラスがいくつか含まれています。[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)クラスは、ワークシートをレンダリングするためのクラスであり、オーバーロードされた[**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)メソッドから直接ワークシートを画像ファイルに変換できます。System.Drawing.Bitmapオブジェクトを返し、イメージファイルをディスク/ストリームに保存できます。省略して、BMP、PNG、GIF、JPG、JPEG、TIFF、EMFなど、さまざまな画像形式がサポートされています。

この資料は、ワークシートを画像に変換する方法を説明します。この作業では、Aspose.Cells for Python via .NETを使用して、テンプレートワークブックからワークシートを画像ファイルに変換します。


### **ワークシートを画像ファイルに変換**

Microsoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました：**Testbook.xlsx**（1つのワークシート）。次に、テンプレートファイルのワークシートSheet1をSheetImage.jpgという画像ファイルに変換します。

コンポーネントがタスクを達成するために使用したコードは以下の通りです。**Testbook.xlsx**のSheet1を画像ファイルに変換し、この変換がどれほど簡単であるかを説明します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Aspose.Cellsを使用して、ワークシートを画像ファイルにページごとに変換する**

この例では、Python用Aspose.Cells via .NETを使用して、複数ページのテンプレートワークブックからワークシートを画像ファイルに変換する方法を示します。

### **ワークシートをページ毎に画像に変換する**

私はMicrosoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました: **Testbook2.xlsx** (1 ワークシート)。

これで、テンプレートファイルのワークシート Sheet1 を画像ファイルに変換します（1ページごとのファイル）。すでにコンソールアプリケーションを作成してコピー作業を行う準備ができているため、コンソールアプリケーションの作成手順をスキップして、直接ワークシートの変換手順に移ります。

以下は、そのコンポーネントがタスクを達成するために使用したコードです。それは Testbook2.xls の Sheet1 をページごとに画像ファイルに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
