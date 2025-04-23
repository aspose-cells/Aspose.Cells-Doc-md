---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.2.2
type: docs
weight: 90
url: /ar/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة تطبيقات Aspose.Cells من الإصدار 8.2.1 إلى 8.2.2 التي قد تكون من المصلحة لمطوري الوحدات / التطبيقات.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.Version**
تمت إضافة الخاصية الجديدة Version إلى فئة BuiltInDocumentPropertyCollection للسماح للمطورين بالحصول على إصدار التطبيق الذي أنشأ جدول بيانات معين.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل [الحصول على إصدار التطبيق الذي أنشأ جدول البيانات](/cells/ar/net/get-the-version-number-of-the-application-that-created-the-excel-document/) لمزيد من المعلومات.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **تمت إضافة خاصية Chart.Worksheet**
قبل إصدار Aspose.Cells 8.2.2، كان من غير الممكن استرداد مثيل الورقة من كائن الرسم البياني الذي يحتفظ به. لقد قام Aspose.Cells 8.2.2 بسد هذه الفجوة من خلال توفير خاصية Chart.Worksheet.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل [الحصول على ورقة البيانات الخاصة بالرسم البياني](/cells/ar/net/get-worksheet-of-the-chart/) لمزيد من المعلومات.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
