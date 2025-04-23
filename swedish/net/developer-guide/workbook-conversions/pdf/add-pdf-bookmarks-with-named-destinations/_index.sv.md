---
title: Lägg till PDF bokmärken med namngivna destinationer
type: docs
weight: 20
url: /sv/net/add-pdf-bookmarks-with-named-destinations/
---

## **Möjliga användningsscenario**

Namngivna destinationer är speciella typer av bokmärken eller länkar i PDF som inte är beroende av PDF-sidor. Det betyder att om sidor läggs till eller tas bort från PDF-filen kan bokmärken bli ogiltiga men namngivna destinationer kommer att förbli intakta. För att skapa namngiven destination, ange egenskapen [**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry/properties/destinationname).

## **Lägg till bokmärken i PDF med namngivna destinationer**

Se följande exempelkod, dess [käll-Excelfil](50528348.xlsx) och dess [utdata-PDF-fil](50528349.pdf). Skärmdumpen visar bokmärken och namngivna destinationer i den resulterande PDF:en. Skärmdumpen beskriver också hur man visar namngivna destinationer och att du behöver en professionell version av Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-AddPDFBookmarksWithNamedDestinations.cs" >}}
{{< app/cells/assistant language="csharp" >}}
