---
title: Ange formler  Meddelande för icke engelska användare
type: docs
weight: 10
url: /sv/python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells för Python via .NET stöder de flesta formler/funktioner som är en del av Microsoft Excel. Utvecklare kan använda dessa formler antingen med API:et eller [designer spreadsheets](/cells/sv/net/what-is-a-designer-spreadsheet/). Aspose.Cells för Python via .NET stöder ett stort antal matematiska, sträng-, booleska, datum/tid-, statistiska, databas-, uppslags- och referensformler. Formlerna ska anges med engelska (USA) stil.

{{% /alert %}} 

## **Meddelande för användare som inte talar engelska**
Det finns två tips som icke-engelska användare måste följa när de skapar formler med Aspose.Cells för Python via .NET:

1. Formler måste skrivas in på engelska. Använd till exempel det engelska "=SUM()" inte det tyska "=SUMME()".
1. Använd alltid komma (,) för att separera funktionsparametrar. För vissa språkalternativ eller inställningar är avgränsaren för funktionsparametrar semikolon, men Aspose.Cells för Python via .NET använder engelskt kommastil. Till exempel, använd "=IF (C5=0,0,C3/C4)" inte "=IF(C5=0;0;C3/C4)"

{{< app/cells/assistant language="python-net" >}}
