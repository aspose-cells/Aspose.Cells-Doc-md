---
title: Объединить несколько книг в одну книгу
linktitle: Слияние книг
type: docs
weight: 66
url: /ru/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Иногда нужно объединить рабочие книги с разным содержимым, таким как изображения, диаграммы и данные, в один файл. Aspose.Cells для Python via .NET поддерживает эту функцию. В этой статье показано, как создать консольное приложение в Visual Studio и объединить рабочие книги с помощью нескольких простых строк кода с использованием Aspose.Cells для Python via .NET.

{{% /alert %}}

## **Объединение книг с изображениями и диаграммами**

Пример кода объединяет две рабочие книги в одну с помощью Aspose.Cells для Python via .NET. Код загружает исходные рабочие книги, использует метод [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) для их объединения и сохраняет итоговую рабочую книгу.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **Продвинутые темы**
- [Объединение нескольких листов в один](/cells/ru/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Объединение файлов](/cells/ru/python-net/merge-files/)

