---
title: Контроль загрузки внешних ресурсов в книге MS Excel во время преобразования в PDF
type: docs
weight: 40
url: /ru/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Возможные сценарии использования**

Ваш файл Excel может содержать внешние ресурсы, например, связанные изображения или объекты. При конвертации вашего файла Excel в PDF, Aspose.Cells извлекает эти внешние ресурсы и отображает их в PDF. Но иногда вам не нужно загружать эти внешние ресурсы, и более того, вы хотите их изменить. Это можно сделать с помощью [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider), реализующего интерфейс [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider).

## **Контроль загрузки внешних ресурсов в книге MS Excel во время преобразования в PDF**

В следующем примере кода объясняется, как использовать [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) для контроля загрузки внешних ресурсов и их изменения. Пожалуйста, проверьте [образец файла Excel](50528322.xlsx), использующийся в коде, и [выходной PDF](50528325.pdf), сгенерированный кодом. [Скриншот](50528326.png) показывает, как [старое внешнее изображение](50528324.png) в примерном файле Excel было заменено на [новое изображение](50528323.png) в выходном PDF.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
