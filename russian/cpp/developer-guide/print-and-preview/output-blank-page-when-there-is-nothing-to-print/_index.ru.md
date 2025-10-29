---  
title: Вывод пустой страницы, если ничего не нужно печатать, с помощью C++  
linktitle: Вывод пустой страницы, когда нечего печатать  
type: docs  
weight: 90  
url: /ru/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Обрабатывайте пустые рабочие листы и выводите пустые страницы с помощью Aspose.Cells и C++.  
---  

## **Возможные сценарии использования**  

Если лист пустой, то Aspose.Cells ничего не распечатает при экспорте рабочего листа в изображение. Вы можете изменить это поведение, используя свойство [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/). Когда вы установите его в **true**, он будет печатать пустую страницу.  

## **Вывод пустой страницы, когда нечего печатать**  

Следующий пример кода создает пустую рабочую книгу с пустым листом и рендерит этот пустой лист в изображение после установки свойства [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) в значение **true**. В результате получается пустая страница, так как нечего печатать, что видно на изображении ниже.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Образец кода**  

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
