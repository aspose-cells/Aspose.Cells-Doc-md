---
title: Kontrollera om VBA-projekt i en arbetsbok är signerat
type: docs
weight: 40
url: /sv/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

 Du kan kontrollera om ditt VBA-projekt är signerat eller inte med hjälp av Microsoft Excel via**Verktyg > Digitala signaturer...** menykommando. På samma sätt kan du kontrollera det programmatiskt med Aspose.Cells[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) metod.

{{% /alert %}}

## **Kontrollera om VBA-projekt i en arbetsbok är signerat**

 Följande kod laddar arbetsboken och kontrollerar om dess VBA-projekt är signerat med[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)fast egendom. Fastigheten kommer tillbaka**Sann** om projektet signeras annars kommer det tillbaka**falsk**.

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
