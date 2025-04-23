---
title: Public API förändringar i Aspose.Cells 8.1.2
type: docs
weight: 70
url: /sv/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringar av Aspose.Cells API från version 8.1.1 till 8.1.2, som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagt stöd för varning om teckensnittsbyte uppstår**
Med Aspose.Cells for Java 8.1.2 har klasserna WarningInfo och WarningType, gränssnittet IWarningCallback, och egenskaperna SaveOptions.WarningCallback och ImageOrPrintOptions.WarningCallback lagts till för att låta utvecklare ta emot varningar när teckensnittsutbyte sker vid konvertering av kalkylblad till bilder, XPS- & PDF-format. 

{{% alert color="primary" %}} 

Se den detaljerade artikeln om [Få varningar för teckensnittsutbyte vid rendering av kalkylblad](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) för mer information.

{{% /alert %}}
## **Raderad föråldrad PdfSaveOptions.ChartImageType Egenskap**
Aspose.Cells for Java 8.1.2 har tagit bort den föråldrade egenskapen PdfSaveOptions.ChartImageType från den offentliga API:en.
{{< app/cells/assistant language="java" >}}
