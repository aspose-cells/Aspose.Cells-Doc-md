---
title: Excelファイルをロードする際にPivotキャッシュレコードを解析する
type: docs
weight: 100
url: /ja/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **可能な使用シナリオ**

Pivot Tableを作成する際に、Microsoft Excelは元のデータのコピーを取り、それをPivot Cacheに保存します。Pivot CacheはMicrosoft Excelのメモリ内に保持されます。それを見ることはできませんが、それがPivot Tableが構築されたりSlicerの選択が変更されたり行または列が移動されたりするときに参照するデータです。これにより、Microsoft ExcelはPivot Tableの変更に非常に敏感になりますが、ファイルのサイズが2倍になる可能性もあります。つまり、Pivot Cacheはソースデータの単なるコピーなので、ファイルサイズが潜在的に2倍になるのは理にかなっています。

Workbookオブジェクト内でExcelファイルをロードするとき、Pivot Cacheのレコードも同時にロードするかどうかを決定することができます。それには[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)プロパティを使用します。このプロパティのデフォルト値は**false**です。Pivot Cacheがかなり大きい場合、これはパフォーマンスを向上させることができます。ただし、Pivot Cacheのレコードもロードする場合は、このプロパティを**true**に設定する必要があります。

## **Excelファイルをロードする際にPivotキャッシュレコードを解析する**

以下のサンプルコードでは、[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)プロパティの使用方法を説明しています。Pivot Cacheのレコードを解析しながら、[サンプルExcelファイル](61767786.xlsx)をロードし、その後、ピボットテーブルを更新して、[出力Excelファイル](61767785.xlsx)として保存しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
