---
title: Excel ファイルのロード中にピボットのキャッシュされたレコードを解析する
type: docs
weight: 70
url: /ja/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Aspose.Cells for Python via .NET の Excel ファイルを読み込むときにピボット キャッシュ レコードを解析する方法。
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **考えられる使用シナリオ**

ピボット テーブルを作成すると、Microsoft Excel はソース データのコピーを取得し、ピボット キャッシュに保存します。ピボット キャッシュは、Microsoft Excel のメモリ内に保持されます。見ることはできませんが、ピボット テーブルを作成するとき、スライサーの選択を変更するとき、または行や列を移動するときに、ピボット テーブルが参照するデータです。これにより、Microsoft Excel はピボット テーブルの変更に非常に敏感になりますが、ファイルのサイズが 2 倍になる可能性もあります。結局のところ、ピボット キャッシュはソース データの複製にすぎないため、ファイル サイズが 2 倍になる可能性があるのは当然です。

Excel ファイルを Workbook オブジェクト内にロードするときに、ピボット キャッシュのレコードもロードするかどうかを決定できます。[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)財産。このプロパティのデフォルト値は *false** です。ピボット キャッシュが非常に大きい場合、パフォーマンスが向上する可能性があります。ただし、ピボット キャッシュのレコードもロードしたい場合は、このプロパティを *true** に設定する必要があります。

##  **Excel ファイルのロード中にピボットのキャッシュされたレコードを解析する**

次のサンプルコードは、[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)財産。それはロードします[サンプル Excel ファイル](61767773.xlsx)ピボットのキャッシュされたレコードを解析している間。次に、ピボット テーブルを更新し、[Excelファイルを出力](61767774.xlsx).

##  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
