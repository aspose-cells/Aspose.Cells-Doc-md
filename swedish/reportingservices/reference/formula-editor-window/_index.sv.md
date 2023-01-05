---
title: Formelredigeringsfönster
type: docs
weight: 20
url: /sv/reportingservices/formula-editor-window/
---
{{% alert color="primary" %}} 

Formelredigeraren låter dig skapa formler för en rapport.

{{% /alert %}} 

Så här redigerar du en formel i en Microsoft Excel-cell:

1. Välj en cell i Microsoft Excel.
1.  Öppna dialogrutan Redigera formel genom att klicka**Redigera formel** på verktygsfältet.
   ([Lägga till formler för Reporting Services](/cells/sv/reportingservices/adding-reporting-services-formulas/) går igenom ett exempel som redigerar en formel.)
 Dialogrutan är uppdelad i avsnitt: redigeringsområdet längst upp och formelområdet längst ner. Använd formelområdet för att fylla i redigeringsområdet.
1.  Välj en kategori (användare, parametrar, fält etc.) från**Rapportfält** lista (listan till vänster).
1.  Välj typ från**Funktioner** lista (i mitten).
1.  Välj ett alternativ från**Operatörer** lista (högerlistan).
1.  Klick**Föra in**för att lägga till uttrycket till**Redigera** område.
1.  Klick**Föra in** när uttrycket är färdigt.
 Formeln infogas i cellen.

**Dialogrutan Redigera formel** 

![todo:image_alt_text](formula-editor-window_1.png)

Dialogrutan Redigera formel är uppdelad i avsnitt, som beskrivs nedan.
#### **Redigera område**
 Det här är området där du skapar eller redigerar en formel. Skapa en formel genom att dubbelklicka på någon av komponenterna som anges i**Rapportfält**, **Funktioner** eller**Operatörer** listor. När du väljer en komponent infogas även den nödvändiga syntaxen. Du kan också ange en formel manuellt.
#### **Formelområde**
Formelområdet innehåller tre sektioner, var och en listar information som används för att bygga en formel.

- Rapportfält - listan till vänster listar alla databasfält som är tillgängliga för rapporten. Den listar också alla formler eller grupper som redan skapats.
- Funktioner - mittlistan innehåller funktioner, förbyggda procedurer som returnerar värden. De utför beräkningar som AVERAGE, SUM, COUNT, SIN, VERSOR och så vidare.
- Operatörer - "handlingsverben" som används i formler. Operatörer beskriver en operation eller en handling som ska ske mellan två eller flera värden. Exempel på operatorer: addera, subtrahera, mindre än och större än etc.
#### **Kontroller**
Dialogrutan har flera kontroller:

|**Knappens namn** |**Beskrivning** |
|:- |:- |
| Ångra| Ångrar en åtgärd.|
| Klistra| Klistrar in en teckensträng som består av komponenterna som anges i formelområdet i redigeringsområdet.|
| Föra in| Tar värdet i redigeringsområdet och infogar det som en formel i en cell.|
| Utgång| Stänger formelredigeraren.|
{{% alert color="primary" %}} 

Relaterade ämnen:

- [Formellista](/cells/sv/reportingservices/formula-list/) - en lista över fält och operatörer.

{{% /alert %}}
