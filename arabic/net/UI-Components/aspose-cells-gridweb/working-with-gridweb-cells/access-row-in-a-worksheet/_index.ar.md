---
title: الوصول إلى GridRow في ورقة العمل
type: docs
weight: 10
url: /ar/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb ، GridRow ، الحصول على الصف
description: يقدم هذا المقال كيفية الحصول على كائن الصف (GridRow) في ورقة العمل في GridWeb.
---
### التكرار عبر الصفوف
**أفضل الممارسات**: 
إذا كنا نريد الوصول إلى جميع الصفوف في ورقة العمل واحدة تلو الأخرى ، يمكننا استخدام المحولات للانتقال بين الصفوف الموجودة. وسيتم ذلك **توفير الذاكرة**.
~~~C#

// الوصول إلى الصف باستخدام المحولات
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
قارن بالكود أدناه ، سيقوم هذا بإنشاء جميع كائنات الصف بغض النظر عما إذا كانت فارغة ، مما سيتسبب في مشاكل في الذاكرة ، لذلك يرجى **عدم** استخدام هذه الطريقة
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
ومع ذلك، يمكنك استخدام طريقة CheckRow للتحقق مما إذا كان الصف فارغًا
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
