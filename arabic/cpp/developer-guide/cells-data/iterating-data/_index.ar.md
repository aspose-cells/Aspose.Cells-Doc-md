---
title: كيفية وأين تستخدم العدادات مع C++
linktitle: تكرار البيانات
type: docs
weight: 55
url: /ar/cpp/how-and-where-to-use-enumerators/
description: تعلم كيفية ومكان استخدام العدادات من خلال واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: كيفية استخدام المعدلات الإحصائية، معدل الخلايا، معدل الصفوف، معدل الأعمدة
---

{{% alert color="primary" %}}

المُععد هو كائن يوفر القدرة على التجول في حاوية أو مجموعة. يمكن استخدام العدادات لقراءة البيانات في المجموعة، لكنها لا يمكن استخدامها لتعديل المجموعة الأساسية، في حين أن IEnumerable هو واجهة تعرف طريقة واحدة GetEnumerator التي تُرجع واجهة IEnumerator، مما يسمح بالوصول للقراءة فقط إلى مجموعة.

توفر واجهات برمجة تطبيقات Aspose.Cells مجموعة من المعدلات الإحصائية، ومع ذلك، يناقش هذا المقال بشكل رئيسي الثلاثة أنواع المذكورة أدناه.

1. معدل الخلايا
1. معدل الصفوف
1. معدل الأعمدة

{{% /alert %}}

## **كيفية استخدام المعدلات الإحصائية**

### **معدل الخلايا**

هناك طرق مختلفة للوصول إلى معدل الخلايا، ويمكن للشخص استخدام أيًا من هذه الطرق استنادًا إلى متطلبات التطبيق. هنا الطرق التي تُرجع معدل الخلايا.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getenumerator/)

تعود الطرق المذكورة أعلاه جميعًا بمُحدِّد العناصر الذي يسمح بجَولة جمعية الخلايا التي تم تهيئتها.

{{% alert color="primary" %}}

أثناء جولة الخلايا، يجب ألا يتم تعديل المجموعة (العمليات التي ستؤدي إلى إنشاء خلية جديدة أو حذف خلية موجودة). وإلا فإن المُحدِّد قد لا يكون قادرًا على جولة جميع الخلايا بشكل صحيح (قد يكون بعض العناصر قد تجولت بشكل متكرر أو تم تخطيها).

{{% /alert %}}

يُظهر المثال البرمجي التالي تنفيذ واجهة IEnumerator لمجموعة الخلايا.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator from Cells collection
    auto cellEnumerator = book.GetWorksheets().Get(0).GetCells().GetEnumerator();
    // Traverse cells in the collection
    while (cellEnumerator.MoveNext())
    {
        auto cell = cellEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Row
    auto rowEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().Get(0).GetEnumerator();
    // Traverse cells in the given row
    while (rowEnumerator.MoveNext())
    {
        auto cell = rowEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Range
    auto rangeEnumerator = book.GetWorksheets().Get(0).GetCells().CreateRange(u"A1:B10").GetEnumerator();
    // Traverse cells in the range
    while (rangeEnumerator.MoveNext())
    {
        auto cell = rangeEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **مُحدِّد الصفوف**

يمكن الوصول إلى عداد الصفوف أثناء استخدام طريقة [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/getenumerator/). يُظهر المثال التالي تنفيذ واجهة IEnumerator لـ [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator for RowCollection
    auto rowsEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().GetEnumerator();

    // Traverse rows in the collection
    while (rowsEnumerator.MoveNext())
    {
        auto row = rowsEnumerator.GetCurrent();
        std::cout << row.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **الحصول على الأعمدة**

يمكن الوصول إلى الأعمدة أثناء استخدام طريقة [**ColumnCollection.Get**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/get/). يُظهر المثال التالي تنفيذ طريقة Get لـ [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sample.xlsx");

    auto cells = book.GetWorksheets().Get(0).GetCells();
    auto columns = cells.GetColumns();

    for (int i = 0; i < columns.GetCount(); ++i)
    {
        auto col = columns.Get(i);
        std::cout << col.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **أين يجب استخدام المُحدِّدات**

لنناقش فوائد استخدام المُحدِّدات، دعونا نأخذ مثالًا واقعيًا.

**سيناريو**

متطلب التطبيق هو التجول عبر جميع الخلايا في [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) معين لقراءة قيمها. قد توجد عدة طرق لتحقيق هذا الهدف. تم توضيح بعض منها أدناه.

### **استخدام نطاق العرض**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Load a file in an instance of Workbook
    Workbook book(inputFilePath);

    // Get Cells collection of first worksheet
    Cells cells = book.GetWorksheets().Get(0).GetCells();

    // Get the MaxDisplayRange
    Range displayRange = cells.GetMaxDisplayRange();

    // Loop over all cells in the MaxDisplayRange
    for (int row = displayRange.GetFirstRow(); row < displayRange.GetRowCount(); row++)
    {
        for (int col = displayRange.GetFirstColumn(); col < displayRange.GetColumnCount(); col++)
        {
            // Read the Cell value
            std::cout << displayRange.Get(row, col).GetStringValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
}
```

### **استخدام MaxDataRow و MaxDataColumn**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get Cells collection of first worksheet
    auto cells2 = book.GetWorksheets().Get(0).GetCells();

    // Get maximum data row and column
    int maxDataRow = cells2.GetMaxDataRow();
    int maxDataColumn = cells2.GetMaxDataColumn();

    // Loop over all cells
    for (int row = 0; row <= maxDataRow; row++)
    {
        for (int col = 0; col <= maxDataColumn; col++)
        {
            // Read the Cell value
            auto currentCell = cells2.GetCell(row, col);
            if (!currentCell.IsNull())
            {
                cout << currentCell.GetStringValue().ToUtf8() << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

كما يمكنك أن تلاحظ أن كلتا الطريقتين المذكورتين تستخدمان تقريبًا نفس المنطق، وهو: الدوران حول جميع الخلايا في المجموعة لقراءة قيم الخلايا. قد يكون هذا مشكلة لعدة أسباب كما سيتم مناقشتها أدناه.

1. تتطلب واجهات برمجة التطبيقات مثل [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/)، [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)، [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/)، [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) و [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) وقتًا إضافيًا لجمع الإحصائيات المقابلة. إذا كانت مصفوفة البيانات (صفوف × أعمدة) كبيرة، فإن استخدام هذه الواجهات يمكن أن يفرض عقبة على الأداء.
1. في معظم الحالات، لا تتم إنشاء جميع الخلايا في النطاق المعطى. في مثل هذه الحالات، فحص كل خلية في البيانات ليس فعَّالًا كمقارنة بفحص الخلايا المهيئة فقط.
1. الوصول إلى خلية في حلقة مثل Cells row، column سيؤدي إلى إنشاء جميع كائنات الخلايا في النطاق، مما قد يؤدي في النهاية إلى حدوث استثناء نفاد الذاكرة.

## **الاستنتاج**

بناءً على الحقائق المذكورة أعلاه، فإن السيناريوهات الممكنة التالية هي التي يجب استخدام المُحدِّدات فيها.

1. الوصول القراءة فقط لمجموعة الخلايا مطلوب، أي؛ المتطلب هو تفقّد الخلايا فقط.
1. يتعين عبور عدد كبير من الخلايا.
1. يجب عبور الخلايا/الصفوف/الأعمدة المهيأة فقط.
