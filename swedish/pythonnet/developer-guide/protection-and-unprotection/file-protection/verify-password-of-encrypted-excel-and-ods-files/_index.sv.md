---
title: Verifiera lösenordet för krypterade filer
type: docs
weight: 10
url: /sv/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: Verifiera lösenordet för krypterade Excel (xlsx, xlsb, xls, xlsm) och OpenOffice (ODS) filer med CShape koder.
---

{{% alert color="primary" %}}
Om Excel (xlsx, xlsb, xls, xlsm) och OpenOffice (ODS) filer är låsta med lösenord, stöder Aspose enkel lösenordsverifiering utan att spara specifika data från filerna.
{{% /alert %}}

## **Verifiera lösenordet för den krypterade filen**

För att verifiera lösenordet för den krypterade filen, tillhandahåller Aspose.Cells för Python via .NET metoden [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Dessa metoder accepterar två parametrar, filsströmmar och lösenordet som ska verifieras.
Följande kodavsnitt demonstrerar användningen av metod [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) för att verifiera om det angivna lösenordet är giltigt eller inte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


{{< app/cells/assistant language="python-net" >}}
