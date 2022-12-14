---
title: Datavalidering
type: docs
weight: 70
url: /sv/java/data-validation/
---
{{% alert color="primary" %}} 

Microsoft Excel tillhandahåller några bra funktioner för att automatiskt filtrera eller validera kalkylbladsdata.

[Datavalidering](/cells/sv/java/data-validation/)är möjligheten att ställa in regler som hänför sig till data som matas in på ett kalkylblad. Använd till exempel validering för att säkerställa att en kolumn märkt DATUM bara innehåller datum, eller att en annan kolumn bara innehåller siffror. Du kan till och med se till att en kolumn märkt DATUM endast innehåller datum inom ett visst intervall. Med datavalidering kan du styra vad som skrivs in i celler i kalkylbladet. Aspose.Cells stöder fullt ut Microsoft Excels datavalidering och autofilterfunktioner. Den här artikeln förklarar hur du använder funktionerna i Microsoft Excel och hur du kodar dem med Aspose.Cells.

{{% /alert %}} 
## **Datavalideringstyper och exekvering**
Microsoft Excel stöder ett antal olika typer av datavalidering. Varje typ används för att styra vilken typ av data som matas in i en cell eller cellintervall. Nedan illustrerar kodavsnitt hur man validerar det:

- [Siffror är hela](/cells/sv/java/data-validation/), det vill säga att de inte har en decimaldel.
- [Decimaltal följer rätt struktur](/cells/sv/java/data-validation/)Kodexemplet definierar att ett cellområde ska ha två decimaler.
- [Värden är begränsade till en lista med värden](/cells/sv/java/data-validation/). Listvalidering definierar en separat lista med värden som kan tillämpas på en cell eller cellintervall.
- [Datum faller inom ett specifikt intervall](/cells/sv/java/data-validation/).
- [Tiden ligger inom ett visst intervall](/cells/sv/java/data-validation/).
- [En text är inom en given teckenlängd](/cells/sv/java/data-validation/).
### **Datavalidering med Microsoft Excel**
Så här skapar du valideringar med Microsoft Excel:

1. I ett kalkylblad väljer du de celler som du vill tillämpa validering på.
1. Från**Data**menyn, välj**Godkännande**.
 Valideringsdialogrutan visas.
1. Klicka på**inställningar**fliken och ange inställningar som visas nedan.

   **Inställningar för datavalidering** 

