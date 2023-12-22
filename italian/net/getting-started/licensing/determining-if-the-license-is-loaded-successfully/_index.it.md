---
title: Determinare se la licenza è stata caricata correttamente
type: docs
weight: 260
url: /it/net/determining-if-the-license-is-loaded-successfully/
description: Scopri come rilevare se la licenza è stata caricata correttamente tramite le API Aspose.Cells per NET.
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) proprietà che puoi utilizzare per determinare se la licenza è stata caricata correttamente o meno. Se accedi a questa proprietà prima di impostare la licenza, verrà restituita**falso** e se chiamerai questa proprietà dopo aver impostato la licenza, verrà restituita**VERO** indicando che la licenza è stata caricata correttamente.

{{% /alert %}}

##  C# codice per determinare se la licenza è stata caricata correttamente

 Il codice seguente accede a[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)proprietà prima di impostare una licenza e restituisce *false**. Quindi carica la licenza e accede nuovamente alla proprietà che ora restituisce *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **Uscita della console**

Ecco l'output della console (debug) del codice di esempio riportato sopra

{{< highlight "java" >}}

False

True

{{< /highlight >}}
