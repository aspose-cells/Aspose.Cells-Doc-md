---
title: Come impostare la proprietà AutoRecupero del Workbook con Golang via C++
linktitle: Come impostare la proprietà AutoRecupero del Workbook
type: docs
weight: 220
url: /it/go-cpp/how-to-set-autorecover-property-of-workbook/
description: Impara come abilitare o disabilitare la proprietà AutoRecover di un workbook usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells per impostare la proprietà AutoRecover di un workbook. Il valore predefinito di questa proprietà è **true**. Quando la imposti a **false** su un workbook, Microsoft Excel disabilita AutoRecover (Autosave) su quel file Excel.

Aspose.Cells fornisce la proprietà [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) per abilitare o disabilitare questa opzione.

{{% /alert %}}

Il seguente codice spiega come usare la proprietà [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) del workbook. Il codice prima legge il valore predefinito di questa proprietà, che è **true**, quindi impostala a **false** e salva il workbook. Poi rilegge il workbook e legge il valore di questa proprietà, che in questo momento è **false**.

## Codice C++ per impostare la proprietà AutoRecover di Workbook

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **Output**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
