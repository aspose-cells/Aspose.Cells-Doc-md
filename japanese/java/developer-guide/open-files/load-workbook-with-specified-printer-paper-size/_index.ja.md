---
title: 指定したプリンター用紙サイズのワークブックを読み込む
type: docs
weight: 790
url: /ja/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

を使用してワークブックをロードするときに、選択したプリンターの用紙サイズを指定できます。[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)） 方法。 MS Excel で新しいファイルを作成すると、用紙サイズがマシンのデフォルト プリンタの設定と同じになることに注意してください。

{{% /alert %}} 
## **指定したプリンター用紙サイズのワークブックを読み込む**
次のサンプル コードは、[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)） 方法。最初にワークブックを作成し、それを XLSX 形式のバイト配列ストリームに保存します。次に、A5 用紙サイズで読み込み、PDF 形式で保存します。次に、A3 用紙サイズで再度読み込み、PDF 形式で再度保存します。出力された PDF を開いて用紙サイズを確認すると、それらが異なっていることがわかります。 1 つは A5 で、もう 1 つは A3 です。をダウンロードしてください[A5出力 PDF](5473435.pdf)と[A3出力 PDF](5473436.pdf)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
