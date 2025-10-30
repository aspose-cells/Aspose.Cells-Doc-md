---
title: Sätta formler  Notis för icke engelska användare med JavaScript via C++
linktitle: Ange formler  Meddelande för icke engelska användare
type: docs
weight: 10
url: /sv/javascript-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.Cells stödjer de flesta formler/funktioner som är en del av Microsoft Excel. Utvecklare kan använda dessa formler med antingen API:n eller [designer kalkylblad](/cells/sv/javascript-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells stöder ett stort antal matematiska, sträng-, boolean-, datum/tid-, statistiska, databas-, uppslags- och referensformler. Formlerna ska specificeras med engelska (US) stil.

{{% /alert %}} 

## **Meddelande för användare som inte talar engelska**
Det finns två tips som icke-engelska användare måste följa när de skapar formler med Aspose.Cells:

1. Formler måste skrivas in på engelska. Använd till exempel det engelska "=SUM()" inte det tyska "=SUMME()".
1. Använd alltid komma (,) för att avgränsa funktionsparametrar. För vissa språkval eller inställningar är avgränsaren för funktionsparametrar semikolon men Aspose.Cells använder det engelska stilkommat. Till exempel, använd "=IF (C5=0,0,C3/C4)" inte "=IF(C5=0;0;C3/C4)".
