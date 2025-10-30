---
title: Lägg till PDF bokmärken med namngivna destinationer med Golang via C++
linktitle: Lägg till PDF bokmärken med namngivna destinationer
type: docs
weight: 20
url: /sv/go-cpp/add-pdf-bookmarks-with-named-destinations/
description: Lär dig hur du lägger till PDF bokmärken med namngivna destinationer med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Namngivna destinationer är speciella typer av bokmärken eller länkar i PDF som inte är beroende av PDF-sidor. Det betyder att om sidor läggs till eller tas bort från PDF kan bokmärkena bli ogiltiga, men de namngivna destinationerna förblir intakta. För att skapa en namngiven destination, vänligen ställ in egenskapen [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/getdestinationname/).

## **Lägg till bokmärken i PDF med namngivna destinationer**

Se följande exempelkod, dess [käll-Excelfil](50528348.xlsx) och dess [utdata-PDF-fil](50528349.pdf). Skärmdumpen visar bokmärken och namngivna destinationer i den resulterande PDF:en. Skärmdumpen beskriver också hur man visar namngivna destinationer och att du behöver en professionell version av Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPdfBookmarksWithNamedDestinations.go" >}}
