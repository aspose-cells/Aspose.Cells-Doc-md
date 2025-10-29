---
title: إدارة المصنف باستخدام C++
linktitle: دفتر العمل
type: docs
weight: 60
url: /ar/cpp/managing-workbooks-and-worksheets/
description: تعلم كيفية إدارة المصنف عبر واجهات برمجة التطبيقات Aspose.Cells for C++.
keywords: كيفية إدارة المصنف باستخدام C++، إدارة المصنف وورقة العمل باستخدام C++، تشغيل المصنف وورقة العمل في C++.
---

{{% alert color="primary" %}}

توفر واجهة برمجة التطبيقات Aspose.Cells for C++ أدوات قوية ومرنة لإدارة المصنفات وورقة العمل. يشرح هذا القسم كيفية إنشاء وفتح والتعامل مع المصنفات وبرمجياً.

{{% /alert %}}

## **إنشاء مصنف جديد**
 لإنشاء مصنف جديد:

1. أنشئ نسخة من فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
2. أضف أوراق العمل إلى المصنف باستخدام فئة [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)
3. احفظ المصنف باستخدام طريقة [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **فتح مصنف موجود**
لفتح مصنف موجود:

1. أنشئ مثيل من فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ومرر مسار الملف إلى المُنشئ.
2. الوصول إلى أوراق العمل باستخدام فئة [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)
3. قم بتعديل المصنف حسب الحاجة.
4. احفظ المصنف باستخدام طريقة [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **إدارة أوراق العمل**
توفر واجهة برمجة التطبيقات Aspose.Cells for C++ مجموعة واسعة من الأساليب لإدارة أوراق العمل، بما في ذلك الإضافة والحذف وإعادة التسمية.

### **إضافة ورقة عمل**
لإضافة ورقة عمل جديدة:

1. قم بالوصول إلى فئة [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) من ملف العمل.
2. استخدم أسلوب [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) لإضافة ورقة عمل جديدة.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **إزالة ورقة العمل**
لإزالة ورقة عمل:

1. قم بالوصول إلى فئة [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) من ملف العمل.
2. استخدم أسلوب [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) لإزالة ورقة عمل بواسطة الفهرس.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **إعادة تسمية ورقة العمل**
لإعادة تسمية ورقة عمل:

1. قم بالوصول إلى فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) من ملف العمل.
2. استخدم أسلوب [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) لإعادة تسمية ورقة العمل.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **الاستنتاج**
Aspose.Cells for C++ توفر مجموعة أدوات شاملة لإدارة ملفات العمل وورقات العمل. سواء كنت بحاجة إلى إنشاء ملف عمل جديد، فتح ملف موجود، أو تعديل أوراق العمل، جعلت Aspose.Cells العمل مع ملفات إكسل سهلاً برمجياً.
{{< app/cells/assistant language="cpp" >}}
