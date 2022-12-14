---
title: Skapa anpassade kommandoknappar
type: docs
weight: 100
url: /sv/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb innehåller speciella knappar som**Skicka in**, **Spara** och**Ångra**. Alla dessa knappar utför specifika uppgifter för Aspose.Cells.GridWeb.
Det är också möjligt att lägga till anpassade knappar som utför anpassade uppgifter. Det här avsnittet förklarar hur du använder den här funktionen.

{{% /alert %}} 
## **Skapa anpassade kommandoknappar**
Så här skapar du en anpassad kommandoknapp i Aspose.Cells.GridWeb:

1. Lägg till Aspose.Cells.GridWeb-kontroll i webbformuläret.
1. Få tillgång till ett arbetsblad.
1. Skapa en instans av klassen CustomCommandButton.
1. Ställ in knappens kommando till något värde. Detta värde används i knappens händelsehanterare.
1. Ställ in knappens text.
1. Ställ in knappens bild-URL.
1. Lägg slutligen till CustomCommandButton-objektet till CustomCommandButtons-samlingen i GridWeb-kontrollen.

{{% alert color="primary" %}} 

Anpassade kommandoknappar kan också läggas till i WYSIWYG-läge med hjälp av dialogrutan Egenskaper i Visual Studio.

{{% /alert %}} 

Utdata från kodavsnitt visas nedan:

**En anpassad kommandoknapp har lagts till i GridWeb-kontrollen** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Händelsehantering av anpassad kommandoknapp**
Den viktigaste aspekten av anpassade kommandoknappar är åtgärden de utför när de klickas. För att ställa in åtgärden, skapa en händelsehanterare för GridWeb-kontrollens CustomCommand-händelse.

CustomCommand-händelsen utlöses alltid när en anpassad kommandoknapp klickas. Så händelsehanteraren måste identifiera den specifika anpassade kommandoknappen som den gäller för av kommandouppsättningen när knappen läggs till i GridWeb-kontrollen. Lägg slutligen till anpassad kod som exekveras när knappen klickas.

I kodexemplet nedan läggs ett textmeddelande till i cellen A1 när knappen klickas.

**Text läggs till i A1-cell när anpassad kommandoknapp klickas** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
