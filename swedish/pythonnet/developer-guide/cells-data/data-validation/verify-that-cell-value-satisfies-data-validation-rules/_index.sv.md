---
title: Bekräfta att cellvärdet uppfyller datavalideringsreglerna
type: docs
weight: 210
url: /sv/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: Lär dig hur du bekräftar att cellvärdet uppfyller datavalideringsreglerna genom Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Python Få cellvalideringsvärde, Python Hämta cellvalideringsvärde, Python Bekräfta om ett värde uppfyller datavalideringsreglerna som har tillämpats på en cell.
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att lägga till datavalideringsregler på celler. Till exempel anger en decimalvalidering att endast nummer mellan 10 och 20 kan matas in. Om en användare matar in ett annat nummer visar Microsoft Excel ett felmeddelande och uppmanar dem att ange ett nummer i rätt intervall. Om du kopierar och klistrar in ett nummer, säg 3, i cellen, kör inte Excel en valideringskontroll eller visar ett felmeddelande.

Ibland är det nödvändigt att kontrollera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen programmatiskt. I fallet ovan bör till exempel inmatningen misslyckas.

{{% /alert %}} 
## **Introduktion**
Aspose.Cells for Python via .NET tillhandahåller [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) metoden för att validera cellvärden programmatiskt. Om värdet i en cell inte uppfyller datavalideringsregeln som tillämpats på den cellen, returnerar den **False**, annars **True**.

Följande exempelkod illustrerar hur [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) metoden fungerar. Först matar den in värdet 3 i C1. Eftersom detta inte uppfyller datavalideringsregeln, returnerar [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) metoden **False**. Sedan matas värdet 15 in i C1. Eftersom detta värde uppfyller datavalideringsregeln, returnerar [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) metoden **True**. På samma sätt returnerar den **False** för värdet 30.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **Output**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
