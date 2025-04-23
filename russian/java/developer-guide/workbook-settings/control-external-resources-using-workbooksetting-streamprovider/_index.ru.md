---
title: Управление внешними ресурсами с помощью WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /ru/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **Возможные сценарии использования**
Иногда ваш файл Excel содержит внешние ресурсы, например, связанные изображения и т. д. Aspose.Cells позволяет управлять этими внешними ресурсами с использованием [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider), который принимает реализацию интерфейса [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider). Когда вы попытаетесь отобразить вашу книгу, содержащую внешние ресурсы, например, связанные изображения, будут вызваны методы интерфейса [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider), которые позволят вам принять соответствующие действия для ваших внешних ресурсов.
## **Управление внешними ресурсами с помощью WorkbookSetting.StreamProvider**
Приведенный ниже образец кода объясняет использование [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). Он загружает [образец файла Excel](61767877.xlsx), содержащий связанное изображение. Код заменяет связанное изображение на [логотип Aspose](61767874.png) и отображает всю книгу в одно изображение с использованием класса [SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender). Ниже приведено скриншот, показывающий образец файла Excel и его [изображение для отображения](61767874.png) в качестве справки. Как видите, сломанное связанное изображение заменено логотипом Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
{{< app/cells/assistant language="java" >}}
