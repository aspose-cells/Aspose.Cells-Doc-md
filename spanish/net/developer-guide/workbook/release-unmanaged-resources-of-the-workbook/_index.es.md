---
title: Liberar recursos no administrados del libro
type: docs
weight: 310
url: /es/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona el método [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) para liberar los recursos no administrados del objeto [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). El patrón de eliminación se utiliza solo para objetos que acceden a recursos no administrados, como manejadores de archivos y tuberías, manejadores de registro, manejadores de espera o punteros a bloques de memoria no administrada. Esto se debe a que el recolector de basura es muy eficiente al reclamar objetos administrados no utilizados, pero no puede reclamar objetos no administrados.

{{% /alert %}}

El objeto [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ahora implementa la interfaz *System.IDisposable* que tiene un método [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose). Puedes llamar directamente al método [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) o usar la declaración *Using* para llamar a este método automáticamente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
{{< app/cells/assistant language="csharp" >}}
