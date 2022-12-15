---
title: Formellista
type: docs
weight: 10
url: /sv/reportingservices/formula-list/
---
**Rapportfält**

|**Ange namn** |**Formelnamn**|**Beskrivning**|
|:- |:- |:- |
| Globala fält| ExecutionTime|Datum och tid då rapporten började köras.|
|| ReportServerUrl| URL:en till rapportservern som rapporten körs på.|
|| Rapportnamn| Namnet på rapporten som den är lagrad i rapportserverns databas.|
|| Rapportmapp| Den fullständiga sökvägen till mappen som innehåller rapporten. Detta inkluderar inte rapportserverns URL.|
| Användare| Användar ID| ID för användaren som kör rapporten.|
|| Språk| Språk-ID för användaren som kör rapporten.|
**Rapportfält**

|**Ange namn**|**Beskrivning**|
|:- |:- |
| Parametrar| Parametrarsamlingen innehåller rapportparametrarna i rapporten. Parametrar kan skickas till frågor, användas i filter eller användas i andra funktioner som ändrar rapportens utseende baserat på parametern.|
| Fält| Fältsamlingen innehåller fälten i den aktuella datamängden.|
| Dataset||
**Operatörer**
Aritmetiska operatorer används för att kombinera tal, numeriska variabler, numeriska fält och numeriska funktioner för att få ett annat tal. Jämförelseoperatorer används vanligtvis för att jämföra operander för ett villkor i en kontrollstruktur som en If-sats. Booleska operatorer används vanligtvis med jämförelseoperatorer för att generera villkor för kontrollstrukturer.

|**Ange namn**|**Formelnamn**|**Beskrivning**|
|:- |:- |:- |
| Aritmetisk|^ | Exponentiering, till exempel 2^3.|
||* | Multiplikation, till exempel 2*3.|
||/ | Division, till exempel 2/3.|
||\\\ | Heltalsdivision, till exempel 2\\\3.|
|| Mod| Modul, till exempel 4 Mod 3.|
||+ | Tillägg, till exempel 4 + 3.|
||- | Subtraktion, till exempel 4 – 3.|
| Jämförelse|< | Mindre än till exempel 4< 3 false. |
||<= | Mindre än eller lika, till exempel 4<= 3 false. |
||> | Större än till exempel 4 > 3 sant.|
||>= | Större än eller lika, till exempel 4 >= 3 sant.|
||= | Lika, till exempel 4 = 3 falskt.|
||<> | Inte lika, till exempel 4<> 3 sant.|
|| Tycka om|Jämför en sträng mot ett mönster. Till exempel resultat = sträng Liknande mönster.|
|| Är| Jämför två objektreferensvariabler, till exempel asp Is aspose.|
| Sammankoppling|& | Genererar en strängsammansättning av två uttryck.|
||+ | Lägger till två tal eller returnerar det positiva värdet av ett numeriskt uttryck. Kan också användas för att sammanfoga två stränguttryck.|
| Logisk/Bitvis| Och| Utför en logisk konjunktion på två booleska uttryck, eller en bitvis konjunktion på två numeriska uttryck.|
|| Inte| Utför logisk negation på ett booleskt uttryck, eller bitvis negation på ett numeriskt uttryck.|
|| Eller| Utför en logisk disjunktion på två booleska uttryck, eller en bitvis disjunktion på två numeriska uttryck.|
|| Xor| Utför en logisk uteslutning på två booleska uttryck, eller en bitvis uteslutning på två numeriska uttryck.|
|| Och även| Utför kortslutande logisk konjunktion på två uttryck.|
|| Annars|Utför kortslutande inkluderande logisk disjunktion på två uttryck.|
| Bit Shift|>> | Utför ett aritmetiskt vänsterskift på ett bitmönster.|
||<< | Utför ett aritmetiskt högerskifte på ett bitmönster.|

