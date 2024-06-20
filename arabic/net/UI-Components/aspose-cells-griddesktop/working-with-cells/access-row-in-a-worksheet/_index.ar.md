---
title: الوصول إلى GridRow في ورقة العمل
type: docs
weight: 10
url: /ar/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop، سطر الجدول، الحصول على السطر
description: يقدم هذا المقال كيفية الحصول على كائن السطر (GridRow) في ورقة العمل في GridDesktop.
---
### التكرار عبر الصفوف
**أفضل الممارسات**: 
إذا كنا نريد الوصول إلى جميع الصفوف في ورقة العمل واحدة تلو الأخرى ، يمكننا استخدام المحولات للانتقال بين الصفوف الموجودة. وسيتم ذلك **توفير الذاكرة**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// الوصول إلى الصف باستخدام المحولات
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
قارن بالكود أدناه ، سيقوم هذا بإنشاء جميع كائنات الصف بغض النظر عما إذا كانت فارغة ، مما سيتسبب في مشاكل في الذاكرة ، لذلك يرجى **عدم** استخدام هذه الطريقة
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
ومع ذلك، يمكنك استخدام طريقة CheckRow للتحقق مما إذا كان الصف فارغًا
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
