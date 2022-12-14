---
title: الوصول إلى ورقة العمل
type: docs
weight: 10
url: /ar/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

ورقة العمل هي جزء لا يتجزأ من ملف Excel. في الواقع ، يتكون ملف Excel من ورقة عمل واحدة أو أكثر. يمكن أن تتكون كل ورقة عمل من 65.536 صفاً و 256 عموداً فقط. إنها ورقة العمل التي تحتفظ بالبيانات في ملف Excel.

Aspose.Cells.GridDesktop إنشاء ملفات Excel الحالية والجديدة ومعالجتها ، لذلك هناك بالطبع طريقة للوصول إلى أوراق العمل باستخدام Aspose.Cells.GridDesktop. هذا الموضوع يناقش كيف.

{{% /alert %}} 
## **باستخدام فهرس ورقة العمل**
يمكن للمطورين الوصول إلى مثيل أي ورقة عمل باستخدام فهرس ورقة العمل لأي ورقة عمل مطلوبة كما هو موضح أدناه في المثال. هذا الأسلوب مفيد للتكرار خلال عدد من أوراق العمل في ملف Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **استخدام اسم ورقة العمل**
إذا كان اسم ورقة العمل معروفًا ، فمن الممكن الوصول إلى ورقة العمل باستخدام اسمها كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **الوصول إلى ورقة عمل نشطة**
من المحتمل أن يحتوي ملف Excel على أكثر من ورقة عمل واحدة. يسمى htat الذي يعمل عليه المستخدم ورقة العمل النشطة. من الممكن الوصول إلى الورقة النشطة.

للوصول إلى ورقة عمل نشطة ، يقدم Aspose.Cells.GridDesktop طريقتين:
### **استخدام خاصية AcriveSheetIndex**
تتمثل إحدى طرق الوصول إلى ورقة العمل النشطة باستخدام عنصر التحكم Aspose.Cells.GridDesktop في استخدام خاصية ActiveSheetIndex الخاصة بعنصر تحكم GridDesktop. باستخدام هذه الخاصية ، من الممكن الحصول على فهرس ورقة العمل النشطة في عنصر تحكم Aspose.Cells.GridDesktop. ثم يمكن استخدام هذا الفهرس للوصول إلى ورقة العمل بطريقة تقليدية كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **استخدام أسلوب GetActiveWorksheet**
الطريقة الأخرى هي استدعاء أسلوب GetActiveWorksheet لعنصر التحكم GridDesktop. توفر هذه الطريقة مرجعًا لورقة العمل النشطة حاليًا في Aspose.Cells.GridDesktop control كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
