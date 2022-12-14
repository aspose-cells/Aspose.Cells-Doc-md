---
title: Общедоступный API Изменения в Aspose.Cells 8.1.2
type: docs
weight: 70
url: /ru/java/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.1.1 до 8.1.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлена поддержка предупреждения о замене шрифта.**
В версии Aspose.Cells for Java 8.1.2 были добавлены классы WarningInfo и WarningType, интерфейс IWarningCallback и свойства SaveOptions.WarningCallback и ImageOrPrintOptions.WarningCallback, позволяющие разработчикам получать предупреждения о замене шрифта при преобразовании электронных таблиц в изображения, форматы XPS и PDF.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Получение предупреждений о замене шрифта при рендеринге электронных таблиц](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) Чтобы получить больше информации.

{{% /alert %}}
## **Удалено устаревшее свойство PdfSaveOptions.ChartImageType**
Aspose.Cells for Java 8.1.2 удалил устаревшее свойство PdfSaveOptions.ChartImageType из общего доступа API.
