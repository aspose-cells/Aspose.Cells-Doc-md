---
title: Extensions Web  Compléments Office avec C++
linktitle: Extensions Web  Modules complémentaires Office
type: docs
weight: 130
url: /fr/cpp/web-extensions-office-add-ins/
description: Apprenez comment ajouter et accéder aux extensions Web (compléments Office) dans les fichiers Excel en utilisant Aspose.Cells avec C++.
---

Les extensions Web étendent les applications Office et interagissent avec le contenu des documents Office. Elles ajoutent des fonctionnalités supplémentaires aux clients Office pour améliorer l'expérience utilisateur et la productivité.

Aspose.Cells offre également la possibilité de travailler avec des extensions Web.

## **Ajouter une extension Web**

Vous pouvez ajouter des extensions Web (compléments Office) dans Excel en cliquant sur l'onglet **Insertion** puis en cliquant sur le lien **Store**/**Obtenir des compléments**. Dans la boîte de dialogue Add-ins, recherchez le complément souhaité et ajoutez-le.

Aspose.Cells offre également la fonctionnalité d'ajouter des extensions Web en utilisant les classes [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). L'exemple de code suivant montre comment utiliser les classes [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) pour ajouter une extension Web à un fichier Excel. Veuillez consulter le [fichier Excel de sortie](89849869.xlsx) généré par le code pour référence.

### **Code d'exemple**

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

## **Accéder aux informations sur l'extension Web**

Aspose.Cells permet d'accéder aux informations des extensions Web dans un fichier Excel. L'exemple de code ci-dessous montre comment accéder aux informations des extensions Web en chargeant le [fichier Excel d'exemple](89849870.xlsx). Veuillez consulter la sortie console générée par le code pour référence.

### **Code d'exemple**

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

### **Sortie console**

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
