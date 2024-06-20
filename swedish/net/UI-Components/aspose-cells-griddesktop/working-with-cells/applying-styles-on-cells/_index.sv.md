---
title: Tillämpa stil på cell
type: docs
weight: 50
url: /sv/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop, format, stil, nummerformat, nummerformat
description: Den här artikeln introducerar hur man hämtar eller anger stilformatet i cellen i kalkylarket i GridDesktop.
---

{{% alert color="primary" %}} 

Det här ämnet handlar om att tillämpa stilformat på en cell, vi kommer att täcka nästan alla relaterade egenskaper som kan användas för att tillämpa stil på en cell. Förutom några grundläggande formateringsinställningar kommer vi också att diskutera om att rita ramar och ställa in nummerformat på cellen i detalj.

{{% /alert %}} 
## **Tillämpa en anpassad stil på en cell - Ett exempel**
För att ändra teckensnittet och färgen i en cell med hjälp av Aspose.Cells.GridDesktop, följ stegen nedan:

- Kom åt något önskat **Kalkylblad**
- Få åtkomst till en **Cell** där vi vill tillämpa en **Stil**
- Hämta **Stil** för **Cellen**
- Ange **Stil**-egenskaper enligt dina anpassade behov
- Slutligen, ange **Stil** av **Cellen** med den uppdaterade

Det finns många användbara egenskaper och metoder som erbjuds av **Stil** objektet som utvecklare kan använda för att anpassa stilen enligt deras krav. I koden nedan visas det hur man applicerar anpassad stil på cellen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Rita ramar kring celler**
Med hjälp av **Stil** objektet kan vi rita ramar runt en cell mycket enkelt. Ramarna kan ritas i vilken färg som helst. Dessutom har utvecklare också flexibilitet att välja en specifik typ av linje som kommer att användas för att rita ramar runt cellen. Utvecklare kan använda **SetBorderLine** och **SetBorderColor** metoder av **Stil** objektet för att rita ramar av någon typ och färg. På samma sätt, för att få raminformation om någon cell, kan utvecklare också använda sig av **GetBorderLine** och **GetBorderColor** metoder av **Stil** objektet.
### **Typer av ramar**
Det finns sex typer av ramar som stöds av Aspose.Cells.GridDesktop enligt följande:

- **Vänster**,representerar vänster kant
- **Höger**,representerar höger kant
- **Övre**,representerar övre kant
- **Nedre**,representerar nedre kant
- **Diagonal Nedåt**, representerar diagonal nedåt kant
- **Diagonal Uppåt**, representerar diagonal uppåt kant
### **Typer av Ramlänkar**
En ram består av en linje. Genom att ändra linjens typ ändras ramens utseende. Det finns många typer av ramlänkar som stöds av Aspose.Cells.GridDesktop, vilket också listas nedan:

- **Ingen**, representerar ingen ram
- **Tunn**, representerar solid linjeram
- **Medium**, representerar solid linjeram med linjebredd lika med 2f
- **Streckad**, representerar streckad linjeram
- **Prickad**, representerar prickad linjeram
- **Tjock**, representerar solid linjeram med linjebredd lika med 3f
- **MediumDashed**, representerar streckad linjeram med linjebredd lika med 2f
- **TunnStreckadPrickad**, representerar stödd linjeram
- **MediumStreckadPrickad**, representerar stödd linjeram med linjebredd lika med 2f
- **TunnStreckadPunktad**, representerar stödd punkterad linjeram
- **MediumStreckadPunktad**,representerar stödd punkterad rinjesram med linjebredd lika med 2f
## **Sammanfatta alltihop - Exempel**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Inställning av nummerformat**
Aspose.Cells.GridDesktop erbjuder även olika typer av inställningar för nummerformat. Det finns 58 inbyggda nummerformat som erbjuds av Aspose.Cells.GridDesktop. För att se en komplett lista över alla stödda nummerformat, vänligen hänvisa till [Stödda nummerformat.](/cells/sv/net/list-of-supported-number-formats/)

Alla inbyggda nummerformat tilldelas en **Index**-nummer. **Till exempel** är **Index**-numret för nummerformatet **0.00E+00** **11**. För att använda ett inbyggt nummerformat i en cell kan utvecklare ställa in NumberFormat-egenskapen för **Style**-objekt till **Index**-numret för det specifika nummerformatet. Om utvecklare behöver ha sitt eget anpassade nummerformat kan de också använda egenskapen Custom för **Style**-objekt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
