---
title: Управление диапазонами
linktitle: Диапазоны
type: docs
weight: 75
url: /ru/java/managing-ranges/
---
## **Вступление**

В Excel вы можете выбрать несколько ячеек с помощью поля мыши, набор выбранных ячеек называется «Диапазон».

Например, вы можете щелкнуть левой кнопкой мыши в Cell «A1» Excel, а затем перетащить в ячейку «C4». Выбранную прямоугольную область также можно легко создать как объект, используя Aspose.Cells.

Вот как создать диапазон, указать значение, задать стиль и выполнить другие операции с объектом «Диапазон».

## **Управление диапазонами с помощью Aspose.Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.

### **Создать диапазон**

Если вы хотите создать прямоугольную область, охватывающую A1:C4, вы можете использовать следующий код:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Поместите значение в Cells диапазона**

Скажем, у вас есть диапазон ячеек, который распространяется на A1:C4. Матрица составляет 4 * 3 = 12 ячеек. Отдельные ячейки диапазона располагаются последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].

В следующем примере показано, как ввести некоторые значения в ячейки диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Установить стиль Cells диапазона**

В следующем примере показано, как установить стиль ячеек диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

### **Получить CurrentRegion диапазона**

 CurrentRegion — это свойство, которое возвращает объект Range, представляющий текущий регион.

Текущая область — это диапазон, ограниченный любой комбинацией пустых строк и пустых столбцов. Только для чтения.

В Excel вы можете получить область CurrentRegion:
1. Выберите область (диапазон1) с помощью поля мыши.
2. Нажмите «Главная - Редактирование - Найти и выбрать - Перейти к специальному - Текущая область» или используйте «Ctrl + Shift + *», вы увидите, что Excel автоматически помогает вам выбрать область (диапазон2), теперь вы это сделали, диапазон2 CurrentRegion диапазона1.

Используя Aspose.Cells, вы можете использовать свойство Range.CurrentRegion для выполнения той же функции.

Загрузите следующий тестовый файл, откройте его в Excel, с помощью поля мыши выберите область «A1: D7», затем нажмите «Ctrl + Shift + *», вы увидите выделенную область «A1: C3».

[текущий_регион.xlsx](current_region.xlsx)

Теперь запустите следующий пример, посмотрите, как он работает в Aspose.Cells:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **Предварительные темы**
- [Диапазон автозаполнения файла Excel](/cells/ru/java/autofill-ranges/)
- [Измените источник данных диаграммы на рабочий лист назначения при копировании строк или диапазона](/cells/ru/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Копировать диапазоны Excel](/cells/ru/java/copy-ranges-of-Excel/)
- [Копировать только данные диапазона](/cells/ru/java/copy-range-data-only/)
- [Копировать данные диапазона со стилем](/cells/ru/java/copy-range-data-with-style/)
- [Копировать только стиль диапазона](/cells/ru/java/copy-range-style-only/)
- [Копировать высоты строк исходного диапазона в целевой диапазон](/cells/ru/java/copy-row-heights-of-source-range-to-destination-range/)
- [Создать союзный диапазон](/cells/ru/java/create-union-range/)
- [Вырезать и вставить диапазоны](/cells/ru/java/cut-and-paste-cells/)
- [Удалить диапазоны](/cells/ru/java/delete-ranges-from-Excel/)
- [Обнаружение слияния Cells на рабочем листе](/cells/ru/java/detect-merged-cells-in-a-worksheet/)
- [Получить адрес Cell Count Offset Весь столбец и вся строка диапазона](/cells/ru/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Получить диапазон с внешними ссылками](/cells/ru/java/get-range-with-external-links/)
- [Реализация непоследовательных диапазонов](/cells/ru/java/implementing-non-sequential-ranges/)
- [Вставить диапазоны](/cells/ru/java/insert-ranges-to-Excel/)
- [Объединить или разъединить диапазон Cells](/cells/ru/java/merge-or-unmerge-range-of-cells/)
- [Переместить диапазон Cells на листе](/cells/ru/java/move-range-of-cells-in-a-worksheet/)
- [Именованные диапазоны](/cells/ru/java/named-ranges/)
- [Поиск и замена данных в диапазоне](/cells/ru/java/search-and-replace-data-in-a-range/)

