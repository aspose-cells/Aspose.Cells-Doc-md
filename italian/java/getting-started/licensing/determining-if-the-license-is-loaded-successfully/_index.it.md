---
title: Determinare se la licenza è stata caricata correttamente
type: docs
weight: 210
url: /it/java/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)proprietà che è possibile utilizzare per determinare se la licenza è stata caricata correttamente o meno. Se chiami questo metodo prima di impostare la licenza, restituirà false e se chiamerai questo metodo dopo aver impostato la licenza, restituirà true indicando che la licenza è stata caricata correttamente.

{{% /alert %}}

## **Determinare se la licenza è stata caricata correttamente**

 Il codice seguente accede a[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)metodo prima di impostare una licenza e restituisce false. Quindi carica la licenza e accede nuovamente alla proprietà che ora restituisce true.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Uscita console**

Ecco l'output della console del codice di esempio precedente

{{< highlight "java" >}}

false

true

{{< /highlight >}}
