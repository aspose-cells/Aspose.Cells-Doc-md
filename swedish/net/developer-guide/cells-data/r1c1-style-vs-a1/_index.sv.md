---
title: Excel – R1C1 Referensstil vs. A1
type: docs
weight: 30
url: /sv/net/r1c1-reference-style-vs-a1/
description: R1C1 Referensstil VS. A1-stil med Aspose.Cells for Python via .NET API.
keywords: R1C1 Reference Style VS. A1 style, R1C1 Reference Style, How to switch between R1C1 Reference Style and A1 Reference Style, A1 Reference style.
---
{{% alert color="primary" %}}

Excel är R1C1 och A1 två olika referensstilar som används för att identifiera celler i ett kalkylblad. Observera att valet mellan A1 och R1C1 till stor del är en fråga om personlig preferens. De flesta användare är mer bekanta med A1-stil, men R1C1 kan vara användbar i vissa situationer, särskilt när man arbetar med formler och beräkningar.

{{% /alert %}}

##  **A1 Referensstil**

Detta är standardreferensstilen i Excel. I A1-stil identifieras kolumner med bokstäver (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...), och rader identifieras med siffror (1, 2, 3, ...).
Till exempel kallas cellen i den första kolumnen och andra raden A2.

##  **R1C1 Referensstil**

I R1C1-stil identifieras både rader och kolumner med siffror. Bokstaven "R" representerar radnumret och bokstaven "C" representerar kolumnnumret. Till exempel hänvisar R2C1 till cellen i den andra raden och första kolumnen.

Alla siffror inom hakparenteser refererar till det relativa avståndet från den aktuella cellen. Till skillnad från A1 som hänvisar till kolumner följt av radnummer, gör R1C1 motsatsen: rader följt av kolumner (vilket tar lite att vänja sig vid). Positiva siffror hänvisar till cellerna nedanför och/eller till höger. Negativa tal kommer att referera till celler ovanför och/eller till vänster.

Till exempel är R[2]C[3] en cell 2 rader ner och 3 kolumner till höger. R[-1]C[-4] är en cell 1 rad upp och 4 kolumner till vänster. Om inget nummer visas inom parentes så hänvisar du till samma rad eller kolumn, dvs R[3]C kommer att vara en cell 3 rader under den aktuella cellen i samma kolumn.
<br>
<image src="2.png" width="70%" />

##  **Jämförelse för R1C1 Referensstil och A1 Referensstil**
Här är en snabb jämförelse:
|**A1 stil**|**R1C1 stil**|
| :- | :- |
|A1|
|B3|
|G10|
|AA25|

##  **Hur man växlar mellan R1C1 Reference Style och A1 Reference Style**
Du kan växla mellan dessa referensstilar i Excel-inställningar. Så här ändrar du referensstilen:

1. Gå till fliken "Arkiv".
1. Välj "Alternativ" längst ner.
1. I dialogrutan Excel-alternativ går du till kategorin "Formler".
1. Under avsnittet "Arbeta med formler", markera eller avmarkera alternativet "R1C1-referensstil".
1. Klicka på "OK" för att tillämpa ändringarna.
<br>
<image src="1.png" width="70%" />

##  **Hur man använder R1C1 Reference Style och A1 Reference Style i Excel**
Följande exempel visar hur man beräknar summan av två cellvärden i två stilar.
<br>
A1 Referensstil:
<br>
<image src="4.png" width="70%" />

R1C1 Referensstil:
<br>
<image src="3.png" width="70%" />
