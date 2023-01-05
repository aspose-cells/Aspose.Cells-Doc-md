---
title: Управление внешними ресурсами с помощью WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /ru/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **Возможные сценарии использования**

Иногда ваш файл Excel содержит внешние ресурсы, например связанные изображения и т. д. Aspose.Cells позволяет вам управлять этими внешними ресурсами с помощью[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)что предполагает реализацию[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)интерфейс. Всякий раз, когда вы пытаетесь отобразить свой рабочий лист, содержащий внешние ресурсы, например связанные изображения, методы[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)будет вызван интерфейс, который позволит вам предпринять соответствующие действия для ваших внешних ресурсов.

## **Управление внешними ресурсами с помощью WorkbookSetting.StreamProvider**

Следующий пример кода объясняет использование[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) . Он загружает[образец файла Excel](61767863.xlsx) содержащий связанное изображение. Код заменяет связанное изображение на[Aspose Логотип](61767862.png) и отображает весь лист в одно изображение, используя[**Листрендеринг**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) учебный класс. На следующем снимке экрана показан пример файла Excel и его[визуализированное выходное изображение](61767865.png) для справки. Как видите, неработающее связанное изображение заменено логотипом Aspose.

![дело:изображение_альтернативный_текст](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
