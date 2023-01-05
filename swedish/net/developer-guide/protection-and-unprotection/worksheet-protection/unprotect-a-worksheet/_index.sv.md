---
title: Ta bort skyddet av ett arbetsblad
type: docs
weight: 20
url: /sv/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

Om en utvecklare behöver ta bort skyddet från ett skyddat kalkylblad vid körning så att vissa ändringar kan göras i filen? Detta kan enkelt göras med Aspose.Cells.

{{% /alert %}}

## **Ta bort skyddet av ett arbetsblad**

### **Använder Microsoft Excel**

Så här tar du bort skyddet från ett kalkylblad:

 Från**Verktyg** menyn, välj**Skydd** följd av**Avskydda arket**. Skyddet kommer att tas bort om inte kalkylbladet är lösenordsskyddat. I det här fallet uppmanas en dialogruta att ange lösenordet. Ange lösenordet och kalkylbladet kommer då att vara oskyddat.

### **Ta bort skyddet av ett enkelt skyddat arbetsblad med Aspose.Cells**

 Ett kalkylblad kan oskyddas genom att anropa[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**Avskydda**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)metod.
 Ett enkelt skyddat kalkylblad är ett som inte är skyddat med ett lösenord. Sådana kalkylblad kan oskyddas genom att anropa[**Avskydda**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)metod utan att skicka en parameter.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Ta bort skyddet av ett lösenordsskyddat arbetsblad med Aspose.Cells**

Ett lösenordsskyddat kalkylblad är ett som är skyddat med ett lösenord. Sådana kalkylblad kan oskyddas genom att anropa en överbelastad version av[**Avskydda**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)metod som tar lösenordet som en parameter.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
