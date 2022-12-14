---
title: Sök och ersätt i GridWeb
type: docs
weight: 90
url: /sv/net/search-and-replace-in-gridweb/
---
{{% alert color="primary" %}} 

Ett av de snabbaste sätten att göra repetitiva ändringar i ett stort kalkylblad är att använda sök- och ersätt-funktionen. Find hjälper dig att hitta en textsträng eller data och ersätta den med ett nytt värde. Aspose.Cells.GridWeb tillhandahåller denna funktion. Det gör att du kan söka efter och ersätta med en specifik textsträng eller värde i kalkylbladets klientsida genom en enkel dialog. Det låter dig till och med leta efter partiella data.

{{% /alert %}} 
## **Arbeta med Find/Replace**
### **Dialogrutan Sök/Ersätt**
Det finns två sätt att öppna dialogrutan Sök/Ersätt:

1.  När kontrollen är aktiv, tryck**CTRL+F** för att öppna dialogrutan, eller tryck**CTRL+R** för att öppna dialogrutan med**Byta ut** knappen aktiverad.
1.  Flytta markören till cellområdet i kalkylbladet och högerklicka sedan. Välj**Hitta** eller**Byta ut** från menyn.

   **Välj Sök** 

![todo:image_alt_text](search-and-replace-in-gridweb_1.png)




 En stildialogruta visas.

**Dialogrutan Sök/ersätt** 

![todo:image_alt_text](search-and-replace-in-gridweb_2.png)
### **Använder Hitta**
Att söka:

1. Öppna dialogrutan Sök/Ersätt.
1.  Skriv strängen du vill söka efter i**Hitta vad** fält.
1.  Klick**Hitta nästa** att söka.

Nästa cell som matchar ditt sökvillkor är markerad.

{{% alert color="primary" %}} 

Om ditt sökkriterium inte hittas visas en dialogruta som talar om för dig.

{{% /alert %}} 
### **Sökalternativ**
Det finns några sökalternativ som du kan anpassa i dialogrutan. Tabellen nedan listar dem.

|**Nej.** |**Alternativets namn** |**Beskrivning** |
|:- |:- |:- |
|1 | Liknande fall| Anger om skiftlägeskänsligt ska användas vid sökning.|
|2 | Matcha hela ordet| Anger om hela ordet ska matchas vid sökning.|
|3 | Sök upp|Indikerar om sökningen kommer att göras från botten till toppen.|
|4 | Vanligt uttryck| När den är markerad kommer kontrollen att behandla strängen i textrutan Hitta vad som ett reguljärt uttryck i sökprocessen.|
|5 | Hitta i Formler/Värden| När formlerna är vald kommer kontrollen att matcha formeln eller det oformaterade värdet för cellerna om formeln eller det oformaterade värdet finns. När värden är vald kommer kontrollen endast att matcha det visade värdet för cellerna.|
### **Använder Ersätt**
Så här ersätter du text eller värden:

1.  Öppna dialogrutan Sök/Ersätt genom att trycka på**CTRL+F** , eller välj högerklicka på en cell och välj**Hitta** innan du klickar**Byta ut**.
1.  Skriv ersättningssträngen i**Ersätta med** fält.
1.  Klick**Byta ut**.

Så här ersätter du text:

1. Öppna dialogrutan.
1.  Skriv in texten du vill hitta i**Hitta vad** och texten du vill ersätta den med i**Ersätta med** fält.
1.  Ersätt en förekomst i taget genom att klicka**Hitta nästa** följd av**Byta ut**.
1.  Om du är väldigt säker på vad arbetsbladet innehåller, klicka**Ersätt alla**.

{{% alert color="primary" %}} 

 Om kalkylbladet inte är i redigeringsläge,**Byta ut** knappen visas inte.

{{% /alert %}}
