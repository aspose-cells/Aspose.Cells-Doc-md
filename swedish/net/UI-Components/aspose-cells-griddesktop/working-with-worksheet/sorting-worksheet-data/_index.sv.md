---
title: Sortera arbetsbladsdata
type: docs
weight: 80
url: /sv/net/sorting-worksheet-data/
---
{{% alert color="primary" %}} 

Sortering är en viktig rutinuppgift som vi mest använder vid bearbetning av data. I det här ämnet kommer vi att diskutera med hjälp av ett enkelt exempel hur vi kan sortera data i ett kalkylblad.

{{% /alert %}} 
## **Sortera arbetsbladsdata**
För att sortera data i ett kalkylblad med API av Aspose.Cells.GridDesktop, följ stegen nedan:

-  Först och främst skapa ett globalt objekt av**CellRange** så att den kan nås var som helst inom din klass
-  Skapa en händelsehanterare för**SelectedCellRangeChanged** händelse av**GridDesktop**. **SelectedCellRangeChanged** händelsen utlöses varje gång när ett cellintervall som valts av en användare ändras. Till exempel, om en användare väljer celler (som innehåller data som ska sorteras) kommer denna händelse att triggas varje gång hans urvalsintervall ändras.
-  Händelsehanteraren tillhandahåller**CellRangeEventArgs** argument som ytterligare tillhandahåller uppdateringsintervallet för celler (valda av användaren) i form av en**CellRange** objekt. Så i den här händelsehanteraren kommer vi att tilldela detta**CellRange** objekt (som innehåller uppdaterat cellområde) till den globala**CellRange**objekt så att det även kan användas i andra delar av koden. För att säkerställa att vi inte förlorar cellintervallet kommer vi att skriva händelsehanterarkod i ett villkor
- Nu kan vi skriva lite kod för att sortera arbetsbladsdata. Först och främst, gå till ett önskat arbetsblad
-  Skapa en**SortRange** objekt som kommer att behålla intervallet av celler vars data ska sorteras. I**SortRange** konstruktor, kan vi specificera kalkylbladet, index för startrad och kolumn, antal rader och kolumner som ska sorteras, orientering för sortering (som uppifrån och ner eller från vänster till höger) etc.
-  Nu kan vi ringa**Sortera** metod av**SortRange** objekt för att utföra sorteringen av data. I**Sortera** metod kan vi ange indexet för kolumnen eller raden som ska sorteras och sorteringsordningen (det kan vara**Stigande** eller**Nedåtgående** enligt dina krav)
-  Äntligen kan vi ringa**Ogiltigförklara** metod av**GridDesktop** att rita om celler.

I exemplet nedan har vi demonstrerat hur man sorterar data i en kolumn.

 Skapa ett globalt objekt av CellRange och**SelectedCellRangeChanged**händelse av GridDesktop. Skriv nu koden enligt nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


 Nu skriver vi metod för**Stigande sortering** . Du kan skapa en knapp för**Stigande sortering** och skriv nedan koden inuti dess**Klick** Händelse.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


 Slutligen skriver vi lite kod för att uppnå**Fallande sortering** funktionalitet. Skapa en**Fallande sortering** knappen och skriv nedanstående kod i dess**Klick** Händelse.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
