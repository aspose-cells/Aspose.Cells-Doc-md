---
title: عام API التغييرات في Aspose.Cells 8.2.2
type: docs
weight: 100
url: /ar/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.2.1 إلى 8.2.2 والتي قد تهم مطوري الوحدة / التطبيق.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة إصدار الخاصية لفئة BuiltInDocumentPropertyCollection**
تمت إضافة الإصدار الجديد من الخاصية إلى فئة BuiltInDocumentPropertyCollection للسماح للمطورين بالحصول على إصدار التطبيق أو تعيينه لجدول بيانات معين.

{{% alert color="primary" %}} 

 يرجى مراجعة المقالة التفصيلية على[احصل على نسخة من التطبيق الذي أنشأ جدول البيانات](/cells/ar/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **مخطط الملكية. تمت إضافة ورقة العمل**
قبل إصدار Aspose.Cells 8.2.2 ، لم يكن من الممكن استرداد مثيل ورقة العمل من كائن المخطط الذي يحتوي عليه. لقد ملأ Aspose.Cells 8.2.2 هذه الفجوة من خلال توفير خاصية Chart.Worksheet.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل[احصل على ورقة عمل الرسم البياني](/cells/ar/java/get-worksheet-of-the-chart/) للمزيد من المعلومات.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
