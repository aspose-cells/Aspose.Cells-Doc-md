---
title: قراءة قيم الخلية في خيوط متعددة بشكل متزامن
linktitle: الخيوط المتعددة
type: docs
weight: 1800
url: /ar/net/reading-cell-values-in-multiple-threads-simultaneously/
description: تعلم كيفية قراءة قيم الخلية في خيوط متعددة بشكل متزامن من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: قراءة قيم الخلية في خيوط متعددة بشكل متزامن، Aspose.Cells C# خيوط متعددة، قراءة البيانات في خيوط متعددة
---

{{% alert color="primary" %}}

من الضروري قراءة قيم الخلية في خيوط متعددة بشكل متزامن ، وهو متطلب شائع. يشرح هذا المقال كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

لقراءة قيم الخلية في أكثر من خيط بشكل متزامن، ضبط [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) إلى **true**. إذا لم تفعل ذلك ، قد تحصل على قيم الخلية الخاطئة.

الكود التالي:

1. ينشئ دفتر عمل.
1. إضافة ورقة عمل.
1. ملء ورقة العمل بقيم السلسلة.
1. ثم ينشئ خيطين يقرأان قيمًا بشكل متزامن من الخلايا العشوائية.
   إذا كانت القيم المقروءة صحيحة، لا يحدث شيء. إذا كانت القيم المقروءة غير صحيحة، يتم عرض رسالة.

إذا قمت بتعليق هذا السطر:

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

سيتم عرض الرسالة التالية:

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

وإلا، يعمل البرنامج بدون عرض أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
