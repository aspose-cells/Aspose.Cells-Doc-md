---
title: Konvertera Excelfil till PDF format kompatibelt med PDFA 1a
type: docs
weight: 80
url: /sv/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Möjliga användningsscenario**

PDF/A är en unik variant av PDF som är utformad för långsiktig bevarande av dokument. PDF/A är en ISO-standardiserad version av den bärbara dokumentformatet (PDF), vilket är ett arkivformat av PDF som inbäddar alla använda typsnitt i dokumentet inom PDF-filen. PDF/A skiljer sig från PDF genom att förbjuda funktioner, såsom typsnittlänkning (till skillnad från typsnittsinbäddning) och kryptering. Aspose.Cells möjliggör att du kan spara Excel-filer till PDF/A-kompatibla PDF-filer (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u stöds). Detta ämne beskriver hur du sparar Excel-arbetsboken till en PDF-fil som är PDF/A-kompatibel (PDF/A-1a).

## **Konvertera Excel-fil till PDF-format kompatibelt med PDF/A-1a**

Utvecklare kan använda klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) för att ställa in olika attribut för konverteringen. Genom att ställa in olika egenskaper hos klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) kan du styra utskrift, teckensnitt, säkerhet och komprimeringsinställningar för den utgående PDF:en. Den viktigaste egenskapen är [PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) som gör att du kan spara Excel-filer som PDF/A-kompatibla PDF-filer.

Följande provkod förklarar hur man konverterar Excel-fil till PDF-format kompatibelt med PDF/A-1a. Se [utmatnings-PDF](outputCompliancePdfA1a.pdf) samt en skärmbild för referens.

## **Skärmdump**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
{{< app/cells/assistant language="java" >}}
