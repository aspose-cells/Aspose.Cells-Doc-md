---
title: 印刷するものがない場合に白紙ページを出力する
type: docs
weight: 80
url: /ja/java/output-blank-page-when-there-is-nothing-to-print/
---
##  **考えられる使用シナリオ**

シートが空の場合、ワークシートを画像にエクスポートするときに、Aspose.Cells は何も印刷しません。この動作は次のように変更できます。[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)財産。 *true** に設定すると、空白のページが印刷されます。

##  **印刷するものがない場合に白紙ページを出力する**

次のサンプル コードは、空のワークシートを含む空のワークブックを作成し、設定後に空のワークシートを画像にレンダリングします。[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)プロパティを *true** に設定します。その結果、以下に示すように、印刷するものが何もないため、空白のページが生成されます。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
