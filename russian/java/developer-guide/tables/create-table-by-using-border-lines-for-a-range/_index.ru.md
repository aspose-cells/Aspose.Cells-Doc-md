---
title: Создание таблицы с использованием граничных линий для диапазона
type: docs
weight: 50
url: /ru/java/create-table-by-using-border-lines-for-a-range/
description: Как создать таблицу с диапазоном с использованием граничных линий. Aspose.Cells for Java предоставляет простой в использовании API, который можно использовать для добавления границ к диапазону.
keywords: создать таблицу, диапазон в таблицу, диапазон в таблицу excel, excel диапазон в таблицу, диапазон в таблицу с границами, как создать таблицу из диапазона, преобразовать диапазон в таблицу, excel преобразовать диапазон в таблицу, excel создать таблицу, диапазон в таблицу java 
---

{{% alert color="primary" %}}

Иногда вы хотите создать таблицу, добавив граничные линии для диапазона/cellArea на основе адреса у вас есть. Вы можете использовать метод [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) для создания диапазона ячеек. Метод [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) возвращает объект [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range). Вы можете создать объект [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) и указать соответствующие параметры границы (верхняя, левая, нижняя, правая). Позже вы можете получить ячейки из [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) и применить ваше желаемое форматирование к ячейкам.

{{% /alert %}}

В следующем примере показано, как создать [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) и указать граничные линии для диапазона ячеек.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

После выполнения кода выше мы можем получить созданный файл Excel, содержащий отформатированную таблицу; вот скриншот файла.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
