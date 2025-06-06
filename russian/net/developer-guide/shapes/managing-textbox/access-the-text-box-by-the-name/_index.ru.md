---
title: Доступ к текстовому полю по имени
type: docs
weight: 230
url: /ru/net/access-the-text-box-by-the-name/
---

## Доступ к текстовому полю по имени

Ранее текстовые поля получали доступ по индексу из коллекции [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes), но теперь вы также можете получить доступ к текстовому полю по имени из этой коллекции. Это удобный и быстрый способ получить доступ к вашему текстовому полю, если вы уже знаете его имя.

Приведенный ниже образец кода сначала создает текстовое поле и назначает ему некоторый текст и имя. Затем в следующих строках мы получаем доступ к тому же текстовому полю по его имени и печатаем его текст.

### Код на C# для доступа к текстовому полю по имени

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AccessTextBoxName-AccessTextBoxName.cs" >}}

### Вывод консоли, сгенерированный примерным кодом

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
