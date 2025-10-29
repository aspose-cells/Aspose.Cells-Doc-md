---
title: حفظ الملف في كائن الاستجابة مع Golang عبر C++
linktitle: حفظ الملف في كائن الاستجابة
type: docs
weight: 50
url: /ar/go-cpp/saving-file-to-response-object/
description: تعلم كيفية حفظ الملفات بشكل ديناميكي وإرسالها مباشرة إلى متصفح العميل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تجعل Aspose.Cells من الممكن التلاعب بالملفات. يشرح هذا المقال الطرق المختلفة التي يمكن بواسطتها حفظ الملفات في كائن الاستجابة.

{{% /alert %}}

## **حفظ الملف في كائن الاستجابة**

من الممكن أيضًا إنشاء ملف بشكل ديناميكي وإرساله مباشرة إلى متصفح العميل. من أجل القيام بذلك، استخدم النسخة المطوَّرة خصيصًا للطريقة [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) التي تقبل المعاملات التالية:

- كائن **HttpResponse**.
- اسم الملف.
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/)، نوع إعلان المحتوى النوعي لملف الإخراج.
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/)، نوع تنسيق الملف.

تحدد تعداد [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) ما إذا كان الملف المرسل إلى المستعرض يوفر الخيار للفتح بذاته مباشرة في المستعرض أو في تطبيق مرتبط بامتداد .xls/.xlsx أو امتداد آخر.

يحتوي التعداد على أنواع الحفظ المحددة مسبقًا التالية:

|**النوع**|**الوصف**|
| :- | :- |
|المرفقات|يُرسل جدول البيانات إلى المستعرض ويُفتح في تطبيق كمرفق مرتبط بامتداد .xls/.xlsx أو امتدادات أخرى|
|مضمن|يُرسل المستند إلى المتصفح ويعرض خيارًا لحفظ جدول البيانات على القرص أو فتحه داخل المتصفح|

### **ملفات XLS**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **ملفات XLSX**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **ملفات PDF**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **ملاحظة**

نظرًا لكون الكائن "System.Web.HttpResponse" غير مدرج في .NET5 و .Netstandard
وبالتالي، هذه الوظيفة غير موجودة في إصدار Aspose.Cells .NET5 و .Netstandard. يمكنك الرجوع إلى الكود التالي لحفظ الملف في التدفق، ثم القيام بالعمليات على التدفق.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
