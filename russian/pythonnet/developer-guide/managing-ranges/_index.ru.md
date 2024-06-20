---
title: Управление диапазонами
linktitle: Диапазоны
type: docs
weight: 105
url: /ru/python-net/managing-ranges/
description: В этой статье показано, как управлять диапазонами с помощью Aspose.Cells для Python API via .NET.
keywords: Библиотека Python для Excel, Управление диапазонами в Python, Создание диапазона в Python, Установка значения в ячейках диапазона, Установка стиля ячеек диапазона, Получение CurrentRegion диапазона.
---

## **Введение**

 В Excel можно выбрать несколько ячеек с помощью выделения мышью, набор выбранных ячеек называется "Диапазон".

 Например, вы можете щелкнуть левой кнопкой мыши в ячейке "A1" Excel, а затем перетащить в ячейку "C4". Прямоугольная область, которую вы выбрали, также можно легко создать в виде объекта с использованием Aspose.Cells для Python via .NET.

 Вот как создать диапазон, установить значение, установить стиль и выполнить другие операции с объектом "Диапазон".

## ** Управление диапазонами с использованием библиотеки Aspose.Cells для Python Excel**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

## ** Как создать диапазон**

 Когда вы хотите создать прямоугольную область, расширяющуюся на A1:C4, вы можете использовать следующий код:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## ** Как установить значение в ячейки диапазона**

 Скажем, у вас есть диапазон ячеек, распространяющийся на A1:C4. Матрица составляет 4 * 3 = 12 ячеек. Индивидуальные ячейки диапазона упорядочены последовательно.

 В следующем примере показано, как ввести некоторые значения в ячейки диапазона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **Как установить стиль ячеек диапазона**

В следующем примере показано, как установить стиль ячеек диапазона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **Как получить текущий регион диапазона**

CurrentRegion - это свойство, которое возвращает объект Range, представляющий текущий регион. 

Текущий регион - это диапазон, ограниченный любой комбинацией пустых строк и столбцов. Только для чтения.

В Excel вы можете получить область CurrentRegion следующим образом:
1. Выделите область (range1) с помощью мыши.
2. Нажмите "Домой - Правка - Поиск и выбор - Перейти к специальному - Текущий регион", или используйте "Ctrl+Shift+*", теперь вы увидите, что Excel автоматически помогает вам выбрать область (range2), теперь вы сделали это, range2 - это CurrentRegion range1.

Используя Aspose.Cells для Python via .NET, вы можете использовать свойство "Range.current_region" для выполнения той же функции.

Пожалуйста, загрузите следующий тестовый файл, откройте его в Excel, используйте мышь, чтобы выбрать область "A1:D7", затем нажмите "Ctrl+Shift+*", вы увидите, что область "A1:C3" выбрана.

[current_region.xlsx](current_region.xlsx)

Теперь, выполните следующий пример, посмотрите, как это работает в Aspose.Cells для Python via .NET:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **Продвинутые темы**
- [Автозаполнение диапазона в файле Excel](/cells/ru/python-net/autofill-ranges/)
- [Копирование диапазонов в Excel](/cells/ru/python-net/copy-ranges-of-excel/)
- [Копировать только данные диапазона](/cells/ru/python-net/copy-range-data-only/)
- [Копировать данные диапазона со стилем](/cells/ru/python-net/copy-range-data-with-style/)
- [Копировать только стиль диапазона](/cells/ru/python-net/copy-range-style-only/)
- [Создать объединенный диапазон](/cells/ru/python-net/create-union-range/)
- [Вырезать и вставить диапазон](/cells/ru/python-net/cut-and-paste-cells/)
- [Удалить диапазоны](/cells/ru/python-net/delete-ranges-from-excel/)
- [Получить адрес ячейки смещения количества исходной колонки и строки всего диапазона](/cells/ru/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Вставить диапазоны](/cells/ru/python-net/insert-ranges-to-excel/)
- [Объединить или разделить диапазон ячеек](/cells/ru/python-net/merge-or-unmerge-range-of-cells/)
- [Перемещение диапазона ячеек на листе](/cells/ru/python-net/move-range-of-cells-in-a-worksheet/)
- [Создать именованные диапазоны с учетом книги и листа](/cells/ru/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Поиск и замена данных в диапазоне](/cells/ru/python-net/search-and-replace-data-in-a-range/)

