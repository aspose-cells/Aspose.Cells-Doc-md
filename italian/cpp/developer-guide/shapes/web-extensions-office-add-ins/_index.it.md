---
title: Web Extensions  Office Add in con C++
linktitle: Estensioni Web  Componenti aggiuntivi di Office
type: docs
weight: 130
url: /it/cpp/web-extensions-office-add-ins/
description: Impara come aggiungere e accedere alle Web Extensions (Office Add in) nei file Excel utilizzando Aspose.Cells con C++.
---

Le Web Extensions estendono le applicazioni Office e interagiscono con il contenuto nei documenti Office. Le Web Extensions aggiungono funzionalità aggiuntive ai client Office per migliorare l’esperienza utente e la produttività.

Aspose.Cells fornisce anche la capacità di lavorare con le estensioni Web.

## **Aggiungi estensione Web**

Puoi aggiungere Web Extensions (Office Add-in) in Excel cliccando sulla scheda **Inserisci** e poi cliccando sul collegamento **Store**/**Ottieni componenti aggiuntivi**. Nella casella dei componenti aggiuntivi, cerca l’addin desiderato e aggiungilo.

Aspose.Cells offre anche la funzione di aggiungere Web Extensions utilizzando le classi [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) e [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). Il seguente esempio di codice dimostra l’uso delle classi [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) e [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) per aggiungere un’estensione web a un file Excel. Si prega di consultare il [file Excel di output](89849869.xlsx) generato dal codice come riferimento.

### **Codice di Esempio**

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

## **Accesso alle informazioni sull'estensione Web**

Aspose.Cells fornisce la possibilità di accedere alle informazioni delle Web Extensions in un file Excel. Il seguente esempio di codice dimostra come accedere alle informazioni delle Web Extensions caricando il [file Excel di esempio](89849870.xlsx). Si prega di consultare l’output della console generato dal codice come riferimento.

### **Codice di Esempio**

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

### **Output della console**

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
