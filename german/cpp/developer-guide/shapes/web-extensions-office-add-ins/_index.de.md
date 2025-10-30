---
title: Web Erweiterungen  Office Add Ins mit C++
linktitle: Web Erweiterungen  Office Add ins
type: docs
weight: 130
url: /de/cpp/web-extensions-office-add-ins/
description: Erfahren Sie, wie Sie Web Erweiterungen (Office Add Ins) in Excel Dateien mit Aspose.Cells und C++ hinzufügen und zugreifen.
---

Web-Erweiterungen erweitern Office-Anwendungen und interagieren mit Inhalten in Office-Dokumenten. Web-Erweiterungen fügen den Office-Clients zusätzliche Funktionen hinzu, um die Benutzererfahrung und Produktivität zu verbessern.

Aspose.Cells bietet auch die Möglichkeit, mit Web-Erweiterungen zu arbeiten.

## **Web-Erweiterung hinzufügen**

Sie können Web-Erweiterungen (Office-Add-Ins) in Excel hinzufügen, indem Sie auf die Registerkarte **Einfügen** klicken und dann auf den Link **Store**/**Add-Ins holen**. Im Add-In-Fenster durchsuchen Sie nach dem gewünschten Add-In und fügen es hinzu.

Aspose.Cells bietet auch die Funktion, Web-Erweiterungen mit den Klassen [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) hinzuzufügen. Das folgende Codebeispiel zeigt die Verwendung der Klassen [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/), um eine Web-Erweiterung zu einer Excel-Datei hinzuzufügen. Bitte sehen Sie sich die [Ausgabedatei](89849869.xlsx) an, die durch den Code erstellt wurde.

### **Beispielcode**

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

## **Zugriff auf Web-Erweiterungsinformationen**

Aspose.Cells ermöglicht den Zugriff auf Informationen von Web-Erweiterungen in einer Excel-Datei. Das folgende Codebeispiel zeigt, wie man Web-Erweiterungsinformationen durch Laden der [Beispiel-Excel-Datei](89849870.xlsx) abruft. Bitte sehen Sie sich die Konsolenausgabe an, die vom Code erzeugt wird.

### **Beispielcode**

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

### **Konsolenausgabe**

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
