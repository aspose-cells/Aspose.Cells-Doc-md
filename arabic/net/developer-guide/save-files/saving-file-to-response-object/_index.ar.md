---
title: حفظ الملف في كائن الاستجابة
type: docs
weight: 50
url: /ar/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

تجعل Aspose.Cells من الممكن التلاعب بالملفات. يشرح هذا المقال الطرق المختلفة التي يمكن بواسطتها حفظ الملفات في كائن الاستجابة.

{{% /alert %}}

## **حفظ الملف في كائن الاستجابة**

من الممكن أيضًا إنشاء ملف بشكل ديناميكي وإرساله مباشرة إلى متصفح العميل. من أجل القيام بذلك، استخدم النسخة المطوَّرة خصيصًا للطريقة [**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5) التي تقبل المعاملات التالية:

- كائن ASP.NET [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8).
- اسم الملف.
- [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)، نوع إعلان المحتوى النوعي لملف الإخراج.
- [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)، نوع تنسيق الملف

تحدد تعداد [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) ما إذا كان الملف المرسل إلى المستعرض يوفر الخيار للفتح بذاته مباشرة في المستعرض أو في تطبيق مرتبط بامتداد .xls/.xlsx أو امتداد آخر.

يحتوي التعداد على أنواع الحفظ المحددة مسبقًا التالية:

|**النوع**|**الوصف**|
| :- | :- |
|المرفقات|يُرسل جدول البيانات إلى المستعرض ويُفتح في تطبيق كمرفق مرتبط بامتداد .xls/.xlsx أو امتدادات أخرى|
|مضمن|يُرسل المستند إلى المتصفح ويعرض خيارًا لحفظ جدول البيانات على القرص أو فتحه داخل المتصفح|

### **ملفات XLS**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **ملفات XLSX**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **ملفات PDF**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **ملاحظة**

نظرًا لكون الكائن "System.Web.HttpResponse" غير مدرج في .NET5 و .Netstandard
وبالتالي، هذه الوظيفة غير موجودة في إصدار Aspose.Cells .NET5 و .Netstandard. يمكنك الرجوع إلى الكود التالي لحفظ الملف في التدفق، ثم القيام بالعمليات على التدفق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

