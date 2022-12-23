---
title: Anpassa alla kalkylbladskolumner på en PDF sida
type: docs
weight: 160
url: /sv/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 Ibland vill du skapa en PDF-fil som passar alla ett kalkylblads kolumner på en sida. De[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) egenskapen tillhandahåller denna funktion på ett mycket lättanvänt sätt. Komplexa beräkningar som höjd och bredd på utdata PDF hanteras internt och baseras på uppgifterna i arbetsbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på enstaka PDF sida**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)ser till att alla kolumner i ett kalkylblad renderas till en enda PDF-sida, även om rader kan utökas till flera sidor beroende på data i kalkylbladet.

Exempelkoden nedan visar hur du använder[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)egenskap för att återge ett stort kalkylblad med 100 kolumner.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den renderade PDF-filen visa innehållet i en mycket liten storlek. Det är fortfarande läsbart när det skalas upp i ett visningsprogram som Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler är det bäst att ringa[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
