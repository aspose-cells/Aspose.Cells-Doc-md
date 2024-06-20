---
title: Avskydda ett kalkylark
type: docs
weight: 20
url: /sv/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Om en utvecklare behöver ta bort skydd från ett skyddat kalkylark vid körning så att vissa ändringar kan göras i filen? Detta kan enkelt göras med Aspose.Cells.

{{% /alert %}}

## **Avskydda ett kalkylblad**

### **Använda Microsoft Excel**

För att ta bort skydd från ett arbetsblad:

Från menyn **Verktyg**, välj **Skydd** följt av **Avskydda blad**. Skyddet kommer att tas bort om inte kalkylarket är lösenordsskyddat. I så fall uppmanas en dialogruta om lösenord. Ange lösenordet och kalkylarket kommer att avskyddas då.

### **Avskydda ett enkelt skyddat kalkylark med hjälp av Aspose.Cells**

Ett kalkylark kan avskyddas genom att anropa [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassens [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) metod.
Ett enkelt skyddat kalkylark är ett som inte är skyddat med ett lösenord. Sådana kalkylblad kan avskyddas genom att anropa [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) metoden utan att passera en parameter.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Avskydda ett lösenordsskyddat kalkylark med hjälp av Aspose.Cells**

Ett lösenordsskyddat kalkylark är ett som är skyddat med ett lösenord. Sådana kalkylblad kan avskyddas genom att anropa en överlagrad version av [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) metoden som tar lösenordet som en parameter.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
