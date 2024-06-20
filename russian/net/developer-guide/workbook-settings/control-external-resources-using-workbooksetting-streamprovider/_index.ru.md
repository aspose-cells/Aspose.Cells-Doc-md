---
title: Управление внешними ресурсами с помощью WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /ru/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **Возможные сценарии использования**

Иногда ваш файл Excel содержит внешние ресурсы, например, связанные изображения и т. Д. Aspose.Cells позволяет управлять этими внешними ресурсами с помощью [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider), который принимает реализацию интерфейса [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider). Всякий раз, когда вы попытаетесь отобразить свой лист, содержащий внешние ресурсы, например, связанные изображения, будут вызваны методы интерфейса [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider), что позволит вам принять соответствующие меры по отношению к внешним ресурсам.

## **Управление внешними ресурсами с помощью WorkbookSetting.StreamProvider**

Следующий пример кода объясняет использование [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider). Он загружает [образец файла Excel](61767863.xlsx), содержащий связанное изображение. Код заменяет связанное изображение на [логотип Aspose](61767862.png) и отображает весь лист в одно изображение, используя класс [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender). Ниже приведен скриншот образца файла Excel и его [изображение рендеринга](61767865.png) для справки. Как видно, сломанное связанное изображение заменено на логотип Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
