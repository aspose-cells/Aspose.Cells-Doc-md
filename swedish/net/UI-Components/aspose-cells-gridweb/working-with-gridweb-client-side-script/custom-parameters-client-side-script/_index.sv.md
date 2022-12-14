---
title: Anpassa initialiseringsparametrar
type: docs
weight: 10
url: /sv/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
description: hur man anpassar initialiseringsparametrar i Aspose.Cells.GridWeb klientsideskript.
---
{{% alert color="primary" %}} 

 Utvecklare kan ställa in olika initialiseringsparametervärden för att utföra olika beteenden för Aspose.Cells.GridWeb-kontrollen i acwmain.js.

{{% /alert %}} 
 
### **Parametrar**
 
|**Parameter**|**Beskrivning**|
|:- |:- |
|needInitAlignmentAdjust|om man ska göra vertikal justering för cellinnehåll vid initiering, det kommer att få lite tid att göra justeringen, om kalkylbladet har stora celler, blir prestandan dålig, om användaren inte bryr sig om den vertikala justeringen, då kan han ställa in den till vara falsk, standardvärdet är sant|
|fokusera inuti| om man ska fokusera inom cellomfånget, är standardvärdet sant|
|kopiera_med_stil|om du vill kopiera med stil, är standardvärdet false vilket betyder att endast kopiera cellinnehåll|
|använd ESCAsLeave|standardbeteendet när du trycker på esc fungerar som avbryt redigeringsoperation på cellen, om vi ställer in det här värdet till sant, kommer vi bara att behandla det som en kortknapp för att lämna cellen utan att ändra tillbaka till föregående värde, och det kommer också att ändra insidans redigeringssätt för snabb redigering är standardvärdet falskt|
|behöver Valideraallt|om alla valideringar på det aktiva arket ska valideras när validering görs, (i aspx kontrollpanel ForceValidation="True") . standardvärdet är falskt|
|scrollToInvalidate|om man ska rulla och visa den första ogiltigförklarade cellen när needValidateall är satt till true. standardvärdet är sant.|
 
 
 Utdata från kodexemplet visas nedan, vänligen kontrollera[exempel på excel-fil](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
 inuti redigeringssätt -- när du skriver in text kommer det gamla cellvärdet fortfarande att behållas

![todo:image_alt_text](focus_inside_true.png)

**focusinside=falskt** 
snabb redigering -- när du anger text kommer det gamla cellvärdet att skrivas över, om du vill redigera baserat på det gamla cellvärdet kan du klicka på cellen

![todo:image_alt_text](focus_inside_false.png)

 
 