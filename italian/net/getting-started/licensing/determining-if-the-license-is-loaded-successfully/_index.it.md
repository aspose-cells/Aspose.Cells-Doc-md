---
title: Determinare se la licenza è stata caricata correttamente
type: docs
weight: 260
url: /it/net/determining-if-the-license-is-loaded-successfully/
description: Scopri come rilevare se la licenza è stata caricata correttamente attraverso le API Aspose.Cells for NET.
keywords: Come individuare se la licenza è stata caricata correttamente in C#, Determinare se la licenza è stata caricata correttamente usando C#, Verificare se la licenza è stata caricata correttamente tramite C#, controllare lo stato della licenza.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la proprietà [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) che puoi utilizzare per determinare se la licenza è stata caricata correttamente o meno. Se accedi a questa proprietà prima di impostare la licenza, restituirà **false** e se chiamerai questa proprietà dopo aver impostato la licenza, restituirà **true** indicando che la licenza è stata caricata correttamente.

{{% /alert %}}

## Codice C# per determinare se la licenza è stata caricata correttamente

Il seguente codice accede alla proprietà [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) prima di impostare una licenza e restituisce **false**. Successivamente carica la licenza e accede nuovamente alla proprietà che ora restituisce **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Output della console**

Ecco l'output della console (debug) del codice di esempio sopra

{{< highlight java >}}

False

True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
