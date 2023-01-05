---
title: Spåra konverteringsförlopp för Excel till TIFF
type: docs
weight: 140
url: /sv/java/track-conversion-progress-of-excel-to-tiff/
---
## **Möjliga användningsscenarier**

Ibland kan det ta lite tid att konvertera stora Excel-filer. Under denna tid kanske du vill visa dokumentkonverteringsförloppet istället för bara en laddningsskärm för att förbättra användbarheten av din applikation. Aspose.Cells stöder konverteringsprocess för spårning av dokument genom att tillhandahålla**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**gränssnitt. De**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**gränssnitt ger**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**och**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** metoder som du kan implementera i din anpassade klass. Du kan också kontrollera vilka sidor som renderas som visas i*TestTiffPageSavingCallback*anpassad klass.

## **Spåra konverteringsförlopp för Excel till TIFF**

Följande kodexempel laddar[source excel-fil](sampleUseWorkbookRenderForImageConversion.xlsx) och skriver ut dess konverteringsförlopp i konsolen med hjälp av*TestTiffPageSavingCallback*anpassad klass som implementerar**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**gränssnitt. Den genererade utdatafilen bifogas för din referens.

[Utdatafil](DocumentConversionProgressForTiff_out.tiff)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

Följande är koden för*TestTiffPageSavingCallback*anpassad klass.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Konsolutgång**

Börja spara sidindex 0 av sidorna 10</br>
Avsluta att spara sidindex 0 av sidorna 10</br>
Börja spara sidindex 1 av sidorna 10</br>
Avsluta att spara sidindex 1 av sidorna 10</br>
Börja spara sidindex 2 av sidorna 10</br>
Avsluta att spara sidindex 2 av sidorna 10</br>
Börja spara sidindex 3 av sidorna 10</br>
Avsluta att spara sidindex 3 av sidorna 10</br>
Börja spara sidindex 4 av sidorna 10</br>
Avsluta att spara sidindex 4 av sidorna 10</br>
Börja spara sidindex 5 av sidorna 10</br>
Avsluta att spara sidindex 5 av sidorna 10</br>
Börja spara sidindex 6 av sidorna 10</br>
Avsluta att spara sidindex 6 av sidorna 10</br>
Börja spara sidindex 7 av sidorna 10</br>
Avsluta att spara sidindex 7 av sidorna 10</br>
Börja spara sidindex 8 av sidorna 10</br>
Avsluta att spara sidindex 8 av sidorna 10
