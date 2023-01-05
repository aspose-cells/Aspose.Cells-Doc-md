---
title: Avgör om licensen har laddats
type: docs
weight: 210
url: /sv/java/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)egendom som du kan använda för att avgöra om licensen har laddats eller inte. Om du anropar den här metoden innan du ställer in licensen kommer den att returnera false och om du anropar den här metoden efter att ha ställt in licensen kommer den att returnera true vilket indikerar att licensen har laddats.

{{% /alert %}}

## **Avgör om licensen har laddats**

 Följande kod ger åtkomst till[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)metod innan du ställer in en licens och den returnerar falskt. Sedan laddar den licensen och kommer åt egendomen igen som nu returnerar sant.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Konsolutgång**

Här är konsolutgången för ovanstående exempelkod

{{< highlight "java" >}}

false

true

{{< /highlight >}}
