---
title: スプレッドシートをCSV形式にエクスポートする際に、空行のセパレーターを保持します
type: docs
weight: 110
url: /ja/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する**

Aspose.Cellsは、スプレッドシートをCSV形式に変換する際に行のセパレーターを保持する機能を提供します。これには、[**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions)クラスの[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)プロパティを使用します。[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)はブール値のプロパティです。ExcelファイルをCSVに変換する際に空白の行のセパレーターを保持するには、[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)プロパティを**true**に設定します。

以下のサンプルコードは、[元のExcelファイル](KeepSeparatorsForBlankRow.xlsx)を読み込みます。[**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)プロパティを**true**に設定して、[KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv)として保存します。スクリーンショットには、元のExcelファイル、スプレッドシートをCSVに変換したときに生成されるデフォルトの出力、[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)を**true**に設定したときに生成される出力の比較が表示されています。

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
