---
title: قراءة قيم الخلية في خيوط متعددة بشكل متزامن
linktitle: الخيوط المتعددة
type: docs
weight: 1800
url: /ar/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: تعرف على كيفية قراءة قيم الخلايا في خيوط متعددة في نفس الوقت من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: قراءة قيم الخلايا في عدة خيوط في وقت واحد باستخدام Node.js عبر C++، Aspose.Cells C++ متعددة الخيوط، قراءة البيانات في خيوط متعددة
---

{{% alert color="primary" %}}

من الضروري قراءة قيم الخلية في خيوط متعددة بشكل متزامن ، وهو متطلب شائع. يشرح هذا المقال كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

لقياس قيم الخلايا في أكثر من خيط واحد في نفس الوقت، اضبط [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) على **true**. إذا لم تفعل ذلك، قد تحصل على قيم خلايا غير صحيحة.

الكود التالي:

1. ينشئ دفتر عمل.
1. إضافة ورقة عمل.
1. ملء ورقة العمل بقيم السلسلة.
1. ثم ينشئ خيطين يقرأان قيمًا بشكل متزامن من الخلايا العشوائية.
   إذا كانت القيم المقروءة صحيحة، لا يحدث شيء. إذا كانت القيم المقروءة غير صحيحة، يتم عرض رسالة.

إذا قمت بتعليق هذا السطر:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

سيتم عرض الرسالة التالية:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

وإلا، يعمل البرنامج بدون عرض أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
