---
title: Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML с помощью Golang через C++
linktitle: Скрытие перекрывающегося контента с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Используйте CrossHideRight с Aspose.Cells в C++, чтобы скрывать перекрытый контент при сохранении в HTML.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML вы можете указать разные типы перекрестий для строк ячеек. По умолчанию Aspose.Cells генерирует HTML согласно Microsoft Excel, однако при изменении типа пересечения на [**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype) он скрывает все строки справа в ячейке, которые перекрываются или налегают на содержимое ячейки.

## **Скрытие перекрывающегося содержимого с CrossHideRight при сохранении в Html**

Следующий пример загружает [пример файла Excel](64716894.xlsx) и сохраняет его в [вывод HTML](64716893.zip) после установки [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/) в [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). Скриншот показывает, как [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) влияет на вывод HTML по сравнению со стандартным выводом.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
