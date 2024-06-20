---
title: スプレッドシートをCSV形式にエクスポートする際に、空行のセパレーターを保持します
type: docs
weight: 160
url: /ja/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する**

Aspose.Cellsは、スプレッドシートをCSV形式に変換する際に行のセパレーターを保持する機能を提供します。これには、[**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions)クラスの[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)プロパティを使用します。[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)はブール値のプロパティです。ExcelファイルをCSVに変換する際に空白の行のセパレーターを保持するには、[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)プロパティを**true**に設定します。

次のサンプルコードでは、[ソースExcelファイル](84378743.xlsx)をロードします。[**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)プロパティを**true**に設定し、[output.csv](84378744.csv)として保存します。スクリーンショットは、ソースExcelファイルと、スプレッドシートをCSVに変換した際のデフォルトの出力と、[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)を**true**に設定した際の出力を比較したものです。

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
