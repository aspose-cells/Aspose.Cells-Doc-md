---
title: スプレッドシートをCSV形式にエクスポートする際に、空行のセパレーターを保持します
type: docs
weight: 160
url: /ja/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for Python via .NET APIを使用して、スプレッドシートをCSV形式にエクスポートする際に空白の行の区切り記号を保持する方法。
keywords: PythonでスプレッドシートをCSV形式にエクスポートする際に空行の区切りを保持する、ExcelファイルをCSV形式で保存する際に空行の区切りを保持するPython via NET、ExcelをCSV形式でエクスポートする際に空行の区切りを保持する。
---

## **CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する**

Aspose.Cells for Python via .NETはスプレッドシートをCSV形式に変換する際に空行の区切り記号を保持する機能を提供します。このために、[**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)クラスの[**TxtSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/)プロパティを使用できます。[**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)はブール値のプロパティです。空行を区切り記号として保持するには、[**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)プロパティを**true**に設定します。

次のサンプルコードでは、[ソースExcelファイル](84378743.xlsx)をロードします。[**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)プロパティを**true**に設定し、[output.csv](84378744.csv)として保存します。スクリーンショットは、ソースExcelファイルと、スプレッドシートをCSVに変換した際のデフォルトの出力と、[**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)を**true**に設定した際の出力を比較したものです。

![todo:image_alt_text](result.jpg)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
