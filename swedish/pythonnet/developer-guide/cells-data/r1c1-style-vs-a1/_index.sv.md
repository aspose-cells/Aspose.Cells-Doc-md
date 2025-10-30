---
title: Excel – R1C1 Referenstyp mot A1
type: docs
weight: 30
url: /sv/python-net/r1c1-reference-style-vs-a1/
description: R1C1 Referenstyp MOT A1 stil genom användning av Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, R1C1 Referenstyp MOT A1 stil med Python, R1C1 Referenstyp med Python, Hur man växlar mellan R1C1 Referenstyp och A1 Referenstyp med Python, A1 Referenstyp
---

{{% alert color="primary" %}}

I Excel är R1C1 och A1 två olika referenstyper som används för att identifiera celler i ett kalkylblad. Observera att valet mellan A1 och R1C1 är i stor utsträckning en fråga om personlig preferens. De flesta användare är mer bekanta med A1-stilen, men R1C1 kan vara användbart i vissa situationer, särskilt när man arbetar med formler och beräkningar.

{{% /alert %}}

## **A1 Referenstyp**

Detta är standardreferenstypen i Excel. I A1-stil identifieras kolumner med bokstäver (A, B, C, ..., Z, AA, AB, ... ZZ, AAA, AAB, ...) och rader identifieras med nummer (1, 2, 3, ...).
Till exempel, cellen i första kolumnen och andra raden hänvisas till som A2.

## **R1C1 Referenstyp**

I R1C1-stil identifieras både rader och kolumner med siffror. Bokstaven "R" representerar radnumret och bokstaven "C" representerar kolumnnumret. Till exempel, refererar R2C1 till cellen i andra raden och första kolumnen.

Eventuella siffror inom hakparenteser hänvisar till relativt avstånd från den aktuella cellen. Till skillnad från A1 som hänvisar till kolumner följt av radnummer, gör R1C1 det motsatta: rader följt av kolumner (vilket tar lite tid att vänja sig vid). Positiva siffror kommer att hänvisa till celler nedanför och/eller korsvis till höger. Negativa siffror kommer att hänvisa till celler ovanför och/eller till vänster.

Till exempel är R[2] C[3] en cell 2 rader ned och 3 kolumner till höger. R[-1] C[-4] är en cell 1 rad upp och 4 kolumner till vänster. Om inget nummer visas inom hakparenteserna hänvisar du till samma rad eller kolumn, dvs. R[3]C kommer att vara en cell 3 rader under den aktuella cellen i samma kolumn.
<br>
<image src="2.png" width="70%" />

## **Jämförelse för R1C1 Referenstyp och A1 Referenstyp**
Här är en snabb jämförelse:
|**A1-stil**|**R1C1-stil**|
| :- | :- |	
|A1|R1C1
|B3|R3C2
|G10|R10C7
|AA25|R25C27

## **Hur man växlar mellan R1C1 Referenstyp och A1 Referenstyp**
Du kan växla mellan dessa referenstyper i Excelinställningar. För att ändra referenstypen:

1. Gå till fliken "Arkiv".
1. Välj "Alternativ" längst ner.
1. I dialogrutan för Excel-alternativ, gå till kategorin "Formler".
1. Under avsnittet "Arbeta med formler", markera eller avmarkera alternativet "R1C1 referenstyp".
1. Klicka på "OK" för att tillämpa ändringarna.
<br>
<image src="1.png" width="70%" />

## **Hur man använder R1C1 Referenstyp och A1 Referenstyp i Excel**
Följande exempel visar hur man beräknar summan av två cellvärden i två stilar.
<br>
A1 referensstil:
<br>
<image src="4.png" width="70%" />

R1C1 referensstil:
<br>
<image src="3.png" width="70%" />
{{< app/cells/assistant language="python-net" >}}
