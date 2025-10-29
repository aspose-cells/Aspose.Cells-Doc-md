---
title: Доступ и обновление частей форматированного текста ячейки
linktitle: Редактирование текста с использованием разнообразного форматирования
type: docs
weight: 40
url: /ru/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: Узнайте, как получить доступ и обновить части форматированного текста ячейки с помощью Aspose.Cells for Python via .NET API.
keywords: Библиотека Python для Excel, Доступ и обновление форматированного текста ячейки на Python, Получить форматированный текст ячейки на Python, Редактировать форматированный текст ячейки на Python, Доступ к форматированному тексту ячейки на Python, Обновить форматированный текст ячейки на Python, Изменить форматированный текст ячейки на Python.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET позволяет получить доступ и обновить части форматированного текста ячейки. Для этого вы можете использовать методы [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) и [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list). Эти методы будут возвращать и принимать массивы объектов [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting), которые можно использовать для доступа и обновления различных свойств шрифта, таких как имя шрифта, цвет шрифта, полужирность и т. д.

{{% /alert %}}

## **Доступ и обновление частей Rich Text ячейки**

В следующем коде демонстрируется использование методов [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) и [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) с использованием [исходного файла excel](5112369.xlsx), который вы можете загрузить по предоставленной ссылке. Исходный файл Excel содержит форматированный текст в ячейке A1. В нем 3 части и каждая часть имеет разный шрифт. Приведенный ниже фрагмент кода получает доступ к этим частям и обновляет первую часть новым именем шрифта. Наконец, он сохраняет книгу как [файл excel результата](5112366.xlsx). При открытии вы увидите, что шрифт первой части текста изменился на **"Arial"**.

### Код на C#, чтобы получить доступ и обновить части форматированного текста ячейки

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
