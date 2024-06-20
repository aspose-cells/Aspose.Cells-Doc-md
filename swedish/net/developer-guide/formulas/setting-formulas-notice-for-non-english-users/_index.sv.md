---
title: Ange formler  Meddelande för icke engelska användare
type: docs
weight: 10
url: /sv/net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder de flesta av de formler/funktioner som ingår i Microsoft Excel. Utvecklare kan använda dessa formler med antingen API:en eller [designarkalkylbladen](/cells/sv/net/what-is-a-designer-spreadsheet/). Aspose.Cells stöder ett stort antal matematiska, sträng, booleska, datum/tid, statistiska, databas-, sök- och referens formler. Formlerna ska anges med engelska (US)-stil.

{{% /alert %}} 
## **Meddelande för användare som inte talar engelska**
Det finns två tips som icke-engelska användare måste följa när de skapar formler med Aspose.Cells:

1. Formler måste skrivas in på engelska. Använd till exempel det engelska "=SUM()" inte det tyska "=SUMME()".
1. Använd alltid ett kommatecken (,) för att avgränsa funktionsparametrar. I vissa språkalternativ eller inställningar är avdelaren för funktionsparametrar ett semikolon, men Aspose.Cells använder det engelska kommatecknet. Använd till exempel "=IF (C5=0,0,C3/C4)" inte "=IF(C5=0;0;C3/C4)"
