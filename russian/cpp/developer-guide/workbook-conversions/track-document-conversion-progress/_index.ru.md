---
title: Отслеживание прогресса преобразования документа с помощью C++
linktitle: Отслеживание процесса конвертации документа
type: docs
weight: 970
url: /ru/cpp/track-document-conversion-progress/
description: Узнайте, как отслеживать прогресс преобразования документа в C++ с помощью Aspose.Cells для повышения удобства использования приложения.
---

## **Возможные сценарии использования**

Иногда преобразование больших файлов Excel занимает некоторое время. В этот период вы можете отображать прогресс преобразования документа вместо просто экрана загрузки, чтобы повысить удобство использования вашего приложения. Aspose.Cells поддерживает отслеживание прогресса преобразования документа через интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). Интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) предоставляет методы [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) и [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/), которые можно реализовать в вашем собственном классе. Также вы можете управлять тем, какие страницы рендерятся, как показано в пользовательском классе `TestPageSavingCallback`.

## **Отслеживание прогресса конвертации документов**

Следующий пример кода загружает исходный файл Excel и выводит прогресс его преобразования в консоль, используя пользовательский класс `TestPageSavingCallback`, реализующий интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/).

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Page " << args.GetPageIndex() + 1 << " is starting to save." << std::endl;
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "Page " << args.GetPageIndex() + 1 << " has been saved." << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"PagesBook1.xlsx";
    U16String outputFilePath = outDir + u"DocumentConversionProgress.pdf";

    Workbook workbook(inputFilePath);
    PdfSaveOptions pdfSaveOptions;

    TestPageSavingCallback callback;
    pdfSaveOptions.SetPageSavingCallback(&callback);

    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Document conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Следующий код — это пользовательский класс `TestPageSavingCallback`.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class TestPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Start saving page index " << args.GetPageIndex() 
                  << " of pages " << args.GetPageCount() << std::endl;

        if (args.GetPageIndex() < 2)
        {
            args.SetIsToOutput(false);
        }
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "End saving page index " << args.GetPageIndex() 
                  << " of pages " << args.GetPageCount() << std::endl;

        if (args.GetPageIndex() >= 8)
        {
            args.SetHasMorePages(false);
        }
    }
};
```

## **Вывод в консоль**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
