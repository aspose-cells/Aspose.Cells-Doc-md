---
title: スプレッドシートを画像にレンダリングする際にデフォルトフォントを設定する
type: docs
weight: 840
url: /ja/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティを使用して、スプレッドシートを画像にレンダリングする際にデフォルトフォントを設定してください。このプロパティは、ワークブックのデフォルトフォントが文字をレンダリングできない場合にのみ有効になります。[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティで指定されたデフォルトフォントは、無効または存在しないフォントを持つすべてのセルに使用されます。

{{% /alert %}} 
## **スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定**
以下のサンプルコードは、ワークブックを作成し、最初のワークシートのセルA4にテキストを追加し、そのフォントを無効または存在しないフォントに設定します。その後、ワークシートのイメージを2枚取得します。最初のイメージは、[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティを*Courier New*に設定して取得され、2番目のイメージは、[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティを*Times New Roman*に設定して取得されます。

[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティを*Courier New*に設定した後の出力画像です。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティを*Times New Roman*に設定した後の出力画像です。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
