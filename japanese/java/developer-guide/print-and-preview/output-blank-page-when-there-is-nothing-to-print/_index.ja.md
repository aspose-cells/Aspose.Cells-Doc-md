---
title: 空白ページを出力する。印刷するものがない場合
type: docs
weight: 80
url: /ja/java/output-blank-page-when-there-is-nothing-to-print/
---

## **可能な使用シナリオ**

シートが空の場合、Aspose.Cellsはワークシートを画像にエクスポートする際に何も印刷しません。これを[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)プロパティを使用して変更できます。これを**true**に設定すると、空白ページが印刷されます。

## **印刷するものがない場合、空白ページを出力**

空のワークシートを持つ空のワークブックを作成し、[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)プロパティを**true**に設定してから空のワークシートを画像にレンダリングするサンプルコードは以下の通りです。結果として、印刷する内容がないため、空白のページが生成されます。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
