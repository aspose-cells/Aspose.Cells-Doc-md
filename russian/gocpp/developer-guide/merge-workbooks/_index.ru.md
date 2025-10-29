---
title: Объедините несколько рабочих книг в одну с помощью Golang через C++
linktitle: Слияние книг
type: docs
weight: 66
url: /ru/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Узнайте, как объединить несколько рабочих книг в одну, используя Aspose.Cells с Golang через C++.
---

{{% alert color="primary" %}}

Иногда необходимо объединить рабочие книги с различным содержимым, таким как изображения, диаграммы и данные, в одну книгу. Aspose.Cells поддерживает эту функцию. Эта статья показывает, как создать консольное приложение в Visual Studio и объединить рабочие книги с помощью нескольких простых строк кода Aspose.Cells.

{{% /alert %}}

## **Объединение книг с изображениями и диаграммами**

Приведенный пример кода объединяет две книги в одну книгу с помощью Aspose.Cells. Код загружает исходные книги, использует метод [**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) для их объединения и сохраняет выходную книгу.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **Продвинутые темы**
- [Объединение нескольких листов в один](/cells/ru/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Объединение файлов](/cells/ru/cpp/merge-files/)
