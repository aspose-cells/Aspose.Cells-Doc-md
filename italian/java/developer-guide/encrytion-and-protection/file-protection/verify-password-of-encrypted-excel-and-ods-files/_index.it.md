---
title: Verifica password dei file crittografati
type: docs
weight: 10
url: /it/java/verify-password-of-encrypted-excel-and-ods-files/
description: Verifica la password dei file Excel crittografati (xlsx, xlsb, xls, xlsm) e dei file Open office (ODS) utilizzando codici Java.
---

{{% alert color="primary" %}}
Se i file Excel (xlsx, xlsb, xls, xlsm) e i file Open office (ODS) sono bloccati con password, Aspose.Cells for Java supporta una semplice verifica della password senza analizzare dati specifici dei file.
{{% /alert %}}

## **Verifica la password del file crittografato**

Per verificare la password del file crittografato, Aspose.Cells for Java fornisce il metodo [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)). Il metodo accetta due parametri, lo stream del file e la password che deve essere verificata.
Il seguente frammento di codice dimostra l'uso del metodo [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) per verificare se la password fornita è valida o meno.

### **Codice di Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

