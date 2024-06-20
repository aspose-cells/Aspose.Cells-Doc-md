---
title: 指定したプリンター用紙サイズでワークブックをロード
type: docs
weight: 430
url: /ja/net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize)メソッドを使用してワークブックをロードする際に、希望のプリンター用紙サイズを指定できます。新しいファイルをMS Excelで作成した場合、プリンターの設定と同じ用紙サイズになりますのでご注意ください。

{{% /alert %}}

次のサンプルコードは[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize)メソッドの使用法を示しています。まずワークブックを作成し、それをXLSX形式のメモリストリームに保存します。その後、A5用紙サイズでロードし、PDF形式で保存します。次に、A3用紙サイズで再度ロードし、再度PDF形式で保存します。出力されたPDFを開いて用紙サイズを確認すると、異なることがわかります。一つはA5で、もう一つはA3です。参照のために、[A5出力PDF](5115234.pdf)と[A3出力PDF](5115233.pdf) をダウンロードしてください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
