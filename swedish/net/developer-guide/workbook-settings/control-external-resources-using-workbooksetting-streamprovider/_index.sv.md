---
title: Styr externa resurser med WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /sv/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **Möjliga användningsscenarier**

Ibland innehåller din Excel-fil externa resurser t.ex. länkade bilder etc. Aspose.Cells låter dig styra dessa externa resurser med hjälp av[**Arbetsbok.Inställningar.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)som tar genomförandet av[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)gränssnitt. Närhelst du försöker rendera ditt kalkylblad som innehåller externa resurser t.ex. länkade bilder, metoderna för[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)gränssnitt kommer att anropas vilket gör att du kan vidta lämpliga åtgärder för dina externa resurser.

## **Styr externa resurser med WorkbookSetting.StreamProvider**

Följande exempelkod förklarar användningen av[**Arbetsbok.Inställningar.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) . Den laddar[exempel på Excel-fil](61767863.xlsx) som innehåller en länkad bild. Koden ersätter den länkade bilden med[Aspose Logotyp](61767862.png) och renderar hela arket till en enda bild med hjälp av[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) klass. Följande skärmdump visar exemplet på Excel-filen och dess[renderad utdatabild](61767865.png) för en referens. Som du kan se är den trasiga länkade bilden ersatt med Aspose Logotyp.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
