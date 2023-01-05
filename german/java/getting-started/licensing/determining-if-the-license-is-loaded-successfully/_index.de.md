---
title: Bestimmen, ob die Lizenz erfolgreich geladen wurde
type: docs
weight: 210
url: /de/java/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells bietet[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)-Eigenschaft, mit der Sie feststellen können, ob die Lizenz erfolgreich geladen wurde oder nicht. Wenn Sie diese Methode aufrufen, bevor Sie die Lizenz festlegen, wird „false“ zurückgegeben, und wenn Sie diese Methode nach dem Festlegen der Lizenz aufrufen, wird „true“ zurückgegeben, was darauf hinweist, dass die Lizenz erfolgreich geladen wurde.

{{% /alert %}}

## **Bestimmen, ob die Lizenz erfolgreich geladen wurde**

 Der folgende Code greift auf die[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)-Methode vor dem Festlegen einer Lizenz und gibt false zurück. Dann lädt es die Lizenz und greift erneut auf die Eigenschaft zu, die jetzt wahr zurückgibt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes

{{< highlight "java" >}}

false

true

{{< /highlight >}}
