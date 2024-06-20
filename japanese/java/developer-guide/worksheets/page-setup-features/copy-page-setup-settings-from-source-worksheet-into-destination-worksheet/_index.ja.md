---
title: ソースワークシートからページ設定を宛先ワークシートにコピー
type: docs
weight: 10
url: /ja/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---

## **可能な使用シナリオ**

ブックに新しいシートを追加すると、デフォルトのページ設定が含まれています。ワークシート間で設定（[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)）を転送する必要がある場合があります。この文書では、Aspose.Cells APIを使用して、ワークシート間でページ設定をコピーする方法について説明します。

## **ソースワークシートからページ設定を宛先ワークシートにコピー**

次のサンプルコードは、[**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy(com.aspose.cells.PageSetup,%20com.aspose.cells.CopyOptions)) メソッドを使用して、1つのワークシートから別のワークシートにページ設定をコピーする方法を示しています。次のサンプルコードとそのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **コンソール出力**

{{< highlight java >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
