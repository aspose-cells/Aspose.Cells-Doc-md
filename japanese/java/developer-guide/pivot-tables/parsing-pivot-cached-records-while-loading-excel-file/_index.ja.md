---
title: Excel ファイルの読み込み中にピボット キャッシュ レコードを解析する
type: docs
weight: 100
url: /ja/java/parsing-pivot-cached-records-while-loading-excel-file/
---
## **考えられる使用シナリオ**

ピボット テーブルを作成すると、Microsoft Excel はソース データのコピーを取得し、ピボット キャッシュに保存します。ピボット キャッシュは、Microsoft Excel のメモリ内に保持されます。見ることはできませんが、ピボット テーブルを作成したり、スライサーの選択を変更したり、行/列を移動したりするときに、ピボット テーブルが参照するデータです。これにより、Microsoft Excel がピボット テーブルの変更に非常に反応しやすくなりますが、ファイルのサイズが 2 倍になることもあります。結局、ピボット キャッシュはソース データの単なる複製であるため、ファイル サイズが潜在的に 2 倍になることは理にかなっています。

Workbook オブジェクト内に Excel ファイルをロードするときに、ピボット キャッシュのレコードもロードするかどうかを決定できます。[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)財産。このプロパティのデフォルト値は**間違い**.ピボット キャッシュが非常に大きい場合は、パフォーマンスが向上する可能性があります。ただし、Pivot Cache のレコードもロードする場合は、このプロパティを次のように設定する必要があります。**真実**.

## **Excel ファイルの読み込み中にピボット キャッシュ レコードを解析する**

次のサンプル コードは、[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)財産。それは[サンプル Excel ファイル](61767786.xlsx)ピボット キャッシュ レコードの解析中。次に、ピボット テーブルを更新して、[出力エクセルファイル](61767785.xlsx).

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
