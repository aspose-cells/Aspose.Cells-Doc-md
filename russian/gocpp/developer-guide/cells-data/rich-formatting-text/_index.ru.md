---
title: Получение и обновление части богатого текста ячейки с помощью Golang через C++
linktitle: Редактирование текста с использованием разнообразного форматирования
type: docs
weight: 40
url: /ru/go-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Узнайте, как получать доступ и обновлять части форматированного текста ячейки через API Aspose.Cells for C++.
keywords: Получить доступ и обновить обогащенный текст ячейки, получить обогащенный текст ячейки, отредактировать обогащенный текст ячейки, получить доступ к обогащенному тексту ячейки, обновить обогащенный текст ячейки, изменить обогащенный текст ячейки
---

{{% alert color="primary" %}}

Aspose.Cells позволяет получить доступ к обновлению разделов обогащенного текста ячейки. Для этой цели вы можете использовать методы [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) и [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/). Эти методы будут возвращать и принимать массивы объектов [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/), которые вы сможете использовать для доступа и обновления различных свойств шрифта, таких как имя шрифта, цвет шрифта, полужирный и т. д.

{{% /alert %}}

## **Доступ и обновление частей Rich Text ячейки**

Следующий пример показывает использование методов [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) и [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) с помощью исходного файла Excel ([исходный файл](5112369.xlsx)). В исходном файле Excel в ячейке A1 есть богатый текст с 3 частями, каждая с разным шрифтом. Скрипт получает эти части и обновляет шрифт первой части на "Arial". Обновленная рабочая книга сохраняется как [выходной файл Excel](5112366.xlsx).

### C++ код для доступа и обновления частей богатого текста

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RichFormattingText.go" >}}
### Вывод консоли, сгенерированный примерным кодом

Вот вывод в консоль при использовании [исходного файла Excel](5112369.xlsx):

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
