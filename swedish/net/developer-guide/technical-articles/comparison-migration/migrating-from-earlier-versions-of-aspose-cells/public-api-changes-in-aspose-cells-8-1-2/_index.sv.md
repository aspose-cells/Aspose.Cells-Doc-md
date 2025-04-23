---
title: Public API förändringar i Aspose.Cells 8.1.2
type: docs
weight: 60
url: /sv/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringar av Aspose.Cells API från version 8.1.1 till 8.1.2, som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagt stöd för varning om teckensnittsbyte uppstår**
Med Aspose.Cells for .NET 8.1.2 har WarningInfo, WarningType-klasser, IWarningCallback-gränssnittet och SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback-egenskaperna lagts till för att underlätta användaren att få varning om teckensnittsbyte uppstår vid konvertering av kalkylblad till bilder eller PDF-format. 

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Få varningar för teckensnittsbyte vid rendering av kalkylblad](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Raderad föråldrad PdfSaveOptions.ChartImageType Egenskap**
Aspose.Cells for .NET 8.1.2 har tagit bort den föråldrade PdfSaveOptions.ChartImageType-egenskapen från det offentliga API.
{{< app/cells/assistant language="csharp" >}}
