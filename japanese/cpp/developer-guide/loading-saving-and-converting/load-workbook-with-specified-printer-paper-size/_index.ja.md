---
title: 指定したプリンター用紙サイズでワークブックをロード
type: docs
weight: 430
url: /ja/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)メソッドを使用してワークブックをロードする際に、希望のプリンター用紙サイズを指定できます。新しいファイルをMS Excelで作成した場合、プリンターの設定と同じ用紙サイズになりますのでご注意ください。

{{% /alert %}}

次のサンプルコードは[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)メソッドの使用法を説明しています。まずワークブックを作成し、それをXLSX形式のメモリストリームに保存します。次にA5用紙サイズでそれをロードし、PDF形式で保存します。それを再度A3用紙サイズでロードし、再びPDF形式で保存します。出力されたPDFを開いて用紙サイズを確認すると、異なることが分かります。1つはA5で、もう1つはA3です。コードによって生成された[A5出力PDF](PrinterSize-a5_out.pdf)と[A3出力PDF](PrinterSize-a3_out.pdf)を参照するためにダウンロードしてください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
