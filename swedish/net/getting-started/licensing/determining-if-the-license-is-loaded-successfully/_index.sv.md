---
title: Avgör om licensen har laddats
type: docs
weight: 260
url: /sv/net/determining-if-the-license-is-loaded-successfully/
description: "Lär dig hur du upptäcker om licensen har laddats framgångsrikt via Aspose.Cells för NET API:er."
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) egendom som du kan använda för att avgöra om licensen har laddats eller inte. Om du kommer åt den här egenskapen innan du ställer in licensen kommer den tillbaka**falsk** och om du kommer att anropa den här egenskapen efter att ha ställt in licensen kommer den tillbaka**Sann** indikerar att licensen har laddats.

{{% /alert %}}

##  C#-kod för att avgöra om licensen har lästs in

 Följande kod ger åtkomst till[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)egendom innan du ställer in en licens och den returnerar *falsk**. Sedan laddar den licensen och kommer åt fastigheten igen som nu returnerar *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **Konsolutgång**

Här är konsolen (debug) utdata för ovanstående exempelkod

{{< highlight "java" >}}

False

True

{{< /highlight >}}
