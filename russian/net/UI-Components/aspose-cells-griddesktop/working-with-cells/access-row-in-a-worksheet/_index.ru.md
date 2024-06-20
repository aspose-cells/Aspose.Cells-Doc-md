---
title: Доступ к GridRow в рабочем листе
type: docs
weight: 10
url: /ru/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop, GridRow, получить строку
description: В этой статье рассматривается способ получения объекта строки (GridRow) в рабочем листе в GridDesktop.
---
### Перебор строк
**Лучшие практики**:
если мы хотим получить доступ ко всем строкам в листе по одной, мы можем использовать **итераторы** для обхода существующих строк. это позволит **экономить память**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Получение строки с использованием итераторов
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
сравните нижеприведенный код, он создаст все объекты строки, независимо от того, является ли он пустым, что приведет к проблемам с памятью, поэтому, пожалуйста, **не используйте** этот способ
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
однако вы можете использовать метод CheckRow, чтобы проверить, пустая ли строка
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
