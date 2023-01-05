---
title: Управление загрузкой внешних ресурсов в книге MS Excel при рендеринге на PDF
type: docs
weight: 40
url: /ru/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Возможные сценарии использования**

Ваш файл Excel может содержать внешние ресурсы, например связанные изображения или объекты. Когда вы конвертируете свой файл Excel в PDF, Aspose.Cells извлекает эти внешние ресурсы и отображает их в PDF. Но иногда вы не хотите загружать эти внешние ресурсы и более того, вы хотите манипулировать ими. Вы можете сделать это, используя[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)который реализует[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)интерфейс.

## **Управление загрузкой внешних ресурсов в книге MS Excel при рендеринге на PDF**

В следующем примере кода объясняется, как использовать[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)контролировать загрузку внешних ресурсов и манипулировать ими. Пожалуйста, проверьте[образец файла Excel](50528353.xlsx)используется внутри кода и[вывод PDF](50528354.pdf)генерируется кодом.[Скриншот](50528357.png)показывает, как[старый внешний образ](50528356.png)в образце файла Excel был заменен на[новое изображение](50528355.png)на выходе PDF.

![дело:изображение_альтернативный_текст](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
