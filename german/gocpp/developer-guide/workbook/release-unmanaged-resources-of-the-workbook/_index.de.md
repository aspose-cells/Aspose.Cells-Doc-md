---
title: Freigeben unmanaged Ressourcen des Arbeitsbuchs mit Golang via C++
linktitle: Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe
type: docs
weight: 310
url: /de/go-cpp/release-unmanaged-resources-of-the-workbook/
description: Erlernen Sie, wie Sie unmanaged Ressourcen der Arbeitsmappe mit Aspose.Cells in Golang über C++ freigeben.
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Methode [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) zur Freigabe der nicht verwalteten Ressourcen des Objekts [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) an. Das Freigabemuster wird nur für Objekte verwendet, die auf nicht verwaltete Ressourcen zugreifen, wie Datei- und Pipe-Handles, Registrierungshandles, Wartehandles oder Zeiger auf Blöcke nicht verwalteten Speichers. Dies liegt daran, dass der Garbage-Collector sehr effizient beim Freigeben nicht verwendeter verwalteter Objekte ist, aber nicht verwaltete Objekte nicht freigeben kann.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) Objekt implementiert jetzt die *IDisposable* Schnittstelle, die eine einzelne Methode [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) hat. Sie können entweder direkt die [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) Methode aufrufen oder die *Using* Anweisung verwenden, um diese Methode automatisch aufzurufen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}
