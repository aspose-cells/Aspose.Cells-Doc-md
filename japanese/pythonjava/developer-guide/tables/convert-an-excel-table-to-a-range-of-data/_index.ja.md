---
title: Excelのテーブルをデータの範囲に変換する
type: docs
weight: 10
url: /ja/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Excelのテーブルをデータの範囲に変換する**
Aspose.Cells for Python via Java は、Excelテーブルをデータの範囲に変換するオプションを提供します。このために、APIは[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) メソッドを提供しています。次のコードスニペットは、[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) メソッドの使用例を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **オプションを指定してExcelテーブルをデータの範囲に変換する**
テーブルをデータの範囲に変換する際に追加のオプションを提供できます。[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) クラスを使用して、テーブルの最終行インデックスを設定するために[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) クラスのインスタンスを[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) メソッドに渡すことができます。次のコードスニペットは、[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) クラスの使用例を示しています。指定した行インデックスまでテーブルの書式設定が保持され、それ以降の書式設定が削除されます。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
