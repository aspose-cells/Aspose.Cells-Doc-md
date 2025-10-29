---  
title: إنشاء دفتر عمل مشترك باستخدام Aspose.Cells مع C++  
linktitle: إنشاء دفتر عمل مشترك باستخدام Aspose.Cells  
type: docs  
weight: 40  
url: /ar/cpp/create-shared-workbook-with-aspose-cells/  
description: تعلم كيفية إنشاء دفتر عمل مشترك باستخدام Aspose.Cells مع C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

يسمح لك Microsoft Excel بمشاركة دفتر العمل كما هو موضح في لقطة الشاشة التالية. عند مشاركة دفتر العمل، يمكن لأكثر من مستخدم تحرير دفتر العمل على الشبكة. يتيح لك Aspose.Cells إنشاء دفتر عمل مشترك باستخدام خاصية [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **إنشاء دفتر عمل مشترك باستخدام Aspose.Cells**  

يخلق الكود النموذجي التالي دفتر عمل مشترك عن طريق تعيين الخاصية [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) كـ **true**. عندما تفتح ملف Excel المخرج ([ملف الإخراج](55541786.xlsx)) في Microsoft Excel، سترى **مشترك** مع اسم دفتر العمل كما هو موضح في لقطة الشاشة هذه.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **الكود المثالي**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create Workbook object
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>();

    // Share the Workbook
    wb->GetSettings().SetShared(true);

    // Save the Shared Workbook
    wb->Save(u"outputSharedWorkbook.xlsx");

    std::cout << "Shared workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
