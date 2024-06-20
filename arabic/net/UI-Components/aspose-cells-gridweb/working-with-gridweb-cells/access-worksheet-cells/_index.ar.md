---
title: الوصول إلى خلية ورقة العمل
type: docs
weight: 10
url: /ar/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: يقدم هذا المقال كيفية الحصول على الخلية (GridCell) في GridWeb.
---

{{% alert color="primary" %}} 

يناقش هذا الموضوع الخلايا، مع مراجعة للميزة الأساسية لـ Aspose.Cells.GridWeb: الوصول إلى الخلايا.

{{% /alert %}} 
## **الوصول إلى الخلايا في ورقة عمل**
تحتوي كل ورقة عمل على خاصية بالاسم Cells وهي في الواقع مجموعة من كائنات GridCell حيث يمثل كائن GridCell خلية في Aspose.Cells.GridWeb. يمكن الوصول إلى أي خلية باستخدام Aspose.Cells.GridWeb. هناك طريقتان مفضلتان، يتم مناقشة كل منهما أدناه.


### **استخدام اسم الخلية**
تحتوي جميع الخلايا على اسم فريد. على سبيل المثال، A1، A2، B1، B2 إلخ. يسمح Aspose.Cells.GridWeb للمطورين بالوصول إلى أي خلية مرغوبة باستخدام اسم الخلية. ببساطة قم بتمرير اسم الخلية (كفهرس) إلى مجموعة الخلايا في GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**تنويه**

الوصول إلى GridCell باستخدام cells [cellName] قد يستهلك المزيد من الذاكرة. سيتم دائمًا إنشاء كائن خلية جديد (GridCell) بغض النظر عما إذا كانت الخلية فارغة أم لا.


### **استخدام فهرس الصف والعمود**


يمكن أيضًا التعرف على الخلية من خلال موقعها من حيث فهرس الصف والعمود. ما عليك سوى تمرير فهرس صف الخلية وفهرس عمودها إلى مجموعة الخلايا في ورقة العمل الشبكية. هذا النهج أسرع من السابق.

**أفضل الممارسات**: 

إذا كنا نريد الحصول على قيمة الخلية أو نمط الخلية ولا نريد القيام بعملية التحديث، يمكننا استخدام طريقة **CheckCell** التي ستعيد قيمة فارغة إذا لم تكن الخلية موجودة. سيتم ذلك **توفير الذاكرة**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**أفضل الممارسات**: 
### تكرير الخلايا
إذا كنا نريد الوصول إلى جميع الخلايا في ورقة العمل واحدة تلو الأخرى ، يمكننا استخدام **iterators** للانتقال بين الخلايا الموجودة. سيتم ذلك **توفير الذاكرة**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
قارن الكود أدناه الذي هو **سيء** ، سيقوم هذا بإنشاء كائنات الخلايا بغض النظر عما إذا كانت فارغة ، وبالتالي سيسبب مشاكل الذاكرة ، لذا من فضلك **لا ت** استخدم هذا الطريقة
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r< cells.MaxRow;r++)
 {
     for(int c=0;c< cells.MaxColumn; c++)
     {
         Console.WriteLine(cells[r,c].ToString());
     }
 }
~~~
