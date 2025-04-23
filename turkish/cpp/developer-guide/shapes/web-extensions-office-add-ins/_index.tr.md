---
title: Web Eklentileri  Office Eklentileri C++ ile
linktitle: Web Eklentileri  Ofis Eklentileri
type: docs
weight: 130
url: /tr/cpp/web-extensions-office-add-ins/
description: Aspose.Cells kullanarak Excel dosyalarına Web Eklentileri (Office Eklentileri) ekleme ve erişme hakkında bilgi edinin.
---

Web Eklentileri, Office uygulamalarını genişletir ve Office belgelerindeki içerikle etkileşime girer. Web Eklentileri, Office kullanıcı deneyimini ve üretkenliğini artırmak amacıyla ek fonksiyonlar ekler.

Aspose.Cells, Web Eklentileri ile çalışma kabiliyeti de sunar.

## **Web Eklentisi Ekleme**

Excel'de Web Eklentileri (Office Eklentileri) ekleyebilirsiniz, bunun için **Ekle** sekmesine tıklayın ve sonra **Mağaza**/**Ekle Eklentileri Al** bağlantısını tıklayın. Eklentiler kutusunda, istediğiniz eklentiyi arayın ve ekleyin.

Aspose.Cells, ayrıca [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) sınıflarını kullanarak Web Eklentileri ekleme özelliği sağlar. Aşağıdaki kod örneği, [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) sınıflarını kullanarak bir Excel dosyasına web eklentisi eklemeyi gösterir. Lütfen referans olarak kod tarafından oluşturulan [çıktı Excel dosyasına](89849869.xlsx) bakın.

### **Örnek Kod**

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

## **Web Eklentisi Bilgilerine Erişme**

Aspose.Cells, Excel dosyasındaki Web Eklentileri bilgisine erişim sağlar. Aşağıdaki kod örneği, [örnek Excel dosyasını](89849870.xlsx) yükleyerek web eklentisi bilgisine nasıl ulaşılacağını gösterir. Kod tarafından üretilen konsol çıktısına bakın.

### **Örnek Kod**

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

### **Konsol Çıktısı**

{{< highlight java >}}
Width: 350
IsVisible: True
IsLocked: False
DockState: right
StoreName: en-US
StoreType: OMEX
WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
{{< /highlight >}}
