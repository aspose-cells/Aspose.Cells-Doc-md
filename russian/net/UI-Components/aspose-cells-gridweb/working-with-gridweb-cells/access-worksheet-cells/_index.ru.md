---
title: Доступ к ячейке рабочего листа
type: docs
weight: 10
url: /ru/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: В этой статье описано, как получить ячейку (GridCell) в GridWeb.
---

{{% alert color="primary" %}} 

В этой теме рассматриваются ячейки, рассматривается наиболее базовая функция Aspose.Cells.GridWeb: доступ к ячейкам.

{{% /alert %}} 
## **Доступ к ячейкам на рабочем листе**
Каждый рабочий лист содержит свойство с именем Cells, которое на самом деле представляет собой коллекцию объектов GridCell, где объект GridCell представляет ячейку в Aspose.Cells.GridWeb. Возможно получить доступ к любой ячейке, используя Aspose.Cells.GridWeb. Существует два предпочтительных метода, каждый из которых обсуждается ниже.


### **Использование имени ячейки**
У всех ячеек есть уникальное имя. Например, A1, A2, B1, B2 и т. д. Aspose.Cells.GridWeb позволяет разработчикам получить доступ к любой желаемой ячейке, используя имя ячейки. Просто передайте имя ячейки (в качестве индекса) в коллекцию Cells GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**Примечание**

Доступ к GridCell, используя cells[cellName], может потреблять больше памяти, он всегда будет создавать новый объект ячейки (GridCell), независимо от того, существует ли ячейка или нет.


### **Использование индексов строки и столбца**


Ячейку также можно распознать по ее расположению в терминах индексов строки и столбца. Просто передайте индексы строки и столбца ячейке в коллекцию Cells GridWorksheet. Этот подход быстрее, чем предыдущий.

**Лучшие практики**:

Если мы хотим получить значение ячейки или стиль ячейки и не хотим выполнять операцию обновления, мы можем использовать метод **CheckCell**, который вернет null, если ячейка не существует, это **сэкономит память**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**Лучшие практики**:
### Итерация по ячейкам
если мы хотим получить доступ ко всем ячейкам в листе по одной, мы можем использовать **итераторы** для обхода существующих ячеек. это позволит **экономить память**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
сравните нижеприведенный код, который является **плохим**, это приведет к созданию всех объектов ячеек, независимо от того, является ли он нулевым, что вызовет проблемы с памятью, поэтому, пожалуйста, **не используйте** этот способ
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
