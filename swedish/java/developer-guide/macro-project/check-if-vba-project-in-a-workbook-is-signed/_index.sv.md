---
title: Kontrollera om VBA projektet i en arbetsbok är signerat
type: docs
weight: 40
url: /sv/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Du kan kontrollera om ditt VBA-projekt är signerat eller inte med Microsoft Excel via **Verktyg > Digitala signaturer...** menyalternativ. På liknande sätt kan du kontrollera det programmatiskt med hjälp av Aspose.Cells [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) metoden.

{{% /alert %}}

## **Kontrollera om VBA-projektet i en arbetsbok är signerat**

Följande kod laddar arbetsboken och kontrollerar om dess VBA-projekt är signerat med hjälp av [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) egenskapen. Egenskapen returnerar **true** om projektet är signerat, annars returnerar den **false**.

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
