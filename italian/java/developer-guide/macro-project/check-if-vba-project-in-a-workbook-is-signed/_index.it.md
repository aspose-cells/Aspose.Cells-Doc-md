---
title: Controlla se il progetto VBA in una cartella di lavoro è firmato
type: docs
weight: 40
url: /it/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

 Puoi verificare se il tuo progetto VBA è firmato o meno utilizzando Microsoft Excel tramite**Strumenti > Firme digitali...** comando di menù. Allo stesso modo, puoi controllarlo a livello di codice usando Aspose.Cells[**Cartella di lavoro.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) metodo.

{{% /alert %}}

## **Controlla se il progetto VBA in una cartella di lavoro è firmato**

 Il codice seguente carica la cartella di lavoro e controlla se il relativo progetto VBA è firmato utilizzando[**Cartella di lavoro.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)proprietà. La proprietà tornerà**VERO** se il progetto è firmato altrimenti tornerà**falso**.

## Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
