---
title: Golang経由でC++を使用してExcelファイルの読み込み時にピボットキャッシュレコードを解析
linktitle: ピボットキャッシュレコードの解析
type: docs
weight: 70
url: /ja/go-cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Aspose.Cells for C++を使用してExcelファイル読み込み時のピボットキャッシュレコード解析方法を学びます。
---

## **可能な使用シナリオ**

Pivot Tableを作成する際に、Microsoft Excelは元のデータのコピーを取り、それをPivot Cacheに保存します。Pivot CacheはMicrosoft Excelのメモリ内に保持されます。それを見ることはできませんが、それがPivot Tableが構築されたりSlicerの選択が変更されたり行または列が移動されたりするときに参照するデータです。これにより、Microsoft ExcelはPivot Tableの変更に非常に敏感になりますが、ファイルのサイズが2倍になる可能性もあります。つまり、Pivot Cacheはソースデータの単なるコピーなので、ファイルサイズが潜在的に2倍になるのは理にかなっています。

Workbookオブジェクト内にExcelファイルをロードするときに、Pivot Cacheのレコードも一緒に読み込むかどうかを[**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getparsingpivotcachedrecords/)プロパティを使用して決定できます。このプロパティのデフォルト値は**false**です。Pivot Cacheがかなり大きい場合、パフォーマンスが向上することがあります。しかし、Pivot Cacheのレコードも読み込む場合は、このプロパティを**true**に設定する必要があります。

## **Excelファイルをロードする際にPivotキャッシュレコードを解析する**

以下のサンプルコードは、[**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getparsingpivotcachedrecords/)プロパティの使用方法を説明します。それは[Pivot Cacheのレコードを解析しながら](61767773.xlsx)サンプルExcelファイルをロードし、ピボットテーブルをリフレッシュして[出力Excelファイル](61767774.xlsx)として保存しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ParsingPivotCachedRecordsWhileLoadingExcelFile.go" >}}
