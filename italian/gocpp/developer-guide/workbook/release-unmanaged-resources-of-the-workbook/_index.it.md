---
title: Rilascia le risorse non gestite del workbook con Golang tramite C++
linktitle: Rilascia le risorse non gestite del libro di lavoro
type: docs
weight: 310
url: /it/go-cpp/release-unmanaged-resources-of-the-workbook/
description: Impara come rilasciare risorse non gestite del foglio di lavoro utilizzando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce il metodo [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) per rilasciare le risorse non gestite dell'oggetto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Il modello di smaltimento viene utilizzato solo per gli oggetti che accedono a risorse non gestite, come gestori di file e di pipe, gestori di registro, gestori di attesa o puntatori a blocchi di memoria non gestita. Questo perché il garbage collector è molto efficiente nel recuperare gli oggetti gestiti inutilizzati, ma non è in grado di recuperare gli oggetti non gestiti.

{{% /alert %}}

 L'oggetto [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) ora implementa l'interfaccia *IDisposable* che ha un singolo metodo [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/). Puoi chiamare direttamente il metodo [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) oppure usare l'istruzione *Using* per chiamare automaticamente questo metodo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}
