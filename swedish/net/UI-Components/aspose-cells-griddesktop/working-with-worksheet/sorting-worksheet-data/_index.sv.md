---
title: Sortering av Arbetsbladsdata
type: docs
weight: 80
url: /sv/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop,sortera,sortera,sortera data,data sortering
description: Den här artikeln introducerar hur man sorterar data i arbetsblad i GridDesktop.
---

{{% alert color="primary" %}} 

Sortering är en viktig rutinmässig uppgift som vi mestadels använder under bearbetning av data. I det här ämnet kommer vi att diskutera med hjälp av ett enkelt exempel hur vi kan sortera data i ett arbetsblad.

{{% /alert %}} 
## **Sortera arbetsbladsdata**
För att sortera data i ett arbetsblad med hjälp av API:et för Aspose.Cells.GridDesktop, följ stegen nedan:

- För det första skapa ett globalt objekt av **CellRange** så att det kan åtkommas var som helst i omfånget av din klass
- Skapa en händelsehanterare för händelsen **SelectedCellRangeChanged** av **GridDesktop**. **SelectedCellRangeChanged**-händelsen utlöses varje gång en cellintervall valt av en användare ändras. Till exempel, om en användare väljer celler (som innehåller data som ska sorteras) så skulle denna händelse utlösas varje gång hans valintervall skulle ändras.
- Händelsehanteraren tillhandahåller argumentet **CellRangeEventArgs** som vidare tillhandahåller uppdateringsintervallet för celler (valt av användaren) i form av ett **CellRange**-objekt. Så, i denna händelsehanterare, kommer vi tilldela detta **CellRange**-objekt (innehållande uppdaterat cellintervall) till det globala **CellRange**-objektet så att det också kan användas i andra delar av koden. För att säkerställa att vi inte förlorar cellintervallen, kommer vi att skriva händelsehanterarkod inuti ett villkor.
- Nu kan vi skriva lite kod för att sortera arbetsbladsdata. Först och främst, åtkomst till ett önskat arbetsblad
- Skapa ett **SortRange**-objekt som kommer att behålla intervallet för celler vars data ska sorteras. I **SortRange**-konstruktören kan vi specificera arbetsbladet, startradens och kolumnens index, antalet rader och kolumner att sortera, sorteringens orientering (som högst till lägst eller vänster till höger) osv.
- Nu kan vi anropa **Sort**-metoden för **SortRange**-objektet för att utföra sorteringen av data. I **Sort**-metoden kan vi specificera indexet för kolumnen eller raden som ska sorteras och sortera ordning (som kan vara **Stigande** eller **Fallande** enligt dina krav)
- Slutligen kan vi anropa metoden **Invalidate** för **GridDesktop** för att rita om celler.

I det följande exemplet har vi visat hur man sorterar data i en kolumn.

Skapa ett globalt objekt av CellRange och **SelectedCellRangeChanged**-händelse av GridDesktop. Skriv nu koden enligt nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


Nu skriver vi metod för **Stigande Sortering**. Du kan skapa en knapp för **Stigande Sortering** och skriva nedanstående kod inuti dess **Klick**-händelse.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


Slutligen skriver vi lite kod för att uppnå funktionalitet för **Fallande Sortering**. Skapa en **Fallande Sortering**-knapp och skriv nedanstående kod inuti dess **Klick**-händelse.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
