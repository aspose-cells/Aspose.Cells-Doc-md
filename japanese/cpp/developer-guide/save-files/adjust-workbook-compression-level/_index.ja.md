---
title: C++でワークブックの圧縮レベルを調整する
linktitle: Workbookの圧縮レベルを調整
type: docs
weight: 180
url: /ja/cpp/adjust-workbook-compression-level/
description: ファイルサイズと処理時間を最適化するために、Aspose.Cells for C++を使用してワークブックの圧縮レベルを調整する方法を学びます。
---

## **ワークブックの圧縮レベルを調整する**

開発者は、より大きなワークブックを扱うときに、ファイルサイズよりも処理時間を優先するか、その逆を優先するかもしれません。Aspose.Cellsは、ワークブックの圧縮レベルを設定するために使用できる[**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/)列挙型を提供します。 [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/)列挙型は、次のメンバーを提供します。

- レベル1：最も速くて効果の低い圧縮。
- レベル2：レベル1よりもやや遅いが、より優れています。
- レベル3：レベル2よりもやや遅いが、より優れています。
- レベル4：レベル3よりもやや遅いが、より優れています。
- レベル5：レベル4よりもやや遅く、より効果的な圧縮。
- レベル6：速度と圧縮効率の良いバランス。
- レベル7：かなり良い圧縮！
- レベル8：レベル7よりも優れた圧縮！
- レベル9："ベスト"の圧縮、ベストは入力データストリームのサイズを最も減らすことを意味します。これは最も遅い圧縮でもあります。

次のコードスニペットは、[**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/)列挙型の使用を示し、Level1、Level6、Level9の変換時間を比較します。また、生成されたファイルのサイズを比較することもできます。

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"LargeSampleFile.xlsx");

    // Create XlsbSaveOptions object
    XlsbSaveOptions options;

    // Set compression level to 1 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level1);
    auto start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_1_out.xlsb", options);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 1 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 6 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level6);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_6_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 6 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 9 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level9);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_9_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 9 Elapsed Time: " << duration.count() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
