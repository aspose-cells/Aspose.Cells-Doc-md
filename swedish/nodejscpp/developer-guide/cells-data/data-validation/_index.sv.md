---  
title: Datavalidering
type: docs  
weight: 90  
url: /sv/nodejs-cpp/data-validation/  
description: Lär dig hur man lägger till datavalidering med hjälp av API n Aspose.Cells for Node.js via C++.  
keywords: Lägg till Data Validation Node.js via C++, Hämta Validation Value Node.js via C++, Lägg till Whole Number Data Validation Node.js via C++, Lägg till List Data Validation Node.js via C++, Lägg till Date Data Validation Node.js via C++, Lägg till Time Data Validation Node.js via C++, Lägg till Text Length Data Validation Node.js via C++, Lägg till CellArea till befintlig validering Node.js via C++, Kontrollera om valideringen i cellen är dropdown Node.js via C++, Lägg till anpassad validering Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel erbjuder bra funktioner för att automatiskt filtrera eller validera arbetsbladdata. Aspose.Cells stöder fullt ut Microsoft Excels data validerings- och autofilterfunktioner. Denna artikel förklarar hur man använder funktionerna i Microsoft Excel och hur man kodar dem med Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

## **Datavalideringstyper och utförande**  

Datavalidering är förmågan att ställa regler om data som skrivs in på ett arbetsblad. Använd till exempel validering för att säkerställa att en kolumn märkt DATUM endast innehåller datum, eller att en annan kolumn endast innehåller siffror. Du skulle även kunna säkerställa att en kolumn märkt DATUM endast innehåller datum inom ett visst intervall. Med datavalidering kan du kontrollera vad som skrivs in i celler på arbetsbladet.  

Microsoft Excel stöder ett antal olika typer av datavalidering. Varje typ används för att styra vilken typ av data som skrivs in i en cell eller cellområde. Nedan illustrerar kodsnuttar hur man validerar att:  

- Siffror är hela, det vill säga att de inte har en decimaldel.  
- Decimaltal följer rätt struktur. Kodexemplet definierar att en rad celler ska ha två decimaler.  
- Värden är begränsade till en lista med värden. Listvalidering definierar en separat lista med värden som kan tillämpas på en cell eller cellområde.  
- Datum ligger inom ett specifikt intervall.  
- En tid ligger inom ett specifikt intervall.  
- En text är inom en given teckenlängd.  

### **Datavalidering med Microsoft Excel**  

För att skapa valideringar med Microsoft Excel:  

1. I ett kalkylblad, välj de celler till vilka du vill applicera validering.  
1. Från menyn **Data**, välj **Validering**. Valideringsdialogen visas.  
1. Klicka på fliken **Inställningar** och ange inställningar.  

### **Datavalidering med Aspose.Cells for Node.js via C++**  

Datavalidering är en kraftfull funktion för att validera information som matas in i kalkylblad. Med datavalidering kan utvecklare tillhandahålla användare med en lista över val, begränsa datamatare till en specifik typ eller storlek, osv.  
I Aspose.Cells for Node.js via C++ har varje [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) klass en [**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--) metod som representerar en samling av [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) objekt. För att ställa in valideringen, ställ in några av egenskaperna hos klassen [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) enligt följande:  

- Typ – representerar valideringstypen, som kan specificeras genom att använda ett av de fördefinierade värdena i enum [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype).  
- Operator – representerar operatorn som ska användas i valideringen, som kan specificeras genom att använda ett av de fördefinierade värdena i enum [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype).  
- Formel1 - representerar värdet eller uttrycket associerat med den första delen av datavalideringen.  
- Formel2 - representerar värdet eller uttrycket associerat med den andra delen av datavalideringen.  

När egenskaperna för [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) objektet har konfigurerats, kan utvecklare använda strukturen [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) för att lagra information om cellområdet som ska valideras med hjälp av den skapade valideringen.  

#### **Typer av Datavalidering**  

Enum [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) har följande medlemmar:  

