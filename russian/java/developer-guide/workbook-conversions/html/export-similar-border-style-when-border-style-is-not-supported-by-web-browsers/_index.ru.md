---
title: Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб браузерами
type: docs
weight: 70
url: /ru/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Возможные сценарии использования**

Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются веб-браузерами. Когда вы преобразовываете такой файл Excel в HTML с помощью Aspose.Cells, такие границы удаляются. Однако Aspose.Cells также может поддерживать отображение аналогичных границ с [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle). Пожалуйста, установите его значение **true**, и неподдерживаемые границы также будут экспортированы в файл HTML.

## **Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами**

Следующий образец кода загружает [образец файла Excel](64716832.xlsx), который содержит неподдерживаемые границы, как показано на следующем снимке экрана. Снимок экрана дополнительно иллюстрирует эффект свойства [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) внутри [выходного HTML](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
