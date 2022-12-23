---
title: Создание таблицы
type: docs
weight: 40
url: /ru/java/creating-a-list-object/
---
{{% alert color="primary" %}}

Одним из преимуществ электронных таблиц является то, что они позволяют создавать различные типы списков, например, списки телефонов, списки задач, списки транзакций, активов или пассивов. Несколько пользователей могут работать вместе, чтобы использовать, создавать и поддерживать различные списки.

Aspose.Cells поддерживает создание списков и управление ими.

{{% /alert %}}

## **Преимущества стола**

Преобразование списка данных в фактический объект списка дает ряд преимуществ:

- Новые строки и столбцы включаются автоматически.
- Итоговую строку в нижней части списка можно легко добавить для отображения СУММЫ, СРЕДНЕГО, СЧЕТА и т. д.
- Столбцы, добавленные справа, автоматически включаются в объект списка.
- Диаграммы на основе строк и столбцов будут расширены автоматически.
- Именованные диапазоны, назначенные строкам и столбцам, будут расширены автоматически.
- Список защищен от случайного удаления строк и столбцов.

## **Создание таблицы с помощью Microsoft Excel**

**Выбор диапазона данных для создания объекта списка** 

![дело:изображение_альтернативный_текст](creating-a-list-object_1.png)

Отобразится диалоговое окно «Создать список».

**Диалоговое окно «Создать список»** 

![дело:изображение_альтернативный_текст](creating-a-list-object_2.png)

 Реализация объекта List и указание строки итогов (Select**Данные** , тогда**Список** , с последующим**Итоговая строка**).

**Создание объекта списка** 

![дело:изображение_альтернативный_текст](creating-a-list-object_3.png)

## **Создание таблицы с использованием Использование Aspose.Cells API**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. Чтобы создать[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) на листе используйте[**СписокОбъектов**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) свойство collection класса Worksheet. Каждый[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) фактически является объектом[**КоллекцияОбъектовСписка**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class, который дополнительно предоставляет метод add для добавления объекта List и указания диапазона ячеек для списка.

В соответствии с указанным диапазоном ячеек объект «Список» создается на листе по номеру Aspose.Cells. Используйте атрибуты (например, ShowTotals, ListColumns и т. д.)[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)класс для управления списком.

 В приведенном ниже примере мы создали тот же[**СписокОбъект**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)используя Aspose.Cells API, как мы создали с помощью Microsoft Excel в предыдущем разделе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
