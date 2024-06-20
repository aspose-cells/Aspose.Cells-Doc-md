---
title: Доступ и изменение значения ячейки
type: docs
weight: 20
url: /ru/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: В этой статье рассматривается, как получить и изменить значение ячейки в GridDesktop.
---

{{% alert color="primary" %}} 

В предыдущей теме мы обсудили доступ к ячейкам листа. В этой теме мы просто расширим эту тему, чтобы показать разработчикам, как они могут получить доступ и изменить значения ячеек, используя API Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Доступ и изменение значения ячейки с использованием Aspose.Cells.GridDesktop**
Перед тем как получить доступ и изменить значение ячейки, мы должны знать, как получить доступ к ячейкам. Существует три подхода к доступу к ячейкам листа. Для получения дополнительной информации о этих трех подходах, пожалуйста, [Доступ к ячейкам на листе.](/cells/ru/net/accessing-cells-in-a-worksheet/)

У каждой ячейки есть свойство с именем Значение . После того как ячейка получена, разработчики могут получить доступ и изменить содержимое свойства Значение, чтобы получить доступ и изменить значение ячейки.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**ВАЖНО:** Использование свойства Значение ячейки для изменения ее значения - хороший метод для установки значения одной или нескольких ячеек. Если нужно установить значения многих ячеек, то производительность этого подхода будет плохой. Таким образом, для установки значений многих ячеек вы должны использовать метод **SetCellValue** ячейки для улучшения производительности ваших приложений. Измененная версия приведенного выше фрагмента кода с использованием метода **SetCellValue** показана ниже.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
