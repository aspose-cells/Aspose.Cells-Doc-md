---
title: 指定したプリンター用紙サイズでワークブックをロード
type: docs
weight: 790
url: /ja/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

ワークブックを読み込む際に、[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-)メソッドでお好みのプリンタ用紙サイズを指定できます。新しいファイルをMS Excelで作成した場合、用紙サイズはお使いのマシンのデフォルトプリンタの設定と同じになることに注意してください。

{{% /alert %}} 
## **指定されたプリンタ用紙サイズでワークブックを読み込む**
以下のサンプルコードは、[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-)メソッドの使用例です。最初にワークブックを作成し、バイト配列ストリームにXLSX形式で保存します。その後A5用紙サイズで読み込み、PDF形式で保存します。その後A3用紙サイズで再度読み込み、またPDFに保存します。出力されたPDFを開き、用紙サイズを確認すると、異なることがわかります。一つはA5、もう一つはA3です。生成された[A5出力PDF](5473435.pdf)と[A3出力PDF](5473436.pdf)をダウンロードしてください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
