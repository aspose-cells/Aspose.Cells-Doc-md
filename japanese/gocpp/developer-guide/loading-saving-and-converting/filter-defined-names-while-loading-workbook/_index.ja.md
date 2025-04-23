---
title: ワークブックを読み込む際に定義名をフィルタリングする
type: docs
weight: 50
url: /ja/go-cpp/filter-defined-names-while-loading-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsでは、ブック内に定義された名前をフィルタリングしたり削除したりできます。[[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/)]を使用して、ワークブックの読み込み時に定義された名前をロードしてください。ただし、定義された名前を削除すると、ワークブック内の数式が壊れる可能性があることに注意してください。

## **ワークブックを読み込む際に定義名をフィルタリングする**

以下のサンプルコードは、定義された名前を含むセル **C1** の数式 *=SUM(MyName1, MyName2)* を持つ [サンプルExcelファイル](#)を読み込みます。ワークブックの読み込み時に ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) を使って定義された名前を削除しているため、出力ExcelファイルのセルC1の数式は壊れ、*#NAME?*となります。コードの効果を示すスクリーンショットも併せて掲載しています。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
