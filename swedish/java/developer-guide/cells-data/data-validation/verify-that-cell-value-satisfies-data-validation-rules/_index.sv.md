---
title: Verifiera att Cell-värdet uppfyller reglerna för datavalidering
type: docs
weight: 90
url: /sv/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel tillåter användare att lägga till datavalideringsregler i kalkylbladsceller. Till exempel kan en decimalvalidering tillämpas för att begränsa siffrorna mellan 10 och 20. Om något annat nummer utanför det angivna intervallet anges, visar Microsoft Excel ett felmeddelande och uppmanar användaren att ange ett nummer från rätt intervall igen. Om användaren kopierar klistrar in ett nummer, säg 3, i cellen, kör Excel inte valideringskontrollen eller visar ett felmeddelande.

{{% /alert %}}

## Verifiera att Cell-värdet uppfyller reglerna för datavalidering

Ibland är det nödvändigt att dynamiskt verifiera om ett givet värde uppfyller de datavalideringsregler som tillämpas på cellen. För detta ändamål tillhandahåller API:erna Aspose.Cells[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) metod. Om värdet i en cell inte uppfyller datavalideringsregeln som tillämpas på den cellen, returneras det**Falsk** , annat**Sann**.

Följande exempel Microsoft Excel-fil används med exempelkoden nedan för att testa[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) metod. Som du kan se i ögonblicksbilden att cellerna**C1** har**decimaldatavalidering** tillämpas och accepterar endast värden**mellan 10 och 20** . När cellens värde är mellan 10 och 20,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) kommer att returnera**Sann** , annars kommer den tillbaka**Falsk**.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

 Följande exempelkod illustrerar hur[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) metod fungerar. Först anger den värdet 3 i C1. Eftersom detta inte uppfyller regeln för datavalidering,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) metod returnerar**Falsk** . Sedan anger den värdet 15 i C1. Eftersom detta värde uppfyller datavalideringsregeln,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) metod returnerar**Sann** . På samma sätt återkommer den**Falsk** för värde 30.

## Java-kod för att verifiera om ett Cell-värde uppfyller reglerna för datavalidering

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Konsolutdata genererad av exempelkoden

Här är konsolutgången som genereras när exempelkoden exekveras med exemplet på Excel-filen som visas ovan.

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
