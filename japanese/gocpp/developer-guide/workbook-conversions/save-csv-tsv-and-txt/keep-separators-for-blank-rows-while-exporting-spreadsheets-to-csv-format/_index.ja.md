---
title: 空白行のセパレータを保持したままスプレッドシートをCSV形式にエクスポートする方法をGolang経由でC++で学ぶ。
linktitle: スプレッドシートをCSV形式にエクスポートする際に、空行のセパレーターを保持します
type: docs
weight: 160
url: /ja/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cellsを使用してGolang経由でC++でスプレッドシートをCSVにエクスポートする際に空白行のセパレータを保持する方法を学ぶ。
---

## **CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する**

Aspose.Cellsは、スプレッドシートをCSV形式に変換する際にライン区切りを保持する機能を提供します。そのために、[**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/)クラスの[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)プロパティを使用できます。[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)はブール型のプロパティです。ExcelファイルをCSVに変換するときに空白行の区切りを保持するには、[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)プロパティを**true**に設定します。

以下のサンプルコードは、[ソースExcelファイル](84378743.xlsx)を読み込み、[**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)プロパティを**true**に設定し、[出力.csv](84378744.csv)として保存します。スクリーンショットは、ソースExcelファイル、CSV変換時に生成されたデフォルト出力、そして[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)を**true**に設定した場合の出力の比較を示しています。

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
