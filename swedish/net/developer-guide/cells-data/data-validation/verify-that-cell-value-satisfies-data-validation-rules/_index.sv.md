---
title: Bekräfta att cellvärdet uppfyller datavalideringsreglerna
type: docs
weight: 210
url: /sv/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Lär dig hur man kontrollerar att cellvärdet uppfyller datavalideringsreglerna genom Aspose.Cells for .NET API..
keywords: Få Cell Valideringsvärde, Hämta Cell Valideringsvärde, Verifiera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att lägga till datavalideringsregler på celler. Till exempel anger en decimalvalidering att endast nummer mellan 10 och 20 kan matas in. Om en användare matar in ett annat nummer visar Microsoft Excel ett felmeddelande och uppmanar dem att ange ett nummer i rätt intervall. Om du kopierar och klistrar in ett nummer, säg 3, i cellen, kör inte Excel en valideringskontroll eller visar ett felmeddelande.

Ibland är det nödvändigt att kontrollera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen programmatiskt. I fallet ovan bör till exempel inmatningen misslyckas.

{{% /alert %}} 
## **Introduktion**
Aspose.Cells tillhandahåller metoden [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)  för att validera cellvärden programmatiskt. Om värdet i en cell inte uppfyller datavalideringsregeln som applicerats på den cellen returnerar den **Falskt**, annars **Sant**.

Följande exempelkod illustrerar hur metoden [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) fungerar. Först matar den in värdet 3 i C1. Eftersom detta inte uppfyller datavalideringsregeln returnerar metoden [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) **Falskt**. Sedan matar den in värdet 15 i C1. Eftersom detta värde uppfyller datavalideringsregeln returnerar metoden [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) **Sant**. På liknande sätt returnerar den **Falskt** för värdet 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Output**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
