---
title: قراءة Cell القيم في مواضيع متعددة في وقت واحد
linktitle: خيوط متعددة
type: docs
weight: 1800
url: /ar/net/reading-cell-values-in-multiple-threads-simultaneously/
description: تعرف على كيفية قراءة قيم Cell في مؤشرات الترابط المتعددة في وقت واحد من خلال Aspose.Cells for .NET API.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
---
{{% alert color="primary" %}}

تعد الحاجة إلى قراءة قيم الخلايا في سلاسل رسائل متعددة في وقت واحد مطلبًا شائعًا. يشرح هذا المقال كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

 لقراءة قيم الخلايا في أكثر من مؤشر ترابط واحد في وقت واحد، قم بتعيين[**ورقة عمل.Cells.قراءة متعددة الخيوط**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)إلى *صحيح**. إذا لم تقم بذلك، فقد تحصل على قيم الخلايا الخاطئة.

الكود التالي:

1. يقوم بإنشاء مصنف.
1. إضافة ورقة عمل.
1. يملأ ورقة العمل بقيم السلسلة.
1. ثم يقوم بعد ذلك بإنشاء خيطين يقرأان القيم من الخلايا العشوائية في نفس الوقت.
 إذا كانت القيم المقروءة صحيحة، فلن يحدث شيء. إذا كانت القيم المقروءة غير صحيحة، فسيتم عرض رسالة.

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

وبخلاف ذلك، يعمل البرنامج دون ظهور أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
