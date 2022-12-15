---
title: Создание объекта списка
type: docs
weight: 20
url: /ru/python-java/creating-a-list-object/
---
Использование рабочих листов упрощает работу, например, с различными типами списков. списки телефонов, списки задач. и т. д. Aspose.Cells поддерживает создание списков и управление ими.

## **Преимущества объекта списка**

Преобразование списка данных в фактический объект списка дает ряд преимуществ:

- Новые строки и столбцы включаются автоматически.
- Итоговую строку в нижней части списка можно легко добавить для отображения СУММЫ, СРЕДНЕГО, СЧЕТА и т. д.
- Столбцы, добавленные справа, автоматически включаются в объект List.
- Диаграммы на основе строк и столбцов будут расширены автоматически.
- Именованные диапазоны, назначенные строкам и столбцам, будут расширены автоматически.
- Список защищен от случайного удаления строк и столбцов.

## **Создание объекта списка с использованием Microsoft Excel**

**Выбор диапазона данных для создания объекта списка** 

![дело:изображение_альтернативный_текст](picture1.png)

Отобразится диалоговое окно «Создать список».

**Диалоговое окно «Создать список»** 

![дело:изображение_альтернативный_текст](picture2.png)

Реализация объекта List и указание строки итогов (Select**Данные**, тогда**Список**, с последующим**Итоговая строка**).

**Создание объекта списка** 

![дело:изображение_альтернативный_текст](picture3.png)

## **Создание объекта списка с использованием Aspose.Cells API**

Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. Чтобы создать[**СписокОбъект**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)на листе используйте[**СписокОбъектов**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)коллекционное имущество г.[**Рабочий лист**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)учебный класс. Каждый[**СписокОбъект**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)фактически является объектом[**КоллекцияОбъектовСписка**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)класс, который дополнительно обеспечивает[**добавлять**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) для добавления объекта List и указания диапазона ячеек для списка.

В соответствии с указанным диапазоном ячеек объект List создается на листе по номеру Aspose.Cells. Используйте атрибуты (например, ShowTotals, ListColumns и т. д.)[**СписокОбъект**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)класс для управления списком.

В приведенном ниже примере мы создали тот же[**СписокОбъект**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)используя Aspose.Cells for Python via Java API, как мы создали с помощью Microsoft Excel в предыдущем разделе.

## Исходный код

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
