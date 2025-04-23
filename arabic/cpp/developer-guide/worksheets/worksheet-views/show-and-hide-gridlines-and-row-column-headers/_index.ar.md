---
title: عرض وإخفاء خطوط الشبكة وعناوين الصفوف والأعمدة باستخدام ++C
linktitle: إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود
type: docs
weight: 30
url: /ar/cpp/show-and-hide-gridlines-and-row-column-headers/
description: يوفر هذا المقال شفرة عينة لاستخدام API أو المكتبة C++ لإخفاء أو عرض خطوط الشبكة وعناوين الصفوف والأعمدة لورقة عمل إكسل برمجياً.
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إخفاء وعرض خطوط الشبكة لورقة العمل التي يكون ظهورها افتراضيًا. كما يوفر التحكم في رؤوس الصف والعمود لورقة العمل.

{{% /alert %}}

## **إظهار وإخفاء خطوط الشبكة**

تحتوي جميع ورقات العمل في Excel على خطوط شبكية افتراضيًا. تساعد في تحديد الخلايا بحيث يكون من السهل إدخال البيانات في خلايا معينة. تمكِّن الخطوط الشبكية من عرض ورقة العمل كمجموعة من الخلايا، حيث يمكن تحديد كل خلية بسهولة.

### **التحكم في رؤية خطوط الشبكة**

تقدم Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تتيح للمطورين الوصول إلى كل ورقة عمل في ملف إكسل. تمثل الورقة بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. للتحكم في ظهور خطوط الشبكة، استخدم خاصية فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/). [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) خاصية Boolean، مما يعني أنها يمكن أن تخزن فقط قيمة **true** أو **false**.

#### **جعل خطوط الشبكة مرئية**

اجعل خطوط الشبكة مرئية من خلال تعيين خاصية {5} في فئة {0} إلى **true**.

#### **إخفاء خطوط الشبكة**

اخفِ خطوط الشبكة من خلال تعيين خاصية {5} في فئة {0} إلى **false**.

يوضح المثال أدناه استخدام خاصية [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) عن طريق فتح ملف إكسل (book1.xls)، إخفاء خطوط الشبكة على الورقة الأولى، وحفظ الملف المعدل باسم output.xls.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إظهار وإخفاء رؤوس الصف والعمود**

جميع ورقات العمل في ملف Excel مكونة من خلايا مرتبة في صفوف وأعمدة. جميع الصفوف والأعمدة لها قيم فريدة يتم استخدامها لتحديدها وتحديد الخلايا الفردية. على سبيل المثال، يتم ترقيم الصفوف - 1، 2، 3، 4، الخ. - وترتيب الأعمدة ترتيبها أبجديًا - أ، ب، ج، د، الخ. تظهر قيم الصف والعمود في الرؤوس. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية هذه الرؤوس للصف والعمود.

### **التحكم في رؤية ورقات العمل**

تقدم Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تتيح للمطورين الوصول إلى كل ورقة عمل في ملف إكسل. تمثل الورقة بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. للتحكم في ظهور رؤوس الصفوف والأعمدة، استخدم خاصية فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) خاصية Boolean، مما يعني أنها يمكن أن تخزن فقط قيمة **true** أو **false**.

#### **جعل رؤوس الصف/العمود مرئية**

اجعل رؤوس الصفوف والأعمدة مرئية بتعيين خاصية {5} في فئة {0} إلى **true**.

#### **إخفاء رؤوس الصف/العمود**

اخفِ رؤوس الصفوف والأعمدة عن طريق تعيين خاصية [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) للفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) إلى **خطأ**.

يوضح المثال الكامل أدناه كيفية استخدام خاصية [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) عن طريق فتح ملف إكسل (book1.xls)، وإخفاء رؤوس الصفوف والأعمدة في الورقة الأولى، وحفظ الملف المعدل كـ output.xls.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طريقتي [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) و [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) من الفئة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) لجعل صفوف وأعمدة متعددة مرئية.

{{% /alert %}}
