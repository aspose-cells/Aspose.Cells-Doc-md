---
title: إدارة دفتر العمل مع Golang عبر C++
linktitle: دفتر العمل
type: docs
weight: 60
url: /ar/go-cpp/managing-workbooks-and-worksheets/
description: تعلم كيفية إدارة المصنف عبر واجهات برمجة التطبيقات Aspose.Cells for C++.
keywords: كيفية إدارة المصنف باستخدام C++، إدارة المصنف وورقة العمل باستخدام C++، تشغيل المصنف وورقة العمل في C++.
---

{{% alert color="primary" %}}

توفر واجهة برمجة التطبيقات Aspose.Cells for C++ أدوات قوية ومرنة لإدارة المصنفات وورقة العمل. يشرح هذا القسم كيفية إنشاء وفتح والتعامل مع المصنفات وبرمجياً.

{{% /alert %}}

## **إنشاء مصنف جديد**
 لإنشاء مصنف جديد:

1. أنشئ نسخة من فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).
2. أضف أوراق عمل إلى دفتر العمل باستخدام فئة [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. احفظ دفتر العمل باستخدام دالة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **فتح مصنف موجود**
لفتح مصنف موجود:

1. أنشئ نسخة من فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) ومرر مسار الملف إلى المنشئ.
2. الوصول إلى أوراق العمل باستخدام فئة [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. قم بتعديل المصنف حسب الحاجة.
4. احفظ دفتر العمل باستخدام دالة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **إدارة أوراق العمل**
توفر واجهة برمجة التطبيقات Aspose.Cells for C++ مجموعة واسعة من الأساليب لإدارة أوراق العمل، بما في ذلك الإضافة والحذف وإعادة التسمية.

### **إضافة ورقة عمل**
لإضافة ورقة عمل جديدة:

1. الوصول إلى فئة [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) من دفتر العمل.
2. استخدم الدالة [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_sheettype/) لإضافة ورقة عمل جديدة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **إزالة ورقة العمل**
لإزالة ورقة عمل:

1. الوصول إلى فئة [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) من دفتر العمل.
2. استخدم الدالة [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat_string/) لإزالة ورقة عمل عبر الفهرس.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **إعادة تسمية ورقة العمل**
لإعادة تسمية ورقة عمل:

1. الوصول إلى فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) من دفتر العمل.
2. استخدم الدالة [SetName](https://reference.aspose.com/cells/go-cpp/worksheet/setname/) لإعادة تسمية ورقة العمل.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **الاستنتاج**
Aspose.Cells for C++ توفر مجموعة أدوات شاملة لإدارة ملفات العمل وورقات العمل. سواء كنت بحاجة إلى إنشاء ملف عمل جديد، فتح ملف موجود، أو تعديل أوراق العمل، جعلت Aspose.Cells العمل مع ملفات إكسل سهلاً برمجياً.
