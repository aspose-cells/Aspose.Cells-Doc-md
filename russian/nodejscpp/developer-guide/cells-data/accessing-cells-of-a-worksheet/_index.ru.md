---
title: Доступ к ячейкам листа
type: docs
weight: 10
url: /ru/nodejs-cpp/accessing-cells-of-a-worksheet/
description: В этой статье показано, как определить максимальный диапазон отображения листа и получать доступ к ячейкам через API Aspose.Cells for Node.js via C++.
keywords: Получить объект ячейки, доступ к ячейкам, получить максимальный диапазон отображения листа. 
---

{{% alert color="primary" %}}

Все листы могут содержать данные, которые в основном хранятся в ячейках (из которых состоит лист). Ячейка — это основная часть листа, использующаяся для построения всего листа как последовательности строк и столбцов. Перед попыткой доступа к данным листа необходимо получить доступ к его ячейкам. В этой теме мы обсудим несколько основных подходов к доступу к ячейкам листа во время выполнения с помощью Aspose.Cells for Node.js via C++.

{{% /alert %}}

## **Как получить доступ к ячейкам**

Aspose.Cells for Node.js via C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), который позволяет получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллецию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), которая представляет все ячейки листа.

Мы можем использовать коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) для доступа к ячейкам листа. Aspose.Cells for Node.js via C++ предоставляет три основных способа доступа к ячейкам в листе:

1. Использование имени ячейки.
2. Использование индекса строки и столбца ячейки.
1. Использование индекса ячейки в коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)

**ВАЖНО:** Мы отметили, что третий подход является самым быстрым, а первый - самым медленным. Разница в производительности между подходами очень мала, поэтому не стоит беспокоиться о снижении производительности, какой бы подход вы ни использовали.

### **Как получить объект Ячейки по имени ячейки**

Разработчики могут получить доступ к любой конкретной ячейке, передав ее имя ячейки в коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) в качестве индекса.

Если вы создаете пустой лист на старте, количество коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) равно нулю. Когда вы используете этот подход для доступа к ячейке, он будет проверять, существует ли эта ячейка в коллекции или нет. Если да, то возвращает объект ячейки в коллекции, в противном случае создает новый объект [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), добавляет объект в коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) и затем возвращает объект. Этот подход является самым простым способом доступа к ячейке, если вы знакомы с Microsoft Excel, но он самый медленный по сравнению с другими подходами.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **Как получить объект Ячейки по индексу строки и столбца ячейки**

Разработчики могут получить доступ к любой конкретной ячейке, передав индексы ее строки и столбца в коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Этот подход работает так же, как и первый подход.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **Как получить объект Ячейки по индексу ячейки в коллекции ячеек**

К ячейке также можно получить доступ, передав числовой индекс ячейки в коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

Если вы используете этот подход для доступа к ячейкам, может быть сгенерировано исключение, если числовой индекс ячейки находится вне диапазона. Этот подход является самым быстрым для доступа к ячейкам, но важно знать, что если вы используете этот подход для доступа к объекту ячейки, числовой индекс может измениться после добавления новых ячеек в коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Объекты ячеек в коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) внутренне сортируются по индексам строки и столбца.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **Как получить максимальный диапазон отображения листа**

Aspose.Cells for Node.js via C++ для Node.js через C++ позволяет разработчикам получать доступ к максимальному отображаемому диапазону листа. Максимальный диапазон отображения — это диапазон ячеек между первой и последней ячейкой с содержимым — удобно при копировании, выборе или отображении всего содержимого листа в изображении.

Вы можете получить доступ к максимальному диапазону отображения листа с помощью [**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--). В следующем примере кода показано, как получить доступ к свойству [**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