| **Medlemsnamn** | **Beskrivning** |  
| :- | :- |  
|AnyValue|Betecknar ett värde av valfri typ.  
|WholeNumber|Betecknar valideringstyp för heltal.  
|Decimal|Betecknar valideringstyp för decimaltal.  
|List|Betecknar valideringstyp för nedrullningslistan.  
|Date|Betecknar valideringstyp för datum.  
|Time|Betecknar valideringstyp för tid.  
|TextLength|Betecknar valideringstyp för längden av text.  
|Custom|Betecknar anpassad valideringstyp.  

##### **Heltalsdatavalidering**  

Med denna typ av validering kan användare bara ange heltal inom ett specificerat intervall i de validerade cellerna. Följande kodexempel visar hur man implementerar WholeNumber-typ av validering. Exemplet skapar samma data validering med Aspose.Cells for Node.js via C++ som vi skapade med Microsoft Excel ovan.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **Listvalidering**  

Denna typ av validering tillåter användaren att mata in värden från en nedrullningslista. Det tillhandahåller en lista: en serie rader som innehåller data. I exemplet läggs ett andra kalkylblad till för att hålla listkällan. Användare kan endast välja värden från listan. Valideringsområdet är cellområdet A1:A5 i det första kalkylbladet.  

Det är viktigt här att du ställer in egenskapen [**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-) på **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **Datumdata validering**  

Med denna typ av validering anger användare datumvärden inom ett angivet intervall eller enligt specifika kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange datum mellan 1970 och 1999. Här är valideringsområdet cell B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **Tidsdata validering**  

Med denna typ av validering kan användare ange tider inom ett angivet intervall eller enligt vissa kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange tider mellan 09:00 och 11:30 förmiddag. Här är valideringsområdet cell B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **Textlängd data validering**  

Med denna typ av validering kan användare ange textvärden av en angiven längd i de validerade cellerna. I exemplet är användaren begränsad att ange strängvärden med högst 5 tecken. Valideringsområdet är cell B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **Data valideringsregler**  

När datavalideringar implementeras kan valideringen kontrolleras genom att tilldela olika värden i cellerna. [**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) kan användas för att hämta valideringsresultatet. Följande exempel visar den här funktionen med olika värden. Exempelfilen kan hämtas via länken nedan för testning:  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **Kontrollera om valideringen i cellen är rullgardinsmeny**  

Som vi har sett finns det många typer av valideringar som kan implementeras inom en cell. Om du vill kontrollera om valideringen är en rullgardinslista, kan [**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--)-metoden användas för att testa detta. Följande exempel visar användningen av denna egenskap. En testfil kan laddas ner via länken nedan:  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **Lägg till CellArea till befintlig validering**  

Det kan finnas situationer där du vill lägga till [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) till befintliga [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation). När du lägger till [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) med [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-) kontrollerar Aspose.Cells alla befintliga områden för att se om det nya området redan finns. Om filen har många valideringar kan detta påverka prestandan. För att lösa detta finns metoden [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-). Parametern *checkIntersection* anger om korsningen mellan ett givet område och befintliga valideringsområden ska kontrolleras. Att sätta den till **false** kommer att inaktivera kontroll av andra områden. Parametern *checkEdge* indikerar om de tillämpade områdena ska kontrolleras. Om det nya området blir det övre vänstra området, byggs interna inställningar om. Om du är säker på att det nya området inte är det övre vänstra, kan du ange denna parameter som **false**.  

Följande kodsnutt visar användningen av [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-)-metoden för att lägga till en ny [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) till befintliga [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

Käll- och utdataexcelfilerna är bilagda som referens.  

[Källfil](96928093.xlsx)  

[Utdatafil](96928220.xlsx)  

## **Fortsatta ämnen**  
- [Hämta cellvalidering i ODS-filer](/cells/sv/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [Få validering som tillämpas på en cell](/cells/sv/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [Verifiera att cellvärdet uppfyller datavalideringsreglerna](/cells/sv/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

