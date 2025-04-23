---
title: Avgöra om licensen har laddats framgångsrikt
type: docs
weight: 210
url: /sv/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells ger [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) egenskap som du kan använda för att avgöra om licensen har laddats framgångsrikt eller inte. Om du anropar den här metoden innan du anger licensen kommer den att returnera false och om du anropar den här metoden efter att ha angett licensen kommer den att returnera true och indikera att licensen har laddats framgångsrikt.

{{% /alert %}}

## **Avgöra om licensen har laddats framgångsrikt**

I följande kod har åtkomst till [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)-metoden innan en licens anges och den returnerar false. Sedan laddar den licensen och får åtkomst till egenskapen igen som nu returnerar true.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Konsoloutput**

Här är konsoloutputen av ovanstående kodexempel

{{< highlight java >}}

false

true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
