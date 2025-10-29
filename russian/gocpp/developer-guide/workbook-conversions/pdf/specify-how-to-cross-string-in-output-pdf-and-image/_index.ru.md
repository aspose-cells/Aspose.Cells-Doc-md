---
title: Укажите, как пересекать строки в выводимом PDF и изображениях с помощью Golang через C++
linktitle: Указание того, как пересекать строку в выходном PDF и изображении
type: docs
weight: 120
url: /ru/go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Узнайте, как управлять переполнением текста в PDF и изображениях с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку длиной больше ширины ячейки, содержимое переполняет ячейку, если следующая ячейка в следующем столбце пуста или отсутствует. Сохраняя файл Excel в PDF или изображение, вы можете управлять этим переполнением, задавая тип обрезки, используя перечисление [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). В нем есть следующие значения:

- **TextCrossType.Default**: отображать текст как в MS Excel, что зависит от следующей ячейки. Если следующая ячейка пуста, строка будет обрезана или укорочена.

- **TextCrossType.CrossKeep**: отображать строку как в MS Excel при экспорте в PDF/изображение.

- **TextCrossType.CrossOverride**: отображать весь текст, пересекающий другие ячейки, и переопределять содержимое пересекаемых ячеек.

- **TextCrossType.StrictInCell**: Отображать только строку в пределах ширины ячейки.

## **Указание того, как пересекать строку в выходном PDF/изображении с использованием TextCrossType**

Следующий пример загружает пример файла Excel и сохраняет его в формате PDF/изображение, задавая разные [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). Образец файла Excel и выходные файлы можно скачать по ссылкам ниже:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Образец кода

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}
