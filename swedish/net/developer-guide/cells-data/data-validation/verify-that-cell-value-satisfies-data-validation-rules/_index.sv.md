---
title: Verifiera att Cell-värdet uppfyller reglerna för datavalidering
type: docs
weight: 210
url: /sv/net/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att lägga till datavalideringsregler i celler. Till exempel anger en decimalvalidering att endast siffror mellan 10 och 20 kan anges. Om en användare anger ett annat nummer. Microsoft Excel visar ett felmeddelande och uppmanar dem att ange ett nummer i rätt intervall. Om du kopierar och klistrar in ett nummer, säg 3, i cellen, kör Excel inte en valideringskontroll eller visar ett felmeddelande.

Ibland är det nödvändigt att verifiera om ett värde uppfyller datavalideringsreglerna som tillämpas på cellen programmatiskt. I fallet ovan bör till exempel posten misslyckas.

{{% /alert %}} 
## **Introduktion**
 Aspose.Cells tillhandahåller[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metod för att validera cellvärden programmatiskt. Om värdet i en cell inte uppfyller datavalideringsregeln som tillämpas på den cellen, returneras det**Falsk** , annat**Sann**.

 Följande exempelkod illustrerar hur[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metoden fungerar. Först anger den värdet 3 i C1. Eftersom detta inte uppfyller regeln för datavalidering,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metod returnerar**Falsk** . Sedan anger den värdet 15 i C1. Eftersom detta värde uppfyller datavalideringsregeln,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metod returnerar**Sann** . På samma sätt återkommer den**Falsk** för värde 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Produktion**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
