---
title: Lägg till PDF bokmärken med namngivna destinationer
type: docs
weight: 20
url: /sv/java/add-pdf-bookmarks-with-named-destinations/
---

## **Möjliga användningsscenario**

Namngivna destinationer är speciella typer av bokmärken eller länkar i PDF som inte är beroende av PDF-sidor. Det betyder att om sidor läggs till eller tas bort från PDF-filen kan bokmärken bli ogiltiga men namngivna destinationer kommer att förbli intakta. För att skapa namngiven destination, ange egenskapen [**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName).

## **Lägg till bokmärken i PDF med namngivna destinationer**

Se det följande kodexemplet, dess [käll-Excel-fil](50528370.xlsx) och dess [utdata-PDF-fil](50528369.pdf). Skärmbilden visar bokmärken och namngivna destinationer i den genererade PDF-filen. Skärmbilden beskriver även hur man visar namngivna destinationer och att du behöver Professional-versionen av Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}
