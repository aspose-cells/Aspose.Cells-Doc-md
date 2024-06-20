---
title: Använd Format Painter
type: docs
weight: 80
url: /sv/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: Denna artikel introducerar formatpenseln i GridDesktop.
---

{{% alert color="primary" %}} 

Formatpenseln är en funktion i MS Excel som har anpassats i Aspose.Cells.GridDesktop. Det är en mycket trevlig funktion. För dem som ännu inte har använt den här funktionen låter formatpenseln användare tillämpa formateringsinställningarna för vilken fokuserad cell som helst på en annan cell. Implementeringen av den här funktionen är mycket enkel. I det här ämnet kommer vi också att täcka det.

{{% /alert %}} 
## **Använda Format Painter**
Funktionen **Format Painter** kräver att användare väljer en cell vars formateringsinställningar du vill tillämpa på andra celler och sedan anropet **StartFormatPainter** metoden **GridDesktop**. Det finns två lägen för formatpenseln enligt följande:

- **Använd formatpensel en gång**
- **Använd formatpensel alltid**
### **Använd formatpensel en gång**
Om utvecklare vill använda formatpenselns funktion endast en gång för att tillämpa formateringsinställningarna för en fokuserad cell på en enda cell kan de göra det genom att anropa **StartFormatPainter** metoden och skicka ett **false** värde till den. Detta **false** värde förhindrar formatpensel från att måla för evigt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Använda formatpensel alltid**
Att använda formatpenseln alltid är en användbar funktion när vi behöver tillämpa formateringsinställningarna på fler än en cell. Utvecklare kan uppnå den här funktionen genom att helt enkelt anropa **StartFormatPainter** metoden och skicka ett **true** värde till den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


Den här typen av formatpensel fortsätter att måla för evigt om vi inte stoppar den. Så för att stoppa formatpenseln från att måla alltid kan vi helt enkelt anropa **EndFormatPainter** metoden av **GridDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
