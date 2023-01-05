---
title: Använder Format Painter
type: docs
weight: 80
url: /sv/net/using-format-painter/
---
{{% alert color="primary" %}} 

Formatmålare är funktionen i MS Excel som har anpassats i Aspose.Cells.GridDesktop. Det är en väldigt trevlig funktion. För de personer som ännu inte har använt den här funktionen tillåter format painter användare att tillämpa formateringsinställningarna för valfri fokuserad cell till en annan cell. Implementeringen av denna funktion är mycket enkel. I det här ämnet kommer vi också att ta upp det.

{{% /alert %}} 
## **Använder Format Painter**
 Funktionen av**Formatmålare** kräver att användare väljer en cell vars formateringsinställningar du vill tillämpa på andra celler och sedan anropar**StartFormatPainter** metod**GridDesktop**. Det finns två lägen för formatmålare enligt följande:

- **Använder Format Painter en gång**
- **Använd alltid Format Painter**
### **Använder Format Painter en gång**
 Om utvecklare vill använda funktionen i formatmålare bara en gång för att tillämpa formateringsinställningarna för en fokuserad cell på en enskild cell kan de göra det genom att anropa**StartFormatPainter** metod och godkänt a**falsk** värde till det. Detta**falsk** värde kommer att förbjuda formatmålare från att måla för alltid.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Använd alltid Format Painter**
Att använda formatmålare är alltid en användbar funktion när vi behöver tillämpa formateringsinställningarna på mer än en cell. Utvecklare kan uppnå den här funktionen genom att helt enkelt ringa**StartFormatPainter** metod och godkänt a**Sann** värde till det.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


 Den här typen av formatmålare fortsätter att måla för evigt om vi inte stoppar det. Så för att stoppa formatmålare från att alltid måla kan vi helt enkelt ringa**EndFormatPainter** metod av**GridDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
