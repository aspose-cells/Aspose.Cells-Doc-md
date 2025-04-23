---
title: Verifiera lösenordet för krypterade filer
type: docs
weight: 10
url: /sv/java/verify-password-of-encrypted-excel-and-ods-files/
description: Verifiera lösenord för krypterade Excel (xlsx, xlsb, xls, xlsm) och OpenOffice (ODS) filer med Java koder.
---

{{% alert color="primary" %}}
Om Excel (xlsx, xlsb, xls, xlsm) och OpenOffice (ODS)-filer är låsta med lösenord, stödjer Aspose.Cells for Java enkel verifiering av lösenord utan att analysera specifika data i filerna.
{{% /alert %}}

## **Verifiera lösenordet för den krypterade filen**

För att verifiera lösenordet för den krypterade filen tillhandahåller Aspose.Cells for Java metoden [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-). Metoden accepterar två parametrar, filström och lösenordet som ska verifieras.
Följande kodavsnitt demonstrerar användningen av metod [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) för att verifiera om det angivna lösenordet är giltigt eller inte.

### **Exempelkod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

{{< app/cells/assistant language="java" >}}
