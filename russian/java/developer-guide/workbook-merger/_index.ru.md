---
title: Объединить несколько книг в одну книгу
linktitle: Слияние книг
type: docs
weight: 50
url: /ru/java/combine-multiple-workbooks-into-a-single-workbook/
description: Объедините несколько книг в одну книгу, используя Java код и Aspose.Cells for Java API.
keywords: объединить несколько рабочих книг в одну, объединить несколько рабочих книг в одну java, объединить несколько рабочих книг в одну с помощью java, объединить несколько рабочих книг в одну рабочую книгу с помощью java, объединить несколько рабочих книг в одну рабочую книгу java, java код для объединения нескольких рабочих книг в одну рабочую книгу, как объединить несколько рабочих книг в одну рабочую книгу с помощью java, как объединить несколько рабочих книг в одну с помощью java, объединить несколько рабочих книг в одну с помощью java, как объединить несколько рабочих книг в одну java, как объединить несколько рабочих книг в одну с помощью java
---

{{% alert color="primary" %}}

Иногда вам может понадобиться объединить рабочие книги с различным содержанием, таким как изображения, диаграммы и данные в одну рабочую книгу. Aspose.Cells поддерживает эту функцию. В этой статье показано, как создать простое приложение для объединения рабочих книг всего лишь с несколькими простыми строками кода, используя Aspose.Cells.

{{% /alert %}}

## **Объединение рабочих книг**

В приведенном примере кода две рабочие книги объединяются в одну рабочую книгу с помощью Aspose.Cells for Java. Код загружает исходные рабочие книги, использует метод [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)), чтобы объединить их и сохраняет вывод рабочую книгу.

### **Исходные книги**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Выходные книги**

- [combined.xlsx](5473095.xlsx)

### **Скриншоты**

Ниже приведены скриншоты исходной и выходной книг.

{{% alert color="primary" %}}

Вы можете использовать любые исходные книги. Эти изображения приведены только в целях иллюстрации.

{{% /alert %}}

**Первый лист книги с диаграммами - столбцы**

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Второй лист книги с диаграммами - линейный**

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Первый лист книги с картинками - изображение**

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Все три листа в объединенной книге - столбцы, линейный, изображение**

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

В следующем отрывке кода показано, как объединить несколько рабочих книг в одну рабочую книгу.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CombineMultipleWorkbooks-CombineMultipleWorkbooks.java" >}}

## **Дополнительные ресурсы**

{{% alert color="primary" %}}

Вам могут пригодиться статья [Объединение нескольких листов в одном документе](/cells/ru/java/combine-multiple-worksheets-into-a-single-worksheet/), чтобы получить дополнительную информацию.

{{% /alert %}}

## **Продвинутые темы**
- [Объединение нескольких листов в одном документе](/cells/ru/java/combine-multiple-worksheets-into-a-single-worksheet/)
- [Объединение файлов](/cells/ru/java/merge-files/)

