---
title: Spåra konverteringsstatus för Excel till TIFF med Golang via C++
linktitle: Följ konverteringsframstegen från Excel till TIFF
type: docs
weight: 190
url: /sv/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: Lär dig hur du spårar konverteringsprocessen för Excel filer till TIFF format med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland kan konvertering av stora Excel-filer ta tid. Under denna tid kanske du vill visa konverteringsprogressen för dokumentet istället för en laddningsskärm för att förbättra användbarheten av din applikation. Aspose.Cells stöder spårning av konverteringsprogressen genom att tillhandahålla gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). Gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) tillhandahåller metoderna [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) och [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) som du kan implementera i din egna klass. Du kan också kontrollera vilka sidor som renderas, som demonstreras i den anpassade klassen *TestPageSavingCallback*.

## **Spåra konverteringsframsteg för Excel till TIFF**

Följande kodexempel laddar in den [källa Excel-filen](95584311.xlsx) och skriver ut dess konverteringsprogress i konsolen med hjälp av den anpassade klassen *TestPageSavingCallback* som implementerar gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). Utdatafilen som genereras är bifogad för din referens.

[Output File](95584312.tiff)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
Följande är koden för den anpassade klassen *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
## **Konsoloutput**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
