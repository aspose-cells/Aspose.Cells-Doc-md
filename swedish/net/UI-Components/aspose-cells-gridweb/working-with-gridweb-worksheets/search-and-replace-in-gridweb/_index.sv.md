---
title: Sök och ersätt i GridWeb
type: docs
weight: 90
url: /sv/net/aspose-cells-gridweb/search-and-replace-in-gridweb/
keywords: GridWeb,sök,ersätt
description: Den här artikeln introducerar hur man söker och ersätter i GridWeb.
---

{{% alert color="primary" %}} 

Ett av de snabbaste sätten att göra upprepande ändringar i en stor kalkylblad är att använda funktionen Hitta och ersätt. Hitta hjälper dig att hitta en textsträng eller data och ersätta det med ett nytt värde. Aspose.Cells.GridWeb ger denna funktion. Den gör det möjligt för dig att söka efter och ersätta med en specifik textsträng eller värde i kalkylarket klient-sida genom en enkel dialogruta. Den låter dig till och med söka efter partiella data.

{{% /alert %}} 
## **Arbeta med Hitta/Ersätt**
### **Hitta/Ersätt Dialogrutan**
Det finns två sätt att öppna Hitta/Ersätt dialogrutan på:

1. När kontrollen är aktiv, tryck på **CTRL+F** för att öppna dialogrutan, eller tryck på **CTRL+R** tangenten för att öppna dialogrutan med **Ersätt**-knappen aktiverad.
1. Flytta markören till cellområdet i kalkylbladet, högerklicka sedan. Välj **Hitta** eller **Ersätt** från menyn. 

   **Välja Hitta** 

![todo:image_alt_text](search-and-replace-in-gridweb_1.png)




En stil dialogruta visas. 

**Hitta/ersätt dialogrutan** 

![todo:image_alt_text](search-and-replace-in-gridweb_2.png)
### **Använda Hitta**
För att söka:

1. Öppna Hitta/ersätt dialogrutan.
1. Skriv in den sträng du vill söka efter i fältet **Hitta vad**.
1. Klicka på **Hitta nästa** för att söka.

Nästa cell som matchar din sökning markeras.

{{% alert color="primary" %}} 

Om din sökfråga inte hittas visas en dialogruta för att meddela dig.

{{% /alert %}} 
### **Sökalternativ**
Det finns några sökalternativ som du kan anpassa i dialogrutan. Tabellen nedan listar dem.

|**Nr.** |**Alternativnamn** |**Beskrivning** |
| :- | :- | :- |
|1 |Matcha skiftläge |Indikerar om sökning ska vara skiftlägeskänslig. |
|2 |Matcha helt ord |Indikerar om hela ordet ska matchas i sökningen. |
|3 |Sök uppåt |Indikerar om sökningen ska göras från botten till toppen. |
|4 |Reguljärt uttryck |När det är markerat kommer kontrollen att behandla strängen i fältet Hitta vad som ett reguljärt uttryck i sökprocessen. |
|5 |Hitta i formler/värden |När Formler är valt matchar kontrollen formeln eller den oformaterade värdet för cellerna om formeln eller det oformaterade värdet är närvarande. När Värden är valt matchar kontrollen endast det visade värdet för cellerna. |
### **Använda Ersätt**
För att ersätta text eller värden:

1. Öppna Hitta/ersätt dialogrutan genom att trycka på **CTRL+F**, eller högerklicka på en cell och välj **Hitta** innan du klickar på **Ersätt**.
1. Skriv in ersättningssträngen i fältet **Ersätt med**.
1. Klicka på **Ersätt**.

För att ersätta text:

1. Öppna dialogrutan.
1. Skriv in den text du vill hitta i fältet **Hitta vad**, och den text du vill ersätta den med i fältet **Ersätt med**.
1. Ersätt en förekomst åt gången genom att klicka på **Hitta nästa** följt av **Ersätt**.
1. Om du är väldigt säker på vad arbetsbladet innehåller, klicka på **Ersätt alla**.

{{% alert color="primary" %}} 

Om arbetsbladet inte är i redigeringsläge visas inte **Ersätt**-knappen.

{{% /alert %}}
