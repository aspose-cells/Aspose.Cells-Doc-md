---
title: تحميل أوراق عمل محددة في دفتر العمل باستخدام C++
linktitle: تحميل الأوراق العمل المحددة في كتيب عمل
type: docs
weight: 100
url: /ar/cpp/load-specific-worksheets-in-a-workbook/
description: تعلم كيفية تحميل أوراق عمل محددة في دفتر العمل باستخدام Aspose.Cells مع C++ لتحسين الأداء وتقليل استهلاك الذاكرة.
---

{{% alert color="primary" %}}

 بشكل افتراضي، يقوم Aspose.Cells بتحميل كامل جدول البيانات إلى الذاكرة. من الممكن تحميل أوراق عمل محددة فقط، الأمر الذي يمكن أن يحسن الأداء ويستهلك ذاكرة أقل. هذا النهج مفيد عند العمل مع دفتر عمل كبير يتكون من العديد من أوراق العمل.

{{% /alert %}}

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoad : public LoadFilter {
public:
    CustomLoad() : LoadFilter(LoadDataFilterOptions::All) {}

    // Override StartSheet to customize loading behavior
    void StartSheet(Worksheet& sheet) override {
        // Custom logic for loading specific worksheet
    }
};

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Define a new Workbook
    Workbook workbook;

    // Load the workbook with the specified worksheet only
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new CustomLoad());

    // Create the workbook with custom load options
    workbook = Workbook(srcDir + u"TestData.xlsx", loadOptions);

    // Perform your desired task

    // Save the workbook
    workbook.Save(srcDir + u"outputFile.out.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

 إليكم تنفيذ فئة `CustomLoad`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoad : public LoadFilter
{
public:
    CustomLoad() : LoadFilter() {}
    ~CustomLoad() {}

    void StartSheet(Worksheet& sheet) override
    {
        if (sheet.GetName() == u"Sheet2")
        {
            // Load everything from worksheet "Sheet2"
            SetLoadDataFilterOptions(LoadDataFilterOptions::All);
        }
        else
        {
            // Load nothing
            SetLoadDataFilterOptions(LoadDataFilterOptions::Structure);
        }
    }
};
```
{{< app/cells/assistant language="cpp" >}}
