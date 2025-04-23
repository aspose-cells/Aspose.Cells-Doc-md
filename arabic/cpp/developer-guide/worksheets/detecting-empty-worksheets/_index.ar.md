---
title: كشف الأوراق الفارغة باستخدام C++
linktitle: كشف الأوراق العمل الفارغة
type: docs
weight: 410
url: /ar/cpp/detecting-empty-worksheets/
description: يعرض هذا المقال كود يوضح كيفية اكتشاف الأوراق الفارغة في ملفات Excel برمجيًا باستخدام واجهة برمجة تطبيقات C++ مع مكتبة Aspose.Cells.
keywords: كشف ورقة العمل الفارغة، العثور على ورقة عمل Excel فارغة باستخدام C++
---

## **فحص الخلايا المعبأة**

يمكن أن تحتوي أوراق العمل على خلية أو أكثر مملوءة بالقيم، حيث يمكن أن تكون القيمة بسيطة (نص، رقم، تاريخ/وقت) أو عبارة عن صيغة أو قيمة قائمة على الصيغة. في مثل هذه الحالة، من السهل اكتشاف ما إذا كانت ورقة العمل فارغة أم لا. كل ما علينا التحقق منه هو خاصية [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) أو [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/). إذا أعادت الخصائص المذكورة قيمة صفرية أو موجبة، فهذا يعني أن خلية أو أكثر قد تم تعبئتها. ومع ذلك، إذا أعادت أي من هذه الخصائص القيمة -1، فهذا يدل على عدم تعبئة أية خلايا في ورقة العمل المعطاة.

{{% alert color="primary" %}}

مجموعة الصفوف والأعمدة لديها فهرس يبدأ من الصفر، لذلك، الخلية عند الصف 0 والعمود 0 تعني أول خلية في ورقة العمل، وهي A1.

{{% /alert %}}

## **فحص الخلايا المهيأة الفارغة**

جميع الخلايا التي تحتوي على قيم يتم تهيئتها تلقائيًا. ومع ذلك، هناك احتمال أن تحتوي ورقة العمل على خلايا تحتوي فقط على تنسيق. في مثل هذه الحالة، ستعيد خاصية [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) أو [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) القيمة -1، مما يدل على غياب القيم المملوءة. ولكن لا يمكن اكتشاف الخلايا المهيأة بسبب تنسيق الخلية باستخدام هذا النهج. للتحقق مما إذا كانت ورقة العمل تحتوي على خلايا مهيأة فارغة، يُنصح باستخدام طريقة `MoveNext` على المُعدِر الذي تم الحصول عليه من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). إذا كانت طريقة `MoveNext` تُرجع **true**، فهذا يعني وجود خلية أو أكثر مهيأة في ورقة العمل المعطاة.

## **فحص الأشكال**

من الممكن أن لا تحتوي ورقة العمل المعطاة على خلايا مملوءة، ومع ذلك، قد تحتوي على أشكالObjects مثل أدوات التحكم والرسوم البيانية والصور، وغيرها. إذا أردنا التحقق مما إذا كانت ورقة العمل تحتوي على شكل معين، يمكننا فحص خاصية [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/). أي قيمة موجبة تشير إلى وجود شكل واحد أو أكثر في ورقة العمل.

## **نموذج برمجة**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
