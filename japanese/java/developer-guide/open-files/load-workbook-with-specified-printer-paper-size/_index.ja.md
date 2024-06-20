---
title: 指定したプリンター用紙サイズでワークブックをロード
type: docs
weight: 790
url: /ja/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

LoadOptions.setPaperSize()メソッドを使用して、ワークブックを読み込む際に使用するプリンタ用紙サイズを指定できます。ただし、MS Excelで新しいファイルを作成する場合、プリンタ設定がデフォルトになることに留意してください。

{{% /alert %}} 
## **指定されたプリンタ用紙サイズでワークブックを読み込む**
以下のサンプルコードは、まずワークブックを作成し、XLSX形式のバイト配列ストリームとして保存します。その後、A5用紙サイズでロードし、PDF形式で保存します。その後、A3用紙サイズで再度ロードし、再度PDF形式で保存します。出力されたPDFを開いて用紙サイズを確認すると、一方はA5で、もう一方はA3であることがわかります。コードによって生成された[A5出力PDF](5473435.pdf)と[A3出力PDF](5473436.pdf)を参照のためにダウンロードしてください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
