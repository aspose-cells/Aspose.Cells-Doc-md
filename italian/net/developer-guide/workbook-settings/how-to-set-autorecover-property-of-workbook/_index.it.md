---
title: Come impostare la proprietà AutoRecupero del Workbook
type: docs
weight: 220
url: /it/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Puoi utilizzare Aspose.Cells per impostare la proprietà AutoRecover del foglio di lavoro. Il valore predefinito di questa proprietà è **true**. Quando lo imposti su **false** su un foglio di lavoro, Microsoft Excel disabilita l'AutoRecover (salvataggio automatico) su quel file Excel.

Aspose.Cells fornisce la proprietà [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) per abilitare o disabilitare questa opzione.

{{% /alert %}}

Il codice seguente spiega come utilizzare la proprietà [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) del foglio di lavoro. Il codice legge innanzitutto il valore predefinito di questa proprietà che è **true**, quindi lo imposta su **false** e salva il foglio di lavoro. Successivamente legge nuovamente il foglio di lavoro e legge il valore di questa proprietà che è **false** in quel momento.

## Codice C# per impostare la proprietà AutoRecover del foglio di lavoro

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Output**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
