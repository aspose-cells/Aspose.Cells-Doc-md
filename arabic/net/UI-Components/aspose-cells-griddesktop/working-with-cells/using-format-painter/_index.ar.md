---
title: باستخدام نسخ التنسيق
type: docs
weight: 80
url: /ar/net/using-format-painter/
---
{{% alert color="primary" %}} 

رسام التنسيق هو ميزة MS Excel التي تم تكييفها في Aspose.Cells.GridDesktop. إنها ميزة لطيفة للغاية. بالنسبة لأولئك الأشخاص الذين لم يستخدموا هذه الميزة بعد ، يسمح رسام التنسيق للمستخدمين بتطبيق إعدادات التنسيق لأي خلية مركزة على خلية أخرى. تنفيذ هذه الميزة بسيط للغاية. في هذا الموضوع ، سوف نغطي ذلك أيضًا.

{{% /alert %}} 
## **باستخدام نسخ التنسيق**
 ميزة**شكل الرسام** يتطلب من المستخدمين تحديد خلية تريد تطبيق إعدادات التنسيق الخاصة بها على خلايا أخرى ثم الاتصال**StartFormatPainter** طريقة**الشبكة**. يوجد وضعان لرسام التنسيق على النحو التالي:

- **باستخدام نسخ التنسيق مرة واحدة**
- **استخدام نسخ التنسيق دائمًا**
### **باستخدام نسخ التنسيق مرة واحدة**
 إذا أراد المطورون استخدام ميزة رسام التنسيق لمرة واحدة فقط لتطبيق إعدادات التنسيق لخلية مركزة على خلية واحدة ، فيمكنهم القيام بذلك عن طريق الاتصال**StartFormatPainter** طريقة وتمرير أ**خاطئة** قيمة لها. هذه**خاطئة** القيمة ستمنع رسام التنسيق من الرسم إلى الأبد.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **استخدام نسخ التنسيق دائمًا**
يعد استخدام رسام التنسيق دائمًا ميزة مفيدة عندما نحتاج إلى تطبيق إعدادات التنسيق على أكثر من خلية واحدة. يمكن للمطورين تحقيق هذه الميزة بمجرد الاتصال**StartFormatPainter** طريقة وتمرير أ**حقيقي** قيمة لها.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


 هذا النوع من رسام التنسيق يستمر في الرسم إلى الأبد ما لم نوقفه. لذلك ، لإيقاف رسام التنسيق من الرسم دائمًا ، يمكننا ببساطة الاتصال**EndFormatPainter** طريقة**الشبكة**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
