---
title: Determining if the License is loaded successfully
type: docs
weight: 210
url: /java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells provides [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) property which you can use to determine if the license is loaded successfully or not. If you call this method before setting the license, it will return false and if you will call this method after setting the license, it will return true indicating that license has been loaded successfully.

{{% /alert %}}

## **Determining if the License is loaded successfully**

The following code accesses the [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) method before setting a license and it returns false. Then it loads the license and accesses the property again which now returns true.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Console Output**

Here is the console output of the above sample code

{{< highlight java >}}

false

true

{{< /highlight >}}
