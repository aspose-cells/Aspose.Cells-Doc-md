---
title: Verifica password dei file crittografati
type: docs
weight: 10
url: /it/net/verify-password-of-encrypted-excel-and-ods-files/
description: Verifica la password dei file Excel crittografati (xlsx, xlsb, xls, xlsm) e dei file Open office (ODS) utilizzando codici CSharp.
---

{{% alert color="primary" %}}
Se i file Excel (xlsx, xlsb, xls, xlsm) e i file Open office (ODS) sono bloccati da password, Aspose supporta una semplice verifica della password senza l'analisi di dati specifici dei file.
{{% /alert %}}

## **Verifica la password del file crittografato**

Per verificare la password del file crittografato, Aspose.Cells for .NET fornisce il metodo [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword). Questi metodi accettano due parametri: lo stream del file e la password da verificare.
Il seguente frammento di codice dimostra l'uso del metodo [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) per verificare se la password fornita è valida o meno.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
