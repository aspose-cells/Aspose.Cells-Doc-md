---
title: Anpassa initialiseringsparametrar
type: docs
weight: 10
url: /sv/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb, anpassa, anpassa parametrar
description: hur man anpassar initialiseringsparametrar i Aspose.Cells.GridWeb klientsidans skript.
---

{{% alert color="primary" %}} 

Utvecklare kan sätta olika initialiseringsparametervärden för att utföra olika beteenden för Aspose.Cells.GridWeb-kontrollen i acwmain.js.  

{{% /alert %}} 

### **Parametrar**

|**Parameter**|**Beskrivning**|
| :- | :- |
|needInitAlignmentAdjust| om vertikal justering för cellinnehåll vid initialisering, kommer det att ta lite tid att göra justeringsarbetet, om arbetsbladet har stora celler, kommer prestandan vara dålig, om användaren inte bryr sig om den vertikala justeringen kan hen ställa in den till falskt, standardvärdet är sant |
|focusinside| om fokus ska ligga inuti cellspannet, standardvärdet är sant |
|copy_with_style| om kopiera med stil, standardvärdet är falskt vilket innebär att endast cellinnehållet kopieras |
|useESCAsLeave| det förinställda beteendet när man trycker på esc fungerar som att avbryta redigeringsoperationen på cellen, om vi ställer in detta värde till sant, kommer vi bara att behandla det som en genväg för att lämna cellen utan att ändra tillbaka till det tidigare värdet, och det kommer också att ändra redigeringsmetoden inuti till snabb redigeringssättet , standardvärdet är falskt |
|needValidateall| om validera alla valideringar på den aktiva plattan när validering utförs, (i aspx-kontrollsidan ställ in ForceValidation="True"). standardvärdet är falskt |
|scrollToInvalidate| om man ska rulla och föra den första ogiltiga cellen i vy när needValidateall är satt till sant. standardvärdet är sant. |


Utmatningen av kodexemplet visas nedan. Vänligen kontrollera [provkalkylfilen](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
inne i redigeringsläge - när du anger text kommer det gamla cellvärdet fortfarande att behållas   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
snabbt redigeringsläge - när du anger text kommer det gamla cellvärdet att skrivas över, om du vill redigera baserat på det gamla cellvärdet kan du klicka på cellen

![todo:image_alt_text](focus_inside_false.png)



