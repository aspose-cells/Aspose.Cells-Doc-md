---
title: الوصول إلى GridCell في ورقة العمل
type: docs
weight: 10
url: /ar/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: يقدم هذا المقال كيفية الحصول على كائن الخلية (GridCell) في ورقة العمل في GridDesktop.
---

{{% alert color="primary" %}} 

لقد تحدثنا حتى الآن عن العمل مع ورق العمل والصفوف والأعمدة ولكن هذا هو الوقت للانتقال بعمق أكبر والحديث عن الخلايا. لذا، في هذا الموضوع، سنبدأ حديثنا حول الخلايا مع ميزة أساسية للوصول إليها.

{{% /alert %}} 
## **الوصول إلى الخلية في ورقة العمل**
يمكننا الوصول إلى أي خلية في ورقة العمل باستخدام واجهة برمجة التطبيقات (API) لـ Aspose.Cells.GridDesktop. يمكن أن تكون هناك ثلاث طرق ممكنة للوصول إلى الخلية على النحو التالي:

- **باستخدام اسم الخلية**
- **باستخدام مؤشرات الصف والعمود**
- **الحصول على الخلية التي تم تركيزها**

دعونا نناقش كل الطرق الثلاثة أعلاه واحدة تلو الأخرى.
### **استخدام اسم الخلية**
تحتوي جميع الخلايا في ورقة العمل على اسم فريد. على سبيل المثال، A1، A2، B1، B2 وما إلى ذلك. تتيح Aspose.Cells.GridDesktop للمطورين الوصول إلى أي خلية مطلوبة باستخدام اسم الخلية. كل ما علينا فعله هو تمرير اسم الخلية (كفهرس) إلى مجموعة **Cells** في **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**تنويه**

الوصول إلى GridCell باستخدام cells [cellName] قد يستهلك المزيد من الذاكرة. سيتم دائمًا إنشاء كائن خلية جديد (GridCell) بغض النظر عما إذا كانت الخلية فارغة أم لا.

### **استخدام مؤشرات صف الخلية والعمود**

**أفضل الممارسات**: 

إذا كنا نريد الحصول على قيمة الخلية أو نمط الخلية ولا نريد القيام بعملية التحديث، يمكننا استخدام طريقة **CheckCell** التي ستعيد قيمة فارغة إذا لم تكن الخلية موجودة. سيتم ذلك **توفير الذاكرة**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// الوصول إلى خلية باستخدام مؤشرات الصف والعمود
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

يمكن أيضًا التعرف على الخلية في ورقة العمل باستخدام موقعها فيما يتعلق بمؤشرات صفها وعمودها. كل ما علينا فعله هو تمرير مؤشرات الصف والعمود للخلية إلى مجموعة **Cells** في **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**تنويه**

قد يستهلك الوصول إلى خلية الشبكة باستخدام cells[rowIndex, columnIndex] المزيد من الذاكرة. سيقوم دائمًا بإنشاء كائن خلية جديد (GridCell) بغض النظر عما إذا كانت الخلية فارغة أم لا.


### **الحصول على الخلية المُركزة**
إذا كنت لا تعرف بدقة أي خلية يجب الوصول إليها. بعد ذلك، تُتيح Aspose.Cells.GridDesktop أيضًا الوصول إلى خلية تكون حاليًا في تركيز المستخدم. باستخدام هذه الميزة، يمكنك السماح للمستخدم باختيار أي خلية ومن ثم يمكنك الوصول إلى تلك الخلية في الخلفية. يمكن تحقيق ذلك ببساطة باستخدام طريقة **GetFocusedCell** في **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**أفضل الممارسات**: 
### تكرير الخلايا
إذا كنا نريد الوصول إلى جميع الخلايا في ورقة العمل واحدة تلو الأخرى ، يمكننا استخدام **iterators** للانتقال بين الخلايا الموجودة. سيتم ذلك **توفير الذاكرة**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
قارن الكود أدناه الذي هو **سيء** ، سيقوم هذا بإنشاء كائنات الخلايا بغض النظر عما إذا كانت فارغة ، وبالتالي سيسبب مشاكل الذاكرة ، لذا من فضلك **لا ت** استخدم هذا الطريقة
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 for(int r=0;r< sheet.RowsCount;r++)
 {
     for(int c=0;c< sheet.ColumnsCount; c++)
     {
         Console.WriteLine(sheet.Cells[r,c].ToString());
     }
 }
~~~

