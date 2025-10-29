---
title: استخدام أجزاء XML مخصصة في Aspose.Cells باستخدام C++
linktitle: استخدام أجزاء XML مخصصة
type: docs
weight: 390
url: /ar/cpp/use-custom-xml-parts-in-aspose-cells/
description: تعرّف على كيفية استخدام أجزاء XML مخصصة في ملفات إكسل برمجياً باستخدام Aspose.Cells مع C++.
---

## استخدام أجزاء XML المخصصة في Aspose.Cells

أجزاء XML المخصصة هي البيانات XML المخزنة بواسطة تطبيقات مختلفة مثل SharePoint داخل ملف إكسل. يتم استهلاك هذه البيانات بواسطة تطبيقات مختلفة تتطلبها. لا يستخدم Microsoft Excel هذه البيانات، لذلك لا يوجد واجهة رسومية لإضافتها. يمكنك عرض هذه البيانات بتغيير امتداد **.xlsx** إلى **.zip** ثم فتحه باستخدام **WinZip**. يمكنك أيضًا فتح ملف ZIP باستخدام أي أداة ضغط خارجية لنظام Windows مثل WinRAR أو WinZip. البيانات موجودة داخل مجلد **customXml**.

يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells عبر طريقة [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/).

يستخدم الكود النموذجي التالي طريقة [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) لإضافة **Book Catalog XML**، واسمه **BookStore**. يظهر الصورة التالية نتيجة هذا الكود. كما ترى، تم إضافة XML فهرس الكتب داخل عقدة BookStore، وهو اسم الخاصية تلك.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## كود C++ لاستخدام أجزاء XML مخصصة

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

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## مقال ذو صلة

- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند](/cells/ar/cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="cpp" >}}
