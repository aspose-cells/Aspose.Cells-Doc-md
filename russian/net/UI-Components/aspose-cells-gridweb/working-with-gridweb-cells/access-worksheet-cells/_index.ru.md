---
title: Рабочий лист доступа Cells
type: docs
weight: 10
url: /ru/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

В этом разделе обсуждаются ячейки, рассматривается самая основная функция Aspose.Cells.GridWeb: доступ к ячейкам.

{{% /alert %}} 
## **Доступ к Cells на рабочем листе**
Каждый рабочий лист содержит свойство с именем Cells, которое на самом деле представляет собой набор объектов GridCell, где объект GridCell представляет ячейку в Aspose.Cells.GridWeb. Можно получить доступ к любой ячейке, используя Aspose.Cells.GridWeb. Существует два предпочтительных метода, каждый из которых обсуждается ниже.


### **Использование имени Cell**
Все ячейки имеют уникальное имя. Например, A1, A2, B1, B2 и т. д. Aspose.Cells.GridWeb позволяет разработчикам получать доступ к любой нужной ячейке, используя имя ячейки. Просто передайте имя ячейки (в качестве индекса) в коллекцию Cells таблицы GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **Использование индексов строк и столбцов**
Ячейку также можно распознать по ее местоположению с точки зрения индексов строк и столбцов. Просто передайте индексы строки и столбца ячейки в коллекцию Cells таблицы GridWorksheet. Этот подход более быстрый, чем описанный выше.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
