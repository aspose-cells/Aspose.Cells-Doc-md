---
title: Создание объекта списка
type: docs
weight: 20
url: /ru/python-java/creating-a-list-object/
---

Использование листов упрощает работу с различными типами списков, например, списками телефонов, списками задач и т. д. Aspose.Cells поддерживает создание и управление списками.

## **Преимущества объекта списка**

Есть несколько преимуществ при преобразовании списка данных в фактический объект List:

- Новые строки и столбцы автоматически включаются.
- Итоговая строка внизу списка легко добавляется для отображения SUM, AVERAGE, COUNT и т. д.
- Добавленные столбцы справа автоматически включаются в объект списка.
- Графики, основанные на строках и столбцах, будут автоматически расширены.
- Именованные диапазоны, присвоенные строкам и столбцам, будут автоматически расширены.
- Список защищен от случайного удаления строк и столбцов.

## **Создание объекта списка с использованием Microsoft Excel**

Выбор диапазона данных для создания объекта списка 

![todo:image_alt_text](picture1.png)

Это отображает диалоговое окно Создать список.

Диалоговое окно Создать список 

![todo:image_alt_text](picture2.png)

Реализация объекта списка и указание общего ряда (выберите **Данные**, затем **Список**, затем **Общая строка**).

Создание объекта списка 

![todo:image_alt_text](picture3.png)

## **Создание объекта списка с использованием API Aspose.Cells**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection), которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) предоставляет широкий диапазон свойств и методов для управления листом. Чтобы создать [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) на листе, используйте свойство коллекции [**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects) класса [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) на самом деле является объектом класса [**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection), который также предоставляет метод [**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) для добавления объекта списка и указания диапазона ячеек для списка.

Согласно указанному диапазону ячеек, объект списка создается в листе с помощью Aspose.Cells. Используйте атрибуты (например, ShowTotals, ListColumns и т. д.) класса [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) для управления списком.

В приведенном ниже примере мы создали тот же [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) с использованием API Aspose.Cells для Python via Java, что и в Microsoft Excel в предыдущем разделе.

## Исходный код

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
