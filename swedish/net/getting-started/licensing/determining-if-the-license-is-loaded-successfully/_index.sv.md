---
title: Avgöra om licensen har laddats framgångsrikt
type: docs
weight: 260
url: /sv/net/determining-if-the-license-is-loaded-successfully/
description: Lär dig hur du upptäcker om licensen har laddats framgångsrikt via Aspose.Cells for NET API.
keywords: Hur man upptäcker om licensen har laddats framgångsrikt i C#, Avgör om licensen har laddats framgångsrikt med hjälp av C#, Kontrollera om licensen har laddats framgångsrikt via C#, kontrollera licensens status.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller egenskapen [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) som du kan använda för att avgöra om licensen har laddats framgångsrikt eller inte. Om du har åtkomst till denna egenskap innan du har ställt in licensen kommer den att returnera **false** och om du kommer att anropa denna egenskap efter att ha ställt in licensen, kommer den att returnera **true** vilket indikerar att licensen har laddats framgångsrikt.

{{% /alert %}}

## C#-kod för att avgöra om licensen har laddats framgångsrikt

Följande kod har åtkomst till [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) egenskapen innan en licens har ställts in och den returnerar **false**. Sedan laddar den licensen och har åtkomst till egenskapen igen vilket nu returnerar **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Konsoloutput**

Här är konsol (felsöknings) utdata av ovanstående provkod

{{< highlight java >}}

False

True

{{< /highlight >}}
