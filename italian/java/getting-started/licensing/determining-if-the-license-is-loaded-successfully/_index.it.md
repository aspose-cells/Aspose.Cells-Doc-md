---
title: Determinare se la licenza è stata caricata correttamente
type: docs
weight: 210
url: /it/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la proprietà [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) che puoi utilizzare per determinare se la licenza è stata caricata correttamente o meno. Se chiami questo metodo prima di impostare la licenza, restituirà false e se chiami questo metodo dopo aver impostato la licenza, restituirà true indicando che la licenza è stata caricata correttamente.

{{% /alert %}}

## **Determinare se la licenza è stata caricata correttamente**

Il seguente codice accede al metodo [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) prima di impostare una licenza e restituisce false. Quindi carica la licenza e accede nuovamente alla proprietà che ora restituisce true.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Output della console**

Ecco l'output console del codice di esempio sopra

{{< highlight java >}}

false

true

{{< /highlight >}}
