---
title: Importera data från en DataTable till Rutnätet
type: docs
weight: 50
url: /sv/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop, import, data, datatable
description: Den här artikeln introducerar hur man importerar data i GridDesktop.
---

{{% alert color="primary" %}} 

Sedan utgivningen av .NET Framework har Microsoft gett ett utmärkt sätt att lagra data i offlineläge i form av ett DataTable-objekt. Förstående utvecklares behov stöder även Aspose.Cells.GridDesktop import av data från en datatabell. Detta ämne diskuterar hur man gör detta.

{{% /alert %}} 
## **Exempel**
För att importera innehållet i en datatabell med hjälp av Aspose.Cells.GridDesktop-kontrollen:

1. Lägg till Aspose.Cells.GridDesktop-kontrollen på en form.
1. Skapa ett DataTable-objekt som innehåller datan som ska importeras.
1. Hämta en referens till ett önskat arbetsblad.
1. Importera datatabellens innehåll till arbetsbladet.
1. Ställ in arbetsbladets kolumnrubriker enligt kolumnnamnen i datatabellen.
1. Ställ in bredden på kolumnerna, om så önskas.
1. Visa arbetsbladet.

I det givna exemplet nedan har vi skapat ett DataTable-objekt och fyllt det med viss data hämtad från en databastabell som heter Produkter. Slutligen har vi importerat data från det DataTable-objektet till ett önskat arbetsblad med hjälp av Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
