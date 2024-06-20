---
title: Lägg till GridWeb på Webbformulär
type: docs
weight: 10
url: /sv/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: I den här artikeln introduceras hur man arbetar med webbformulär i GridWeb.
---

{{% alert color="primary" %}} 

Det här ämnet ger en grundläggande steg-för-steg-guide för nybörjare för att hjälpa dem skapa och använda Aspose.Cells.GridWeb-kontrollen i webbapplikationer.

{{% /alert %}} 
## **Skapa & Använda Aspose.Cells.GridWeb Control**
### **Steg 1: Skapa ett webbapplikationsprojekt**
Skapa först ett webbapplikationsprojekt där Aspose.Cells.GridWeb-kontrollen ska användas:

1. Öppna Visual Studio.
1. Från **Arkiv**-menyn väljer du **Ny** följt av **Projekt**. 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



En Ny projektdialog visas.

1. Välj **ASP.NET Web Application** för önskat språk. 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. Välj **Webbformulär**-mall. 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. Lägg till ett nytt webbformulär i projektet.
### **Steg 2: Bädda in kontrollen i webbformuläret**
Dra och släpp Aspose.Cells.GridWeb-kontrollen från Visual Studio-verktygslådan till webbformuläret. 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

För att lära dig hur du lägger till Aspose.Cells Grid-kontroller i Visual Studio-verktygslådan, läs [Integrera Aspose.Cells.Grid Controls with Visual Studio.NET](/cells/sv/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

När kontrollen har lagts till i formuläret renderas den så här: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **Steg 3: Ändra storleken på kontrollen**
Formuläret renderas med en standardstorlek. Justera storleken genom att dra i kanterna eller hörnen. 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **Steg 4: Ställa in kontrollens egenskaper**
Aspose.Cells.GridWeb-kontrollen kan även konfigureras med olika egenskaper. 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

Det är möjligt att justera många egenskaper hos kontrollen med hjälp av egenskapsdialogen. Grundläggande egenskaper inkluderar höjd, bredd, färg och visuella stilar. Avancerade egenskaper inkluderar redigeringsläge, sessionläge och dubbelklicksläge. Dessutom är det möjligt att ställa in anpassade händelsehanterare i egenskapsdialogen.

Det finns också några extra konfigurationsverktyg för Aspose.Cells.GridWeb som kan ses längst ner i egenskapsdialogen som hyperlänkar, eller högerklicka på GridWeb-kontrollen för att hitta dem. Dessa konfigurationsverktyg inkluderar:

- Anpassade kommandoknappar
#### **Anpassade kommandoknappar**
För att öppna redigeraren för anpassade kommandoknappar:
Högerklicka på GridWeb-kontrollen och välj **Anpassade kommandoknappar**. 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



Dialogrutan för anpassad kommandoknappskollektion visas. 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

Dialogrutan låter utvecklare lägga till och ta bort anpassade kommandoknappar i GridWeb-kontrollen.


### **Viktigt**
Aspose.Cells.GridWeb tillhandahåller även sina resursfiler med kontrollen. "acw_client" är en mapp (i din installationsmapp) som innehåller filer och Aspose.Cells.GridWeb använder denna mapp för att hantera sin interna konfiguration och annan funktionalitet; den har skriptfiler, bildfiler och andra filer för att specificera GridWebs beteende och utföra andra operationer. Konfigurationsfilen används för att hantera inbäddade klientresurser (bilder, skript, etc.). Dessutom, när du behöver distribuera webbapplikationen med GridWeb-kontrollen, bör du också kopiera mappen "acw_client" till din projektmapp minst din webbapplikation (som distribueras över servern) kan inte hitta den. Du kan alltid ange resursmappen genom att lägga till följande kodrader i konfigurationsavsnittet (t.ex. i web.config-filen i ditt VS.NET-projekt):



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

Sökvägen är alltid relaterad till projektets mapp. Du bör inte använda någon mapp som ligger utanför projektets mapp. Så det är nödvändigt att kopiera mappen "acw_client" (i din GridWeb-installationsmapp) till projektets mapp/undermapp.

{{% /alert %}}
### **Steg 5: Kör webbapplikationen**
Kör applikationen genom att trycka på Ctrl+F5 eller klicka på **Start**-knappen. 

När applikationen körs i en webbläsare visas sidan WebForm1.aspx, nu med en tom Aspose.Cells.GridWeb-kontroll. Lägg till värden i celler genom att klicka på dem. Det är också möjligt att utföra andra uppgifter som att ändra höjden på en rad eller bredden på en kolumn, kopiera (Ctrl+C) eller klippa (Ctrl+X) celldata till urklippet och klistra in (Ctrl+V) data till cellen. För att utföra fler operationer, högerklicka på kontrollen för att se hela listan över alternativ. 

**Kontextmeny för GridWeb-kontroll** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
