---
title: Укажите, как пересекать строки в выводимом HTML с использованием HtmlCrossType с Golang через C++
linktitle: Укажите HtmlCrossType в выводимом HTML
type: docs
weight: 140
url: /ru/go-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Узнайте, как управлять переполнением строк в HTML выводе с помощью Aspose.Cells for C++ и HtmlCrossType.
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, превышающую ширину ячейки, строка переполняется, если следующая ячейка в следующем столбце пустая или null. При сохранении файла Excel в HTML этот переполнение можно контролировать, задавая тип пересечения с помощью перечисления [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/). Оно включает следующие значения:

- **HtmlCrossType.Default**: Отображается как в MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка пересечется или будет усечена.

- **HtmlCrossType.MSExport**: Отображение строки как при экспорте HTML из MS Excel.

- **HtmlCrossType.Cross**: Отображение строки пересечения HTML, производительность при создании больших HTML-файлов будет более чем в десять раз быстрее, чем при установке значения Default или FitToCell.

- **HtmlCrossType.FitToCell**: отображает строку только внутри ширины ячейки.

## **Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType**

Следующий пример кода загружает [пример файла Excel](51740732.xlsx) и сохраняет его в формате HTML, задавая разные значения [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/). Пожалуйста, скачайте [выходные HTML](51740734.zip), созданные этим кодом. Пример файла Excel содержит изображение с красной рамкой, как показано на этом скриншоте, который демонстрирует эффект значений [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) на выводимый HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputHtmlUsingHtmlcrosstype.go" >}}
