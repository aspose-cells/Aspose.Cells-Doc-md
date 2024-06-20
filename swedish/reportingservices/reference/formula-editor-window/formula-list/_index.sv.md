---
title: Formellista
type: docs
weight: 10
url: /sv/reportingservices/formula-list/
---

**Rapportfält**

|**Satsnamn** |**Formelnamn**|**Beskrivning**|
| :- | :- | :- |
|Globala fält |ExecutionTime |Datum och tid då rapporten började köras. |
| |ReportServerUrl |URL till rapportservern där rapporten körs. |
| |ReportName |Namnet på rapporten som det är lagrat i rapportserverns databas. |
| |ReportFolder |Den fullständiga sökvägen till mappen som innehåller rapporten. Detta inkluderar inte rapportserver-URLen. |
|Användare |UserID |Användar-ID för den som kör rapporten. |
| |Språk |Språk-ID för användaren som kör rapporten. |
**Rapportfält**

|**Satsnamn**|**Beskrivning**|
| :- | :- |
|Parameters |Samling innehåller de rapportparametrar inom rapporten. Parametrar kan skickas till frågor, användas i filter eller användas i andra funktioner som ändrar rapportens utseende baserat på parametern. |
|Fält |Samling innehåller fälten inom den aktuella datasetet. |
|DataSet ||
**Operatorer**
Aritmetiska operatorer används för att kombinera nummer, numeriska variabler, numeriska fält och numeriska funktioner för att få ett annat nummer. Jämförelseoperatorer används vanligtvis för att jämföra operand för ett villkor i en kontrollstruktur, såsom en If-sats. Booleska operatorer används vanligtvis med jämförelseoperatorer för att generera villkor för kontrollstrukturer.

|**Satsnamn**|**Formelnamn**|**Beskrivning**|
| :- | :- | :- |
|Aritmetik |^ |Upphöjt till, till exempel 2^3. |
| |* |Multiplikation, till exempel 2*3. |
| |/ |Division, till exempel 2/3. |
| |\\\ |Heltalsdivision, till exempel 2\\\3. |
| |Mod |Modulus, till exempel 4 Mod 3. |
| |+ |Addition, till exempel 4 + 3. |
| |- |Subtraktion, till exempel 4 – 3. |
|Jämförelse |< |Mindre än, till exempel 4 < 3 falskt. |
| |<= |Mindre än eller lika med, till exempel 4 <= 3 falskt. |
| |> |Större än, till exempel 4 > 3 sant. |
| |>= |Större än eller lika med, till exempel 4 >= 3 sant. |
| |= |Lika med, till exempel 4 = 3 falskt. |
| |<> |Inte lika, till exempel 4 <> 3 sant. |
| |Like |Jämför en sträng mot ett mönster. Till exempel resultat = sträng Like mönster. |
| |Is |Jämför två objektreferensvariabler, till exempel asp Is aspose. |
Konkatinering |& |Genererar en strängkonkatination av två uttryck. |
| |+ |Lägger till två nummer eller returnerar det positiva värdet av ett numeriskt uttryck. Kan också användas för att konkatenera två stränguttryck. |
Logiskt/Bitvis |Och |Utför en logisk sammansättning av två booleska uttryck eller en bitvis sammansättning av två numeriska uttryck. |
| |Not |Utför logisk negation på ett booleskt uttryck eller bitvis negation på ett numeriskt uttryck. |
| |Eller |Utför en logisk disjunktion på två booleska uttryck eller en bitvis disjunktion på två numeriska uttryck. |
| |Xor |Utför en logisk uteslutning på två booleska uttryck eller en bitvis uteslutning på två numeriska uttryck. |
| |OchSedan |Utför kortslutande logisk konjunktion på två uttryck. |
| |EllerSedan |Utför kortslutande inklusiv logisk disjunktion på två uttryck. |
Bitförskjutning |>> |Utför en aritmetisk vänsterskiftning på ett bitmönster. |
| |<< |Utför en aritmetisk högerskiftning på ett bitmönster. |

