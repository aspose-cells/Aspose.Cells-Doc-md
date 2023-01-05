---
title: الوصول إلى Cells في ورقة عمل
type: docs
weight: 10
url: /ar/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

لقد ناقشنا العمل مع أوراق العمل والصفوف والأعمدة حتى الآن ولكن هذا هو الوقت المناسب للتعمق أكثر والتحدث عن الخلايا. لذلك ، في هذا الموضوع ، سنبدأ مناقشتنا حول الخلايا ذات الميزة الأساسية للوصول إلى الخلايا.

{{% /alert %}} 
## **الوصول إلى Cells في ورقة عمل**
يمكننا الوصول إلى أي خلية في ورقة العمل باستخدام API من Aspose.Cells.GridDesktop. يمكن أن تكون هناك ثلاث طرق ممكنة للوصول إلى الخلايا على النحو التالي:

- **باستخدام Cell الاسم**
- **استخدام مؤشرات الصف والعمود Cell**
- **التركيز Cell**

دعونا نناقش جميع الطرق الثلاثة المذكورة أعلاه واحدًا تلو الآخر.
### **باستخدام Cell الاسم**
 جميع الخلايا في ورقة العمل لها اسم فريد. على سبيل المثال ، A1 ، A2 ، B1 ، B2 إلخ. Aspose.Cells.GridDesktop يسمح للمطورين بالوصول إلى أي خلية مرغوبة باستخدام اسم الخلية الخاص بها. كل ما يتعين علينا القيام به هو تمرير اسم الخلية (كفهرس) إلى ملف**Cells** جمع**ورقة عمل**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **استخدام مؤشرات الصف والعمود Cell**
 يمكن أيضًا التعرف على خلية في ورقة العمل باستخدام موقعها من حيث فهارس الصفوف والأعمدة. كل ما يتعين علينا القيام به هو تمرير فهارس الصفوف والعمود للخلية إلى ملف**Cells** جمع**ورقة عمل**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **التركيز Cell**
 إذا كنت لا تعرف بدقة تلك الخلية التي سيتم الوصول إليها. ثم Aspose.Cells.GridDesktop يسمح لك أيضًا بالوصول إلى خلية موجودة حاليًا في بؤرة المستخدم. باستخدام هذه الميزة ، يمكنك السماح للمستخدم بتحديد أي خلية ومن ثم يمكنك الوصول إلى تلك الخلية في الخلفية. يمكن تحقيق ذلك ببساطة عن طريق استخدام**GetFocusedCell** طريقة**ورقة عمل**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
