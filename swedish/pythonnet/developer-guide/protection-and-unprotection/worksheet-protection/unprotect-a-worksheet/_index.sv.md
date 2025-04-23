---
title: Avskydda ett kalkylark
type: docs
weight: 20
url: /sv/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Om en utvecklare behöver ta bort skydd från ett skyddat arbetsblad under körning så att vissa ändringar kan göras i filen? Detta kan enkelt göras med Aspose.Cells för Python via .NET.

{{% /alert %}}

## **Avskydda ett kalkylblad**

### **Använda Microsoft Excel**

För att ta bort skydd från ett arbetsblad:

Från menyn **Verktyg**, välj **Skydd** följt av **Avskydda blad**. Skyddet kommer att tas bort om inte kalkylarket är lösenordsskyddat. I så fall uppmanas en dialogruta om lösenord. Ange lösenordet och kalkylarket kommer att avskyddas då.

### **Avsäkrings av ett enkelt skyddat arbetsblad med Aspose.Cells för Python via .NET**

Ett kalkylark kan avskyddas genom att anropa [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassens [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) metod.
Ett enkelt skyddat kalkylark är ett som inte är skyddat med ett lösenord. Sådana kalkylblad kan avskyddas genom att anropa [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) metoden utan att passera en parameter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Avsäkrings av ett lösenordsskyddat arbetsblad med Aspose.Cells för Python via .NET**

Ett lösenordsskyddat kalkylark är ett som är skyddat med ett lösenord. Sådana kalkylblad kan avskyddas genom att anropa en överlagrad version av [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/) metoden som tar lösenordet som en parameter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

