---
title: Verifiera lösenord som används för att skydda arbetsbladet
type: docs
weight: 370
url: /sv/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET API har förbättrat [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection)-klassen genom att introducera några användbara egenskaper & metoder. En sådan metod är [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) som tillåter att specificera ett lösenord som en instans av *string* och verifierar om samma lösenord har använts för att skydda [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

{{% /alert %}}

[**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) metoden returnerar **true** om det angivna lösenordet matchar lösenordet som användes för att skydda det angivna kalkylarket och **false** om det angivna lösenordet inte matchar. Följande kodstycke använder [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) metoden i samarbete med [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) egenskapen för att upptäcka lösenordsskyddet och verifierar lösenordet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

{{< app/cells/assistant language="python-net" >}}
