---
title: Come impostare la proprietà AutoRecover della cartella di lavoro
type: docs
weight: 220
url: /it/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

È possibile utilizzare Aspose.Cells per impostare la proprietà AutoRecover della cartella di lavoro. Il valore predefinito di questa proprietà è**VERO** . Quando lo imposti**falso** su una cartella di lavoro, Microsoft Excel disabilita il salvataggio automatico (salvataggio automatico) su quel file Excel.

 Aspose.Cells fornisce[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) property per abilitare o disabilitare questa opzione.

{{% /alert %}}

 Il codice seguente spiega come utilizzare[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) proprietà della cartella di lavoro. Il codice prima legge il valore predefinito di questa proprietà che è**VERO** , quindi lo imposta come**falso** e salva la cartella di lavoro. Quindi legge di nuovo la cartella di lavoro e legge il valore di questa proprietà che è**falso** in questo momento.

## C# per impostare la proprietà AutoRecover di Workbook

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Produzione**

Ecco l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
