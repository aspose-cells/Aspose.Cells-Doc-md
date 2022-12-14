---
title: Datavalidering
type: docs
weight: 90
url: /sv/net/data-validation/
---
{{% alert color="primary" %}}

Microsoft Excel tillhandahåller några bra funktioner för att automatiskt filtrera eller validera kalkylbladsdata.Aspose.Cells stöder fullt ut Microsoft Excels datavalidering och AutoFilter-funktioner. Den här artikeln förklarar hur du använder funktionerna i Microsoft Excel och hur du kodar dem med Aspose.Cells.

{{% /alert %}}

## **Datavalideringstyper och exekvering**

Datavalidering är möjligheten att sätta regler för data som skrivs in på ett kalkylblad. Använd till exempel validering för att säkerställa att en kolumn märkt DATUM bara innehåller datum, eller att en annan kolumn bara innehåller siffror. Du kan till och med se till att en kolumn märkt DATUM endast innehåller datum inom ett visst intervall. Med datavalidering kan du styra vad som skrivs in i celler i kalkylbladet.

Microsoft Excel stöder ett antal olika typer av datavalidering. Varje typ används för att styra vilken typ av data som matas in i en cell eller cellintervall. Nedan illustrerar kodavsnitt hur man validerar det:

- Tal är hela, det vill säga att de inte har en decimaldel.
- Decimaltal följer rätt struktur. Kodexemplet definierar att ett cellområde ska ha två decimaler.
- Värden är begränsade till en lista med värden. Listvalidering definierar en separat lista med värden som kan tillämpas på en cell eller cellintervall.
- Datum faller inom ett specifikt intervall.
- En tid ligger inom ett specifikt intervall.
- En text är inom en given teckenlängd.

### **Datavalidering med Microsoft Excel**

Så här skapar du valideringar med Microsoft Excel:

1. I ett kalkylblad väljer du de celler som du vill tillämpa validering på.
1.  Från**Data** menyn, välj**Godkännande**. Valideringsdialogrutan kommer att visas.
1.  Klicka på**inställningar** fliken och ange inställningar.

### **Datavalidering med Aspose.Cells**

