---
title: Skapa anpassade kommandoknappar
type: docs
weight: 100
url: /sv/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb, kommando, kommandoknappar, anpassade
description: Denna artikel introducerar hur man skapar anpassade kommandoknappar i GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb innehåller specialknappar som **Skicka in**, **Spara** och **Ångra**. Alla dessa knappar utför specifika uppgifter för Aspose.Cells.GridWeb.
Det är också möjligt att lägga till anpassade knappar som utför anpassade uppgifter. Denna artikel förklarar hur man använder den här funktionen.

{{% /alert %}} 
## **Skapande av Anpassade Kommandoknappar**
För att skapa en anpassad kommandoknapp i Aspose.Cells.GridWeb:

1. Lägg till Aspose.Cells.GridWeb-kontroll på webbformuläret.
2. Hämta ett arbetsblad.
1. Skapa en instans av klassen CustomCommandButton.
1. Ange knappens kommando till ett värde. Detta värde används i knappens händelsehanterare.
1. Ange knappens text.
1. Ange knappens bild-URL.
1. Slutligen, lägg till objektet CustomCommandButton i GridWeb-kontrollens CustomCommandButtons-samling.

{{% alert color="primary" %}} 

Anpassade kommandoknappar kan också läggas till i WYSIWYG-läge med hjälp av Visual Studios Egenskapsdialog.

{{% /alert %}} 

Koden för exempel är visas nedan:

**En anpassad kommandoknapp läggs till i GridWeb-kontrollen** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Hantering av Anpassad Kommandoknappshändelse**
Det viktigaste med anpassade kommandoknappar är den åtgärd de utför när de klickas på. För att ange åtgärden, skapa en händelsehanterare för GridWeb-kontrollens CustomCommand-händelse.

CustomCommand-händelsen utlöses alltid när en anpassad kommandoknapp klickas på. Så måste händelsehanteraren identifiera den specifika anpassade kommandoknappen som den gäller för genom att använda Kommando som satts när knappen läggs till i GridWeb-kontrollen. Slutligen, lägg till anpassad kod som körs när knappen klickas på.

I kodexemplet nedan läggs ett textmeddelande till cellen A1 när knappen klickas på.

**Text läggs till i cell A1 när anpassad kommandoknapp klickas på** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
