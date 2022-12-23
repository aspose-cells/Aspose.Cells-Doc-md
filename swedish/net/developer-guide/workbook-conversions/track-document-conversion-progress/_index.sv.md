---
title: Spåra dokumentkonverteringsförlopp
type: docs
weight: 970
url: /sv/net/track-document-conversion-progress/
---
## **Möjliga användningsscenarier**

 Ibland kan det ta lite tid att konvertera stora Excel-filer. Under denna tid kanske du vill visa dokumentkonverteringsförloppet istället för bara en laddningsskärm för att förbättra användbarheten av din applikation. Aspose.Cells stöder konverteringsprocess för spårning av dokument genom att tillhandahålla**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** gränssnitt. De**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**gränssnitt ger**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**och**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**metoder som du kan implementera i din anpassade klass. Du kan också styra vilka sidor som renderas som visas i T*estPageSavingCallback*anpassad klass.

## **Spåra dokumentkonverteringsförlopp**

 Följande kodexempel laddar[source excel-fil](94896151.xlsx) och skriver ut dess konverteringsförlopp i konsolen med hjälp av*TestPageSavingCallback* anpassad klass som implementerar**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**gränssnitt.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

Följande är koden för*TestPageSavingCallback*anpassad klass.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

## **Konsolutgång**

Börja spara sidindex 0 av sidorna 11</br>
Sluta spara sidindex 0 av sidorna 11</br>
Börja spara sidindex 1 av sidorna 11</br>
Avsluta att spara sidindex 1 av sidorna 11</br>
Börja spara sidindex 2 av sidorna 11</br>
Avsluta att spara sidindex 2 av sidorna 11</br>
Börja spara sidindex 3 av sidorna 11</br>
Avsluta att spara sidindex 3 av sidorna 11</br>
Börja spara sidindex 4 av sidorna 11</br>
Avsluta att spara sidindex 4 av sidorna 11</br>
Börja spara sidindex 5 av sidorna 11</br>
Avsluta att spara sidindex 5 av sidorna 11</br>
Börja spara sidindex 6 av sidorna 11</br>
Avsluta att spara sidindex 6 av sidorna 11</br>
Börja spara sidindex 7 av sidorna 11</br>
Avsluta att spara sidindex 7 av sidorna 11</br>
Börja spara sidindex 8 av sidorna 11</br>
Avsluta att spara sidindex 8 av sidorna 11
