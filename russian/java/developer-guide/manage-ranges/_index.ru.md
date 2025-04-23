---
title: Управление диапазонами
linktitle: Диапазоны
type: docs
weight: 75
url: /ru/java/managing-ranges/
---

## **Введение**

 В Excel можно выбрать несколько ячеек с помощью выделения мышью, набор выбранных ячеек называется "Диапазон".

Например, вы можете щелкнуть левой кнопкой мыши в ячейке "A1" в Excel, а затем перетащить в ячейку "C4". Прямоугольная область, которую вы выбрали, также легко создается в виде объекта с помощью Aspose.Cells.

 Вот как создать диапазон, установить значение, установить стиль и выполнить другие операции с объектом "Диапазон".

## **Управление диапазонами с использованием Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

### **Создать диапазон**

 Когда вы хотите создать прямоугольную область, расширяющуюся на A1:C4, вы можете использовать следующий код:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Поместить значение в ячейки диапазона**

Предположим, что у вас есть диапазон ячеек, который расширяется от A1 до C4. Матрица состоит из 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].

 В следующем примере показано, как ввести некоторые значения в ячейки диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Установить стиль ячеек диапазона**

В следующем примере показано, как установить стиль ячеек диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **Продвинутые темы**
- [Автозаполнение диапазона в файле Excel](/cells/ru/java/autofill-ranges/)
- [Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона](/cells/ru/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Копирование диапазонов в Excel](/cells/ru/java/copy-ranges-of-Excel/)
- [Копировать только данные диапазона](/cells/ru/java/copy-range-data-only/)
- [Копировать данные диапазона со стилем](/cells/ru/java/copy-range-data-with-style/)
- [Копировать только стиль диапазона](/cells/ru/java/copy-range-style-only/)
- [Копировать высоты строк исходного диапазона в целевой диапазон](/cells/ru/java/copy-row-heights-of-source-range-to-destination-range/)
- [Создать объединенный диапазон](/cells/ru/java/create-union-range/)
- [Вырезать и вставить диапазоны](/cells/ru/java/cut-and-paste-cells/)
- [Удалить диапазоны](/cells/ru/java/delete-ranges-from-Excel/)
- [Обнаружение объединенных ячеек в листе](/cells/ru/java/detect-merged-cells-in-a-worksheet/)
- [Получить адрес ячейки смещения количества исходной колонки и строки всего диапазона](/cells/ru/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Получить диапазон с внешними ссылками](/cells/ru/java/get-range-with-external-links/)
- [Реализация не последовательных диапазонов](/cells/ru/java/implementing-non-sequential-ranges/)
- [Вставить диапазоны](/cells/ru/java/insert-ranges-to-Excel/)
- [Объединить или разделить диапазон ячеек](/cells/ru/java/merge-or-unmerge-range-of-cells/)
- [Перемещение диапазона ячеек на листе](/cells/ru/java/move-range-of-cells-in-a-worksheet/)
- [Именованные диапазоны](/cells/ru/java/named-ranges/)
- [Поиск и замена данных в диапазоне](/cells/ru/java/search-and-replace-data-in-a-range/)

{{< app/cells/assistant language="java" >}}
