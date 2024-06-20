---
title: Изменения в публичном API Aspose.Cells 8.1.2
type: docs
weight: 60
url: /ru/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.1.1 до 8.1.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные открытые методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлена поддержка предупреждений при замене шрифта**
С Aspose.Cells for .NET 8.1.2 были добавлены классы WarningInfo, WarningType, интерфейс IWarningCallback и свойства SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback, чтобы облегчить пользователю получение предупреждений, если происходит замена шрифта при преобразовании электронных таблиц в изображения или формат PDF. 

{{% alert color="primary" %}} 

Пожалуйста, проверьте подробную статью на [Получение предупреждений о замене шрифта при визуализации электронных таблиц](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Удален устаревшее свойство PdfSaveOptions.ChartImageType**
Aspose.Cells for .NET 8.1.2 удалило устаревшее свойство PdfSaveOptions.ChartImageType из общедоступного API.
