---
title: Upptäck om arbetsbladet är lösenordsskyddat
type: docs
weight: 360
url: /sv/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Det är möjligt att skydda arbetsböcker och arbetsblad separat. Till exempel kan ett kalkylblad innehålla ett eller flera arbetsblad som är lösenordsskyddade, men själva kalkylbladet kan vara skyddat eller inte. Aspose.Cells för Python via .NET APIs ger möjlighet att upptäcka om ett givet arbetsblad är lösenordsskyddat eller inte. Den här artikeln visar användningen av Aspose.Cells för Python via .NET API för att uppnå detta.

{{% /alert %}}

Aspose.Cells för Python via .NET har exponerat [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) egenskapen för att avgöra om ett arbetsblad är lösenordsskyddat eller inte. Boolean-typen [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) egenskapen returnerar **true** om [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) är lösenordsskyddat och **false** om inte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

