---
title: Liberar recursos no administrados del libro de trabajo
type: docs
weight: 290
url: /es/java/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}} 

 Aspose.Cells proporciona[Libro de trabajo.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\) ) método para liberar los recursos no gestionados de la[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)objeto. El patrón de eliminación se usa solo para objetos que acceden a recursos no administrados, como identificadores de archivos y conductos, identificadores de registro, identificadores de espera o punteros a bloques de memoria no administrada. Esto se debe a que el recolector de elementos no utilizados es muy eficaz para reclamar objetos administrados no utilizados, pero no puede reclamar objetos no administrados.

{{% /alert %}} 
## **Liberar recursos no administrados del libro de trabajo**
El siguiente código de ejemplo muestra cómo hacer uso de la[Libro de trabajo.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
