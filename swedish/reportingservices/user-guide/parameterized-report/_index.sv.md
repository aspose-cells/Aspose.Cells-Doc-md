---
title: Parameteriserad rapport
type: docs
weight: 60
url: /sv/reportingservices/parameterized-report/
---
{{% alert color="primary" %}} 

 A*parametriserad rapport* är en rapport som accepterar ingångsvärden som används när rapporten bearbetas.

 Med en parametriserad rapport kan du variera resultatet av en rapport baserat på de värden som ställs in vid körning. Reporting Services stöder två typer av parametrar: frågeparametrar och rapportparametrar.

- **Fråga parametrar** används för att välja eller filtrera data under databehandling. Om en frågeparameter anges måste ett värde tillhandahållas antingen av användaren eller som standardegenskaper för att slutföra SELECT-satsen eller den lagrade proceduren som hämtar data för en rapport.
- **Rapportparametrar**används under rapportbehandlingen för att visa en annan aspekt av data. En rapportparameter används vanligtvis för att filtrera en stor uppsättning poster, men den kan ha andra användningsområden beroende på frågorna och uttrycken i rapporten.

 Rapportparametrar skiljer sig från frågeparametrar genom att de definieras i en rapport och bearbetas av rapportservern, medan frågeparametrar definieras som en del av datauppsättningsfrågan och bearbetas på databasservern. I Aspose.Cells.Report.Designer anges frågeparametrar vid tidpunkten för att skapa frågan i Microsoft Query.

Du kan skapa rapportparametrar och mappa frågeparametrar till motsvarande rapportparameter i Aspose.Cells.Report.Designer. På så sätt är det möjligt att välja värden för rapportparametrar och få dem skickade i frågan för att begränsa data som hämtas från datakällan.

{{% /alert %}} 
###### **Det här avsnittet innehåller följande ämnen:**
- [Skapa rapportparametrar](/cells/sv/reportingservices/creating-report-parameters/)
- [Ändra rapportparametrar](/cells/sv/reportingservices/modifying-report-parameters/)
- [Mappning av frågeparametrar till rapportparametrar](/cells/sv/reportingservices/mapping-query-parameters-to-report-parameters/)
