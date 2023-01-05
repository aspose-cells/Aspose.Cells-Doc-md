---
title: Доступ и изменение значений Cell
type: docs
weight: 20
url: /ru/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[Рабочий лист доступа Cells](/cells/ru/net/access-worksheet-cells/) обсуждали доступ к ячейкам. Этот раздел расширяет это обсуждение, чтобы показать, как получить доступ к значениям ячеек и изменить их с помощью Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Доступ и изменение значения Cell**
### **Строковые значения**
 Прежде чем получить доступ и изменить значение ячейки, вам необходимо знать, как получить доступ к ячейкам. Подробнее о различных подходах к доступу к ячейкам см.[Рабочий лист доступа Cells](/cells/ru/net/access-worksheet-cells/).

Каждая ячейка имеет свойство с именем StringValue. После доступа к ячейке разработчики могут использовать свойство StringValue для доступа к строковому значению ячейки. Для изменения значений ячеек предусмотрен специальный метод PutValue, который можно использовать для обновления строкового значения ячейки.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Все типы значений**
Метод PutValue объекта ячейки имеет 8 доступных перегрузок, которые можно использовать для изменения любого типа значения (логического, int, double, DateTime и строки) в ячейке.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Существует также перегруженная версия метода PutValue, которая может принимать любое значение в строковом формате и автоматически преобразовывать его в нужный тип данных. Чтобы это произошло, передайте логическое значение true другому параметру метода PutValue, как показано ниже в примере.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
