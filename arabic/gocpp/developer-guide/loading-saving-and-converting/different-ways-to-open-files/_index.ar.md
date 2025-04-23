---
title: طرق مختلفة لفتح الملفات
linktitle: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

مع Aspose.Cells، يمكنك فتح ملفات، على سبيل المثال، لاسترجاع البيانات أو لاستخدام قالب تصميم لتسريع عملية التطوير. تدعم Aspose.Cells فتح مجموعة واسعة من الملفات، مثل جداول بيانات Microsoft Excel (XLS، XLSX، XLSM، XLSB)، CSV، أو ملفات TabDelimited.

{{% /alert %}}

## **فتح ملف عبر مسار**

يمكن للمطورين فتح ملف Microsoft Excel باستخدام مساره على الكمبيوتر المحلي عن طريق تحديده في منشئ فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). مرر المسار كسلسلة نصية في المنشئ. ستقوم Aspose.Cells بكشف نوع تنسيق الملف تلقائيًا.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **فتح ملف باستخدام تدفق البيانات (Stream)**

من الممكن أيضاً فتح ملف Excel كتيار. للقيام بذلك، استخدم الإصدار المحدث من المُنشئ الذي يأخذ كائن *Stream* الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
