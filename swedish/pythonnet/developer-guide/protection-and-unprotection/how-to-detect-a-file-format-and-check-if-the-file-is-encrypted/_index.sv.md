---
title: Hur man upptäcker ett filformat och kontrollerar om filen är krypterad
type: docs
weight: 2700
url: /sv/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Ibland måste du upptäcka filformatet innan du öppnar det eftersom filändelsen inte garanterar att filinnehållet är lämpligt. Filen kan vara krypterad (en lösenordsskyddad fil), så den kan inte läsas direkt, eller så bör den inte läsas. Aspose.Cells för Python via .NET ger den [**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format) statiska metoden och några relevanta API:er som du kan använda för att bearbeta dokument.

{{% /alert %}}

Följande exempelkod illustrerar hur man upptäcker ett filformat (med hjälp av filvägen) och kontrollerar dess förlängning. Du kan också avgöra om filen är krypterad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

{{< app/cells/assistant language="python-net" >}}
