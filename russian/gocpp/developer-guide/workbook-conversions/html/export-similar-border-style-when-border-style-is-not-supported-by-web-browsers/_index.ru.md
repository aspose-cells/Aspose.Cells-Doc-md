---
title: Экспортируйте похожие стили границ, когда стиль границы не поддерживается веб браузерами с помощью Golang через C++
linktitle: Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб браузерами
type: docs
weight: 70
url: /ru/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Узнайте, как экспортировать похожие стили границ, когда они неподдерживаются веб браузерами, с помощью Aspose.Cells и Golang через C++.
---

## **Возможные сценарии использования**

Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются веб-браузерами. При конвертации такого файла Excel в HTML с помощью Aspose.Cells такие границы будут удалены. Однако Aspose.Cells также может отображать такие границы с помощью свойства [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/). Установите его значение в **true**, и неподдерживаемые границы также будут экспортированы в HTML.

## **Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами**

Следующий пример загружает [пример файла Excel](64716806.xlsx), содержащий неподдерживаемые границы, как показано на скриншоте. Скриншот дополнительно иллюстрирует эффект свойства [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/) в выводимом HTML ([вывод HTML](64716804.zip)).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
