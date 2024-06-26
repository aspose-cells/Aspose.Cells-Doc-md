---
title: دمج وفك دمج الخلايا في GridDesktop
linktitle: دمج وفك دمج الخلايا
type: docs
weight: 90
url: /ar/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop، دمج، فك الدمج
description: يقدم هذا المقال مفهوم الدمج والفك في GridDesktop.
---

{{% alert color="primary" %}} 

في هذا الموضوع، سنناقش ميزة الدمج وفك الدمج لخلايا ورقة العمل. تعتبر هذه الميزة مفيدة في الحالات التي نحتاج فيها إلى توسيع بعض الصفوف أو الأعمدة لتعزيز قراءة البيانات.

{{% /alert %}} 
## **دمج الخلايا**
لدمج الخلايا في خلية واحدة كبيرة، يُرجى اتباع الخطوات التالية:

- الوصول إلى أي **ورقة عمل** مرغوبة
- إنشاء **نطاق من الخلايا** ليتم دمجه
- **دمج** نطاق الخلايا في خلية كبيرة

يمكنك استخدام طريقة **دمج** في **ورقة العمل** لدمج الخلايا. ومع ذلك، يمكن تعريف نطاق الخلايا باستخدام كائن **CellRange**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **فك الدمج**
لفك الدمج عن خلية كبيرة إلى العديد من الخلايا، يُرجى اتباع الخطوات التالية:

- الوصول إلى أي **ورقة عمل** مرغوبة
- الوصول إلى الخلية المدمجة التي تحتاج إلى فك دمجها
- **فك دمج** الخلية الكبيرة إلى العديد من الخلايا باستخدام موقع الخلية المدمجة

يمكنك استخدام طريقة **فك الدمج** في **ورقة العمل** لفك دمج خلية باستخدام موقعها.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

عند دمج الخلايا في خلية واحدة ثم يتم تطبيق إعدادات التنسيق من الخلية العلوية اليسرى (في نطاق الخلايا) على الخلية المدمجة ولكن عند فك دمج الخلية، تحافظ جميع الخلايا الغير مدمجة على إعدادات التنسيق الخاصة بها.

{{% /alert %}}
