---
title: Объединение нескольких листов в один лист
type: docs
weight: 70
url: /ru/java/combine-multiple-worksheets-into-a-single-worksheet/
description: Объединение нескольких листов в один лист с использованием кода Java и API Aspose.Cells for Java.
keywords: объединить несколько листов в один, объединить несколько листов в один java, объединить несколько листов в один с помощью java, объединить несколько листов в один лист с помощью java, объединить несколько листов в один лист java, java код для объединения нескольких листов в один лист, как объединить несколько листов в один лист с помощью java, как объединить несколько листов в один с помощью java, объединить несколько листов в один с помощью java, как объединить несколько листов в один java, как объединить несколько листов в один с помощью java
---

{{% alert color="primary" %}}

Иногда вам нужно объединить несколько листов в один. Это легко сделать с помощью API Aspose.Cells. В этой статье будет показан пример кода, который читает исходную книгу и объединяет данные всех исходных листов в один лист внутри целевой книги.

{{% /alert %}}

## **Как объединить листы**

В приведенном ниже образце использован метод [**Range.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#copy-com.aspose.cells.Range-) для копирования всех исходных листов в один лист внутри целевой книги.

### **Исходная рабочая книга**

Вы можете использовать любую исходную рабочую книгу. В этом примере мы используем исходную рабочую книгу, в которой есть три листа.

**Лист 1**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_1.jpg)

**Лист 2**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_2.jpg)

**Лист 3**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_3.jpg)

### **Выходная рабочая книга**

Запуск следующего кода создает рабочую книгу с одним листом, содержащим данные всех трех листов.

**На выходном листе теперь содержатся данные всех 3 исходных листов**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_4.jpg)

## **Загрузить исходную рабочую книгу и выходную рабочую книгу**

- [Исходная рабочая книга](5473078.xlsx)
- [Выходная рабочая книга](5473079.xlsx)

### **Пример кода для объединения нескольких листов в один лист**

Приведенный ниже фрагмент кода показывает, как объединить несколько листов в один лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CombineMultipleWorksheets-CombineMultipleWorksheets.java" >}}

## **Дополнительные ресурсы**

{{% alert color="primary" %}}

Вы можете найти полезной статью [Объединение нескольких рабочих книг в одну рабочую книгу](/cells/ru/java/combine-multiple-workbooks-into-a-single-workbook/) для получения дополнительной информации.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
