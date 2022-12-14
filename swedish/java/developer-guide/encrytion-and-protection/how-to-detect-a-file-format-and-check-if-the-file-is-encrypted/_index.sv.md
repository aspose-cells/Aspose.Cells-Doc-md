---
title: Hur man upptäcker ett filformat och kontrollerar om filen är krypterad
type: docs
weight: 2000
url: /sv/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Ibland behöver du upptäcka en fils format innan du öppnar den eftersom filtillägget inte garanterar att filinnehållet är lämpligt. Filen kan vara krypterad (en lösenordsskyddad fil) så att den inte kan läsas direkt, eller så ska vi inte läsa den. Aspose.Cells tillhandahåller[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)) statisk metod och några relevanta API:er som du kan använda för att bearbeta dokument.

{{% /alert %}}

## **Java-kod för att identifiera filformat och kontrollera om filen är krypterad**

Följande exempelkod illustrerar hur man upptäcker ett filformat (med sökvägen) och kontrollerar dess tillägg. Du kan också avgöra om filen är krypterad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
