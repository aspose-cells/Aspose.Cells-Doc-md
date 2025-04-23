---
title: إدارة الصور باستخدام C++
linktitle: إدارة الصور
type: docs
weight: 10
url: /ar/cpp/managing-pictures/
description: أضف، ضع، وادير الصور في أوراق العمل باستخدام API Aspose.Cells for C++.
---

يسمح Aspose.Cells للمطورين بإضافة الصور إلى جداول البيانات في وقت التشغيل. علاوة على ذلك، يمكن التحكم في تحديد موضع هذه الصور في وقت التشغيل، والأمر الذي يتم مناقشته بتفصيل أكثر في الأقسام القادمة.

يشرح هذا المقال كيفية إضافة الصور، وكيفية إدراج صورة تعرض محتوى خلايا معينة.

## **إضافة الصور**

إضافة الصور إلى جدول بيانات سهل للغاية. يستغرق الأمر سوى بضعة أسطر من الكود:
 ببساطة استدعِ طريقة [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) من [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) (مغلقة في كائن [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). تتطلب الطريقة [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) المعلمات التالية:

- **فهرس الصف الأعلى الأيسر**، فهرس الصف الأعلى.
- **فهرس العمود الأعلى الأيسر**، فهرس العمود الأعلى.
- **اسم ملف الصورة**، اسم ملف الصورة، مع المسار الكامل.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحديد مواقع الصور**

هناك طريقتان ممكنتان للتحكم في تحديد موقع الصور باستخدام Aspose.Cells:

- تحديد موقع نسبي: تعريف موقع نسبي لارتفاع الصف والعرض.
- التمركز المطلق: تحديد الموقع الدقيق على الصفحة حيث سيتم إدراج الصورة، على سبيل المثال، 40 بكسل إلى اليسار و20 بكسل أسفل حافة الخلية.

### **التحديد النسبي**

يمكن للمطورين تحديد موضع الصور نسبة إلى ارتفاع الصف وعرض العمود باستخدام الخاصيتين [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) و [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) من كائن [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). يمكن الحصول على كائن [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) من [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) من خلال تمرير فهرس الصورة الخاص به. يضع هذا المثال صورة في خلية F6.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **التحديد المطلق**

يمكن للمطورين أيضًا تحديد مواقع الصور بشكل مطلق باستخدام الخصائص [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) و [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) لكائن [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). يضع هذا المثال صورة في الخلية F6، على بعد 60 بكسل من اليسار و10 بكسل من أعلى الخلية.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إدراج صورة بناءً على مرجع الخلية**

يتيح Aspose.Cells عرض محتويات خلية ورق العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي ترغب في عرضها. نظرًا لأن الخلية، أو نطاق الخلية، مرتبط بالكائن الرسومي، فإن التغييرات التي تقوم بها في البيانات في تلك الخلية أو نطاق الخلية ستظهر تلقائيًا في الكائن الرسومي.

أضف صورة إلى ورقة العمل عن طريق استدعاء طريقة [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) من [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (مغلقة في كائن [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). تحديد نطاق الخلايا باستخدام الخاصية [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) في كائن [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [إضافة مجموعة رموز مشروطة مع نص الخلية](/cells/ar/cpp/add-conditional-icons-set-with-the-cell-text/)
- [إدراج صورة مرتبطة من عنوان ويب](/cells/ar/cpp/insert-a-linked-picture-from-web-address/)
- [إدراج صورة بناءً على مرجع الخلية](/cells/ar/cpp/insert-a-picture-based-on-cell-reference/)
- [تحميل صورة ويب من عنوان URL إلى ورقة عمل Excel](/cells/ar/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