![todo:image_alt_text](data-validation_1.png)
### **Datavalidering med Aspose.Cells**
Datavalidering är en kraftfull funktion för att validera informationen som skrivs in i kalkylblad. Med datavalidering kan utvecklare ge användarna en lista med valmöjligheter, begränsa datainmatningar till en specifik typ eller storlek, etc.
 I Aspose.Cells, vardera[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klass har en[Valideringar](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)objekt som representerar en samling av[Godkännande](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)objekt. För att ställa in validering, ställ in några av[Godkännande](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)klass egenskaper:

- [Typ](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): representerar valideringstypen, som kan specificeras genom att använda ett av de fördefinierade värdena i[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)uppräkning.
- [Operatör](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): representerar den operator som ska användas i valideringen, som kan specificeras genom att använda ett av de fördefinierade värdena i[Operatörstyp](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)uppräkning.
- [Formel 1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): representerar värdet eller uttrycket som är associerat med den första delen av datavalideringen.
- [Formel 2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): representerar värdet eller uttrycket som är associerat med den andra delen av datavalideringen.

När[Godkännande](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)objektets egenskaper har konfigurerats kan utvecklare använda[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)struktur för att lagra information om cellintervallet som kommer att valideras med den skapade valideringen.
#### **Typer av datavalidering**
Datavalidering låter dig bygga in affärsregler i varje cell så att felaktiga inmatningar resulterar i felmeddelanden. Affärsregler är de policyer och procedurer som styr hur ett företag fungerar. Aspose.Cells stöder alla viktiga typer av datavalidering.

De[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)uppräkning har följande medlemmar:

|**Medlemsnamn**|**Beskrivning**|
|:- |:- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Betecknar ett värde av vilken typ som helst.|
|[HELTAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Betecknar valideringstyp för heltal.|
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Betecknar valideringstyp för decimaltal.|
|[LISTA](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Betecknar valideringstyp för rullgardinsmenyn.|
|[DATUM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Betecknar valideringstyp för datum.|
|[TID](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Betecknar valideringstyp för Tid.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Betecknar valideringstyp för textens längd.|
|[BESTÄLLNINGS](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Anger anpassad valideringstyp.|
#### **Programmeringsexempel: Helnummerdatavalidering**
Med denna typ av validering kan användare endast ange heltal inom ett specificerat intervall i de validerade cellerna. Kodexemplen som följer visar hur man implementerar[HELTAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)valideringstyp. Exemplet skapar samma datavalidering med Aspose.Cells som vi skapade med Microsoft Excel ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Programmeringsexempel: Decimaldatavalidering**
Med denna typ av validering kan användaren ange decimaltal i de validerade cellerna. I exemplet är användaren begränsad till att endast ange decimalvärden och valideringsområdet är A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Programmeringsexempel: Listdatavalidering**
Denna typ av validering tillåter användaren att ange värden från en rullgardinslista. Det ger en lista: en serie rader som innehåller data. Användare kan bara välja värden från listan. Valideringsområdet är cellområdet A1:A5 i det första kalkylbladet.

Det är viktigt här att du ställer in[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) egendom till**Sann**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Programmeringsexempel: Validering av datumdata**
Med denna typ av validering anger användare datumvärden inom ett specificerat intervall, eller uppfyller specifika kriterier, i de validerade cellerna. I exemplet är användaren begränsad till att ange datum mellan 1970 och 1999. Här är valideringsområdet B1-cellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Programmeringsexempel: Tidsdatavalidering**
Med denna typ av validering kan användare ange tider inom ett specificerat intervall, eller uppfylla vissa kriterier, i de validerade cellerna. I exemplet är användaren begränsad att ange tider mellan 09:00 och 11:30. Här är valideringsområdet B1-cellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Programmeringsexempel: Textlängdsdatavalidering**
Med denna typ av validering kan användare ange textvärden av en angiven längd i de validerade cellerna. I exemplet är användaren begränsad till att ange strängvärden med högst 5 tecken. Valideringsområdet är B1-cellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Regler för datavalidering**
 När datavalideringar implementeras kan valideringen kontrolleras genom att tilldela olika värden i cellerna.[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) kan användas för att hämta valideringsresultatet. Följande exempel visar denna funktion med olika värden. Exempelfilen kan laddas ner från följande länk för testning:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Kontrollera om validering i en cell är rullgardinsmeny**
 Som vi har sett finns det många typer av valideringar som kan implementeras inom en cell. Om du vill kontrollera om validering är rullgardinsmeny eller inte,[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) egenskap kan användas för att testa detta. Följande exempelkod visar användningen av den här egenskapen. Exempelfilen för testning kan laddas ner från följande länk:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Lägg till CellArea till befintlig validering**
Det kan finnas fall där du kanske vill lägga till[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)att existera[Godkännande](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). När du lägger till[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)använder sig av[Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells kontrollerar alla befintliga områden för att se om det nya området redan finns. Om filen har ett stort antal valideringar tar detta en prestandaträff. För att övervinna detta tillhandahåller API:n[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) metod. De*check Intersection*parametern anger om skärningspunkten mellan ett givet område och befintliga valideringsområden ska kontrolleras. Ställer in den på**falsk**kommer att inaktivera kontrollen av andra områden. De*checkEdge*parametern indikerar om de applicerade områdena ska kontrolleras. Om det nya området blir det övre vänstra området byggs interna inställningar om. Om du är säker på att det nya området inte är det övre vänstra området kan du ställa in denna parameter som**falsk**.

Följande kodavsnitt visar användningen av[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) metod för att lägga till ny[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)att existera[Godkännande](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Käll- och utdata Excel-filerna bifogas som referens.

[Källfilen](PivotTableHideAndSortSample.xlsx)

[Utdatafil](ValidationsSample_out.xlsx)


## **Förhandsämnen**
- [Få Cell Validering i ODS-filer](/cells/sv/java/get-cell-validation-in-ods-files/)
- [Få validering tillämpad på en Cell](/cells/sv/java/get-validation-applied-on-a-cell/)
- [Verifiera att Cell-värdet uppfyller reglerna för datavalidering](/cells/sv/java/verify-that-cell-value-satisfies-data-validation-rules/)
