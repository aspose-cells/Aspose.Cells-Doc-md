---
title: حفظ الملف إلى كائن الاستجابة
type: docs
weight: 50
url: /ar/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells يجعل من الممكن معالجة الملفات. تشرح هذه المقالة الطرق المختلفة التي يمكن بها حفظ الملفات في كائن استجابة.

{{% /alert %}}

## **حفظ الملف إلى كائن الاستجابة**

 من الممكن أيضًا إنشاء ملف ديناميكيًا وإرساله مباشرة إلى متصفح العميل. للقيام بذلك ، استخدم إصدارًا خاصًا محملاً فوق طاقته من**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**الطريقة التي تقبل المعلمات التالية:

-  ASP.NET**[HttpResponse] (https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse؟view=netframework-4.8)**هدف.
- اسم الملف.
- **[ContentDisposition] (https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**، نوع المحتوى - الترتيب لملف الإخراج.
- **[SaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**، نوع تنسيق الملف

 ال**[ContentDisposition] (https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**يحدد التعداد ما إذا كان الملف الذي يتم إرساله إلى المتصفح يوفر خيار الفتح بنفسه مباشرة في المستعرض أو في تطبيق مرتبط بـ .xls / .xlsx أو امتداد آخر.

يحتوي التعداد على أنواع الحفظ المحددة مسبقًا التالية:

|**يكتب**|**وصف**|
|:- |:- |
|المرفق|يرسل جدول البيانات إلى المتصفح ويفتح في تطبيق ما كمرفق مرتبط بـ .xls / .xlsx أو ملحقات أخرى|
|في النسق|يرسل المستند إلى المتصفح ويقدم خيارًا لحفظ جدول البيانات على القرص أو فتحه داخل المتصفح|

### **ملفات XLS**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **ملفات XLSX**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **ملفات PDF**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **ملحوظة**

نظرًا للكائن "System.Web.HttpResponse" لم يتم تضمينه في .NET5 و .Netstandard ،
لذلك لا توجد هذه الوظيفة في Aspose.Cells .NET5 والإصدار القياسي ، يمكنك الرجوع إلى الكود التالي لحفظ الملف في الدفق ، ثم إجراء العملية على الدفق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

