---
title: Arbeta med GridWeb Events
type: docs
weight: 70
url: /sv/net/working-with-gridweb-events/
---
{{% alert color="primary" %}} 

Alla programmerare måste vara bekanta med händelser och deras syfte. Händelser används för att skicka meddelanden om ändringar som kan inträffa i en kontroll eller klass. Aspose.Cells.GridWeb har flera händelser som kan användas för att utföra specifika uppgifter när vissa förändringar sker i kontrollen.

Det här avsnittet ger en introduktion till alla händelser som stöds av Aspose.Cells.GridWeb-kontrollen tillsammans med några detaljer om hur man hanterar dessa händelser.

{{% /alert %}} 
## **Arbeta med Grid Events**
### **Introduktion till Grid Events**
Aspose.Cells.GridWeb-kontroll stöder flera händelser som ger mer kontroll för att utföra operationer när specifika händelser utlöses i kontrollen. En komplett lista över händelser som stöds av Aspose.Cells.GridWeb-kontroll finns nedan.

{{% alert color="primary" %}} 

Den här listan inkluderar inte händelser som ärvts av Aspose.Cells.GridWeb från klassen Control.

{{% /alert %}} 

|**evenemang** |**Beskrivning** |
|:- |:- |
| CellCommand| Uppstår när kommandohyperlänken för en cell klickas. När den här händelsen avfyras ger dess parameter e.Argument kommandots namn.|
| CellDoubleClick| Uppstår när cellen dubbelklickas.|
| CellError| Uppstår när en cells inmatningsvärde har något fel.|
| Kolumn Raderad|Uppstår när en användare tar bort en kolumn från ett kalkylblad med hjälp av klientsidans meny.|
| Kolumn Raderar| Uppstår när en användare försöker ta bort en kolumn från ett kalkylblad med hjälp av klientsidans meny.|
| KolumnDubbelklicka| Uppstår när kolumnrubriken dubbelklickas.|
| KolumnInfogad| Uppstår när en användare infogar en kolumn i kalkylbladet med hjälp av klientsidans meny.|
| CustomCommand| Uppstår när en användare klickar på en anpassad kommandoknapp.|
| Ladda CustomData| Uppstår när kontrollens EnableSession-egenskap är inställd på false och behöver ladda kalkylbladsdata. Du kan hantera denna händelse i sessionslöst läge för att ladda kalkylbladsdata från en fil eller databas.|
| SidindexÄndrad| Uppstår när kontrollens arksideindex ändras.|
| Radraderad| Uppstår när en användare tar bort en rad från ett kalkylblad med hjälp av klientsidans meny.|
| Radrader| Uppstår när en användare försöker ta bort en rad från ett kalkylblad med hjälp av klientsidans meny.|
| RowDoubleClick|Uppstår när radhuvudet dubbelklickas.|
| RowInserted| Uppstår när en användare infogar en rad i kalkylbladet med hjälp av klientsidans meny.|
| SaveCommand| Uppstår när**Spara** knappen klickas.|
| SheetDataUpdated| Uppstår när kontrollen har laddat in postad data och uppdaterat kalkylbladsdata.|
| SheetTabClick| Uppstår när en arkflik klickas.|
| SubmitCommand| Uppstår när**Skicka in** knappen klickas.|
| Ångra kommando| Uppstår när**Ångra** knappen klickas.|
| AjaxCallFinished| Avfyras när AJAX-uppdateringen av kontrollen är klar. (EnableAJAX ska ställas in på sant).|
| CellModifiedOnAjax| Avfyras när cellen modifieras i AJAX-anrop.|
| OnAfterColumnFilter| Avfyras efter att filtret har applicerats på en kolumn.|
| OnBeforeColumnFilter| Avfyras innan filtret appliceras på en kolumn.|
## **Hantering av Grid Events**
För att utföra en specifik operation för att utlösa en specifik händelse, måste vi skapa en händelsehanterare. En händelsehanterare utför den önskade uppgiften när en viss händelse utlöses. Stegen som illustreras nedan visar hur man hanterar en enkel grid-händelse med Visual Studio.
### **Steg 1: Välj en händelse av Aspose.Cells.GridWeb Control**
1. Välj kontrollen Aspose.Cells.GridWeb och öppna dialogrutan Egenskaper på höger sida.
1.  Klicka på**Fliken Händelser** knapp.
1. Välj en händelse.
 För det här exemplet är SaveCommand-händelsen vald.
### **Steg 2: Skapa en händelsehanterare**
1.  Dubbelklicka på en händelse i dialogrutan Egenskaper.

   **Dubbelklicka på en vald händelse** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




 När händelsen dubbelklickas skapas en händelsehanterare automatiskt av Visual Studio.

**En händelsehanterare skapad av Visual Studio** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. Lägg till kod för att utföra en åtgärd i händelsehanteraren.

 Här, en enda rad kod som sparar rutnätsinnehållet till en Excel-fil när**Spara** knappen har klickats har lagts till.

För att få mer information, flytta markören ovan för att se lite kod så kommer du att få reda på att Visual Studio är intelligent nog att lägga till en händelsehanterare till GridWeb:s SaveCommand-händelse.
### **Steg 3: Kör din applikation**
1. Bygg och kör applikationen.
1.  Klick**Spara**.

 Rutnätets innehåll sparas i en Excel-fil.

**Applikation i körläge** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
