---
title: Verifiera lösenord som används för att skydda arbetsbladet
type: docs
weight: 290
url: /sv/java/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells API:er har förbättrat[**Skydd**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) klass genom att introducera några användbara egenskaper och metoder. En sådan metod är[**verifiera lösenord**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)som gör det möjligt att ange ett lösenord som en instans av String och verifierar om samma lösenord har använts för att skydda arbetsbladet.

{{% /alert %}}

## **Verifiera lösenord som används för att skydda arbetsbladet**

 De[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) metod returnerar**Sann** om det angivna lösenordet matchar lösenordet som används för att skydda det givna kalkylbladet,**falsk** om det angivna lösenordet inte matchar. Följande kodbit använder[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) metod i samband med[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)egenskap för att upptäcka lösenordsskyddet och verifiera lösenordet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
