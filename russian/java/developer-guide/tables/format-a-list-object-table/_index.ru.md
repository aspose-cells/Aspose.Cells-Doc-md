---
title: Форматирование объекта списка — таблица
type: docs
weight: 50
url: /ru/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

Для управления и анализа группы связанных данных можно превратить диапазон ячеек в объект списка (также известный как таблица Excel). Таблица — это последовательность строк и столбцов, которые содержат связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию для каждого столбца в таблице включена фильтрация в строке заголовка, что позволяет быстро фильтровать или сортировать данные объекта списка. Вы можете добавить итоговую строку (специальную строку в списке, которая предоставляет выбор агрегатных функций, полезных для работы с числовыми данными) в объект списка, который предоставляет раскрывающийся список агрегатных функций для каждой ячейки итоговой строки. Aspose.Cells предоставляет параметры для создания списков (или таблиц) и управления ими.

{{% /alert %}}

## **Форматирование объекта списка**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы создать[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) на листе используйте[**СписокОбъектов**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) коллекционное имущество г.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс. Каждый[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) фактически является объектом[**КоллекцияОбъектовСписка**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class, который дополнительно предоставляет метод add для добавления объекта List и указания диапазона ячеек, который он должен охватывать. Согласно указанному диапазону ячеек,[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) создан на листе пользователем Aspose.Cells. Используйте атрибуты (например,[**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) ) принадлежащий[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)класс для форматирования таблицы в соответствии с вашими требованиями.

 В приведенном ниже примере на рабочий лист добавляются образцы данных, добавляется[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) и применяет к нему стили по умолчанию.[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)стили поддерживаются Microsoft Excel 2007/2010.

При выполнении кода генерируется следующий вывод.

**На листе создается форматированная таблица.** 

![дело:изображение_альтернативный_текст](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
