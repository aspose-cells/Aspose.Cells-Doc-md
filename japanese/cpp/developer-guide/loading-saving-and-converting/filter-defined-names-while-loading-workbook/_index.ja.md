---
title: ワークブックを読み込む際に定義名をフィルタリングする
type: docs
weight: 50
url: /ja/cpp/filter-defined-names-while-loading-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsでは、ワークブック内に存在する定義名をフィルタリングまたは削除することができます。定義名をロードするには[**LoadDataFilterOptions::DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)を使用し、ワークブックをロードする際にそれらを削除するには~[**LoadDataFilterOptions::DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)を使用してください。ただし、定義名を削除すると、ワークブック内の数式が壊れる可能性があります。

## **ワークブックを読み込む際に定義名をフィルタリングする**

以下のサンプルコードは、[サンプルExcelファイル](61767860.xlsx)を読み込みます。このファイルはセル*C1*に定義名*SUM(MyName1, MyName2)*が含まれています。ワークブックを読み込む際に定義名を削除するために~[**LoadDataFilterOptions::DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)を使用しているため、出力Excelファイル(61767861.xlsx)のセルC1の数式が壊れ、*#NAME?*が表示されます。サンプルExcelファイルへのコードの効果を示すスクリーンショットを以下に示します。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cpp" >}}
