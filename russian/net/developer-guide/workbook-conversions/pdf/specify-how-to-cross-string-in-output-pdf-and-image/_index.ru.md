---
title: Указание того, как пересекать строку в выходном PDF и изображении
type: docs
weight: 120
url: /ru/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, то строка переполняется, если следующая ячейка в следующем столбце пуста или пуста. Когда вы сохраняете свой файл Excel в PDF / изображение, вы можете контролировать это переполнение, указав тип пересечения с использованием перечисления [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Оно имеет следующие значения

- **TextCrossType.Default**: Отображает текст как MS Excel, который зависит от следующей ячейки. Если следующая ячейка пуста, строка будет пересечена или обрезана.

- **TextCrossType.CrossKeep**: Отображает строку как экспорт MS Excel в PDF/изображение

- **TextCrossType.CrossOverride**: Отображает весь текст, пересекая другие ячейки и заменяя текст перекрываемых ячеек

- **TextCrossType.StrictInCell**: Отображать только строку в пределах ширины ячейки.

## **Указание того, как пересекать строку в выходном PDF/изображении с использованием TextCrossType**

В следующем примере кода загружается образец файла Excel и сохраняется в формат PDF/изображение, указав разные [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Образец файла Excel и выходные файлы можно скачать по следующим ссылкам:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
