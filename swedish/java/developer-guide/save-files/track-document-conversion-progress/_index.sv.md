---
title: Spåra dokumentkonverteringsframsteg
type: docs
weight: 120
url: /sv/java/track-document-conversion-progress/
---

## **Möjliga användningsscenario**

Ibland kan konvertering av stora Excel-filer ta lite tid. Under denna tid kanske du vill visa dokumentkonverteringsframstegen istället för bara en laddningsskärm för att förbättra användbarheten i din applikation. Aspose.Cells stöder spårning av dokumentkonverteringsprocess genom att tillhandahålla gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). Gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) tillhandahåller metoderna [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) och [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) som du kan implementera i din anpassade klass. Du kan även kontrollera vilka sidor som renderas som visas i den anpassade klassen *TestPageSavingCallback*.

## **Spåra Dokumentkonverteringsframsteg**

Följande kodprov laddar [käll-excel-filen](PagesBook1.xlsx) och skriver ut dess konverteringsframsteg i konsolen med hjälp av den anpassade klassen *TestPageSavingCallback* som implementerar gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback).

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

Följande är koden för den egna klassen TestPageSavingCallback.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

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
{{< app/cells/assistant language="java" >}}
