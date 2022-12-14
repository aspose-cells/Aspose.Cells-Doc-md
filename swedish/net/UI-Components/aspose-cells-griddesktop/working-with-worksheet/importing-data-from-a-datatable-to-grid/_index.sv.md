---
title: Importera data från en datatabell till rutnät
type: docs
weight: 50
url: /sv/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

Sedan lanseringen av .NET Framework har Microsoft tillhandahållit ett utmärkt sätt att lagra data i offlineläge i form av ett DataTable-objekt. För att förstå utvecklarnas behov stöder Aspose.Cells.GridDesktop även import av data från en datatabell. Det här ämnet diskuterar hur man gör detta.

{{% /alert %}} 
## **Exempel**
Så här importerar du innehållet i en datatabell med Aspose.Cells.GridDesktop-kontroll:

1. Lägg till Aspose.Cells.GridDesktop-kontroll i ett formulär.
1. Skapa ett DataTable-objekt som innehåller data som ska importeras.
1. Få referensen till ett önskat arbetsblad.
1. Importera datatabellens innehåll till kalkylbladet.
1. Ställ in kolumnrubrikerna i kalkylbladet enligt kolumnnamnen i datatabellen.
1. Ställ in bredden på kolumnerna, om så önskas/
1. Visa arbetsbladet.

I exemplet nedan har vi skapat ett DataTable-objekt och fyllt det med en del data hämtade från en databastabell med namnet Products. Slutligen har vi importerat data från det DataTable-objektet till ett önskat kalkylblad med Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
