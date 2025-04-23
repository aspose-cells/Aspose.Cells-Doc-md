---
title: ワークブックを読み込む際に定義名をフィルタリングする
type: docs
weight: 50
url: /ja/java/filter-defined-names-while-loading-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsでは、ワークブック内に存在する定義名をフィルタリングまたは削除することができます。定義名をロードするには[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES)を使用し、ワークブックをロードする際にそれらを削除するには~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES)を使用してください。ただし、定義名を削除すると、ワークブック内の数式が壊れる可能性があります。

## **ワークブックを読み込む際に定義名をフィルタリングする**

次のサンプルコードは、定義名（MyName1、MyName2）を含むセルC1の数式を持つ[sample Excel file](61767873.xlsx)をロードします。 ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES)を使用して定義名を削除するため、[output Excel file](61767872.xlsx)のセルC1の数式が壊れ、*#NAME?*が表示されます。 サンプルExcelファイルへのコードの影響を示すスクリーンショットは次のとおりです。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
