---
title: Verifica se il progetto VBA in un workbook è firmato
type: docs
weight: 40
url: /it/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Puoi verificare se il tuo progetto VBA è firmato o meno utilizzando Microsoft Excel tramite il comando di menu **Strumenti > Firme digitali...**. Allo stesso modo, è possibile verificarlo programmaticamente utilizzando il metodo Aspose.Cells [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned).

{{% /alert %}}

## **Verifica se il progetto VBA in un foglio di lavoro è firmato**

Il codice seguente carica il workbook e verifica se il suo progetto VBA è firmato utilizzando la proprietà [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned). La proprietà restituirà **true** se il progetto è firmato, altrimenti restituirà **false**.

## Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
{{< app/cells/assistant language="java" >}}