Datavalidering är en kraftfull funktion för att validera informationen som skrivs in i kalkylblad. Med datavalidering kan utvecklare ge användarna en lista med valmöjligheter, begränsa datainmatningar till en specifik typ eller storlek, etc.
 I Aspose.Cells, vardera[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass har en[**Valideringar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)egendom som representerar en samling av[**Godkännande**](https://reference.aspose.com/cells/net/aspose.cells/validation) objekt. För att ställa in validering, ställ in några av[**Godkännande**](https://reference.aspose.com/cells/net/aspose.cells/validation)klassegenskaper enligt följande:

- Typ – representerar valideringstypen, som kan specificeras genom att använda ett av de fördefinierade värdena i[**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)uppräkning.
-  Operatör – representerar den operatör som ska användas i valideringen, som kan specificeras genom att använda ett av de fördefinierade värdena i[**Operatörstyp**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)uppräkning.
- Formel1 – representerar värdet eller uttrycket som är associerat med den första delen av datavalideringen.
- Formel2 – representerar värdet eller uttrycket som är associerat med den andra delen av datavalideringen.

 När[**Godkännande**](https://reference.aspose.com/cells/net/aspose.cells/validation) objektets egenskaper har konfigurerats kan utvecklare använda[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)struktur för att lagra information om cellintervallet som kommer att valideras med den skapade valideringen.

#### **Typer av datavalidering**

 De[**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)uppräkning har följande medlemmar:

|**Medlemsnamn**|**Beskrivning**|
|:- |:- |
|Valfritt värde|Betecknar ett värde av vilken typ som helst.|
|Heltal|Betecknar valideringstyp för heltal.|
|Decimal|Betecknar valideringstyp för decimaltal.|
|Lista|Betecknar valideringstyp för rullgardinsmenyn.|
|Datum|Betecknar valideringstyp för datum.|
|Tid|Betecknar valideringstyp för tid.|
|TextLängd|Betecknar valideringstyp för textens längd.|
|Beställnings|Anger anpassad valideringstyp.|

##### **Helnummerdatavalidering**

Med denna typ av validering kan användare endast ange heltal inom ett specificerat intervall i de validerade cellerna. Kodexemplen som följer visar hur man implementerar WholeNumber-valideringstypen. Exemplet skapar samma datavalidering med Aspose.Cells som vi skapade med Microsoft Excel ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **Listdatavalidering**

Denna typ av validering tillåter användaren att ange värden från en rullgardinslista. Det ger en lista: en serie rader som innehåller data. I exemplet läggs ett andra kalkylblad till som innehåller listkällan. Användare kan bara välja värden från listan. Valideringsområdet är cellområdet A1:A5 i det första kalkylbladet.

 Det är viktigt här att du ställer in[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) egendom till**Sann**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **Datum Validering av data**

Med denna typ av validering anger användare datumvärden inom ett specificerat intervall, eller uppfyller specifika kriterier, i de validerade cellerna. I exemplet är användaren begränsad till att ange datum mellan 1970 och 1999. Här är valideringsområdet B1-cellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **Tidsdatavalidering**

Med denna typ av validering kan användare ange tider inom ett specificerat intervall, eller uppfylla vissa kriterier, i de validerade cellerna. I exemplet är användaren begränsad att ange tider mellan 09:00 och 11:30. Här är valideringsområdet B1-cellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **Textlängd Datavalidering**

Med denna typ av validering kan användare ange textvärden av en angiven längd i de validerade cellerna. I exemplet är användaren begränsad till att ange strängvärden med högst 5 tecken. Valideringsområdet är B1-cellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **Regler för datavalidering**

 När datavalideringar implementeras kan valideringen kontrolleras genom att tilldela olika värden i cellerna.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) kan användas för att hämta valideringsresultatet. Följande exempel visar denna funktion med olika värden. Exempelfilen kan laddas ner från följande länk för testning:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **Kontrollera om validering i cellen är rullgardinsmenyn**

 Som vi har sett finns det många typer av valideringar som kan implementeras inom en cell. Om du vill kontrollera om validering är rullgardinsmeny eller inte,[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) egenskap kan användas för att testa detta. Följande exempelkod visar användningen av den här egenskapen. En provfil för testning kan laddas ner från följande länk:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **Lägg till CellArea till befintlig validering**

 Det kan finnas fall där du kanske vill lägga till[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)att existera[**Godkännande**](https://reference.aspose.com/cells/net/aspose.cells/validation). När du lägger till[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) använder sig av[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells kontrollerar alla befintliga områden för att se om det nya området redan finns. Om filen har ett stort antal valideringar tar detta en prestandaträff. För att övervinna detta tillhandahåller API:n[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) metod. De*check Intersection* parametern anger om skärningspunkten mellan ett givet område och befintliga valideringsområden ska kontrolleras. Ställer in den på**falsk** kommer att inaktivera kontrollen av andra områden. De*checkEdge* parametern indikerar om de applicerade områdena ska kontrolleras. Om det nya området blir det övre vänstra området byggs interna inställningar om. Om du är säker på att det nya området inte är det övre vänstra området kan du ställa in denna parameter som**falsk**.

Följande kodavsnitt visar användningen av[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) metod för att lägga till nytt[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)att existera[**Godkännande**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Käll- och utdata Excel-filerna bifogas som referens.

[Källfilen](96928093.xlsx)

[Utdatafil](96928220.xlsx)


## **Förhandsämnen**
- [Få Cell Validering i ODS-filer](/cells/sv/net/get-cell-validation-in-ods-files/)
- [Få validering tillämpad på en Cell](/cells/sv/net/get-validation-applied-on-a-cell/)
- [Verifiera att Cell-värdet uppfyller reglerna för datavalidering](/cells/sv/net/verify-that-cell-value-satisfies-data-validation-rules/)
