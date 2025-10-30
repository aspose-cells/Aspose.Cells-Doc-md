---
title: Hur man infogar ett kryssymbol
type: docs
weight: 10
url: /sv/net/how-to-insert-tick-symbol-to-excel/
description: Denna artikel introducerar hur man infogar kryssymbol med API Aspose.Cells for .NET.
keywords: Kopiera och klistra in kryssymbolen, använd symbolen eller infogamenyn, ange en Alt kod, använd AutoCorrect eller genvägar, använd emoji /symbolpanel, lägg till en kryssruta / ballotsröstningsruta
---

## **Möjliga användningsscenario**
Att infoga en bock-symbol (✓) kan tjäna olika syften beroende på sammanhanget. Här är några vanliga skäl till varför någon kan infoga en bock-symbol:

1. **Indikering av färdigställande eller framgång**: Det används ofta för att markera att en uppgift är slutförd eller bekräfta att något har gjorts framgångsrikt. Till exempel, i en att-göra-lista kan du använda en bock för att visa att en uppgift har slutförts.

2. **Checklista och undersökningar**: I undersökningar, formulär eller checklistor används en bock för att indikera valda alternativ eller för att visa att ett visst objekt uppfyller de krav som ställts.

3. **Godkännande eller validering**: En bock-symbol kan indikera godkännande eller validering av en handling, beslut eller dokument. Den används ofta i formella eller semi-formella sammanhang.

4. **Designestetik**: I vissa fall används bock-symbolen enbart för dess visuella tilltal eller som en del av ett designelement, till exempel i logotyper, infographics eller presentationer.

5. **Positivt eller korrekt svar**: Det kan användas i utbildningsmaterial för att markera korrekta svar eller den positiva utgången av något.

6. **Indikering av överenskommelse eller samtycke**: En bock kan representera någons samtycke, tillstånd eller erkännande av ett uttalande eller villkor.


## **Hur man infogar en bock-symbol i Excel**
Här är en tydlig guide om hur du infogar en bock (✓ eller ✔) symbol i Excel, med flera metoder:

### Använda symbolmenyn

1. Klicka på cellen där du vill ha bocken.
2. Gå till fliken Infoga på ribbonen.
3. Klicka på Symbol (längst till höger).
4. I dialogrutan Symbol: Välj teckensnitt (Wingdings eller Segoe UI Symbol), leta efter (✔ (Tecken kod 252) eller ✓ (Tecken kod 2713))
5. Klicka på Infoga och stäng.

### Använda tangentbordsgenvägar
1. Alt-kod (Endast Windows): Håll Alt och skriv in koden med det numeriska tangentbordet: Alt + 0252 (✔) — Wingdings-teckensnitt, Alt + 10003 (✓) — Segoe UI Symbol
2. Släpp Alt för att infoga symbolen efter att du skrivit in koden.

### Kopiera och klistra in
Du kan kopiera en bock-symbol och klistra in den i valfri Excel-cell: ✓ (U+2713) och ✔ (U+2714). Kopiera bara härifrån och klistra direkt in i en cell.

### Använda villkorlig formatering med en formel
Du kan skapa automatiska kryssmarkeringar med formler och villkorlig formatering:

1. Ange en formel som: =IF(A1="ja", "✓", "").
2. Anpassa teckenstorlek och justering för utseende.

### Infoga med CHAR-funktionen (Wingdings-typsnitt)
Om du använder Wingdings: =CHAR(252)  →  ✔, Ändra sedan cellens typsnitt till Wingdings för att det ska visas korrekt.

### Infoga med Excel-kryssrutor (Valfritt)

För interaktiva kryssrutor:
1. Gå till Utvecklar-fliken (Aktivera den i Alternativ om den är dold).
2. Klicka på Infoga → Formkontroller → Kryssruta.
3. Placera kryssrutan på bladet.

## **Hur man infogar kryssymbol i Aspose.Cells for .NET**
För att infoga en kryss-symbol (✓) i en cell med Aspose.Cells for .NET kan du använda följande metoder för att uppfylla kraven.

1. Lägg till kryssymbol med Unicode (U+2713).
2. Lägg till kryssymbol med symboltypsnitt (Wingdings 2 eller Webdings).
3. Lägg till kryssymbol med bild.
4. Lägg till kryssymbol med kryssrute-kontroll.
5. Lägg till kryssymbol med villkorsstyrt format.
6. Lägg till kryssymbol med formel.

Här är ett enkelt exempel på hur man infogar kryssymbol i en cell i Aspose.Cells for .NET:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-insert-tick-symbol.cs" >}}

## **Utdataresultat**

Följande skärmbild visar kryssymbolerna skapade av Aspose.Cells for .NET i det exporterade Excel-dokumentet.
<br>
<img src="tick_result.png" width=70% />

{{< app/cells/assistant language="csharp" >}}
