---
title: Доступ и обновление частей форматированного текста Cell
linktitle: Расширенное форматирование текста
type: docs
weight: 40
url: /ru/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

 Aspose.Cells позволяет вам получать доступ и обновлять части форматированного текста ячейки. Для этой цели вы можете использовать[**Cell.Получить символы()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) и[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) методы. Эти методы будут возвращать и принимать массив[**Настройка шрифта**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)объекты, которые вы можете использовать для доступа и обновления различных свойств шрифта, таких как имя шрифта, цвет шрифта, жирность и т. д.

{{% /alert %}}

## **Доступ и обновление частей форматированного текста Cell**

 Следующий код демонстрирует использование[**Cell.Получить символы()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) и[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) метод с использованием[исходный файл excel](5112369.xlsx)который вы можете скачать по предоставленной ссылке. Исходный файл Excel содержит форматированный текст в ячейке A1. Он состоит из 3 частей, и каждая часть имеет свой шрифт. Следующий фрагмент кода обращается к этим частям и обновляет первую часть новым именем шрифта. Наконец, он сохраняет книгу как[выходной файл excel](5112366.xlsx) . Когда вы откроете его, вы обнаружите, что шрифт первой части текста изменился на**"Ариал"**.

### C# код для доступа и обновления частей форматированного текста Cell

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Консольный вывод, сгенерированный примером кода

 Вот вывод консоли приведенного выше примера кода с использованием[исходный файл excel](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

