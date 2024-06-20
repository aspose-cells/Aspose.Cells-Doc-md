---
title: Datavalidering
type: docs
weight: 70
url: /sv/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel tillhandahåller några bra funktioner för att autofiltrera eller validera arbetsbladsdata.

[Datavalidering](/cells/sv/java/data-validation/) är förmågan att ställa regler för data som matas in på ett arbetsblad. Använd till exempel validering för att säkerställa att en kolumnmärkt DATUM endast innehåller datum eller att en annan kolumn endast innehåller nummer. Du kan till och med se till att en kolumnmärkt DATUM endast innehåller datum inom ett visst intervall. Med datavalidering kan du kontrollera vad som matas in i celler på arbetsbladet. Aspose.Cells stöder fullt ut Microsoft Excels datavalidering och autofiltreringsfunktioner. Denna artikel förklarar hur man använder funktionerna i Microsoft Excel och hur man kodar dem med användning av Aspose.Cells.

{{% /alert %}} 
## **Datavalideringstyper och utförande**
Microsoft Excel stöder ett antal olika typer av datavalidering. Varje typ används för att styra vilken typ av data som skrivs in i en cell eller cellområde. Nedan illustrerar kodsnuttar hur man validerar att:

- [Siffror är hela](/cells/sv/java/data-validation/), det vill säga att de inte har en decimaldel.
- [Decimaltal följer rätt struktur](/cells/sv/java/data-validation/). Kodexemplet definierar att en rad celler bör ha två decimalplatser.
- [Värden är begränsade till en lista över värden](/cells/sv/java/data-validation/). Listvalidering definierar en separat lista över värden som kan tillämpas på en cell eller cellintervall.
- [Datum faller inom ett specifikt intervall](/cells/sv/java/data-validation/).
- [Tiden är inom ett specifikt intervall](/cells/sv/java/data-validation/).
- [En text är inom en given teckenlängd](/cells/sv/java/data-validation/).
### **Datavalidering med Microsoft Excel**
För att skapa valideringar med Microsoft Excel:

1. I ett kalkylblad, välj de celler till vilka du vill applicera validering.
1. Från menyn **Data** väljer du **Validering**.
   Valideringsdialogrutan visas.
1. Klicka på fliken **Inställningar** och ange inställningar enligt nedan. 

   **Datavalideringsinställningar** 

![todo:image_alt_text](data-validation_1.png)
### **Datavalidering med Aspose.Cells**
Datavalidering är en kraftfull funktion för att validera information som matas in i kalkylblad. Med datavalidering kan utvecklare tillhandahålla användare med en lista över val, begränsa datamatare till en specifik typ eller storlek, osv.
I Aspose.Cells har varje [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klass en [Validations](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)-objekt som representerar en samling [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)-objekt. För att ställa in validering, ange några av egenskaperna i [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)-klassen:

- [Typ](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): representerar valideringstypen, som kan anges genom att använda något av de fördefinierade värdena i [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)-uppräkningen.
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): representerar operatören som ska användas i valideringen, vilket kan anges genom att använda något av de fördefinierade värdena i [OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)-uppräkningen.
- [Formula1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): representerar värdet eller uttrycket förknippat med den första delen av datavalideringen.
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): representerar värdet eller uttrycket förknippat med den andra delen av datavalideringen.

När egenskaperna för objektet [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) har konfigurerats kan utvecklare använda strukturen [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) för att lagra information om cellområdet som kommer att valideras med den skapade valideringen.
#### **Typer av Datavalidering**
Datavalidering gör det möjligt att bygga affärsregler in i varje cell så att felaktiga inmatningar resulterar i felmeddelanden. Affärsregler är de policys och förfaranden som styr hur ett företag fungerar. Aspose.Cells stöder alla viktiga typer av datavalidering.

Uppräkningen [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType) har följande medlemmar:

