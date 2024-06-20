---
title: Formel redigeringsfönster
type: docs
weight: 20
url: /sv/reportingservices/formula-editor-window/
---

{{% alert color="primary" %}} 

Formelredigeraren låter dig skapa formler för en rapport.

{{% /alert %}} 

För att redigera en formel i en Microsoft Excel-cell:

1. I Microsoft Excel, välj en cell.
1. Öppna dialogrutan Redigera formel genom att klicka på **Redigera formel** i verktygsfältet.
   ([Lägga till rapporteringstjänstformler](/cells/sv/reportingservices/adding-reporting-services-formulas/) går igenom ett exempel som redigerar en formel.)
   Dialogrutan är uppdelad i sektioner: redigeringsområdet högst upp och formelområdet längst ned. Använd formelområdet för att fylla i redigeringsområdet.
1. Välj en kategori (användare, parametrar, fält etc.) från listan **Rapportfält** (den vänstra listan).
1. Välj typen från listan **Funktioner** (i mitten).
1. Välj ett alternativ från listan **Operatorer** (den högra listan).
1. Klicka på **Infoga** för att lägga till uttrycket i **Redigera**-området.
1. Klicka på **Infoga** när uttrycket är komplett.
   Formeln infogas i cellen.

**Dialogrutan Redigera formel** 

![todo:image_alt_text](formula-editor-window_1.png)

Dialogrutan Redigera formel är uppdelad i sektioner, beskrivna nedan.
#### **Redigeringsområdet**
Det här är området där du skapar eller redigerar en formel. Skapa en formel genom att dubbelklicka på någon av komponenterna som listas i listorna **Rapportfält**, **Funktioner** eller **Operatorer**. När du väljer en komponent infogas också nödvändig syntax. Du kan också manuellt skriva in en formel. 
#### **Formelområdet**
Formelområdet innehåller tre sektioner, där varje lista innehåller information som används för att skapa en formel.

- Rapportfält - listan till vänster listar alla databasfält som är åtkomliga för rapporten. Den listar också eventuella formler eller grupper som redan skapats.
- Funktioner - listan i mitten innehåller funktioner, förbyggda procedurer som returnerar värden. De utför beräkningar såsom MEDELVÄRDE, SUMMA, ANTAL, SIN, VERSALER och så vidare.
- Operatorer - de 'actionverb' som används i formler. Operatorer beskriver en operation eller åtgärd som ska utföras mellan två eller flera värden. Exempel på operatorer: lägga till, subtrahera, mindre än och större än osv.
#### **Kontroller**
Dialogrutan har flera kontroller:

|**Knappnamn** |**Beskrivning** |
| :- | :- |
|Undo |Ångrar en åtgärd. |
|Paste |Klistrar in en teckensträng som består av de komponenter som anges i formelområdet i redigeringsområdet. |
|Insert |Tar värdet i redigeringsområdet och infogar det som en formel i en cell. |
|Exit |Stänger Formelredigeraren. |
{{% alert color="primary" %}} 

Relaterade ämnen:

- [Formellista](/cells/sv/reportingservices/formula-list/) - en lista över fält och operatorer.

{{% /alert %}}
