---
title: Доступ и обновление частей форматированного текста ячейки
linktitle: Редактирование текста с использованием разнообразного форматирования
type: docs
weight: 40
url: /ru/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Узнайте, как получить доступ к разделам обогащенного текста ячейки и обновить их с помощью API Aspose.Cells for .NET.
keywords: Получить доступ и обновить обогащенный текст ячейки, получить обогащенный текст ячейки, отредактировать обогащенный текст ячейки, получить доступ к обогащенному тексту ячейки, обновить обогащенный текст ячейки, изменить обогащенный текст ячейки
---

{{% alert color="primary" %}}

Aspose.Cells позволяет получить доступ к обновлению разделов обогащенного текста ячейки. Для этой цели вы можете использовать методы [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) и [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). Эти методы будут возвращать и принимать массивы объектов [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting), которые вы сможете использовать для доступа и обновления различных свойств шрифта, таких как имя шрифта, цвет шрифта, полужирный и т. д.

{{% /alert %}}

## **Доступ и обновление частей Rich Text ячейки**

Следующий код демонстрирует использование методов [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) и [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) с использованием [исходного файла Excel](5112369.xlsx), который вы можете скачать по предоставленной ссылке. Исходный файл Excel содержит обогащенный текст в ячейке A1. В нем 3 раздела и каждый раздел имеет разные шрифты. Следующий отрывок кода получает доступ к этим разделам и обновляет первый раздел с новым названием шрифта. Наконец, он сохраняет книгу как [выходной файл Excel](5112366.xlsx). Когда вы его откроете, вы увидите, что шрифт первого раздела текста изменен на **"Arial"**.

### Код на C#, чтобы получить доступ и обновить части форматированного текста ячейки

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Вывод консоли, сгенерированный примерным кодом

Вот вывод консоли приведенного выше образца кода с использованием [исходного файла Excel](5112369.xlsx).

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

{{< app/cells/assistant language="csharp" >}}
