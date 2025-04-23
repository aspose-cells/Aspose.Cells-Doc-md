---
title: 空白ページを出力する。印刷するものがない場合
type: docs
weight: 90
url: /ja/net/output-blank-page-when-there-is-nothing-to-print/
---

## **可能な使用シナリオ**

シートが空白の場合、Aspose.Cellsはワークシートをイメージにエクスポートする際に何も印刷しません。これを変更するには、[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) プロパティを使用します。これを **true**に設定すると、空白のページが印刷されます。

## **印刷するものがない場合、空白ページを出力**

次のサンプルコードでは、空のワークシートを含む空のワークブックを作成し、[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) プロパティを **true**に設定した後に空のワークシートをイメージにレンダリングします。その結果、何も印刷するものがないため、空白のページが生成されます。画像は以下に表示されています。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
