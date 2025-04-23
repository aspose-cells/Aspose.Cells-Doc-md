---
title: ワークシートがダイアログシートであるかを検索する
type: docs
weight: 100
url: /ja/java/find-if-the-worksheet-is-dialog-sheet/
---

## **可能な使用シナリオ**

ダイアログシートは、ダイアログボックスを含むシートの古い形式です。このようなシートは、Microsoft Excel 2003などの古いバージョンによって挿入される場合があります（以下のスクリーンショットで示されています）。また、Microsoft Excel 2016などの最新バージョンではVBAによって挿入することもできます。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Aspose.Cellsが提供する*[**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)*プロパティを使用して、シートがダイアログシートまたはその他の種類のシートかどうかを見分けることができます。列挙値*[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)*を返す場合、ダイアログシートと取り扱っていることを意味します。

## **ワークシートがダイアログシートであるかを検索する**

以下のサンプルコードは、ダイアログシートを含む*サンプルExcelファイル*(64716841.xlsx)を読み込みます。*[**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)*プロパティをチェックして*[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)*と比較し、そのメッセージを印刷します。詳細については、以下のサンプルコードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **コンソール出力**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
