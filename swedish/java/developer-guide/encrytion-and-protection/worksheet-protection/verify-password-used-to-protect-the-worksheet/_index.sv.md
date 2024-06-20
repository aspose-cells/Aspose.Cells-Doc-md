---
title: Verifiera lösenord som används för att skydda arbetsbladet
type: docs
weight: 290
url: /sv/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells APIs har förbättrat [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection)-klassen genom att introducera några användbara egenskaper och metoder. En sådan metod är [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) som tillåter att specificera ett lösenord som en instans av String och verifierar om samma lösenord har använts för att skydda arbetsbladet.

{{% /alert %}}

## **Verifiera lösenord som används för att skydda arbetsbladet**

Metoden [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) returnerar **true** om det angivna lösenordet matchar med lösenordet som användes för att skydda det angivna arbetsbladet, **false** om det angivna lösenordet inte matchar. Följande kod använder metoden [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) i samband med egenskapen [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) för att upptäcka lösenordsskyddet och verifiera lösenordet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
