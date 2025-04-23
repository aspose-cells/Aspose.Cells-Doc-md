---
title: قراءة قيم الخلية في خيوط متعددة بشكل متزامن
linktitle: الخيوط المتعددة
type: docs
weight: 1100
url: /ar/java/reading-cell-values-in-multiple-threads-simultaneously/
description: تعلم كيفية قراءة قيم الخلية في عدة خيوط بشكل متزامن بواسطة واجهات برمجة التطبيقات Aspose.Cells for Java.
keywords: Java قراءة قيم الخلية في عدة خيوط بشكل متزامن، الخيوط المتعددة لـ Aspose.Cells for Java واجهات برمجة التطبيقات.
---

{{% alert color="primary" %}}

من الضروري قراءة قيم الخلية في خيوط متعددة بشكل متزامن ، وهو متطلب شائع. يشرح هذا المقال كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

## **كيفية قراءة قيم الخلية في عدة خيوط بشكل متزامن مع Aspose.Cells for Java**

لقراءة قيم الخلية في أكثر من خيط بشكل متزامن، قم بضبط [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) إلى **true**. إذا لم تفعل ذلك، قد تحصل على قيم الخلية الخاطئة. يرجى ملاحظة، بعض الميزات مثل تنسيق قيم الخلية لا يتم دعمها لعمليات الخيوط المتعددة. لذلك MultiThreadReading يتمكنك من الوصول إلى البيانات الأصلية للخلية فقط. في بيئة الخيوط المتعددة إذا حاولت الحصول على قيمة المنسقة للخلية، مثل باستخدام Cell.getStringValue() للقيم الرقمية، قد تحصل على نتيجة غير متوقعة أو استثناء.

الكود التالي:

1. ينشئ دفتر عمل.
1. إضافة ورقة عمل.
1. ملء ورقة العمل بقيم السلسلة.
1. ثم ينشئ خيطين يقرأان قيمًا بشكل متزامن من الخلايا العشوائية.
   إذا كانت القيم المقروءة صحيحة، لا يحدث شيء. إذا كانت القيم المقروءة غير صحيحة، يتم عرض رسالة.

إذا قمت بتعليق هذا السطر:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

سيتم عرض الرسالة التالية:

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

وإلا، يعمل البرنامج بدون عرض أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
{{< app/cells/assistant language="java" >}}
