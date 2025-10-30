---
title: Konvertera Excel fil till PDF format som är kompatibelt med PDFA 1a med Golang via C++
linktitle: Konvertera Excelfil till PDF format kompatibelt med PDFA 1a
type: docs
weight: 130
url: /sv/go-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Lär dig hur du konverterar Excel filer till PDF/A 1a kompatibla PDF format med Aspose.Cells med Golang via C++
---

## **Möjliga användningsscenario**

PDF/A är en unik variant av PDF designad för långsiktigt bevarande av dokument. PDF/A är en ISO-standardiserad version av det bärbara dokumentformatsformatet (PDF) som är ett arkivformat för PDF som inbäddar alla typsnitt som används i dokumentet inom PDF-filen. PDF/A skiljer sig från PDF genom att förbjuder funktioner som typsnittlänkning (i stället för typsnittsinbäddning) och kryptering. Aspose.Cells gör det möjligt att spara Excel-filer till PDF/A-kompatibla PDF-filer (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u stöds). Denna guide beskriver hur man sparar arbetsboken i PDF/A-kompatibelt PDF-format.

## **Konvertera Excel-fil till PDF-format kompatibelt med PDF/A-1a**

Utvecklare kan använda klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) för att ställa in olika attribut för konverteringen. Att ställa in olika egenskaper för klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) ger dig kontroll över utskrift, typsnitt, säkerhet och kompressionsinställningar för den valda PDF-filen. Den viktigaste egenskapen är [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/), som gör att du kan spara Excel-filer till PDF/A-kompatibla PDF-filer.

Följande provkod förklarar hur man konverterar Excel-fil till PDF-format kompatibelt med PDF/A-1a. Se [utmatnings-PDF](outputCompliancePdfA1a.pdf) samt skärmbilden för referens.

## **Skärmdump**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelFileToPdfFormatCompatibleWithPdfa1a.go" >}}
