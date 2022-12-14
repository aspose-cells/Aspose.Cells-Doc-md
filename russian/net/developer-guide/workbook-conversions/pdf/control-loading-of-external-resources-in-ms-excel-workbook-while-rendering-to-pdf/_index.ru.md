---
title: Управление загрузкой внешних ресурсов в книгу MS Excel при рендеринге в PDF
type: docs
weight: 40
url: /ru/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Возможные сценарии использования**

 Ваш файл Excel может содержать внешние ресурсы, например связанные изображения или объекты. Когда вы конвертируете файл Excel в PDF, Aspose.Cells извлекает эти внешние ресурсы и преобразует их в PDF. Но иногда вы не хотите загружать эти внешние ресурсы и более того, вы хотите манипулировать ими. Вы можете сделать это, используя[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)который реализует[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)интерфейс.

## **Управление загрузкой внешних ресурсов в книгу MS Excel при рендеринге в PDF**

 В следующем примере кода объясняется, как использовать[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) контролировать загрузку внешних ресурсов и манипулировать ими. Пожалуйста, проверьте[образец файла Excel](50528322.xlsx) используется внутри кода и[вывод PDF](50528325.pdf)генерируется кодом.[Скриншот](50528326.png) показывает, как[старый внешний образ](50528324.png) в образце файла Excel был заменен на[новое изображение](50528323.png) в выходном PDF.

![дело:изображение_альтернативный_текст](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
