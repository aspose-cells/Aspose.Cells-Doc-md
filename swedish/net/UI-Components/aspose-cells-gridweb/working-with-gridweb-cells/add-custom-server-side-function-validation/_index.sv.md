---
title: Lägg till anpassad funktionsvalidering på serversidan
type: docs
weight: 110
url: /sv/net/add-custom-server-side-function-validation/
---
## **Möjliga användningsscenarier**
Ibland kan du behöva implementera datavalidering på serversidan. Aspose.Cells.GridWeb låter dig lägga till anpassad datavalidering på serversidan. Du måste ange cellområdet eller området. Du kan också ställa in valideringsfunktioner på klientsidan för återuppringningar med anpassad validering på serversidan.
## **Lägg till anpassad funktionsvalidering på serversidan**
 Du måste ställa in servervalideringsklassen som implementerar**GridCustomServerValidation** gränssnitt via**GridValidation.ServerValidation** attribut. Du måste också ställa in valideringsfunktionen på klientsidan (den bör skrivas i JavaScript på klientsidan), den här funktionen är obligatorisk för att validera data på klientsidan vid callback. Du kan ställa in felmeddelandesträngen via**GridValidation.ErrorMessage** och titel via**GridValidation.ErrorTitle**fastigheter för dina behov. Se en serie skärmdumpar som visar hur det fungerar (steg för steg) i ett givet scenario efter att ha kört exempelkoden nedan. I exemplet kan du inte uppdatera data i B2:C3-celler. När du försöker redigera dessa celler i arket kommer du att få några felmeddelanden och tidigare värde återställs. Du kan öppna konsolfönstret (i din webbläsare) för att skriva ut cellinformation/detaljer för vissa händelser.

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
