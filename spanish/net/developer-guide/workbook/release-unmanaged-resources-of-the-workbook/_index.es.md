---
title: Liberar recursos no administrados del libro de trabajo
type: docs
weight: 310
url: /es/net/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona[**Libro de trabajo.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) método para liberar los recursos no gestionados de la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)objeto. El patrón de eliminación se usa solo para objetos que acceden a recursos no administrados, como identificadores de archivos y conductos, identificadores de registro, identificadores de espera o punteros a bloques de memoria no administrada. Esto se debe a que el recolector de elementos no utilizados es muy eficaz para reclamar objetos administrados no utilizados, pero no puede reclamar objetos no administrados.

{{% /alert %}}

[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) objeto ahora implementa el*Sistema.IDisposable* interfaz que tiene un solo método[**Disponer()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) . Puede llamar directamente al[**Libro de trabajo.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) método o puede utilizar el*Usando*declaración para llamar a este método automáticamente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
