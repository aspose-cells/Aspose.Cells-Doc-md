---
title: قراءة Cell القيم في خيوط متعددة في نفس الوقت
linktitle: خيوط متعددة
type: docs
weight: 1100
url: /ar/java/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

تعد الحاجة إلى قراءة قيم الخلايا في خيوط متعددة في وقت واحد مطلبًا شائعًا. تشرح هذه المقالة كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

 لقراءة قيم الخلايا في أكثر من مؤشر ترابط واحد في نفس الوقت ، قم بتعيين[**Worksheet.getCells (). setMultiThreadReading ()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) إلى**حقيقي**إذا لم تقم بذلك ، فقد تحصل على قيم خلية خاطئة. يرجى ملاحظة أن بعض الميزات مثل تنسيق قيم الخلايا غير مدعومة لمؤشرات الترابط المتعددة. لذا فإن MultiThreadReading تمكنك فقط من الوصول إلى البيانات الأصلية للخلية فقط. في بيئة مؤشرات الترابط المتعددة ، إذا حاولت الحصول على القيمة المنسقة للخلية ، مثل Cell.getStringValue () للقيم الرقمية ، فقد تحصل على نتيجة غير متوقعة أو استثناء.

الكود التالي:

1. يقوم بإنشاء مصنف.
1. يضيف ورقة عمل.
1. يملأ ورقة العمل بقيم السلسلة.
1. ثم يقوم بإنشاء خيطين يقرآن القيم من الخلايا العشوائية في نفس الوقت.
 إذا كانت القيم المقروءة صحيحة ، فلن يحدث شيء. إذا كانت القيم المقروءة غير صحيحة ، فسيتم عرض رسالة.

إذا قمت بالتعليق على هذا السطر:

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

ثم يتم عرض الرسالة التالية:

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

خلاف ذلك ، يتم تشغيل البرنامج دون إظهار أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
