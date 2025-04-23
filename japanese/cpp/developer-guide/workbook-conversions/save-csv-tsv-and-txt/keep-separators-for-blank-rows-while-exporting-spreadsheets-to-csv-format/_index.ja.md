---
title: 空白の行に区切り記号を保持しながら、スプレッドシートをCSV形式にエクスポートする（C++）
linktitle: スプレッドシートをCSV形式にエクスポートする際に、空行のセパレーターを保持します
type: docs
weight: 160
url: /ja/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cellsを使用して、スプレッドシートをCSV形式にエクスポートする際に空白行の区切り記号を保持する方法を学習します。
---

## **CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する**

Aspose.Cellsは、スプレッドシートをCSV形式に変換する際にライン区切りを保持する機能を提供します。そのために、[**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/)クラスの[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)プロパティを使用できます。[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)はブール型のプロパティです。ExcelファイルをCSVに変換するときに空白行の区切りを保持するには、[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)プロパティを**true**に設定します。

以下のサンプルコードは、[ソースExcelファイル](84378743.xlsx)を読み込み、[**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)プロパティを**true**に設定し、[出力.csv](84378744.csv)として保存します。スクリーンショットは、ソースExcelファイル、CSV変換時に生成されたデフォルト出力、そして[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)を**true**に設定した場合の出力の比較を示しています。

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(inputFilePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
    options.SetKeepSeparatorsForBlankRow(true);

    // Save the file with the options
    workbook.Save(outDir + u"output.csv", options);

    std::cout << "File saved successfully as output.csv!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
