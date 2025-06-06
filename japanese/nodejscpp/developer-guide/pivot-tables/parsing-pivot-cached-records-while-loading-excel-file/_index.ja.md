---
title: Excelファイルをロードする際にPivotキャッシュレコードを解析する
type: docs
weight: 70
url: /ja/nodejs-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **可能な使用シナリオ**

Pivot Tableを作成する際に、Microsoft Excelは元のデータのコピーを取り、それをPivot Cacheに保存します。Pivot CacheはMicrosoft Excelのメモリ内に保持されます。それを見ることはできませんが、それがPivot Tableが構築されたりSlicerの選択が変更されたり行または列が移動されたりするときに参照するデータです。これにより、Microsoft ExcelはPivot Tableの変更に非常に敏感になりますが、ファイルのサイズが2倍になる可能性もあります。つまり、Pivot Cacheはソースデータの単なるコピーなので、ファイルサイズが潜在的に2倍になるのは理にかなっています。

Workbookオブジェクト内にExcelファイルをロードするときに、Pivot Cacheのレコードも一緒に読み込むかどうかを[**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-)プロパティを使用して決定できます。このプロパティのデフォルト値は**false**です。Pivot Cacheがかなり大きい場合、パフォーマンスが向上することがあります。しかし、Pivot Cacheのレコードも読み込む場合は、このプロパティを**true**に設定する必要があります。

## **Excelファイルをロードする際にPivotキャッシュレコードを解析する**

以下のサンプルコードは、[**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-)プロパティの使用方法を説明します。それは[Pivot Cacheのレコードを解析しながら](61767773.xlsx)サンプルExcelファイルをロードし、ピボットテーブルをリフレッシュして[出力Excelファイル](61767774.xlsx)として保存しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.js" >}}

