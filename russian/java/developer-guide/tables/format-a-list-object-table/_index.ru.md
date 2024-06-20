---
title: Форматирование объекта списка  Таблица
type: docs
weight: 50
url: /ru/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

Для управления и анализа группы связанных данных можно преобразить диапазон ячеек в объект списка (также известный как таблица Excel). Таблица представляет собой серию строк и столбцов, содержащих связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию у каждого столбца в таблице включена фильтрация в строке заголовка, чтобы можно было быстро фильтровать или сортировать данные объекта списка. Можно добавить всю строку (специальная строка в списке, предоставляющая выбор агрегатных функций, полезных для работы с числовыми данными) к объекту списка, предоставляющую раскрывающийся список агрегатных функций для каждой ячейки всей строки. Aspose.Cells предоставляет возможности для создания и управления списками (или таблицами).

{{% /alert %}}

## **Форматирование объекта списка**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), позволяющую получить доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы создать [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) в рабочем листе, используйте свойство коллекции [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) на самом деле является объектом класса [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), который дополнительно предоставляет метод add для добавления объекта списка и указания диапазона ячеек для списка. Согласно указанному диапазону ячеек, в рабочем листе Aspose.Cells создается [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject). Используйте атрибуты (например, [**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType)) класса [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject), чтобы форматировать таблицу по вашему запросу.

В приведенном ниже примере добавляются образцовые данные в рабочий лист, добавляется [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) и применяются стили по умолчанию. Стили [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) поддерживаются Microsoft Excel 2007/2010.

Следующий вывод генерируется при выполнении кода.

**В рабочем листе создается отформатированная таблица** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
