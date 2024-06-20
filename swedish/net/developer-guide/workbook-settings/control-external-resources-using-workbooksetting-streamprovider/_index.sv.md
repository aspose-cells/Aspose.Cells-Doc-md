---
title: Styr externa resurser med hjälp av WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /sv/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **Möjliga användningsscenario**

Ibland innehåller din Excel-fil externa resurser t.ex. länkade bilder, etc. Aspose.Cells tillåter dig att kontrollera dessa externa resurser genom att använda [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) som tar implementationen av [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) gränssnittet. När du försöker rendera ditt kalkylblad som innehåller externa resurser t.ex. länkade bilder, kommer metoderna i [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) gränssnittet att anropas vilket gör det möjligt för dig att vidta lämpliga åtgärder för dina externa resurser.

## **Styr externa resurser med hjälp av WorkbookSetting.StreamProvider**

Följande kodexempel förklarar användningen av [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider). Den laddar [prov-Excel-filen](61767863.xlsx) som innehåller en länkad bild. Koden ersätter den länkade bilden med [Aspose-logotypen](61767862.png) och renderar hela arket till en enda bild med hjälp av [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) klassen. Följande skärmdump visar prov-Excel-filen och dess [renderade utdata-bild](61767865.png) som referens. Som du kan se ersätts den trasiga länkade bilden med Aspose-logotypen.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
