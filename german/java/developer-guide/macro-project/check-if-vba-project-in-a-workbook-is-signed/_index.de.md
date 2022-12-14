---
title: Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe signiert ist
type: docs
weight: 40
url: /de/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

 Sie können überprüfen, ob Ihr VBA-Projekt signiert ist oder nicht, indem Sie Microsoft Excel über verwenden**Extras > Digitale Signaturen...** Menübefehl. Ebenso können Sie es programmgesteuert mit Aspose.Cells überprüfen[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) Methode.

{{% /alert %}}

## **Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe signiert ist**

 Der folgende Code lädt die Arbeitsmappe und prüft, ob ihr VBA-Projekt mit signiert ist[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)Eigentum. Das Eigentum wird zurückgegeben**Stimmt** Wenn das Projekt signiert ist, wird es andernfalls zurückgegeben**FALSCH**.

## Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