| **Medlemsnamn** | **Beskrivning** |
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Anger ett värde av vilken typ som helst.
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Anger valideringstyp för heltal.
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Anger valideringstyp för decimaltal.
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Anger valideringstyp för nedrullningslist.
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Anger valideringstyp för datum.
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Anger valideringstyp för tid.
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Anger valideringstyp för längden på texten.
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Anger anpassad valideringstyp.
#### **Programexempel: Heltalsdatavalidering**
Med den här typen av validering kan användare endast ange heltal inom ett angivet intervall i de validerade cellerna. Kodexemplen nedan visar hur man implementerar valideringstypen [WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER) med Aspose.Cells. Exemplet skapar samma datavalidering med Aspose.Cells som vi skapade med Microsoft Excel ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Programexempel: Decimaltaldatavalidering**
Med den här typen av validering kan användaren ange decimaltal i de validerade cellerna. I exemplet är användaren begränsad att ange endast decimalvärde och valideringsområdet är A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Programexempel: Lista för datavalidering**
Denna typ av validering gör att användaren kan ange värden från en nedrullningslista. Det tillhandahåller en lista: en serie rader som innehåller data. Användare kan bara välja värden från listan. Valideringsområdet är cellområdet A1:A5 i den första arbetsboken.

Det är viktigt här att du ställer in egenskapen [Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) till **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Programexempel: Datumdatavalidering**
Med denna typ av validering anger användare datumvärden inom ett angivet intervall eller enligt specifika kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange datum mellan 1970 och 1999. Här är valideringsområdet cell B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Programexempel: Tidsdatavalidering**
Med denna typ av validering kan användare ange tider inom ett angivet intervall eller enligt vissa kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange tider mellan 09:00 och 11:30 förmiddag. Här är valideringsområdet cell B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Programexempel: Textlängd för datavalidering**
Med denna typ av validering kan användare ange textvärden av en angiven längd i de validerade cellerna. I exemplet är användaren begränsad att ange strängvärden med högst 5 tecken. Valideringsområdet är cell B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Data valideringsregler**
När datavalideringar är implementerade kan valideringen kontrolleras genom att tilldela olika värden i cellerna. [Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) kan användas för att hämta valideringsresultatet. Följande exempel demonstrerar denna funktion med olika värden. Testfilen kan laddas ner från följande länk för testning:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Kontrollera om validering i en cell är en nedrullningslista**
Som vi har sett finns det många typer av valideringar som kan implementeras inom en cell. Om du vill kontrollera om valideringen är en nedrullningslista eller inte kan egenskapen [Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) användas för att testa detta. Följande kodexempel demonstrerar användningen av denna egenskap. Testfilen kan laddas ner från följande länk för testning:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Lägg till CellArea till befintlig validering**
Det kan finnas fall där du vill lägga till [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) till befintlig [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). När du lägger till [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) med hjälp av [Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), kontrollerar Aspose.Cells alla befintliga områden för att se om det nya området redan finns. Om filen har ett stort antal valideringar påverkar detta prestandan. För att komma över detta tillhandahåller API:et metoden [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)). Parametern *checkIntersection* anger områdets snitt med befintliga valideringsområden. Om du ställer in den till **false** inaktiveras kontrollen av andra områden. Parametern *checkEdge* anger om kanten ska kontrolleras. Om det nya området blir det övre vänstra området byggs interna inställningar om igen. Om du är säker på att det nya området inte är det övre vänstra området kan du ställa in den här parametern som **false**.

Följande kodsnutt demonstrerar användningen av metoden [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) för att lägga till ny [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) till befintlig [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Käll- och utdataexcelfilerna är bilagda som referens.

[Källfil](PivotTableHideAndSortSample.xlsx)

[Output-fil](ValidationsSample_out.xlsx)


## **Fortsatta ämnen**
- [Hämta cellvalidering i ODS-filer](/cells/sv/java/get-cell-validation-in-ods-files/)
- [Få validering som tillämpas på en cell](/cells/sv/java/get-validation-applied-on-a-cell/)
- [Verifiera att cellvärdet uppfyller datavalideringsreglerna](/cells/sv/java/verify-that-cell-value-satisfies-data-validation-rules/)
