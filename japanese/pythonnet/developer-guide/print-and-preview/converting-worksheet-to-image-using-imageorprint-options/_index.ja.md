---
title: ImageOrPrintオプションを使用してワークシートを画像に変換する
type: docs
weight: 90
url: /ja/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

このドキュメントは、ワークシートを画像ファイルに変換し、画像と印刷オプションを適用し、解像度、TIFF圧縮、画像形式、ページ品質などのオプションを適用する方法について詳しく説明します。

{{% /alert %}}

## **ワークシートをイメージとして保存する - 異なるアプローチ**

時には、ワークシートを画像として提示したい場合があります。アプリケーションやWebページにワークシートの画像を挿入したいときです。これには、Word文書やPDF、PowerPointに画像を挿入したり、他のシナリオで活用したりできます。単純に、ワークシートを画像としてレンダリングし、それを他の場所で使用できるようにしたいのです。Aspose.Cells for Python via .NETは、Excelのワークシートを画像に変換することをサポートしています。また、画像のフォーマット、解像度（縦横両方）、画質などさまざまなオプションの設定も可能です。

Office Automationを試すことができますが、Office Automationには独自の欠点があります。セキュリティ、安定性、拡張性、速度、価格、機能など、いくつかの理由や問題があります。要するに、Microsoft自身もソフトウェアソリューションからのOffice Automationを強く勧めていません。

この資料では、Visual Studio .NETでコンソールアプリケーションを作成し、複数の画像と印刷オプションを使ってワークシートを画像に変換する方法を、最も簡単なコード例とともに紹介します。Aspose.Cells for Python via .NET APIを使用します。

あなたはあなたのプログラム/プロジェクトに[**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering)名前空間をインポートする必要があります。例えば、[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)などの価値のあるクラスがいくつかあります。

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)クラスは、イメージを描画するためのワークシートを表し、あなたが望む属性やオプションでワークシートをイメージファイルに直接変換できるオーバーロードされた[**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)メソッドを持っています。それはSystem.Drawing.Bitmapオブジェクトを返すことができ、イメージファイルをディスク/ストリームに保存することができます。サポートされるイメージ形式はいくつかあります、例えばBMP、PNG、GIFF、JPEG、TIFF、EMFなどです。

## **Aspose.Cellsを使用してワークシートを画像に変換する(ImageOrPrint オプションを使用)**

### **Microsoft Excelでテンプレートワークブックを作成する**

私はMS Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました。これで、テンプレートファイルのワークシート **Sheet1** を画像ファイル **SheetImage.tiff** に変換し、水平および垂直解像度、TiffCompressionなどの異なるイメージオプションを適用します。

### **ワークシートを画像ファイルに変換**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **WorkbookRenderを使用した画像変換**

TIFF画像には複数のフレームを含めることができます。複数フレームまたはページを持つTIFF画像としてワークブック全体を保存できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
