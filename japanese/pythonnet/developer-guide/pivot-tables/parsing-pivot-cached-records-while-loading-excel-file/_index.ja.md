---
title: Excelファイルをロードする際にPivotキャッシュレコードを解析する
type: docs
weight: 70
url: /ja/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Aspose.Cells for Python via .NETを使用してExcelファイルを読み込む際のPivot Cached Recordsのパーシング方法。
keywords: Aspose.Cells for Python via .NETのExcel、Excel Pythonライブラリを使用してExcelファイルを読み込む際のPivot Cached Recordsのパーシング方法。
---

## **可能な使用シナリオ**

Pivot Tableを作成する際に、Microsoft Excelは元のデータのコピーを取り、それをPivot Cacheに保存します。Pivot CacheはMicrosoft Excelのメモリ内に保持されます。それを見ることはできませんが、それがPivot Tableが構築されたりSlicerの選択が変更されたり行または列が移動されたりするときに参照するデータです。これにより、Microsoft ExcelはPivot Tableの変更に非常に敏感になりますが、ファイルのサイズが2倍になる可能性もあります。つまり、Pivot Cacheはソースデータの単なるコピーなので、ファイルサイズが潜在的に2倍になるのは理にかなっています。

Workbookオブジェクト内にExcelファイルをロードするときに、Pivot Cacheのレコードも一緒に読み込むかどうかを[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)プロパティを使用して決定できます。このプロパティのデフォルト値は**false**です。Pivot Cacheがかなり大きい場合、パフォーマンスが向上することがあります。しかし、Pivot Cacheのレコードも読み込む場合は、このプロパティを**true**に設定する必要があります。

## **Excelファイルを読み込む際のPivot Cached Recordsのパーシング方法**

以下のサンプルコードは、[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)プロパティの使用方法を説明します。それは[Pivot Cacheのレコードを解析しながら](61767773.xlsx)サンプルExcelファイルをロードし、ピボットテーブルをリフレッシュして[出力Excelファイル](61767774.xlsx)として保存しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
