---
title: تحقق مما إذا كان مشروع VBA محميًا ومقفلًا للمراجعة باستخدام C++
linktitle: التحقق مما إذا كان مشروع VBA محميًا ومقفلا للعرض
type: docs
weight: 30
url: /ar/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: تعلم كيفية التحقق مما إذا كان مشروع VBA محميًا ومقفلًا للمراجعة في ملفات Excel باستخدام Aspose.Cells for C++.
---

## التحقق مما إذا كان مشروع VBA محميًا ومقفلًا للمراجعة في C++

يسمح Aspose.Cells بالتحقق مما إذا كان مشروع VBA لملف Excel محميًا ومقفلًا للمراجعة. لهذا، يوفر API الخاصية [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/). إذا كانت مغلقة للمراجعة، فإن الخاصية [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) تُرجع **true**.

## **الكود المثالي**

يحمّل الكود التالي ملف إكسل النموذجي ([ملف النموذج](43352065.xlsm)) ويفحص ما إذا كان مشروع VBA الخاص بملف إكسل محميًا ومقفلًا للمراجعة. يرجى أيضًا مراجعة ناتجه في وحدة وحدة التحكم كمرجع.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

هذا هو مخرج الكونسول للكود العيني أعلاه عند تنفيذه مع [ملف Excel عيني](43352065.xlsm) المقدم.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
