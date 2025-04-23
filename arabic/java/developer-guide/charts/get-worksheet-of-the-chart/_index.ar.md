---
title: الحصول على ورقة البيانات للشارت
type: docs
weight: 80
url: /ar/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

في بعض الأحيان، قد ترغب في الوصول إلى ورقة عمل من مرجع شارت. توفر Aspose.Cells ال [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) المعني الذي يعيد مرجع الورقة التي تحتوي على الشارت.

{{% /alert %}}

## مثال

يوضح المثال التالي كيفية استخدام ال [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) المعني. يطبع الكود أولاً اسم الورقة، ثم يصل إلى الشارت الأول على الورقة. ثم يطبع اسم الورقة مرة أخرى باستخدام ال [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) المعني.

### كود Java للوصول إلى ورقة البيانات من الرسم البياني

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي

فيما يلي الناتج الناتج عن مثال الشفرة. كما تلاحظ، يقوم بطباعة نفس اسم ورقة البيانات في كلتا المرتين.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
