---
title: Bekräfta att cellvärdet uppfyller datavalideringsreglerna
type: docs
weight: 210
url: /sv/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Lär dig hur du verifierar att cellvärdet uppfyller datavalideringsregler med API Aspose.Cells for Node.js via C++.
keywords: Hämta cellvalideringsvärde Node.js via C++, Hämta cellvalideringsvärde Node.js via C++, Verifiera om ett värde uppfyller datavalideringsreglerna som tillämpats på cellen Node.js via C++
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att lägga till datavalideringsregler på celler. Till exempel specificerar en decimaltalsvalidering att endast nummer mellan 10 och 20 kan matas in. Om en användare matar in ett annat nummer visar Excel ett felmeddelande och frågar användaren att ange ett nummer inom rätt intervall. Om du kopierar och klistrar in ett nummer, säg 3, i cellen, kör inte Excel någon valideringskontroll eller visar något felmeddelande.

Ibland är det nödvändigt att kontrollera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen programmatiskt. I fallet ovan bör till exempel inmatningen misslyckas.

{{% /alert %}} 
## **Introduktion**
Aspose.Cells for Node.js via C++ tillhandahåller metoden [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) för att validera cellvärden programmatiskt. Om värdet i en cell inte uppfyller datavalideringsregeln för den cellen, returneras **false**, annars **true**.

Följande exempel illustrerar hur metoden [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) fungerar. Först matar den in värdet 3 i C1. Eftersom detta inte uppfyller datavalideringsregeln, returnerar metoden **false**. Sedan matar den in värdet 15 i C1. Eftersom detta värde uppfyller datavalideringsregeln, returnerar metoden **true**. På samma sätt returnerar den **false** för värdet 30.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **Output**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
