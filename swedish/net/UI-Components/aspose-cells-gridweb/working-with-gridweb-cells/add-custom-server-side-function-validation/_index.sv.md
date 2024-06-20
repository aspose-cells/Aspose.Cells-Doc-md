---
title: Lägg till anpassad servervalideringsfunktion
type: docs
weight: 110
url: /sv/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb, server sidans validering
description: Den här artikeln introducerar hur man arbetar med server sidans validering i GridWeb.
---

## **Möjliga användningsscenario**
Ibland kan du behöva implementera datavalidering på server-sidan. Aspose.Cells.GridWeb gör att du kan lägga till anpassad server-sidans datavalidering. Du måste specificera cellområdet eller området. Du kan även ställa in klient-sidans valideringsfunktioner för återuppringningar med anpassad server-sidans validering.
## **Lägg till anpassad server-sidans valideringsfunktion**
Du måste ange den servervalideringsklass som implementerar gränssnittet **GridCustomServerValidation** via attributet **GridValidation.ServerValidation**. Du måste också ange klient-sidans valideringsfunktion (den ska skrivas i JavaScript på klient-sidan), denna funktion måste validera datan på klienten vid återuppringning. Du kan ange felmeddelandesträngen via egenskapen **GridValidation.ErrorMessage** och titel via egenskapen **GridValidation.ErrorTitle** för dina behov. Vänligen se en serie skärmdumpar som visar hur det fungerar (steg för steg) i ett givet scenario efter att ha utfört det provkod nedan. I exemplet kan du inte uppdatera data i cellerna B2:C3. När du försöker redigera dessa celler i kalkylarket kommer du att uppmanas av felmeddelanden och det tidigare värdet återställs. Du kan öppna konsolfönstret (i din webbläsare) för att skriva ut cellens info/detaljer för vissa händelser. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
