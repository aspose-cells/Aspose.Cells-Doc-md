---
title: Ange formler  Meddelande för icke engelska användare
type: docs
weight: 20
url: /sv/java/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder de flesta av de formler/funktioner som ingår i Microsoft Excel. Utvecklare kan använda dessa formler med antingen API:et eller [design kalkylblad](/cells/sv/java/what-is-a-designer-spreadsheet/). Aspose.Cells stöder en stor uppsättning matematiska, sträng, booleska, datum/tid, statistiska, databas-, söknings- och referensformler. Formlerna bör anges med engelsk (US) stil.

Det finns två tips som icke-engelska användare måste följa när de skapar formler med Aspose.Cells:

1. Formler måste anges på engelska.
   Till exempel, använd det engelska "=SUM()" och inte det tyska "=SUMME()".
1. Använd alltid ett kommatecken (,) för att avgränsa funktionsparametrar.
   För vissa språgalternativ eller inställningar är avgränsaren för funktionsparametrar ett semikolon, men Aspose.Cells använder det engelska kommat. Använd till exempel "=IF (C5=0,0,C3/C4)" och inte "=IF(C5=0;0;C3/C4)". 

{{% /alert %}}
