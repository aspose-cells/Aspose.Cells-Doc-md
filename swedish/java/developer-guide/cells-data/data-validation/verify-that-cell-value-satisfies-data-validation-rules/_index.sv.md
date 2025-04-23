---
title: Bekräfta att cellvärdet uppfyller datavalideringsreglerna
type: docs
weight: 90
url: /sv/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att lägga till datavalideringsregler till arbetsbladsceller. Till exempel kan en decimalvalidering tillämpas för att begränsa siffror mellan 10 och 20. Om något annat nummer utanför detta angivna intervall skrivs in, visar Microsoft Excel ett felmeddelande och uppmanar användaren att ange om ett nummer från den korrekta intervallet. Om användaren kopierar och klistrar in ett nummer, säg 3, i cellen, kör inte Excel valideringskontrollen eller visar ett felmeddelande.

{{% /alert %}}

## Verifiera att cellvärdet uppfyller datavalideringsregler

Ibland är det nödvändigt att dynamiskt verifiera om ett angivet värde uppfyller de datavalideringsregler som tillämpats på cellen. För detta ändamål tillhandahåller Aspose.Cells API:erna [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) metoden. Om värdet i en cell inte uppfyller de datavalideringsregler som tillämpats på den cellen, returnerar den **Falskt**, annars **Sant**.

Den följande prov Microsoft Excel-filen används med den provkoden nedan för att testa [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) metoden. Som du kan se i ögonblicksbilden har cellerna **C1** **decimal datavalidering** tillämpad och kommer endast att acceptera värden **mellan 10 och 20**. När värdet på cellen är mellan 10 och 20, kommer [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) metoden att returnera **Sant**, annars kommer den att returnera **Falskt**.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

Den följande provkoden illustrerar hur [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) metoden fungerar. Först matar den in värdet 3 i C1. Därför att detta inte uppfyller datavalideringsregeln, returnerar [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) metoden **Falskt**. Sedan matar den in värdet 15 i C1. Eftersom detta värde uppfyller datavalideringsregeln, returnerar [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) metoden **Sant**. På samma sätt returnerar den **Falskt** för värdet 30.

## Java-kod för att verifiera om ett cellvärde uppfyller datavalideringsregler

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Konsolutdata som genereras av exempelkoden

Här är konsoloutputen som genereras när provkoden körs med den prov Excel-filen som visas ovan.

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
