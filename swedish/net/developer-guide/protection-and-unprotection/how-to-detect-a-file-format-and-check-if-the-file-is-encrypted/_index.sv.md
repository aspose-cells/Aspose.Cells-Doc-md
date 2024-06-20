---
title: Hur man upptäcker ett filformat och kontrollerar om filen är krypterad
type: docs
weight: 2700
url: /sv/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Ibland behöver du upptäcka en filformat innan du öppnar den eftersom filändelsen inte garanterar att filinnehållet är lämpligt. Filen kan vara krypterad (en lösenordsskyddad fil) så att den inte kan läsas direkt eller så borde vi inte läsa den. Aspose.Cells tillhandahåller den statiska metoden [**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) och några relevanta APIer som du kan använda för att bearbeta dokument.

{{% /alert %}}

Följande exempelkod illustrerar hur man upptäcker ett filformat (med hjälp av filvägen) och kontrollerar dess förlängning. Du kan också avgöra om filen är krypterad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
