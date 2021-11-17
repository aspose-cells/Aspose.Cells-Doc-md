---
title: Determining if the License is loaded successfully
type: docs
weight: 260
url: /net/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells provides [**Workbook.IsLicensed**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) property which you can use to determine if the license is loaded successfully or not. If you access this property before setting the license, it will return **false** and if you will call this property after setting the license, it will return **true** indicating that license has been loaded successfully.

{{% /alert %}}

## C# code to determine if the License is loaded successfully

The following code accesses the [**Workbook.IsLicensed**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) property before setting a license and it returns **false**. Then it loads the license and accesses the property again which now returns **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Console Output**

Here is the console (debug) output of the above sample code

{{< highlight java >}}

False

True

{{< /highlight >}}
