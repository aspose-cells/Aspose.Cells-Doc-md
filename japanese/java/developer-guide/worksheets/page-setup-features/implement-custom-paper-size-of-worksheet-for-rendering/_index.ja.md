---
title: レンダリング用のワークシートのカスタム用紙サイズを実装する
type: docs
weight: 30
url: /ja/java/implement-custom-paper-size-of-worksheet-for-rendering/
---

## **可能な使用シナリオ**

MS Excelにはカスタム用紙サイズを作成する直接的なオプションはありませんが、ExcelファイルをPDFファイル形式にレンダリングする際に、希望のワークシートのカスタム用紙サイズを設定することができます。この文書では、Aspose.Cells APIを使用してワークシートのカスタム用紙サイズを設定する方法について説明します。

## **レンダリングのためのワークシートのカスタム用紙サイズを実装する**

Aspose.Cellsを使用すると、ワークシートの希望する用紙サイズを [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) の [**customPaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#customPaperSize-double-double-) メソッドを使用して指定できます。次のサンプルコードは、ワークブック内の最初のワークシートのカスタム用紙サイズを指定する方法を説明しています。参照のために、以下のコードによって生成された [出力PDF](45056030.pdf) もご覧ください。

## **スクリーンショット**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.java" >}}
{{< app/cells/assistant language="java" >}}
