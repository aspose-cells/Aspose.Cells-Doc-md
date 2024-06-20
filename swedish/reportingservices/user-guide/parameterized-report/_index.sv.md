---
title: Parameteriserad rapport
type: docs
weight: 60
url: /sv/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

En *parameteriserad rapport* är en rapport som accepterar inmatningsvärden som används när rapporten bearbetas. 

Med en parameteriserad rapport kan du variera utdata av en rapport baserat på de värden som är inställda vid körning. Rapporterings tjänsterna stödjer två typer av parametrar: frågeparametrar och rapportparametrar. 

- **Frågeparametrar** används för att välja eller filtrera data under data bearbetning. Om en frågeparameter anges måste ett värde tillhandahållas antingen av användaren eller via standard egenskaper för att slutföra SELECT uttalandet eller lagrad procedur som hämtar data för en rapport.
- **Rapportparametrar** används under rapportbearbetning för att visa en annan aspekt av datan. En rapport parameter används vanligtvis för att filtrera en stor uppsättning poster, men den kan ha andra användningsområden beroende på frågorna och uttrycken i rapporten.

Rapportparametrar skiljer sig från frågeparametrar i det att de är definierade i en rapport och bearbetas av rapport servern, medan frågeparametrar är definierade som en del av dataset frågan och bearbetas på databas servern. I Aspose.Cells.Report.Designer anges frågeparametrar vid fråga skapande tid i Microsoft fråga. 

Du kan skapa rapportparametrar och kartlägga frågeparametrar till motsvarande rapportparameter i Aspose.Cells.Report.Designer. På så sätt är det möjligt att välja värden för rapportparametrar och få dem vidarebefordrade i frågan för att begränsa den data hämtad från datakällan.

{{% /alert %}} 
###### **Denna avsnitt innehåller följande ämnen:** 
- [Skapar rapportparametrar](/cells/sv/reportingservices/creating-report-parameters/)
- [Modifiera rapportparametrar](/cells/sv/reportingservices/modifying-report-parameters/)
- [Kartläggning av frågeparametrar till rapportparametrar](/cells/sv/reportingservices/mapping-query-parameters-to-report-parameters/)
