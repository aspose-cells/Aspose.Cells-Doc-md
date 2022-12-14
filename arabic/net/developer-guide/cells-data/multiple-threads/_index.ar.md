---
title: قراءة Cell القيم في خيوط متعددة في نفس الوقت
linktitle: خيوط متعددة
type: docs
weight: 1800
url: /ar/net/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

تعد الحاجة إلى قراءة قيم الخلايا في خيوط متعددة في وقت واحد مطلبًا شائعًا. تشرح هذه المقالة كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

 لقراءة قيم الخلايا في أكثر من مؤشر ترابط واحد في نفس الوقت ، قم بتعيين[**ورقة عمل Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) إلى**حقيقي**. إذا لم تقم بذلك ، فقد تحصل على قيم خلية خاطئة.

الكود التالي:

1. يقوم بإنشاء مصنف.
1. يضيف ورقة عمل.
1. يملأ ورقة العمل بقيم السلسلة.
1. ثم يقوم بإنشاء خيطين يقرآن القيم من الخلايا العشوائية في نفس الوقت.
 إذا كانت القيم المقروءة صحيحة ، فلن يحدث شيء. إذا كانت القيم المقروءة غير صحيحة ، فسيتم عرض رسالة.

إذا قمت بالتعليق على هذا السطر:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

ثم يتم عرض الرسالة التالية:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

خلاف ذلك ، يتم تشغيل البرنامج دون إظهار أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
