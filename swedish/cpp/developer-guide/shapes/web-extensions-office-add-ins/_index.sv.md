---
title: Webutvidgningar  Office tillägg med C++
linktitle: Webbutökningar  Office tillägg
type: docs
weight: 130
url: /sv/cpp/web-extensions-office-add-ins/
description: Lär dig att lägga till och komma åt Webutvidgningar (Office tillägg) i Excel filer med Aspose.Cells och C++.
---

Webutvidgningar utökar Office-applikationer och interagerar med innehållet i Office-dokument. Webutvidgningar tillför ytterligare funktionalitet till Office-klienter för att förbättra användarupplevelsen och produktiviteten.

Aspose.Cells ger också möjligheten att arbeta med webbutökningar.

## **Lägg till webbförlängning**

Du kan lägga till Webutvidgningar (Office-tillägg) i Excel genom att klicka på fliken **Insätt** och sedan klicka på länken **Butik**/**Hämta tillägg**. I Tilläggsboxen bläddrar du efter det tillägg du vill ha och lägger till det.

Aspose.Cells erbjuder också möjligheten att lägga till Webutvidgningar med hjälp av [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/)- och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/)-klasserna. Följande kodexempel visar hur man använder [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/)- och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/)-klasser för att lägga till ett webbutvidgning till en Excel-fil. Se [utdata-Excelfilen](89849869.xlsx) genererad av koden för referens.

### **Exempelkod**

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

## **Få tillgång till information om webbförlängning**

Aspose.Cells ger möjligheten att komma åt information om Webutvidgningar i en Excel-fil. Följande kodexempel visar hur man får åtkomst till webbutvidgningsinformation genom att ladda [exempel-Excelfilen](89849870.xlsx). Se den genererade konsolutmatningen för referens.

### **Exempelkod**

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

### **Konsoloutput**

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
