---
title: スプレッドシートを画像にレンダリングする際のデフォルト フォントの設定
type: docs
weight: 840
url: /ja/java/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}} 

をご利用ください[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティを使用して、スプレッドシートを画像にレンダリングする際のデフォルト フォントを設定します。このプロパティは、ワークブックの既定のフォントが文字をレンダリングできない場合にのみ有効です。で指定されたデフォルトのフォント[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティは、無効または存在しないフォントを持つすべてのセルに使用されます。

{{% /alert %}} 
## **スプレッドシートを画像にレンダリングする際のデフォルト フォントの設定**
次のサンプル コードは、ワークブックを作成し、最初のワークシートのセル A4 にテキストを追加し、そのフォントを無効または存在しないフォントに設定します。次に、ワークシートの 2 つの画像を取得します。最初の画像は、[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティへ*クーリエ 新規* 番目の画像は、[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティへ*タイムズ ニュー ローマン*.

これは、設定後の出力イメージです。[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティへ*クーリエ 新規*.

![todo:画像_代替_文章](set-default-font-while-rendering-spreadsheet-to-images_1.png)

これは、設定後の出力イメージです。[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティへ*タイムズ ニュー ローマン*.

![todo:画像_代替_文章](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
