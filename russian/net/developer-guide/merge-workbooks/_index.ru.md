---
title: Объединить несколько книг в одну книгу
linktitle: Слияние книг
type: docs
weight: 66
url: /ru/net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Иногда вам нужно объединить книги с различным содержанием, таким как изображения, диаграммы и данные, в одну книгу. Aspose.Cells поддерживает эту функцию. В этой статье показано, как создать консольное приложение в Visual Studio и объединить книги с помощью Aspose.Cells с помощью нескольких простых строк кода.

{{% /alert %}}

## **Объединение книг с изображениями и диаграммами**

Приведенный пример кода объединяет две книги в одну книгу с помощью Aspose.Cells. Код загружает исходные книги, использует метод [**Workbook.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) для их объединения и сохраняет выходную книгу.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **Продвинутые темы**
- [Объединение нескольких листов в один](/cells/ru/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Объединение файлов](/cells/ru/net/merge-files/)
