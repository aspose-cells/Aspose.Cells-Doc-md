---
title: إضافات الويب  إضافات Office باستخدام C++
linktitle: الإضافات الإلكترونية للويب  إضافات Office
type: docs
weight: 130
url: /ar/cpp/web-extensions-office-add-ins/
description: تعلم كيفية إضافة والوصول إلى إضافات الويب (إضافات Office) في ملفات إكسل باستخدام Aspose.Cells مع C++.
---

تمتد إضافات الويب تطبيقات Office وتتفاعل مع محتوى مستندات Office. تضيف إضافات الويب وظائف إضافية لعملاء Office لتحسين تجربة المستخدم والإنتاجية.

توفر Aspose.Cells أيضًا القدرة على العمل مع ملحقات الويب.

## **إضافة ملحق ويب**

 يمكنك إضافة إضافات الويب (إضافات Office) في إكسل بالنقر على علامة التبويب **إدراج** ثم النقر على رابط **المتجر** / **الحصول على الإضافات**. في مربع الإضافات، تصفح الإضافة التي تريدها وأضفها.

توفر Aspose.Cells أيضًا ميزة إضافة إضافات الويب باستخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). يوضح نموذج الكود التالي استخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) لإضافة إضافة ويب إلى ملف إكسل. يرجى مراجعة ملف إكسل الناتج [ملف الإكسل الناتج](89849869.xlsx) باستخدام الكود للمراجعة.

### **الكود المثالي**

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

## **الوصول إلى معلومات ملحق الويب**

توفر Aspose.Cells القدرة على الوصول إلى معلومات إضافات الويب في ملف إكسل. يوضح مثال الكود التالي كيف يمكن الوصول إلى معلومات الإضافة عن طريق تحميل ملف إكسل العينة [ملف إكسل عينة](89849870.xlsx). يرجى الاطلاع على مخرجات وحدة التحكم التي تم إنشاؤها بواسطة الكود للمراجعة.

### **الكود المثالي**

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

### **مخرجات الوحدة**

{{< highlight java >}}
Width: 350
IsVisible: True
IsLocked: False
DockState: right
StoreName: en-US
StoreType: OMEX
WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
{{< /highlight >}}
