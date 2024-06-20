---
title: ワークブックおよびワークシートの印刷プレビュー
type: docs
weight: 130
url: /ja/java/workbook-and-worksheet-print-preview/
---

## **使用シナリオ**

何百万ページものExcelファイルをPDFまたは画像に変換する必要がある場合があります。そのようなファイルの処理には多くの時間とリソースがかかります。このような場合、ワークブックおよびワークシートの印刷プレビュー機能が役立つことがあります。ファイルを変換する前に、ユーザーは総ページ数を確認してからファイルを変換するかどうかを決定できます。この記事は、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)クラスを使用して総ページ数を調べる方法に焦点を当てています。

## **ワークブックおよびワークシートの印刷プレビュー**

Aspose.Cellsは印刷プレビュー機能を提供します。そのために、APIは[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)のクラスを提供します。ワークブック全体の印刷プレビューを作成するには、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)および[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)オブジェクトをコンストラクタに渡して[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)クラスのインスタンスを作成します。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)クラスは生成されたプレビューのページ数を返す[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)メソッドを提供します。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)クラスと同様に、[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)クラスは特定のワークシートの印刷プレビューを生成するために使用されます。ワークシートの印刷プレビューを作成するには、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)および[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)オブジェクトをコンストラクタに渡して[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)クラスのインスタンスを作成します。[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)クラスは生成されたプレビューのページ数を返す[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)メソッドを提供します。

次のコードスニペットは、[サンプルExcelファイル](Book1.xlsx)を使用して[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)の両方のクラスを使用する方法を示しています。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

上記のコードを実行した結果生成された出力は次のとおりです。

### **コンソール出力**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
