---
title: Skriv GridWeb Client Side Script
type: docs
weight: 10
url: /sv/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

Utvecklare kan skriva skript på klientsidan för Aspose.Cells.GridWeb-kontrollen. Detta innebär att det är möjligt att anropa en JavaScript-funktion på klientsidan för att utföra en specifik uppgift relaterad till GridWeb-kontrollen. Till exempel kan utvecklare skriva JavaScript-funktioner för att skicka GridWeb-data till en server eller visa ett varningsmeddelande när ett valideringsfel uppstår etc.

Det här ämnet förklarar den här funktionen med hjälp av exempel.

{{% /alert %}} 
## **Skriva klientsideskript för Aspose.Cells.GridWeb**
### **Grundläggande information**
Aspose.Cells.GridWeb tillhandahåller två egenskaper som skapats specifikt för att stödja skript på klientsidan:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Skapa JavaScript-funktioner på en ASPX-sida och tilldela namnen på dessa funktioner till egenskaperna OnSubmitClientFunction och OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

JavaScript-funktionen som kommer att tilldelas egenskapen OnSubmitClientFunction måste definieras korrekt enligt nedan:

**JavaScript**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

där [arg]parametern representerar kommandot som genereras av kontrollen. Kommandot kan vara "Spara", "Skicka", "Ångra" etc. och parametern [cancelEdit] är ett booleskt värde, som indikerar om användarinmatningen avbryts eller inte.

Alla JavaScript-funktioner som tilldelats egenskapen OnSubmitClientFunction anropas varje gång av GridWeb-kontrollen innan GridWeb-data skickas till en server. På liknande sätt, om en funktion är tilldelad till egenskapen OnValidationErrorClientFunction kommer den funktionen att anropas varje gång ett valideringsfel inträffar.

{{% /alert %}} 
### **Funktioner för skriptning på klientsidan**
Aspose.Cells.GridWeb exponerar också funktioner speciellt för klient-side scripting. Dessa funktioner kan användas inom JavaScript-funktioner för att få mer kontroll över Aspose.Cells.GridWeb. Dessa funktioner på klientsidan inkluderar följande:

|**Funktioner**|**Beskrivning**|
|:- |:- |
|updateData(bool cancelEdit)|Uppdaterar alla klientdata för Aspose.Cells.GridWeb innan de skickas till servern. Om parametern cancelEdit är sant så ignorerar GridWeb all användarinmatning.|
|validateAll()|Används för att kontrollera om det finns några valideringsfel i användarinmatningen. Om det finns ett fel returnerar funktionen false, annars true .|
|submit(string arg, bool avbrytRedigera)|Anropa den här funktionen för att skicka tillbaka eller skicka data till servern. Denna funktion utför både uppgifter som är att uppdatera data och validera användarinmatning. Denna funktion kan även avfyra en kommandohändelse på serversidan. Använd parametern arg för att skicka ditt kommando. Till exempel: kommandot SAVE används för att klicka på**Spara** knappen på kommandofältet för GridWeb-kontrollen och kommandot CCMD:MYCOMMAND aktiverar en CustomCommand-händelse.|
|setActiveCell(int rad, int kolumn)|Används för att aktivera en specifik cell.|
|setCellValue(int rad, int kolumn, strängvärde)|Används för att sätta ett värde i valfri cell som anges med dess rad- och kolumnnummer.|
|getCellValue(int rad, int kolumn)|Returnerar värdet för en viss cell.|
|getActiveRow()|Används tillsammans med funktionen getActiveColumn() för att bestämma positionen för en aktiv cell.|
|getActiveColumn()|Används tillsammans med funktionen getActiveRow() för att bestämma positionen för en aktiv cell.|
|getSelectRange()|Returnerar det senast valda intervallet.|
|setSelectRange()|Väljer det givna intervallet.|
|clearSelections()|Raderar alla markeringar exklusive aktuell aktiv cell.|
|getCellsArray()| Den används med andra relaterade funktioner som getCellName(), getCellValueByCell(), getCellRow() och getCellColumn(). Läs den här artikeln för mer information om användningen av denna funktion:[Läs värdena för GridWeb-cellerna på klientsidan](/cells/sv/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
För att skapa ett testprogram som innehåller skript på klientsidan som fungerar med Aspose.Cells.GridWeb, följ stegen nedan:

1. Skapa JavaScript-funktioner som ska anropas av GridWeb.
 Dessa funktioner kommer att läggas till på ASP.NET-sidorna<script></script>märka.
1. Tilldela namnen på funktionerna till egenskaperna OnSubmitClientFunction och OnValidationErrorClientFunction.

Utdata från kodexemplet visas nedan:

**En validering tillagd till C1-cellen** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

 Lägg till ett ogiltigt värde och klicka**Spara**. Ett valideringsfel uppstår och ValidationErrorFunction exekveras.

**ValidationErrorFunction anropas vid valideringsfel** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

 Tills du anger ett giltigt värde skickas ingen data till servern. Ange ett giltigt värde och klicka**Spara**. Bekräftelsefunktionen körs.

**ConfirmFunction anropade innan GridWeb-data skickades till servern** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
