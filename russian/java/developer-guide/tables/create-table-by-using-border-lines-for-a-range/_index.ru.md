---
title: Создайте таблицу, используя линии границ для диапазона
type: docs
weight: 50
url: /ru/java/create-table-by-using-border-lines-for-a-range/
description: Как создать таблицу с диапазоном, используя линии границ. Aspose.Cells for Java предоставляет простой в использовании API, который можно использовать для добавления границ к диапазону.
keywords: create table, range to table, range to table excel, excel range to table, range to table with borders, how to create table from range, convert range to table, excel convert range to table, excel create table, range to table java 
---
{{% alert color="primary" %}}

 Иногда вы хотите создать таблицу, добавив линии границ для**Спектр**/**CellArea** на основе адреса ячеек, которые у вас есть. Ты можешь использовать[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) для создания диапазона ячеек.[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) метод возвращает[**Спектр**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) объект. Вы можете создать[**Стиль**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) объекта и соответственно укажите параметры границ (верхняя, левая, нижняя, правая). Позже вы можете получить клетки[**Спектр**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)и примените желаемое форматирование к ячейкам.

{{% /alert %}}

 В следующем примере показано, как создать[**Спектр**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)и укажите границы для ячеек диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

После запуска приведенного выше кода мы можем получить сгенерированный файл Excel, содержащий отформатированную таблицу; вот скриншот файла.

![дело:изображение_альтернативный_текст](create-table-by-using-border-lines-for-a-range_1.png)
