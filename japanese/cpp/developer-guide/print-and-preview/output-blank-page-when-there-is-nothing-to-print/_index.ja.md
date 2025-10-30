---  
title: 出力する内容がない場合に空白ページを出力する（C++）  
linktitle: 空白ページを出力する。印刷するものがない場合  
type: docs  
weight: 90  
url: /ja/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Aspose.Cellsを使用して、空のワークシートを処理し、空白ページを印刷します（C++）。  
---  

## **可能な使用シナリオ**  

シートが空の場合、Aspose.Cellsはワークシートを画像にエクスポートするときに何も印刷しません。この動作は[**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/)プロパティを使用して変更できます。これを**true**に設定すると、空白ページが印刷されます。  

## **印刷するものがない場合、空白ページを出力**  

以下のサンプルコードは、空のワークブック（空のワークシートを含む）を作成し、[**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/)プロパティを**true**に設定した後、その空のワークシートを画像にレンダリングします。その結果、印刷すべき内容がないため空白ページが生成され、その画像は以下のように表示されます。  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **サンプルコード**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
{{< app/cells/assistant language="cpp" >}}
