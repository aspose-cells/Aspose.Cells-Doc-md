---
title: Anpassa alla kalkylbladskolumner på en enda PDF sida
type: docs
weight: 160
url: /sv/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Ibland vill du generera en PDF-fil där alla kalkylbladets kolumner passar på en sida. Egenskapen [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) tillhandahåller denna funktion på ett mycket lättanvänt sätt. Komplexa beräkningar som höjden och bredden på utdata-PDF:en hanteras internt och baseras på data i kalkylbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på en enda PDF-sida**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) ser till att alla kolumner i ett kalkylblad renderas till en enda PDF-sida, även om rader kan expandera till flera sidor beroende på data i kalkylbladet.

Exempelkoden nedan visar hur du använder [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)-egenskapen för att rendera ett stort kalkylblad med 100 kolumner.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den genererade PDF-filen visa innehållet i väldigt liten storlek. Det är fortfarande läsbart när det skalas upp i en visningsapplikation som Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
