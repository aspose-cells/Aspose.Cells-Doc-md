---
title: 指定したプリンター用紙サイズのワークブックを読み込む
type: docs
weight: 430
url: /ja/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

を使用してワークブックをロードするときに、選択したプリンターの用紙サイズを指定できます。[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize)方法。 MS Excel で新しいファイルを作成すると、用紙サイズがマシンのデフォルト プリンタの設定と同じになることに注意してください。

{{% /alert %}}

次のサンプル コードは、[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize)方法。最初にワークブックを作成し、XLSX 形式でメモリ ストリームに保存します。次に、A5 用紙サイズで読み込み、PDF 形式で保存します。次に、A3 用紙サイズで再度読み込み、PDF 形式で再度保存します。出力された PDF を開いて用紙サイズを確認すると、それらが異なっていることがわかります。 1 つは A5 で、もう 1 つは A3 です。をダウンロードしてください[A5出力PDF](5115234.pdf)と[A3出力PDF](5115233.pdf)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
