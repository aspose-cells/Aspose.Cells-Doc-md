---
title: Управление диапазонами с помощью Golang через C++
linktitle: Диапазоны
type: docs
weight: 105
url: /ru/go-cpp/managing-ranges/
description: Узнайте, как управлять диапазонами в файлах Excel с помощью Aspose.Cells на Golang через C++. Создавайте, изменяйте и стилизуйте диапазоны программным способом.
---

## **Введение**

 В Excel можно выбрать несколько ячеек с помощью выделения мышью, набор выбранных ячеек называется "Диапазон".

Например, вы можете щелкнуть левой кнопкой мыши в ячейке "A1" в Excel, а затем перетащить в ячейку "C4". Прямоугольная область, которую вы выбрали, также легко создается в виде объекта с помощью Aspose.Cells.

 Вот как создать диапазон, установить значение, установить стиль и выполнить другие операции с объектом "Диапазон".

## **Управление диапазонами с использованием Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Создать диапазон**

 Когда вы хотите создать прямоугольную область, расширяющуюся на A1:C4, вы можете использовать следующий код:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges.go" >}}
### **Поместить значение в ячейки диапазона**

Предположим, что у вас есть диапазон ячеек, который расширяется от A1 до C4. Матрица состоит из 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].

 В следующем примере показано, как ввести некоторые значения в ячейки диапазона.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-1.go" >}}
### **Установить стиль ячеек диапазона**

В следующем примере показано, как установить стиль ячеек диапазона.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-2.go" >}}
### **Получить текущий регион диапазона**

CurrentRegion - это свойство, которое возвращает объект Range, представляющий текущий регион. 

Текущий регион - это диапазон, ограниченный любой комбинацией пустых строк и столбцов. Только для чтения.

В Excel вы можете получить область CurrentRegion следующим образом:
1. Выделите область (range1) с помощью мыши.
2. Нажмите "Домой - Правка - Поиск и выбор - Перейти к специальному - Текущий регион", или используйте "Ctrl+Shift+*", теперь вы увидите, что Excel автоматически помогает вам выбрать область (range2), теперь вы сделали это, range2 - это CurrentRegion range1.

Используя Aspose.Cells, вы можете использовать свойство "Range.CurrentRegion" для выполнения той же функции.

Пожалуйста, загрузите следующий тестовый файл, откройте его в Excel, используйте мышь, чтобы выбрать область "A1:D7", затем нажмите "Ctrl+Shift+*", вы увидите, что область "A1:C3" выбрана.

[current_region.xlsx](current_region.xlsx)

Теперь запустите следующий пример, посмотрите, как это работает в Aspose.Cells:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-3.go" >}}

## **Продвинутые темы**
- [Автозаполнение диапазона в файле Excel](/cells/ru/cpp/autofill-ranges/)
- [Копирование диапазонов в Excel](/cells/ru/cpp/copy-ranges-of-Excel/)
- [Копировать только данные диапазона](/cells/ru/cpp/copy-range-data-only/)
- [Копировать данные диапазона со стилем](/cells/ru/cpp/copy-range-data-with-style/)
- [Копировать только стиль диапазона](/cells/ru/cpp/copy-range-style-only/)
- [Создать объединенный диапазон](/cells/ru/cpp/create-union-range/)
- [Вырезать и вставить диапазон](/cells/ru/cpp/cut-and-paste-cells/)
- [Удалить диапазоны](/cells/ru/cpp/delete-ranges-from-Excel/)
- [Получить адрес ячейки смещения количества исходной колонки и строки всего диапазона](/cells/ru/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Вставить диапазоны](/cells/ru/cpp/insert-ranges-to-Excel/)
- [Объединить или разделить диапазон ячеек](/cells/ru/cpp/merge-or-unmerge-range-of-cells/)
- [Перемещение диапазона ячеек на листе](/cells/ru/cpp/move-range-of-cells-in-a-worksheet/)
- [Создать именованные диапазоны с учетом книги и листа](/cells/ru/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Поиск и замена данных в диапазоне](/cells/ru/cpp/search-and-replace-data-in-a-range/)
