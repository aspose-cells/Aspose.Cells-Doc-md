---
title: Feststellen, ob die Lizenz erfolgreich geladen wird
type: docs
weight: 210
url: /de/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)-Eigenschaft, die Sie verwenden können, um zu bestimmen, ob die Lizenz erfolgreich geladen wurde oder nicht. Wenn Sie diese Methode aufrufen, bevor Sie die Lizenz eingeben, gibt sie false zurück. Wenn Sie diese Methode nach dem Eingeben der Lizenz aufrufen, gibt sie true zurück, was darauf hinweist, dass die Lizenz erfolgreich geladen wurde.

{{% /alert %}}

## **Überprüfen, ob die Lizenz erfolgreich geladen wurde**

Der folgende Code greift auf die [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)-Methode zu, bevor eine Lizenz eingefügt wird, und gibt false zurück. Dann lädt er die Lizenz und greift erneut auf die Eigenschaft zu, die nun true zurückgibt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielscodes

{{< highlight java >}}

false

true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
