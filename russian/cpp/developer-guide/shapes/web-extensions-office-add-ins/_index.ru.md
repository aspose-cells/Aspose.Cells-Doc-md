---
title: Расширения веб — надстройки Office с C++
linktitle: Веб расширения  дополнения для офиса
type: docs
weight: 130
url: /ru/cpp/web-extensions-office-add-ins/
description: Узнайте, как добавлять и получать доступ к расширениям веб — Office (надстройкам) в файлах Excel с помощью Aspose.Cells и C++.
---

Расширения веб расширяют возможности приложений Office и взаимодействуют с содержимым документов Office. Они добавляют дополнительную функциональность клиентским приложениям Office для улучшения пользовательского опыта и повышения производительности.

Aspose.Cells также предоставляет возможность работать с веб-расширениями.

## **Добавить веб-расширение**

Вы можете добавить расширения веб (надстройки Office) в Excel, кликнув на вкладку **Вставка**, а затем на ссылку **Магазин**/**Получить надстройки**. В окне надстроек найдите нужную надстроку и добавьте её.

Aspose.Cells также предоставляет возможность добавлять расширения веб, используя классы [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). Следующий пример демонстрирует использование классов [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) для добавления веб-расширения в файл Excel. Пожалуйста, посмотрите на [выходной файл Excel](89849869.xlsx), созданный этим кодом.

### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the WebExtension collection from the workbook's worksheets
    WebExtensionCollection extensions = workbook.GetWorksheets().GetWebExtensions();
    WebExtensionTaskPaneCollection taskPanes = workbook.GetWorksheets().GetWebExtensionTaskPanes();

    // Add a new WebExtension and WebExtensionTaskPane
    int32_t extensionIndex = extensions.Add();
    int32_t taskPaneIndex = taskPanes.Add();

    // Get the newly added WebExtension and configure it
    WebExtension extension = extensions.Get(extensionIndex);
    extension.GetReference().SetId(u"wa104379955");
    extension.GetReference().SetStoreName(u"en-US");
    extension.GetReference().SetStoreType(WebExtensionStoreType::OMEX);

    // Get the newly added WebExtensionTaskPane and configure it
    WebExtensionTaskPane taskPane = taskPanes.Get(taskPaneIndex);
    taskPane.SetIsVisible(true);
    taskPane.SetDockState(u"right");
    taskPane.SetWebExtension(extension);

    // Save the workbook with the added WebExtension
    workbook.Save(outDir + u"AddWebExtension_Out.xlsx");

    std::cout << "WebExtension added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Доступ к информации веб-расширения**

Aspose.Cells предоставляет возможность получать информацию о расширениях веб в файле Excel. Следующий пример показывает, как получить информацию о веб-расширениях, загрузив [пример файла Excel](89849870.xlsx). Обратите внимание на вывод в консоль, сгенерированный кодом.

### **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook workbook(srcDir + u"WebExtensionsSample.xlsx");

    // Get the collection of web extension task panes
    WebExtensionTaskPaneCollection taskPanes = workbook.GetWorksheets().GetWebExtensionTaskPanes();

    // Iterate through each task pane and print its properties
    for (int i = 0; i < taskPanes.GetCount(); ++i)
    {
        WebExtensionTaskPane taskPane = taskPanes.Get(i);

        std::cout << "Width: " << taskPane.GetWidth() << std::endl;
        std::cout << "IsVisible: " << taskPane.IsVisible() << std::endl;
        std::cout << "IsLocked: " << taskPane.IsLocked() << std::endl;
        std::cout << "DockState: " << taskPane.GetDockState().ToUtf8() << std::endl;
        std::cout << "StoreName: " << taskPane.GetWebExtension().GetReference().GetStoreName().ToUtf8() << std::endl;
        std::cout << "WebExtension.Id: " << taskPane.GetWebExtension().GetId().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();

    return 0;
}
```

### **Вывод в консоль**

{{< highlight java >}}
Width: 350
IsVisible: True
IsLocked: False
DockState: right
StoreName: en-US
StoreType: OMEX
WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
