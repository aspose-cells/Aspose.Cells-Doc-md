---
title: Spåra konverteringsförlopp för Excel till TIFF
type: docs
weight: 190
url: /sv/net/track-conversion-progress-of-excel-to-tiff/
---
## **Möjliga användningsscenarier**

 Ibland kan det ta lite tid att konvertera stora Excel-filer. Under denna tid kanske du vill visa dokumentkonverteringsförloppet istället för bara en laddningsskärm för att förbättra användbarheten av din applikation. Aspose.Cells stöder konverteringsprocess för spårning av dokument genom att tillhandahålla**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** gränssnitt. De**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**gränssnitt ger**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**och**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**metoder som du kan implementera i din anpassade klass. Du kan också styra vilka sidor som renderas som visas i T*estPageSavingCallback*anpassad klass.

## **Spåra konverteringsförlopp för Excel till TIFF**

 Följande kodexempel laddar[source excel-fil](95584311.xlsx) och skriver ut dess konverteringsförlopp i konsolen med hjälp av*TestPageSavingCallback* anpassad klass som implementerar**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**gränssnitt. Den genererade utdatafilen bifogas som referens.

[Utdatafil](95584312.tiff)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Följande är koden för*TestTiffPageSavingCallback*anpassad klass.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
Avsluta att spara sidindex 8 av sidorna 10</br>

