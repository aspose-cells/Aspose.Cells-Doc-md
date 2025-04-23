---
title: Spåra dokumentkonverteringsframsteg
type: docs
weight: 970
url: /sv/net/track-document-conversion-progress/
---

## **Möjliga användningsscenario**

Ibland kan det ta tid att konvertera stora Excel-filer. Under den tiden kan du vilja visa dokumentkonverteringsframsteg istället för bara en laddningsskärm för att förbättra användbarheten i din applikation. Aspose.Cells stöder att spåra dokumentkonverteringsprocessen genom att tillhandahålla [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-gränssnittet. [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-gränssnittet tillhandahåller [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)- och [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)-metoder som du kan implementera i din egen klass. Du kan också styra vilka sidor som ska renderas som visas i den egna klassen TestPageSavingCallback.

## **Spåra Dokumentkonverteringsframsteg**

Följande kodexempel läser in den [källa excel-filen](94896151.xlsx) och skriver ut dess konverteringsframsteg i konsolen genom att använda den egna klassen TestPageSavingCallback som implementerar [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-gränssnittet.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

Följande är koden för den egna klassen TestPageSavingCallback.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
