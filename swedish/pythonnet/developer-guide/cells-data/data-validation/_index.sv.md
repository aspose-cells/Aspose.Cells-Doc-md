---
title: Datavalidering
type: docs
weight: 90
url: /sv/python-net/data-validation/
description: Lär dig hur du lägger till datavalidering genom Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Lägg till datavalidering med Python, Hämta valideringsvärde med Python, Lägg till datavalidering för heltal med Python, Lägg till datavalidering för lista med Python, Lägg till datavalidering för datum med Python, Lägg till datavalidering för tid med Python, Lägg till datavalidering för textlängd med Python, Lägg till CellArea till befintlig validering med Python, Kontrollera om validering i cellen är en rullgardinsmeny, Lägg till anpassad validering  
---

{{% alert color="primary" %}}

Microsoft Excel erbjuder några bra funktioner för att filtrera automatiskt eller validera kalkylbladsdata. Aspose.Cells för Python via .NET stöder fullt ut Microsoft Excels datavalidering och AutoFilter-funktioner. Den här artikeln förklarar hur man använder funktionerna i Microsoft Excel och hur man kodar dem med hjälp av Aspose.Cells för Python via .NET.

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

### **Datavalidering med Aspose.Cells för Python Excel-biblioteket**

Datavalidering är en kraftfull funktion för att validera information som matas in i kalkylblad. Med datavalidering kan utvecklare tillhandahålla användare med en lista över val, begränsa datamatare till en specifik typ eller storlek, osv.
I Aspose.Cells för Python via .NET har varje [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klass en [**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/) egenskap som representerar en samling av [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) objekt. För att ställa in validering, ställ in några av [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) klassens egenskaper enligt följande:

- typ - representerar valideringstypen, som kan specificeras genom att använda ett av de fördefinierade värdena i [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) -uppräkningen.
- Operator - representerar operatören som ska användas i valideringen, vilket kan specificeras genom att använda en av de fördefinierade värdena i [**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype) uppräkningen.
- formel1 - representerar värdet eller uttrycket som är associerat med den första delen av datavalideringen.
- formel2 - representerar värdet eller uttrycket associerat med den andra delen av datavalideringen.

När [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) objektets egenskaper har konfigurerats, kan utvecklare använda [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) strukturen för att lagra information om cellområdet som kommer att valideras med den skapade valideringen.

#### **Typer av Datavalidering**

[**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) uppräkning har följande medlemmar:

| **Medlemsnamn** | **Beskrivning** |
| :- | :- |
|ANY_VALUE|Betecknar ett värde av vilken typ som helst.|
|WHOLE_NUMBER|Betecknar valideringstypen för heltal.|
|DECIMAL|Betecknar valideringstypen för decimaltal.|
|LIST|Betecknar valideringstypen för rullgardinsmeny.|
|DATE|Betecknar valideringstypen för datum.|
|TIME|Betecknar valideringstypen för tid.|
|TEXT_LENGTH|Betecknar valideringstypen för textlängd.|
|CUSTOM|Betecknar anpassad valideringstyp.|

##### **Heltalsdatavalidering**

Med den här typen av validering kan användare endast ange heltal inom ett specificerat intervall i de validerade cellerna. Kodexemplen som följer visar hur man implementerar valideringstypen Heltal. Exemplet skapar samma datavalidering med Aspose.Cells för Python via .NET som vi skapade med Microsoft Excel ovan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **Listvalidering**

Denna typ av validering tillåter användaren att mata in värden från en nedrullningslista. Det tillhandahåller en lista: en serie rader som innehåller data. I exemplet läggs ett andra kalkylblad till för att hålla listkällan. Användare kan endast välja värden från listan. Valideringsområdet är cellområdet A1:A5 i det första kalkylbladet.

Det är viktigt här att du ställer in [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) egenskapen till **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **Datumdata validering**

Med denna typ av validering anger användare datumvärden inom ett angivet intervall eller enligt specifika kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange datum mellan 1970 och 1999. Här är valideringsområdet cell B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **Tidsdata validering**

Med denna typ av validering kan användare ange tider inom ett angivet intervall eller enligt vissa kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange tider mellan 09:00 och 11:30 förmiddag. Här är valideringsområdet cell B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **Textlängd data validering**

Med denna typ av validering kan användare ange textvärden av en angiven längd i de validerade cellerna. I exemplet är användaren begränsad att ange strängvärden med högst 5 tecken. Valideringsområdet är cell B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **Data valideringsregler**

När datavalideringar är implementerade kan valideringen kontrolleras genom att tilldela olika värden i cellerna. [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) kan användas för att hämta valideringsresultatet. Följande exempel visar denna funktion med olika värden. Testfilen kan laddas ner från följande länk för testning:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **Kontrollera om valideringen i cellen är rullgardinsmeny**

Som vi har sett finns det många typer av valideringar som kan implementeras i en cell. Om du vill kontrollera om valideringen är en rullgardinsmeny eller inte, kan [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/)-egenskapen användas för att testa detta. Följande kodexempel demonstrerar användningen av denna egenskap. En exempelfil för testning kan laddas ned från länken nedan:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **Lägg till CellArea till befintlig validering**

Det kan finnas fall där du vill lägga till [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) till befintlig [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation). När du lägger till [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) med hjälp av [**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea), kontrollerar Aspose.Cells alla befintliga områden för att se om det nya området redan finns. Om filen har många valideringar påverkar detta prestandan. För att komma runt detta tillhandahåller API:et metoden [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool). Parametern *checkIntersection* indikerar om det ska kontrolleras om det nya området korsar andra valideringsområden. Om den sätts till **false** inaktiveras kontrollen av andra områden. Parametern *checkEdge* indikerar om de tillämpade områdena ska kontrolleras. Om det nya området blir det översta vänstra området byggs interna inställningar om. Om du är säker på att det nya området inte är det översta vänstra området kan du ställa in denna parameter som **false**.

Följande kodsnutt demonstrerar användningen av [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool)-metoden för att lägga till ny [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) till befintlig [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

Käll- och utdataexcelfilerna är bilagda som referens.

[Källfil](96928093.xlsx)

[Utdatafil](96928220.xlsx)


## **Fortsatta ämnen**
- [Hämta cellvalidering i ODS-filer](/cells/sv/python-net/get-cell-validation-in-ods-files/)
- [Få validering som tillämpas på en cell](/cells/sv/python-net/get-validation-applied-on-a-cell/)
- [Verifiera att cellvärdet uppfyller datavalideringsreglerna](/cells/sv/python-net/verify-that-cell-value-satisfies-data-validation-rules/)
