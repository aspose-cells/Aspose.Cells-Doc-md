---
title: 指定したプリンター用紙サイズでワークブックをロード
type: docs
weight: 430
url: /ja/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)メソッドを使用してワークブックをロードする際に、希望のプリンター用紙サイズを指定できます。新しいファイルをMS Excelで作成した場合、プリンターの設定と同じ用紙サイズになりますのでご注意ください。

{{% /alert %}}

[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)メソッドの使用例を示すサンプルコードです。まず、ブックを作成し、メモリストリームにXLSX形式で保存します。その後、A5用紙サイズで読み込み、PDF形式で保存します。次に、A3用紙サイズで読み込み、再びPDFとして保存します。出力されたPDFを開き、用紙サイズを確認すると、片方はA5、もう片方はA3であることがわかります。コードで生成された[A5出力PDF](PrinterSize-a5_out.pdf)および[A3出力PDF](PrinterSize-a3_out.pdf)をダウンロードしてください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
