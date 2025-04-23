---
title: Konvertera Excelfil till PDF format kompatibelt med PDFA 1a
type: docs
weight: 130
url: /sv/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Möjliga användningsscenario**

PDF/A är en unik variant av PDF som är utformad för långsiktig bevarande av dokument. PDF/A är en ISO-standardiserad version av den bärbara dokumentformatet (PDF), vilket är ett arkivformat av PDF som inbäddar alla använda typsnitt i dokumentet inom PDF-filen. PDF/A skiljer sig från PDF genom att förbjuda funktioner, såsom typsnittlänkning (till skillnad från typsnittsinbäddning) och kryptering. Aspose.Cells möjliggör att du kan spara Excel-filer till PDF/A-kompatibla PDF-filer (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u stöds). Detta ämne beskriver hur du sparar Excel-arbetsboken till en PDF-fil som är PDF/A-kompatibel (PDF/A-1a).

## **Konvertera Excel-fil till PDF-format kompatibelt med PDF/A-1a**

Utvecklare kan använda klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) för att ställa in olika attribut för konverteringen. Genom att ställa in olika egenskaper för klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) får du kontroll över utskrifts-, teckensnitts-, säkerhets- och komprimeringsinställningar för utmatnings-PDF-filen. Den viktigaste egenskapen är [**PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) som gör det möjligt att spara Excel-filer till PDF/A-kompatibla PDF-filer.

Följande provkod förklarar hur man konverterar Excel-fil till PDF-format kompatibelt med PDF/A-1a. Se [utmatnings-PDF](outputCompliancePdfA1a.pdf) samt skärmbilden för referens.

## **Skärmdump**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
{{< app/cells/assistant language="csharp" >}}
