---
title: Come impostare la proprietà AutoRecupero del Workbook
type: docs
weight: 220
url: /it/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells for Python via .NET per impostare la proprietà AutoRecover del workbook. Il valore predefinito di questa proprietà è **true**. Quando la imposti su **false**, Microsoft Excel disabilita AutoRecover (Autosave) su quel file Excel.

Aspose.Cells for Python via .NET fornisce la proprietà [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) per abilitare o disabilitare questa opzione.

{{% /alert %}}

Il codice seguente spiega come usare la proprietà [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) del workbook. Il codice legge prima il valore predefinito di questa proprietà, che è **true**, quindi la imposta come **false** e salva il workbook. Poi legge di nuovo il workbook e verifica il valore di questa proprietà, che in questo momento è **false**.

## Codice C# per impostare la proprietà AutoRecover del foglio di lavoro

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **Output**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
