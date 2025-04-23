---
title: تنفيذ النطاقات غير المتسلسلة باستخدام C++
linktitle: تنفيذ النطاقات غير المتتالية
type: docs
weight: 700
url: /ar/cpp/implementing-non-sequential-ranges/
description: تعلم كيفية إنشاء نطاقات مسماة باستخدام خلايا غير متجاورة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}} 

عادةً ما تكون المجموعات المسماة مستطيلة مع الخلايا متقاربة ومتصلة ببعضها البعض. ولكن في بعض الأحيان، قد تحتاج إلى استخدام نطاق خانة غير متتالي حيث لا تكون الخلايا متصلة. تدعم Aspose.Cells إنشاء نطاق مسمى بخلايا غير متصلة.

{{% /alert %}} 

 يعرض المثال أدناه كيفية إنشاء نطاق غير متسلسل مسمى بواسطة Aspose.Cells for C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
