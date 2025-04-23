---
title: ワークブックを読み込む際に定義名をフィルタリングする
type: docs
weight: 50
url: /ja/python-net/filter-defined-names-while-loading-workbook/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETは、ワークブック内の定義済み名前をフィルターまたは削除することを可能にします。[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)を使って定義済み名前を読み込み、~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)を使ってそれらを削除します。ただし、定義済み名前を削除すると、ワークブック内の式が破損する可能性があることに注意してください。

## **ワークブックを読み込む際に定義名をフィルタリングする**

以下のサンプルコードは、[サンプルExcelファイル](61767860.xlsx)を読み込みます。このファイルはセル*C1*に定義名*SUM(MyName1, MyName2)*が含まれています。ワークブックを読み込む際に定義名を削除するために~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)を使用しているため、出力Excelファイル(61767861.xlsx)のセルC1の数式が壊れ、*#NAME?*が表示されます。サンプルExcelファイルへのコードの効果を示すスクリーンショットを以下に示します。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

