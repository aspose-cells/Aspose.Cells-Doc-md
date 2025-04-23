---
title: XLSBのリビジョンをXLSMに変換するC++コード
linktitle: XLSBのリビジョンをXLSMに変換する
type: docs
weight: 290
url: /ja/cpp/convert-revision-of-xlsb-to-xlsm/
description: Aspose.Cells を使用して XLSB ファイルのリビジョンを XLSM 形式に変換する方法を学びます。
---

{{% alert color="primary" %}} 

Aspose.Cells は now XLSB ファイルのリビジョンを XLSM ファイルに完全に変換できます。リビジョンは \xl\revisions パス内にあります。これらを表示するには、あなたの XLSB ファイル拡張子を ZIP に変更してください。\xl\revisions パスには .bin で終わるファイルが含まれています。

Aspose.Cells を使用して XLSB ファイルを XLSM ファイルに変換すると、これらの .bin ファイルが正常に .xml ファイルに変換される様子が、2つのスクリーンショットに示されています。

{{% /alert %}} 

以下のコード例は、Aspose.Cells を使用して XLSB ファイルを XLSM 形式に変換する方法を示しています。

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
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
