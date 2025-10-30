---
title: So setzen Sie die AutoRecover Eigenschaft der Arbeitsmappe mit Golang via C++
linktitle: So legen Sie die Eigenschaft AutoRecover einer Arbeitsmappe fest
type: docs
weight: 220
url: /de/go-cpp/how-to-set-autorecover-property-of-workbook/
description: Erfahren Sie, wie Sie die AutoWiederherstellen Eigenschaft einer Arbeitsmappe mit Aspose.Cells for C++ aktivieren oder deaktivieren.
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um die AutoWiederherstellen-Eigenschaft einer Arbeitsmappe festzulegen. Der Standardwert dieser Eigenschaft ist **true**. Wenn Sie sie auf **false** setzen, deaktiviert Microsoft Excel die AutoWiederherstellen-Funktion (Autospeichern) für diese Excel-Datei.

Aspose.Cells stellt die Eigenschaft [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) bereit, um diese Option zu aktivieren oder zu deaktivieren.

{{% /alert %}}

Der folgende Code erklärt, wie die [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/)-Eigenschaft der Arbeitsmappe verwendet wird. Der Code liest zuerst den Standardwert dieser Eigenschaft aus, der **true** ist, setzt ihn dann auf **false** und speichert die Arbeitsmappe. Danach liest er die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der jetzt **false** ist.

## C++-Code zum Setzen der AutoRecover-Eigenschaft der Arbeitsmappe

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **Ergebnis**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
