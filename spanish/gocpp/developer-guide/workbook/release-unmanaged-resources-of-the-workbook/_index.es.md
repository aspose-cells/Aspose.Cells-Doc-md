---
title: Liberar recursos no gestionados del libro de trabajo con Golang mediante C++
linktitle: Liberar recursos no administrados del libro
type: docs
weight: 310
url: /es/go-cpp/release-unmanaged-resources-of-the-workbook/
description: Aprende cómo liberar recursos no controlados del Libro de trabajo usando Aspose.Cells con Golang a través de C++.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona el método [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) para liberar los recursos no administrados del objeto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). El patrón de eliminación se utiliza solo para objetos que acceden a recursos no administrados, como manejadores de archivos y tuberías, manejadores de registro, manejadores de espera o punteros a bloques de memoria no administrada. Esto se debe a que el recolector de basura es muy eficiente al reclamar objetos administrados no utilizados, pero no puede reclamar objetos no administrados.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) objeto ahora implementa la interfaz *IDisposable* que tiene un método único [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/). Puedes llamar directamente al método [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) o puedes usar la instrucción *Using* para llamar a este método automáticamente.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}
