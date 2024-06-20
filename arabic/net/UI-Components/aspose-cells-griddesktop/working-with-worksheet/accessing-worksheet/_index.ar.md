---
title: الوصول إلى ورقة العمل
type: docs
weight: 10
url: /ar/net/aspose-cells-griddesktop/access-worksheet/
keywords: أداة GridDesktop، ورقة العمل
description: يُقدم هذا المقال كيفية العمل مع ورقة العمل في GridDesktop.
---

{{% alert color="primary" %}} 

ورقة العمل هي جزء أساسي من ملف Excel. في الواقع، يتكون ملف Excel من ورقة عمل واحدة أو أكثر. يمكن أن تتكون كل ورقة عمل من ما يصل إلى 65،536 صف و 256 عمود فقط. إنها الورقة العمل التي تحتوي على البيانات في ملف Excel.

يمكن لـ Aspose.Cells.GridDesktop إنشاء وتلاعب الملفات القائمة والجديدة في Excel لذلك هناك، بالطبع، طريقة للوصول إلى ورقة العمل باستخدام Aspose.Cells.GridDesktop. يناقش هذا الموضوع كيفية ذلك.

{{% /alert %}} 
## **استخدام فهرس ورقة العمل**
يمكن للمطورين الوصول إلى مثيل من أي ورقة عمل باستخدام فهرس ورقة العمل المرغوبة كما هو موضح في المثال أدناه. هذا الأسلوب جيد لتكرار عبر عدد من ورقات العمل في ملف Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **استخدام اسم ورقة العمل**
إذا كان اسم ورقة العمل معروفًا، فمن الممكن الوصول إلى ورقة عمل باستخدام اسمها كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **الوصول إلى ورقة عمل نشطة**
من الممكن أن يحتوي ملف Excel على أكثر من ورقة عمل واحدة. الورقة التي يعمل عليها المستخدم تسمى الورقة العمل النشطة. من الممكن الوصول إلى الورقة النشطة.

للوصول إلى ورقة عمل نشطة، تقدم Aspose.Cells.GridDesktop نهجين:
### **استخدام خاصية AcriveSheetIndex**
طريقة للوصول إلى ورقة عمل نشطة باستخدام تحكم Aspose.Cells.GridDesktop هي استخدام خاصية ActiveSheetIndex لتحكم GridDesktop. باستخدام هذه الخاصية، يكون من الممكن الحصول على فهرس الورقة العمل النشطة في تحكم Aspose.Cells.GridDesktop. يمكن بعد ذلك استخدام هذا الفهرس للوصول إلى الورقة العمل بالطريقة التقليدية كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **استخدام طريقة GetActiveWorksheet**
النهج الآخر هو استدعاء طريقة GetActiveWorksheet في تحكم GridDesktop. تقدم هذه الطريقة مرجعًا لورقة العمل التي تكون نشطة حاليًا في تحكم Aspose.Cells.GridDesktop كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
