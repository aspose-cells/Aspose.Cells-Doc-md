---
title: Skriv GridWeb klientsidsskript
type: docs
weight: 10
url: /sv/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: Denna artikel introducerar hur man arbetar med klientjs apis i GridWeb.
---

{{% alert color="primary" %}} 

Utvecklare kan skriva klientssidan skript för Aspose.Cells.GridWeb-kontrollen. Det betyder att det är möjligt att anropa en JavaScript-funktion klientsidigt för att utföra en specifik uppgift relaterad till GridWeb-kontrollen. Till exempel kan utvecklare skriva JavaScript-funktioner för att skicka GridWeb-data till en server eller visa ett varningsmeddelande när ett valideringsfel uppstår etc.

Denna artikel förklarar den här funktionen med hjälp av exempel.

{{% /alert %}} 
## **Skriva klientssidan skript för Aspose.Cells.GridWeb**
### **Grundläggande information**
Aspose.Cells.GridWeb tillhandahåller två egenskaper som skapats specifikt för att stödja klientssideskript: 

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Skapa JavaScript-funktioner i en ASPX-sida och tilldela namnen på dessa funktioner till OnSubmitClientFunction- och OnValidationErrorClientFunction-egenskaperna.

{{% alert color="primary" %}} 

JavaScript-funktionen som tilldelas OnSubmitClientFunction-egenskapen måste definieras korrekt som visas nedan: 

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

där [arg]-parametern representerar det kommando som genereras av kontrollen. Kommandot kan vara "Save", "Submit", "Undo" etc. och [cancelEdit]-parametern är ett booleskt värde som indikerar om användarindata avbryts eller inte.

Alla JavaScript-funktioner som tilldelas OnSubmitClientFunction-egenskapen kallas varje gång av GridWeb-kontrollen innan den skickar GridWeb-data till en server. Om en funktion tilldelas OnValidationErrorClientFunction-egenskapen så kommer den funktionen att kallas varje gång ett valideringsfel inträffar.

{{% /alert %}} 
### **Funktioner för klient-sideskriptning**
Aspose.Cells.GridWeb exponerar också funktioner speciellt för klient-sideskriptning. Dessa funktioner kan användas inom JavaScript-funktioner för att få mer kontroll över Aspose.Cells.GridWeb. Dessa klient-sida funktioner inkluderar följande: 

| **Funktioner** | **Beskrivning** |
| :- | :- |
|updateData(bool cancelEdit)| Uppdaterar all klientdata av Aspose.Cells.GridWeb innan den skickar den till servern. Om cancelEdit-parametern är sann kasserar GridWeb all användarindata. |
|validateAll()| Används för att kontrollera om det finns några valideringsfel i användarindata. Om det finns ett fel returnerar funktionen false, annars true. |
|submit(string arg, bool cancelEdit)| Anropa den här funktionen för att posta eller skicka data till servern. Denna funktion utför båda uppgifterna, det vill säga uppdatering av data och validering av användarindata. Denna funktion kan också utlösa en kommando händelse på server sidan. Använd arg-parametern för att skicka ditt kommando. Till exempel används kommandot SAVE för att klicka på knappen Spara på kommando raden för GridWeb kontrollen och CCMD: MYCOMMAND-kommandot talar om en anpassad kommando händelse. |
|setActiveCell(int row, int column)| Används för att aktivera en specifik cell. |
|setCellValue(int row, int column, string value)| Används för att sätta ett värde till vilken cell som helst som anges med rad- och kolumnnummer. |
|getCellValue(int row, int column)| Returnerar värdet på vilken cell som helst som anges. |
|getActiveRow()| Används i kombination med funktionen getActiveColumn () för att bestämma positionen för en aktiv cell. |
|getActiveColumn()| Används i kombination med funktionen getActiveRow () för att bestämma positionen för en aktiv cell. |
|getSelectRange()| Returnerar det sista markerade området. |
|setSelectRange()| Väljer det angivna området. |
|clearSelections()|Rensa allt urval utom aktuell aktiv cell.|
|getCellsArray()|Den används med andra relaterade funktioner som getCellName(), getCellValueByCell(), getCellRow() och getCellColumn(). Vänligen läs denna artikel för mer information om användningen av denna funktion: [Läs värdena i GridWeb-cellerna på klientens sida](/cells/sv/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)|
Följ stegen nedan för att skapa en testapplikation med klientbaserade skript som fungerar med Aspose.Cells.GridWeb:

1. Skapa JavaScript-funktioner som ska anropas av GridWeb.
   These functions will be added to the ASP.NET page's <script></script> tag.
1. Tilldela namn på funktionerna till egenskaperna OnSubmitClientFunction och OnValidationErrorClientFunction.

Exempelkoden nedan visar utdata:

**En validering tillagd till cellen C1** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

Lägg till ett ogiltigt värde och klicka på **Spara**. Ett valideringsfel inträffar och ValidationErrorFunction utförs.

**ValidationErrorFunction anropas vid valideringsfel** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

Om du inte anger ett giltigt värde skickas inga data till servern. Ange ett giltigt värde och klicka på **Spara**. ConfirmFunction utförs.

**ConfirmFunction anropas innan GridWeb-data skickas till servern** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
