---
title: スプレッドシートまたはワークブックで使用されているフォントのリストを取得する
type: docs
weight: 20
url: /ja/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **考えられる使用シナリオ**

多くの場合、レンダリング目的でワークブックで使用されているフォントを知る必要があります。ワークブックを PDF または画像に変換する場合、Aspose.Cells では、必要なすべてのフォントがシステムにインストールされているか、.**フォントディレクトリ**Aspose.Cells が必要なフォントを見つけられない場合、システムまたはフォント ディレクトリに存在し、実際のフォントを置き換えることができる他の適切なフォントに置き換えようとします。これにより、PDF またはイメージの望ましくないレンダリングが発生するだけでなく、適切なフォントを見つけるための処理時間もかかります。

このような場合に対処するには、ワークブックで使用されているフォントを把握し、Windows 環境の場合はそれらのフォントをシステムにインストールするか、Windows または Linux 環境の場合はフォント ディレクトリに配置する必要があります。

Aspose.Cells は[Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts()) メソッドを使用して、ワークブックまたはスプレッドシートで使用されているすべてのフォントのリストを返します。

## **スプレッドシートまたはワークブックで使用されているフォントのリストを取得する**

次のサンプル コードは、ソースの Excel ファイルを読み込み、その中で使用されているフォントのリストを取得します。説明のためにいくつかのダミーフォントが追加されたダミーワークシートが 1 つあります。コードがブック内のすべてのフォントを印刷するとき、それらのダミー フォントも印刷します。次のスクリーンショットは、[サンプルエクセルファイル](sampleGetFonts.xlsx)およびダミーフォントのリスト方法。

![todo:画像_代替_文章](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **コンソール出力**

以下は、上記のサンプル コードを特定のコマンドで実行したときのコンソール出力です。[サンプルエクセルファイル](sampleGetFonts.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]{{< /highlight >}}
