---
title: Доступ к GridCell на листе
type: docs
weight: 10
url: /ru/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: В этой статье рассматривается, как получить объект ячейки (GridCell) на листе в GridDesktop.
---

{{% alert color="primary" %}} 

Мы рассмотрели работу с листами, строками и столбцами, но сейчас пришло время поговорить более подробно о ячейках. Итак, в этой теме мы начнем наше обсуждение о ячейках с основной функции доступа к ячейкам.

{{% /alert %}} 
## **Доступ к ячейке на листе**
Мы можем получить доступ к любой ячейке листа, используя API Aspose.Cells.GridDesktop. 
  	Возможны три способа доступа к ячейке: 

- **С использованием имени ячейки**
- **С использованием индексов строки и столбца**
- **Получение фокусированной ячейки**

Давайте обсудим все вышеперечисленные три подхода по очереди.
### **Использование имени ячейки**
Все ячейки в книге Excel имеют уникальное имя. Например, A1, A2, B1, B2 и т. д. Aspose.Cells.GridDesktop позволяет разработчикам получать доступ к любой нужной ячейке, используя её имя. Все, что нам нужно сделать, это передать имя ячейки (в качестве индекса) в коллекцию **Cells** объекта **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**Примечание**

Доступ к GridCell, используя cells[cellName], может потреблять больше памяти, он всегда будет создавать новый объект ячейки (GridCell), независимо от того, существует ли ячейка или нет.

### **Использование индексов строки и столбца ячейки**

**Лучшие практики**:

Если мы хотим получить значение ячейки или стиль ячейки и не хотим выполнять операцию обновления, мы можем использовать метод **CheckCell**, который вернет null, если ячейка не существует, это **сэкономит память**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Получение доступа к ячейке с использованием её индексов строки и столбца
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

Ячейку в книге Excel также можно найти, используя её расположение в терминах индексов строки и столбца. Все, что нам нужно сделать, это передать индексы строки и столбца ячейки в коллекцию **Cells** объекта **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**Примечание**

Доступ к ячейке GridCell с использованием cells[rowIndex, columnIndex] может потреблять больше памяти. Это всегда будет создавать новый объект ячейки (GridCell), независимо от того, пустая ли ячейка или нет.


### **Получение фокусированной ячейки**
Если вы точно не знаете, к какой ячейке нужен доступ, то Aspose.Cells.GridDesktop также позволяет получить доступ к ячейке, которая в данный момент находится в фокусе пользователя. С помощью этой функции можно позволить пользователю выбирать любую ячейку, а затем получить доступ к ней на стороне сервера. Это легко достигается с помощью метода **GetFocusedCell** объекта **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**Лучшие практики**:
### Итерация по ячейкам
если мы хотим получить доступ ко всем ячейкам в листе по одной, мы можем использовать **итераторы** для обхода существующих ячеек. это позволит **экономить память**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
сравните нижеприведенный код, который является **плохим**, это приведет к созданию всех объектов ячеек, независимо от того, является ли он нулевым, что вызовет проблемы с памятью, поэтому, пожалуйста, **не используйте** этот способ
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

