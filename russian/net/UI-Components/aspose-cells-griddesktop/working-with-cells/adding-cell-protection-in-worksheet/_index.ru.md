---
title: Добавление защиты Cell в рабочий лист
type: docs
weight: 130
url: /ru/net/adding-cell-protection-in-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells для GridDesktop позволяет защитить ячейки на листе. Сначала вам нужно защитить свой рабочий лист, а затем вы можете защитить нужные ячейки на рабочем листе. Чтобы защитить рабочий лист, установите**Рабочий лист.Защищено** свойство в true, затем используйте**Рабочий лист.SetProtected()** способ защиты диапазона ячеек.

{{% /alert %}} 
## **Защитите Cell, используя Aspose.Cells.GridDesktop**
 Следующий пример кода защищает все ячейки в диапазоне**А1:Б1** активного листа GridDesktop. Когда вы дважды щелкните любую ячейку в этом диапазоне, вы не сможете редактировать. Это сделает эти ячейки доступными только для чтения.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
