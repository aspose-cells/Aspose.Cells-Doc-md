---
title: Följ konverteringsframstegen från Excel till TIFF
type: docs
weight: 190
url: /sv/net/track-conversion-progress-of-excel-to-tiff/
---

## **Möjliga användningsscenario**

Ibland kan det ta tid att konvertera stora Excel-filer. Under den tiden kan du vilja visa dokumentkonverteringsframsteg istället för bara en laddningsskärm för att förbättra användbarheten i din applikation. Aspose.Cells stöder att spåra dokumentkonverteringsprocessen genom att tillhandahålla [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-gränssnittet. [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-gränssnittet tillhandahåller [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)- och [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)-metoder som du kan implementera i din egen klass. Du kan också styra vilka sidor som ska renderas som visas i den egna klassen TestPageSavingCallback.

## **Spåra konverteringsframsteg för Excel till TIFF**

Följande kodexempel laddar den [ursprungliga excelfilen](95584311.xlsx) och skriver ut dess konverteringsframsteg i konsollen genom att använda den anpassade klassen *TestPageSavingCallback* som implementerar [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-gränssnittet. Den genererade utdatafilen är bifogad för din referens.

[Output File](95584312.tiff)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Följande är koden för den anpassade klassen *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
