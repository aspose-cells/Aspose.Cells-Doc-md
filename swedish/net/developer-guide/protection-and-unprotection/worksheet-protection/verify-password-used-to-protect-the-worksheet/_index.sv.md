---
title: Verifiera lösenord som används för att skydda arbetsbladet
type: docs
weight: 370
url: /sv/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells API:er har förbättrat [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) klassen genom att införa några användbara egenskaper och metoder. En sådan metod är [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) som tillåter att ange ett lösenord som en instans av *string* och verifierar om samma lösenord har använts för att skydda [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) metoden returnerar **true** om det angivna lösenordet matchar lösenordet som användes för att skydda det angivna kalkylarket och **false** om det angivna lösenordet inte matchar. Följande kodstycke använder [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) metoden i samarbete med [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) egenskapen för att upptäcka lösenordsskyddet och verifierar lösenordet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
