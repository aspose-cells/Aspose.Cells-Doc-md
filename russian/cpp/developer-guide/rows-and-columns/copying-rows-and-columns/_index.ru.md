﻿---
title: Копирование строк и столбцов
type: docs
weight: 20
url: /ru/cpp/copying-rows-and-columns/
---
## **Вступление**
Иногда вам нужно скопировать строки и столбцы на листе, не копируя лист целиком. С помощью Aspose.Cells можно копировать строки и столбцы внутри или между книгами.
При копировании строки (или столбца) содержащиеся в ней данные, включая формулы (с обновленными ссылками), а также значения, комментарии, форматирование, скрытые ячейки, изображения и другие объекты чертежа также копируются.
## **Копирование строк и столбцов с помощью Microsoft Excel**
1. Выберите строку или столбец, которые вы хотите скопировать.
1.  Чтобы скопировать строки или столбцы, щелкните**Копировать** на**Стандарт** панели инструментов или нажмите**CTRL**+**С**.
1. Выберите строку или столбец ниже или справа от того места, куда вы хотите скопировать свой выбор.
1.  При копировании строк или столбцов щелкните**Скопировано Cells** на**Вставлять** меню.

{{% alert color="primary" %}} 

 Если вы нажмете**Вставить** на**Стандарт** панель инструментов или нажмите**CTRL**+** V** вместо нажатия команды на**В меню «Вставка**» любое содержимое ячеек назначения заменяется.

{{% /alert %}} 
## **Использование Aspose.Cells**
### **Копирование строк**
Aspose.Cells предоставляет метод CopyRow класса Aspose::Cells::ICells. Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

Метод CopyRow принимает следующие параметры:

- исходный объект Cells,
- индекс исходной строки и
- индекс строки назначения.

Используйте этот метод, чтобы скопировать строку на листе или на другой лист. Метод CopyRow работает аналогично Microsoft Excel. Так, например, вам не нужно явно задавать высоту строки назначения, это значение также копируется.

В следующем примере показано, как скопировать строку на листе. Он использует шаблон файла Excel Microsoft и копирует вторую строку (вместе с данными, форматированием, комментариями, изображениями и т. д.) и вставляет ее в 12-ю строку на том же рабочем листе.

 Вы можете пропустить шаг, который получает исходную высоту строки, используя**GetRowHeigh** метод, а затем устанавливает высоту строки назначения с помощью**SetRowHeight** метод как**КопиРоу** метод автоматически заботится о высоте строки.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows.cpp" >}}

{{% alert color="primary" %}} 

При копировании строк важно отметить связанные изображения, диаграммы или другие объекты чертежа, так как это то же самое с Microsoft Excel:

1. Если индекс исходной строки равен 5, изображение, диаграмма и т. д. копируются, если они содержатся в трех строках (индекс начальной строки равен 4, а индекс конечной строки равен 6).
1. Существующие изображения, диаграммы и т. д. в строке назначения не будут удалены.

{{% /alert %}} 
### **Копирование столбцов**
Aspose.Cells предоставляет метод CopyColumn класса Aspose::Cells::ICells, этот метод копирует все типы данных, включая формулы (с обновленными ссылками) и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из источника. столбец в целевой столбец.

Метод CopyColumn принимает следующие параметры:

- исходный объект Cells,
- индекс исходного столбца и
- индекс столбца назначения.

Используйте метод CopyColumn, чтобы скопировать столбец на лист или на другой лист.

В этом примере столбец копируется с листа и вставляется на лист в другой книге.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns.cpp" >}}