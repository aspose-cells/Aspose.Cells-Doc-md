---
title: Verifiera lösenord som används för att skydda arbetsbladet
type: docs
weight: 370
url: /sv/net/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells API:er har förbättrat[**Skydd**](https://reference.aspose.com/cells/net/aspose.cells/protection) klass genom att introducera några användbara egenskaper och metoder. En sådan metod är[**Verifiera lösenord**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) som gör det möjligt att ange ett lösenord som en instans av*sträng* och verifierar om samma lösenord har använts för att skydda[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

 De[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) metod returnerar**Sann**om det angivna lösenordet matchar lösenordet som används för att skydda det givna kalkylbladet och**falsk** om det angivna lösenordet inte matchar. Följande kodbit använder[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) metod i samband med[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)egenskap för att upptäcka lösenordsskyddet och verifiera lösenordet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
