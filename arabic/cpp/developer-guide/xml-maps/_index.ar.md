---
title: استيراد XML إلى ملف Excel باستخدام C++
linktitle: خرائط XML
type: docs
weight: 210
url: /ar/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: استيراد البيانات من ملف بيانات XML إلى Microsoft Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells إمكانية استيراد خريطة XML داخل ملف العمل باستخدام طريقة [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). يمكنك استيراد خريطة XML باستخدام Microsoft Excel وفقًا للخطوات التالية:

- حدد علامة التبويب **المطور**.
- انقر فوق **استيراد** في القسم XML واتبع الخطوات المطلوبة.

ستحتاج إلى تقديم بياناتك XML لإكمال الاستيراد. إليك [بيانات XML عينية](5115037.txt) يمكنك استخدامها للفحص.

{{% /alert %}}

## **استيراد خريطة XML باستخدام Microsoft Excel**

تُظهر اللقطة الشاشة التالية كيفية استيراد خريطة XML باستخدام Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **استيراد خريطة XML باستخدام Aspose.Cells**

يوضح المثال التالي كيف تستخدم طريقة [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). يقوم بتوليد ملف Excel الناتج كما هو مبين في لقطات الشاشة هذه.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

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

    // Create a workbook
    Workbook workbook;

    // URL that contains your XML data for mapping
    U16String XML(u"http://www.aspose.com/docs/download/attachments/434475650/sampleXML.txt");

    // Import your XML Map data starting from cell A1
    workbook.ImportXml(XML, u"Sheet1", 0, 0);

    // Save workbook
    U16String outputPath = outDir + u"output_out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully with imported XML data!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [إضافة خريطة XML داخل الكتيب باستخدام طريقة XmlMapCollection.Add](/cells/ar/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [تصدير البيانات XML المرتبطة بخريطة XML داخل الكتيب](/cells/ar/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [العثور على اسم عنصر الجذر في خريطة XML](/cells/ar/cpp/find-the-root-element-name-of-xml-map/)
- [ربط الخلايا بعناصر خريطة XML](/cells/ar/cpp/link-cells-to-xml-map-elements/)
