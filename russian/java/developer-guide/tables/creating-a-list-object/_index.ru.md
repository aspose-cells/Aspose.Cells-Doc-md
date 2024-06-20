---
title: Создание таблицы
type: docs
weight: 40
url: /ru/java/creating-a-list-object/
---

{{% alert color="primary" %}}

Одним из преимуществ электронных таблиц является возможность создания различных типов списков, например, списков телефонов, списков задач, списков транзакций, активов или обязательств. Несколько пользователей могут вместе работать с созданием и поддержкой различных списков.

Aspose.Cells поддерживает создание и управление списками.

{{% /alert %}}

## **Преимущества таблицы**

Есть несколько преимуществ при преобразовании списка данных в фактический объект List:

- Новые строки и столбцы автоматически включаются.
- Итоговая строка внизу списка легко добавляется для отображения SUM, AVERAGE, COUNT и т. д.
- Добавленные столбцы справа автоматически включаются в объект списка.
- Графики, основанные на строках и столбцах, будут автоматически расширены.
- Именованные диапазоны, присвоенные строкам и столбцам, будут автоматически расширены.
- Список защищен от случайного удаления строк и столбцов.

## **Создание таблицы с использованием Microsoft Excel**

Выбор диапазона данных для создания объекта списка 

![todo:image_alt_text](creating-a-list-object_1.png)

Это отображает диалоговое окно Создать список.

Диалоговое окно Создать список 

![todo:image_alt_text](creating-a-list-object_2.png)

Реализация объекта Список и указание Итоговой строки (Выберите **Данные**, затем **Список**, затем **Итоговая строка**).

Создание объекта списка 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Создание таблицы с использованием Aspose.Cells API**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), позволяющую получить доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления рабочим листом. Чтобы создать [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) в рабочем листе, используйте свойство коллекции [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) класса Worksheet. Каждый [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) на самом деле является объектом класса [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), который дополнительно предоставляет метод add для добавления объекта списка и указания диапазона ячеек для списка.

Согласно указанному диапазону ячеек, объект списка создается в рабочем листе Aspose.Cells. Используйте атрибуты (например, ShowTotals, ListColumns и т. д.) класса [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject), чтобы контролировать список.

В приведенном ниже примере мы создали тот же [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) с использованием API Aspose.Cells, что и при создании в Microsoft Excel в предыдущем разделе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
