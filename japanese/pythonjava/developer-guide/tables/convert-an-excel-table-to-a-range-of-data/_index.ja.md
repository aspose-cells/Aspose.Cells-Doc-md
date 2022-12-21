---
title: Excel テーブルをデータ範囲に変換する
type: docs
weight: 10
url: /ja/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **Excel テーブルをデータ範囲に変換する**
 Aspose.Cells for Python via Java は、Excel テーブルをデータの範囲に変換するオプションを提供します。このために、API は[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ） 方法。次のコード スニペットは、[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)メソッドを使用して、Excel テーブルをデータ範囲に変換します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **オプションを使用して Excel テーブルを範囲に変換する**
を使用してテーブルを範囲に変換する際に、追加のオプションを指定できます。[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)クラス。のインスタンスを渡すことができます[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)へのクラス[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)メソッドを使用して、追加のオプションを指定します。次のコード スニペットは、[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)テーブルの最後の行インデックスを設定するクラス。テーブルの書式設定は、指定された行インデックスまで保持され、残りの書式設定は削除されます。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
