---
title: Изменения в публичном API Aspose.Cells 8.1.2
type: docs
weight: 70
url: /ru/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.1.1 до 8.1.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные открытые методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлена поддержка предупреждений при замене шрифта**
В Aspose.Cells for Java 8.1.2 были добавлены классы WarningInfo и WarningType, интерфейс IWarningCallback, а также свойства SaveOptions.WarningCallback и ImageOrPrintOptions.WarningCallback, чтобы разработчики могли получать предупреждения при замене шрифтов при конвертации электронных таблиц в изображения, форматы XPS и PDF. 

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со подробной статьей о [Получение предупреждений при замене шрифта при визуализации электронных таблиц](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) для получения дополнительной информации.

{{% /alert %}}
## **Удален устаревшее свойство PdfSaveOptions.ChartImageType**
Aspose.Cells for Java 8.1.2 удалил устаревшее свойство PdfSaveOptions.ChartImageType из публичного API.
{{< app/cells/assistant language="java" >}}
