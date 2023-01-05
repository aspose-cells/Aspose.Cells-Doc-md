---
title: Управление внешними ресурсами с помощью WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /ru/java/control-external-resources-using-workbooksetting-streamprovider/
---
## **Возможные сценарии использования**
Иногда ваш файл Excel содержит внешние ресурсы, например связанные изображения и т. д. Aspose.Cells позволяет вам управлять этими внешними ресурсами с помощью[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)который предполагает реализацию[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)интерфейс. Всякий раз, когда вы пытаетесь отобразить свой рабочий лист, содержащий внешние ресурсы, например связанные изображения, методы[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)будет вызван интерфейс, который позволит вам предпринять соответствующие действия для ваших внешних ресурсов.
## **Управление внешними ресурсами с помощью WorkbookSetting.StreamProvider**
В следующем примере кода объясняется использование[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). Он загружает[образец файла Excel](61767877.xlsx)содержащий связанное изображение. Код заменяет связанное изображение на[Aspose Логотип](61767874.png)и отображает весь лист в одно изображение, используя[Листрендеринг](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)учебный класс. На следующем снимке экрана показан пример файла Excel и его[визуализированное выходное изображение](61767874.png)для справки. Как видите, неработающее связанное изображение заменено логотипом Aspose.

![дело:изображение_альтернативный_текст](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
