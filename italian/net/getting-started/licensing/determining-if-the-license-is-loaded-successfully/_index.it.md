---
title: Determinare se la licenza è stata caricata correttamente
type: docs
weight: 260
url: /it/net/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce[**Workbook.Is Licensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) proprietà che è possibile utilizzare per determinare se la licenza è stata caricata correttamente o meno. Se accedi a questa proprietà prima di impostare la licenza, tornerà**falso** se chiamerai questa proprietà dopo aver impostato la licenza, tornerà**VERO** indicando che la licenza è stata caricata correttamente.

{{% /alert %}}

## Codice C# per determinare se la licenza è stata caricata correttamente

 Il codice seguente accede a[**Workbook.Is Licensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) proprietà prima di impostare una licenza e restituisce**falso** . Quindi carica la licenza e accede nuovamente alla proprietà che ora ritorna**VERO**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Uscita console**

Ecco l'output della console (debug) del codice di esempio precedente

{{< highlight "java" >}}

False

True

{{< /highlight >}}
