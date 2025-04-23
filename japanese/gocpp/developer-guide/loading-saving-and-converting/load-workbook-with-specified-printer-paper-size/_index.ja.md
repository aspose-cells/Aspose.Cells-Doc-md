---
title: 指定したプリンター用紙サイズでワークブックをロード
type: docs
weight: 430
url: /ja/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/) メソッドを使用して、読み込み時に任意のプリンタ用紙サイズを指定できます。なお、MS Excelで新しいファイルを作成すると、用紙サイズはお使いのマシンの既定プリンタの設定と同じになります。

{{% /alert %}}

以下のサンプルコードは、[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/)メソッドの使用例を示しています。最初に、ワークブックを作成し、次にメモリストリームにXLSX形式で保存します。その後、A5用紙サイズでロードし、PDF形式で保存します。次に、A3用紙サイズでロードし、再びPDFで保存します。出力されたPDFの用紙サイズを確認すると、片方はA5、もう片方はA3です。サンプルコードによって生成された[A5出力PDF](#)と[A3出力PDF](#)をダウンロードしてください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
