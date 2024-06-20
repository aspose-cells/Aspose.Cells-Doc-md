---
title: Arbetar med GridWeb händelser
type: docs
weight: 70
url: /sv/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb, händelser, händelse
description: Den här artikeln introducerar hur man arbetar med olika typer av händelser i GridWeb.
---

{{% alert color="primary" %}} 

Alla programmerare måste vara bekanta med händelser och deras syfte. Händelser används för att skicka notiser om ändringar som kan inträffa i en kontroll eller klass. Aspose.Cells.GridWeb har flera händelser som kan användas för att utföra specifika uppgifter när vissa ändringar sker i kontrollen.

Det här ämnet ger en introduktion till alla händelser som stöds av Aspose.Cells.GridWeb-kontrollen tillsammans med några detaljer om hur man hanterar dessa händelser.

{{% /alert %}} 
## **Arbeta med Rutnätshändelser**
### **Introduktion till rutnätshändelser**
Aspose.Cells.GridWeb-kontrollen stöder flera händelser som ger mer kontroll för att utföra operationer när specifika händelser utlöses i kontrollen. En komplett lista över de händelser som stöds av Aspose.Cells.GridWeb-kontrollen finns nedan.

{{% alert color="primary" %}} 

Denna lista inkluderar inte händelser som ärver från Aspose.Cells.GridWeb från Control-klassen.

{{% /alert %}} 

|**Händelser** |**Beskrivning** |
| :- | :- |
|CellCommand | Uppstår när cellens kommandohyperlänk klickas på. När denna händelse utlöses, tillhandahåller dess parameter e.Argument kommandots namn. |
|CellDoubleClick | Uppstår när cellen dubbelklickas på. |
|CellError | Uppstår när en cells inmatningsvärde har något fel. |
|ColumnDeleted | Uppstår när en användare tar bort en kolumn från en arbetsbok med klientsidomeny. |
|ColumnDeleting | Uppstår när en användare försöker ta bort en kolumn från en arbetsbok med klientsidomeny. |
|ColumnDoubleClick | Uppstår när kolumnrubriken dubbelklickas på. |
|ColumnInserted | Uppstår när en användare infogar en kolumn i arbetsboken med klientsidomeny. |
|CustomCommand | Uppstår när en användare klickar på en anpassad kommandoknapp. |
|LoadCustomData | Uppstår när kontrollens EnableSession-egenskap är inställd på false och behöver ladda arbetsboksdata. Du kan hantera denna händelse i sessionslös läge för att ladda arbetsboksdata från en fil eller en databas. |
|PageIndexChanged | Uppstår när kontrollens sidindex för blad ändras. |
|RowDeleted | Uppstår när en användare tar bort en rad från en arbetsbok med klientsidomeny. |
|RowDeleting | Uppstår när en användare försöker ta bort en rad från en arbetsbok med klientsidomeny. |
|RowDoubleClick | Uppstår när radrubriken dubbelklickas på. |
|RowInserted | Uppstår när en användare infogar en rad i arbetsboken med klientsidomeny. |
|SaveCommand | Uppstår när **Spara**-knappen klickas på. |
|SheetDataUpdated | Uppstår när kontrollen har laddat den postade datan och uppdaterat arbetsboksdatan. |
|SheetTabClick | Uppstår när en flik för blad klickas på. |
|SubmitCommand | Uppstår när **Skicka**-knappen klickas på. |
|UndoCommand | Uppstår när **Ångra**-knappen klickas på. |
|AjaxCallFinished | Uppstår när AJAX-uppdateringen av kontrollen är klar. (EnableAJAX ska vara inställt på true). |
|CellModifiedOnAjax | Uppstår när cellen ändras i AJAX-samtal. |
|OnAfterColumnFilter | Uppstår efter att filtret har tillämpats på en kolumn. |
|OnBeforeColumnFilter | Uppstår innan filtret tillämpas på en kolumn. |
## **Hantering av rutnätshändelser**
För att utföra en specifik operation på att utlösa en specifik händelse måste vi skapa en händelsehanterare. En händelsehanterare utför den önskade uppgiften när en viss händelse utlöses. De steg som illustreras nedan visar hur man hanterar en enkel rutnätshändelse med hjälp av Visual Studio.
### **Steg 1: Välja en händelse av Aspose.Cells.GridWeb kontroll**
1. Välj Aspose.Cells.GridWeb-kontrollen och öppna dess Egenskapsdialog på höger sida.
1. Klicka på fliken **Händelser**-knappen.
1. Välj en händelse.
   För detta exempel är sparhändelsen SaveCommand vald.
### **Steg 2: Skapa händelsehanterare**
1. Dubbelklicka på en händelse i egenskapsdialogrutan. 

   **Dubbelklicka på en vald händelse** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




När händelsen dubbelklickas skapas automatiskt en händelsehanterare av Visual Studio. 

**En händelsehanterare skapad av Visual Studio** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. Lägg till kod för att utföra någon åtgärd inne i händelsehanteraren.

Här har en enda rad kod lagts till som sparar rutinens innehåll i en Excelfil när **Spara**-knappen klickas.

För att få mer information, flytta markören ovanför för att se någon kod, då kommer du att upptäcka att Visual Studio är tillräckligt intelligent för att lägga till en händelsehanterare för GridWeb:s SaveCommand-händelse.
### **Steg 3: Kör din applikation**
1. Bygg och kör applikationen.
1. Klicka på **Spara**.

Rutinens innehåll sparas i en Excelfil. 

**Applikation i körläge** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
