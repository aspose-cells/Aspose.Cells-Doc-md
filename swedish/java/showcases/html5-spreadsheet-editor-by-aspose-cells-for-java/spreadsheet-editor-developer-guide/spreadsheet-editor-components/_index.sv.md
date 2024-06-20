---
title: Kalkylbladsredigerare  Komponenter
type: docs
weight: 50
url: /sv/java/spreadsheet-editor-components/
---

Innehållsförteckning

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [Kalkylbladsvisning](#SpreadsheetEditor-Components-WorksheetView)
- [Arbetsbokstjänst](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5 kalkylbladsredigerare är byggd från några komponenter som samverkar för att skapa det kompletta systemet. Här beskriver vi syftet och rollen för varje komponent.
### **Index.html**
Det är en JSF-sida som beskriver gränssnittet för redigeraren och huvudändpunkten för vår applikation. All interaktion som utförs mellan webbläsare och server utförs genom denna ändpunkt.

Förutom att definiera gränssnittet är alla bakre tjänster bundna här med hjälp av JSF-tekniker. När användaren interagerar med gränssnittet skickas händelser och data fram och tillbaka mellan tjänster och användare för att slutföra våra uppgifter t.ex. exportera kalkylblad.

Den har två huvudsakliga intresseområden.

Ribbon

Det flikade verktygsfältet högst upp kallas tekniskt sett ribbon. Det innehåller knappar, rullgardinsmenyer, radiomenyer, textrutor och några dolda fält som används för att utföra många operationer på kalkylbladet. Dessa knappar skickar kommandon till servern när de klickas och uppdaterar arket därefter.

Sheet

Arket består av rader och kolumner. När celler klickas uppdateras ribbon därefter utan att skicka förfrågningar till servern eftersom all data som behövs av ribbon är bifogad till varje cell. Ribbon håller också koll på vald cell, rad och kolumn när användaren navigerar genom arket.

Varje cell har sin egen inbyggda redigerare som blir synlig när en cell är i redigeringsläge.
### **Kalkylbladsvisning**
Det är en visningsomfattande JSF-bakre bön ansvarig för att hantera de dynamiska innehållet i gränssnittet som beskrivs i index.html. Den har händelsehanterare för Ajax-begäranden som utlöses när användaren interagerar med gränssnittet.
### **Arbetsbokstjänst**
Arbetsbokstjänsten är en visningsomfattande JSF-bakre bön. Den fungerar som en tjänstekomponent och laddar och lossar kalkylblad med hjälp av andra tjänster. Den har följande ändpunkter:

**init**

Init är en PostConstruct-metod som utförs direkt efter att objektskapandet är slutfört av Java Application Server. Den kontrollerar om url-parametern finns i begärande parametrar och laddar det motsvarande kalkylarket från den angivna platsen, om möjligt.

**destroy**

Den ansvarar för att rensa upp alla förvärvade resurser när de inte längre behövs.
### **LoaderService**
Den skapar instanser av kalkylblad och behåller dem i minnet så länge de behövs.
### **CellsService**
CellsService hanterar cache av rader, kolumner, celler, formatering och struktur av kalkylblad.
