---
title: إدارة الأوراق العمل
type: docs
weight: 20
url: /ar/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

يمكن للمطورين إنشاء وإدارة صفحات العمل بشكل سهل في ملفات Microsoft Excel برمجياً باستخدام واجهة برمجة التطبيقات المرنة Aspose.Cells. يصف هذا الموضوع النهج لإضافة وإزالة صفحات العمل في ملفات Microsoft Excel.

{{% /alert %}}

توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في الملف.

تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة واسعة من الطرق لإدارة أوراق العمل.

## **إضافة ورقات العمل إلى ملف Excel جديد**

لإنشاء ملف Excel جديد برمجياً:

1. أنشئ كائن من فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).
1. استدعِ طريقة [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) من مجموعة [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/). يُضاف ورقة عمل فارغة تلقائيًا إلى ملف Excel ويمكن الإشارة إليها عن طريق تمرير فهرس الورقة الجديدة إلى مجموعة [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
1. الحصول على مرجع ورقة العمل.
1. القيام بالعمل على أوراق العمل.
1. احفظ ملف Excel الجديد مع الأوراق الجديدة عن طريق استدعاء طريقة [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) من فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **الوصول إلى الأوراق العمل باستخدام فهرس الورقة**

يوضح الكود المصدري التالي كيفية الوصول أو الحصول على أي ورقة عمل عن طريق تحديد فهرستها.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **إزالة الأوراق العمل باستخدام فهرس الورقة**

حذف أوراق العمل بإسمه يعمل بشكل جيد عندما يكون اسم ورقة العمل معروفًا. إذا لم تكن تعرف اسم ورقة العمل، استخدم نسخة محمّلة من طريقة [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) التي تأخذ فهرس الورقة بدلًا من اسمها.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
