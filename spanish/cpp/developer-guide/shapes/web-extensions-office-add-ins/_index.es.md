---
title: Extensiones web  Complementos de Office con C++
linktitle: Extensiones Web  Complementos de Office
type: docs
weight: 130
url: /es/cpp/web-extensions-office-add-ins/
description: Aprende cómo agregar y acceder a Extensiones web (Complementos de Office) en archivos de Excel usando Aspose.Cells con C++.
---

Las Extensiones web amplían las aplicaciones de Office e interactúan con el contenido en los documentos de Office. Las Extensiones web agregan funcionalidad adicional a los clientes de Office para mejorar la experiencia del usuario y la productividad.

Aspose.Cells también proporciona la capacidad de trabajar con extensiones web.

## **Agregar Extensión Web**

Puedes agregar Extensiones Web (Complementos de Office) en Excel haciendo clic en la pestaña **Insertar** y luego en el enlace **Tienda**/**Obtener complementos**. En la caja de Complementos, busca el complemento que deseas y agrégalo.

Aspose.Cells también ofrece la función de agregar Extensiones Web utilizando las clases [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). La siguiente muestra de código demuestra cómo usar las clases [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) para agregar una extensión web a un archivo Excel. Consulta el [archivo Excel de salida](89849869.xlsx) generado por el código como referencia.

### **Código de muestra**

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

## **Acceder a la Información de la Extensión Web**

Aspose.Cells permite acceder a la información de las Extensiones Web en un archivo Excel. La siguiente muestra de código demuestra cómo acceder a la información de la extensión web cargando el [archivo Excel de ejemplo](89849870.xlsx). Consulta la salida de la consola generada por el código.

### **Código de muestra**

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

### **Salida de la consola**

{{< highlight java >}}
Width: 350
IsVisible: True
IsLocked: False
DockState: right
StoreName: en-US
StoreType: OMEX
WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
{{< /highlight >}}
