---
title: 空白ページを出力する。印刷するものがない場合
type: docs
weight: 90
url: /ja/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **可能な使用シナリオ**

シートが空の場合、Aspose.Cells for Python via .NETはワークシートを画像にエクスポートしたときに何も出力しません。この動作を変更するには、[**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print)プロパティを使用します。これを**true**に設定すると、空白ページも出力されるようになります。

## **印刷するものがない場合、空白ページを出力**

次のサンプルコードでは、空のワークシートを含む空のワークブックを作成し、[**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) プロパティを **true**に設定した後に空のワークシートをイメージにレンダリングします。その結果、何も印刷するものがないため、空白のページが生成されます。画像は以下に表示されています。

![todo:image_alt_text](1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
