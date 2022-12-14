---
title: عام API التغييرات في Aspose.Cells 8.2.2
type: docs
weight: 90
url: /ar/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.2.1 إلى 8.2.2 والتي قد تهم مطوري الوحدة / التطبيق.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة الخاصية BuiltInDocumentPropertyCollection.Version**
تمت إضافة الإصدار الجديد من الخاصية إلى فئة BuiltInDocumentPropertyCollection للسماح للمطورين باسترداد إصدار التطبيق الذي أنشأ جدول بيانات معين.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل[احصل على نسخة من التطبيق الذي أنشأ جدول البيانات](/cells/ar/net/get-the-version-number-of-the-application-that-created-the-excel-document/) للمزيد من المعلومات.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **مخطط الملكية. تمت إضافة ورقة العمل**
قبل إصدار Aspose.Cells 8.2.2 ، لم يكن من الممكن استرداد مثيل ورقة العمل من كائن المخطط الذي يحمله. لقد ملأ Aspose.Cells 8.2.2 هذه الفجوة من خلال توفير خاصية Chart.Worksheet.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل[احصل على ورقة عمل الرسم البياني](/cells/ar/net/get-worksheet-of-the-chart/) للمزيد من المعلومات.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
