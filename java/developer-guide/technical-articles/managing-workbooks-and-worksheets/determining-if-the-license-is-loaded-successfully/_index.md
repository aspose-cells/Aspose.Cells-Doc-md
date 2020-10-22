---
title: Determining if the License is loaded successfully
type: docs
weight: 210
url: /java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells provides [**Workbook.isLicensed()**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) property which you can use to determine if the license is loaded successfully or not. If you call this method before setting the license, it will return false and if you will call this method after setting the license, it will return true indicating that license has been loaded successfully.

{{% /alert %}}

## **Determining if the License is loaded successfully**

The following code accesses the [**Workbook.isLicensed()**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) method before setting a license and it returns false. Then it loads the license and accesses the property again which now returns true.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Console Output**

Here is the console output of the above sample code

{{< highlight java >}}

false

true

{{< /highlight >}}
