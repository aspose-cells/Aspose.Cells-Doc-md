---
title: Spåra dokumentkonverteringsframsteg med Golang via C++
linktitle: Spåra dokumentkonverteringsframsteg
type: docs
weight: 970
url: /sv/go-cpp/track-document-conversion-progress/
description: Lär dig hur du spårar dokumentkonverteringsframsteg i C++ med Aspose.Cells för att förbättra applikationens användbarhet.
---

## **Möjliga användningsscenario**

Ibland kan konvertering av stora Excel-filer ta tid. Under den tiden kan du visa dokumentkonverteringsframsteg istället för bara en laddningsskärm för att förbättra användbarheten i din applikation. Aspose.Cells stöder spårning av dokumentkonverteringsframsteg genom att tillhandahålla gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). Gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) ger [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) och [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) metoder som du kan implementera i din anpassade klass. Du kan även kontrollera vilka sidor som renderas, som demonstreras i den anpassade klassen `TestPageSavingCallback`.

## **Spåra Dokumentkonverteringsframsteg**

Följande kodexempel laddar [käll-Excel-filen](94896151.xlsx) och skriver ut dess konverteringsframsteg i konsolen genom att använda den anpassade klassen `TestPageSavingCallback` som implementerar gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/).

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
Följande är koden för den anpassade klassen `TestPageSavingCallback`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
## **Konsoloutput**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
