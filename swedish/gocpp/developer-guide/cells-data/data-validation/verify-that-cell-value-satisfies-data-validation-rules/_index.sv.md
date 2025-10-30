---
title: verifiera att cellvärdet uppfyller datavalideringsregler med Golang via C++
linktitle: Bekräfta att cellvärdet uppfyller datavalideringsreglerna
type: docs
weight: 210
url: /sv/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Lär dig hur du verifierar att cellens värde uppfyller datavalideringsregler via API et Aspose.Cells for C++.
keywords: Få Cell Valideringsvärde, Hämta Cell Valideringsvärde, Verifiera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att lägga till datavalideringsregler på celler. Till exempel specificerar en decimaltalsvalidering att endast nummer mellan 10 och 20 kan matas in. Om en användare matar in ett annat nummer visar Excel ett felmeddelande och frågar användaren att ange ett nummer inom rätt intervall. Om du kopierar och klistrar in ett nummer, säg 3, i cellen, kör inte Excel någon valideringskontroll eller visar något felmeddelande.

Ibland är det nödvändigt att kontrollera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen programmatiskt. I fallet ovan bör till exempel inmatningen misslyckas.

{{% /alert %}} 

## **Introduktion**
Aspose.Cells tillhandahåller metoden [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) för att validera cellvärden programmatiskt. Om värdet i en cell inte uppfyller datavalideringsregeln som tillämpats på den cellen returnerar den **False**, annars **True**.

Följande kodexempel illustrerar hur metoden [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) fungerar. Först anges värdet 3 i C1. Eftersom detta inte uppfyller datavalideringsregeln returnerar den [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) **False**. Sedan anges värdet 15 i C1. Eftersom detta värde uppfyller datavalideringsregeln returnerar den [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) **True**. På samma sätt returnerar den **False** för värdet 30.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **Output**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
