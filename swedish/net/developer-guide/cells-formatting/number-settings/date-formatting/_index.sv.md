---
title: Hur man formaterar nummer som datum
type: docs
weight: 10
url: /sv/net/format-number-to-date/
description: Den här artikeln kommer att visa hur man formaterar nummer till datum med API t Aspose.Cells for .NET.
keywords: formatera nummer som datum, cellnummerinställningar, formatera nummer till datum, datuminställningar, datumformat.
---

## **Möjliga användningsscenario**
Formatering av nummer som datum i Excel (eller annan kalkylbladsprogramvara) är viktigt av flera skäl, särskilt när du arbetar med data som inkluderar tid eller schemaläggningsinformation. Här är varför det är fördelaktigt att formatera nummer till datum:

1. Korrekt tolkning av datumvärden: i Excel lagras datum som serienummer (t.ex. 1 representerar 1 januari 1900 och 44210 representerar den 6 september 2021). Om dessa nummer inte är formaterade som datum kan användare se meningslösa nummer i stället för igenkännbara datum. Korrekt formatering gör att Excel kan visa dem som faktiska datum (t.ex. 06/09/2021 istället för 44210).
1. Förenklar tidsrelaterade beräkningar: Excel kan utföra många beräkningar med datum, såsom att beräkna antalet dagar mellan två datum, lägga till eller dra ifrån dagar, eller bestämma veckodagen. Om numren inte är formaterade som datum kan Excel inte utföra dessa operationer effektivt. Till exempel, om du vill veta antalet dagar mellan 01/09/2023 och 01/10/2023, kan Excel lätt beräkna detta om numren är i datumformat.
1. Säkerställer konsistens: när alla datumrelaterade värden är korrekt formaterade, säkerställer det att alla datum visas i en enhetlig, lättläst stil. Denna konsekvens är viktig i affärsrapporter, projekttidsplaner och databaser där datumkonsistens är avgörande.
Olika regioner använder olika datumformat (t.ex. MM/DD/YYYY i USA versus DD/MM/YYYY i många andra länder), så formatering hjälper till att säkerställa att datum tolkas korrekt.
1. Förbättrar läsbarheten: Datum presenterade i ett standardformat (t.ex. 01/01/2024) är lättare att läsa än råa serienummer som 45000. Rätt datumformatering gör ditt kalkylblad mer användarvänligt och förhindrar förvirring. Detta är särskilt viktigt i sammanhang som schemaläggning, tidslinjer, eventplanering eller historisk data.
1. Hjälper vid sortering och filtrering: när datum är korrekt formaterade erkänner Excel dem som faktiska datum, vilket gör det enklare att sortera eller filtrera data kronologiskt. Till exempel kan du sortera en lista av händelser efter datum eller filtrera ett dataintervall för att visa endast poster mellan två specifika datum. Utan korrekt datumformat kan sorteringen ske baserat på det råa numret i stället för faktiska kalenderdatum.
1. Möjliggör användning av datumfunktioner: Excel tillhandahåller ett brett utbud av kraftfulla datumfunktioner, såsom: IDAG(), DATEDIF(), ARBETSDAG(), ÅR(), MÅNAD(), DAG(). Dessa funktioner kräver att datum är rätt formaterade för att ge korrekta beräkningar.
1. Underlättar visualisering (diagram/tidslinjer): Datum som är formaterade korrekt kan användas för att skapa diagram och grafer där tid är en nyckelaxel. Till exempel, i ett tidslinjediagram, behöver Excel datum i ett igenkännbart format för att plotta händelser exakt över tid. Felaktigt formaterade eller ostrukturerade nummer kan leda till diagram som inte är meningsfulla eller reflekterar felaktig information.
1. Förhindrar feltolkning: råa nummer kan lätt missförstås. Till exempel kan 44210 tolkas som ett generellt numeriskt värde, men när det är formaterat som ett datum är det tydligt att det representerar 6 september 2021. Korrekt formatterade datum hjälper till att undvika felaktig tolkning av data.
1. Underlättar datainmatning: När cellerna är formaterade som datum, får användare en prompt att ange data i ett giltigt datumformat, vilket förhindrar datainmatningsfel och säkerställer att datumvärdena registreras korrekt.
1. Kritisk för schemaläggning och spårning: I alla situationer som innebär schemaläggning, spårning eller deadlines (som projektledning, finansiell prognostisering eller tidskänsliga rapporter) är formatering av nummer som datum avgörande för noggrannhet och förståelse. Det möjliggör bättre planering och genomförande.


## **Hur man formaterar nummer till datum i Excel**
För att formatera ett nummer som datum i Excel, följ dessa steg:

### **Med hjälp av bandet (Startfliken)**
1. Markera cellerna som innehåller talen du vill formatera som datum.
1. Gå till startfliken i bandet.
1. I gruppen Nummer, klicka på nedladdningspilen i rutan för Nummerformat (som kan visa "Allmänt" eller "Tal" som standard).
1. Välj Kort datum eller Långt datum från dropdown-menyn. Kort datum: Visar datumet i ett komprimerat format, t.ex. MM/DD/ÅÅÅÅ (US-format) eller DD/MM/ÅÅÅÅ (internationellt format). Långt datum: Visar datumet i ett mer beskrivande format, t.ex. måndag, januari 1, 2024.
<br>
<img src="1.png" width=60% />

### **Med hjälp av dialogrutan Formatera celler**
1. Markera cellerna du vill formatera.
1. Högerklicka på de markerade cellerna och välj Formatera celler, eller tryck Ctrl + 1 (Windows) eller Cmd + 1 (Mac).
1. I dialogrutan Formatera celler, gå till fliken Nummer.
1. Välj Datum från listan till vänster.
1. Välj önskat datumformat från listan till höger (t.ex. MM/DD/ÅÅÅÅ, DD/MM/ÅÅÅÅ eller anpassade format).
<br>
<img src="2.png" width=60% />
1. Klicka på OK för att tillämpa datumformatet.

## **Hur man formaterar nummer till datum i Aspose.Cells**

För att formatera nummer som datum i biblioteket Aspose.Cells for .NET för att arbeta med Excel-filer kan du tillämpa datumformatering programmatiskt på celler. Så här kan du göra med C# och Aspose.Cells:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Numbers-format-date.cs" >}}
{{< app/cells/assistant language="csharp" >}}
