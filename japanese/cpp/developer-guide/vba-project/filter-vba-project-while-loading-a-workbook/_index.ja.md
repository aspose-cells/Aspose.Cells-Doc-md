---
title: C++を使ってワークブックを読み込みながらVBAプロジェクトをフィルタリングする
linktitle: ワークブックを読み込む際にVBAプロジェクトをフィルタリングする
type: docs
weight: 140
url: /ja/cpp/filter-vba-project-while-loading-a-workbook/
description: Aspose.CellsとC++を使ってExcelワークブックの読み込み時にVBAプロジェクトをフィルタリングする方法を学びます。
---

## **Excelワークブックの読み込み時にVBAプロジェクトをフィルタリング（C++）**

一部の.xlsm/.xslbファイルには非常に大量のマクロ（または非常に長いマクロ）が含まれている場合があります。Aspose.Cellsは、そのようなワークブックを開く際に無条件でメタデータを読み込みます。ただし、多数のワークブックからシート名のみ抽出したい場合は、[**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions)を使用して制御し、不要なコンテンツをスキップできます。このフィルターは、新しいオプション[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions)を導入することで提供されます。

## **サンプルコード**

以下のサンプルコードは、VBAのみがフィルタリングされたワークブックを読み込みます。この機能のテスト用に使用されるサンプルファイルを提供するリンクがあります。

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
