---
title: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe signiert ist
type: docs
weight: 40
url: /de/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Sie können überprüfen, ob Ihr VBA-Projekt mithilfe von Microsoft Excel über das Menü **Extras > Digitale Signaturen...** signiert ist oder nicht. Ebenso können Sie dies programmgesteuert mithilfe der Aspose.Cells [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)-Methode überprüfen.

{{% /alert %}}

## **Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe signiert ist**

Der folgende Code lädt die Arbeitsmappe und überprüft, ob ihr VBA-Projekt mithilfe der [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)-Eigenschaft signiert ist. Die Eigenschaft gibt **true** zurück, wenn das Projekt signiert ist, andernfalls **false**.

## Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
