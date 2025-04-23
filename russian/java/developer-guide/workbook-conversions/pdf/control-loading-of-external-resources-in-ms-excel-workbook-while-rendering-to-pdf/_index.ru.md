---
title: Контроль загрузки внешних ресурсов в книге MS Excel во время преобразования в PDF
type: docs
weight: 40
url: /ru/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Возможные сценарии использования**

Ваш файл Excel может содержать внешние ресурсы, такие как связанные изображения или объекты. При преобразовании файла Excel в PDF, Aspose.Cells извлекает эти внешние ресурсы и преобразует их в PDF. Но иногда вам не нужно загружать эти внешние ресурсы, а кроме этого, вы хотите их изменить. Вы можете сделать это, используя [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider), который реализует интерфейс [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider).

## **Контроль загрузки внешних ресурсов в книге MS Excel во время преобразования в PDF**

Следующий образец кода объясняет, как использовать [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) для контроля загрузки внешних ресурсов и их изменения. Пожалуйста, проверьте [образец файла Excel](50528353.xlsx), используемый внутри кода и [выходной PDF](50528354.pdf), сгенерированный кодом. [Снимок экрана](50528357.png) показывает, как [старое внешнее изображение](50528356.png) в образцовом файле Excel было заменено на [новое изображение](50528355.png) в выходном PDF.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
{{< app/cells/assistant language="java" >}}
