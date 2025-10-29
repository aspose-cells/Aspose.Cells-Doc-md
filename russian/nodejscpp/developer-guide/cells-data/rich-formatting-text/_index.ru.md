---
title: Доступ и обновление частей форматированного текста ячейки
linktitle: Редактирование текста с использованием разнообразного форматирования
type: docs
weight: 40
url: /ru/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Узнайте, как получить доступ и обновлять части богатого текста ячейки через API Aspose.Cells for Node.js via C++.
keywords: Получить доступ и обновить обогащенный текст ячейки, получить обогащенный текст ячейки, отредактировать обогащенный текст ячейки, получить доступ к обогащенному тексту ячейки, обновить обогащенный текст ячейки, изменить обогащенный текст ячейки
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ позволяет получать доступ и обновлять части богатого текста ячейки. Для этого вы можете использовать методы [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) и [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). Эти методы возвращают и принимают массив объектов [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting), который можно использовать для доступа и обновления различных свойств шрифта, таких как название шрифта, цвет шрифта, жирность и т.д.

{{% /alert %}}

## **Доступ и обновление частей Rich Text ячейки**

Следующий код демонстрирует использование методов [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) и [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) с помощью [исходного файла Excel](5112369.xlsx), который можно скачать по предоставленной ссылке. Исходный файл содержит богатый текст в ячейке A1 с тремя частями, каждая из которых имеет разный шрифт. Следующий фрагмент кода получает эти части и обновляет первую частью с новым названием шрифта. В конце он сохраняет файл как [выходной файл Excel](5112366.xlsx). При открытии вы увидите, что шрифт первой части текста изменился на **"Arial"**.

### Код Node.js для доступа к частям богатого текста ячейки и их обновления

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

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

{{< app/cells/assistant language="nodejs-cpp" >}}
