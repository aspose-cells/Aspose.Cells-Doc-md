---
title: قراءة Cell القيم في مواضيع متعددة في وقت واحد
linktitle: خيوط متعددة
type: docs
weight: 1100
url: /ar/java/reading-cell-values-in-multiple-threads-simultaneously/
description: تعرف على كيفية قراءة قيم Cell في سلاسل رسائل متعددة بشكل متزامن مع واجهات برمجة التطبيقات Aspose.Cells for Java.
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

تعد الحاجة إلى قراءة قيم الخلايا في سلاسل رسائل متعددة في وقت واحد مطلبًا شائعًا. يشرح هذا المقال كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

##  **كيفية قراءة قيم Cell في مواضيع متعددة في وقت واحد مع Aspose.Cells for Java**

 لقراءة قيم الخلايا في أكثر من مؤشر ترابط واحد في وقت واحد، قم بتعيين[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)إلى *صحيح**. إذا لم تقم بذلك، فقد تحصل على قيم الخلايا الخاطئة. يرجى ملاحظة أن بعض الميزات، مثل تنسيق قيم الخلايا، غير مدعومة لسلاسل المحادثات المتعددة. لذا فإن MultiThreadReading يمكّنك فقط من الوصول إلى البيانات الأصلية للخلية فقط. في بيئة متعددة الخيوط، إذا حاولت الحصول على القيمة المنسقة للخلية، مثل Cell.getStringValue() للقيم الرقمية، فقد تحصل على نتيجة أو استثناء غير متوقع.

الكود التالي:

1. يقوم بإنشاء مصنف.
1. إضافة ورقة عمل.
1. يملأ ورقة العمل بقيم السلسلة.
1. ثم يقوم بعد ذلك بإنشاء خيطين يقرأان القيم من الخلايا العشوائية في نفس الوقت.
 إذا كانت القيم المقروءة صحيحة، فلن يحدث شيء. إذا كانت القيم المقروءة غير صحيحة، فسيتم عرض رسالة.

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

وبخلاف ذلك، يعمل البرنامج دون ظهور أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
