---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.2.2
type: docs
weight: 100
url: /ar/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة تطبيقات Aspose.Cells من الإصدار 8.2.1 إلى 8.2.2 التي قد تكون من المصلحة لمطوري الوحدات / التطبيقات.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية الإصدار لفئة BuiltInDocumentPropertyCollection**
تمت إضافة الخاصية الجديدة الإصدار إلى فئة BuiltInDocumentPropertyCollection لتمكين المطورين من الحصول على إصدار التطبيق أو تعيينه لجدول بيانات معين.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل على [الحصول على إصدار التطبيق الذي أنشأ جدول البيانات](/cells/ar/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **تمت إضافة خاصية Chart.Worksheet**
قبل إصدار Aspose.Cells 8.2.2، لم يكن من الممكن استعادة مثيل لورق العمل من كائن الرسم البياني الذي يحتوي عليه. قام Aspose.Cells 8.2.2 بسد هذه الثغرة من خلال توفير خاصية Chart.Worksheet.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل [الحصول على ورقة العمل من الرسم البياني](/cells/ar/java/get-worksheet-of-the-chart/) لمزيد من المعلومات.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
