---
title: Styr externa resurser med hjälp av WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /sv/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **Möjliga användningsscenario**
Ibland innehåller din Excel-fil externa resurser, t.ex. länkade bilder, etc. Aspose.Cells låter dig styra dessa externa resurser med hjälp av Workbook.Settings.StreamProvider som tar implementeringen av IStreamProvider-gränssnittet. När du försöker rendera ditt arbetsblad som innehåller externa resurser, t.ex. länkade bilder, kommer metoderna i IStreamProvider-gränssnittet att anropas vilket ger dig möjlighet att vidta lämpliga åtgärder för dina externa resurser.
## **Styr externa resurser med hjälp av WorkbookSetting.StreamProvider**
Följande exempelkod förklarar användningen av Workbook.Settings.StreamProvider. Den läser in den [exempel-Excel-filen](61767877.xlsx) som innehåller en länkad bild. Koden ersätter den länkade bilden med [Aspose-logotypen](61767874.png) och renderar hela bladet till en enda bild med hjälp av klassen SheetRender. Följande skärmdump visar exempel-Excel-filen och dess [renderade bild](61767874.png) för referens. Som du kan se ersätts den trasiga länkade bilden med Aspose-logotypen.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
{{< app/cells/assistant language="java" >}}
