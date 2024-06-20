---
title: استخدام فرشاة التنسيق
type: docs
weight: 80
url: /ar/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: يقدم هذا المقال فرشاة التنسيق في GridDesktop.
---

{{% alert color="primary" %}} 

فرشاة التنسيق هي ميزة في MS Excel تم تكييفها في Aspose.Cells.GridDesktop. إنها ميزة رائعة جدًا. بالنسبة للأشخاص الذين لم يستخدموا هذه الميزة بعد، تسمح فرشاة التنسيق للمستخدمين بتطبيق إعدادات التنسيق لأي خلية مركزها على خلية أخرى. تنفيذ هذه الميزة بسيط للغاية. في هذا الموضوع، سنغطي ذلك أيضًا.

{{% /alert %}} 
## **استخدام فرشاة التنسيق**
تتطلب ميزة **فرشاة التنسيق** من المستخدمين اختيار خلية ترغب في تطبيق إعدادات التنسيق الخاصة بها على الخلايا الأخرى ومن ثم استدعاء الطريقة **StartFormatPainter** من **GridDesktop**. هناك وضعان لفرشاة التنسيق على النحو التالي:

- **استخدام فرشاة التنسيق مرة واحدة**
- **استخدام فرشاة التنسيق دائمًا**
### **استخدام فرشاة التنسيق مرة واحدة**
إذا أراد المطورون استخدام ميزة فرشاة التنسيق لمرة واحدة فقط لتطبيق إعدادات التنسيق لخلية مركزة على خلية واحدة فقط، فيمكنهم فعل ذلك عن طريق استدعاء الطريقة **StartFormatPainter** وتمرير قيمة **false** إليها. ستحول هذه القيمة **false** دائمًا فرشاة التنسيق عن التلوين إلى الأبد.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **استخدام فرشاة التنسيق دائمًا**
لاستخدام فرشاة التنسيق دائمًا، هذه ميزة مفيدة عندما نحتاج إلى تطبيق إعدادات التنسيق على أكثر من خلية واحدة. يمكن للمطورين تحقيق هذه الميزة ببساطة عن طريق استدعاء الطريقة **StartFormatPainter** وتمرير قيمة **true** إليها.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


فرشاة التنسيق هذه تستمر في التلوين دائمًا مالم نوقفها. لذا، لتوقف فرشاة التنسيق عن التلوين باستمرار، يمكننا ببساطة استدعاء الطريقة **EndFormatPainter** من **GridDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
