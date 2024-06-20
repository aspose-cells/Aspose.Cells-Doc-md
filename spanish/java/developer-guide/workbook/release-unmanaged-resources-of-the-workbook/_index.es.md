---
title: Liberar recursos no administrados del libro
type: docs
weight: 290
url: /es/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells proporciona el método [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) para liberar los recursos no administrados del objeto [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). El patrón de eliminación se utiliza solo para objetos que acceden a recursos no administrados, como manijas de archivo y de tuberías, manijas de registro, manijas de espera o punteros a bloques de memoria no administrados. Esto se debe a que el recolector de basura es muy eficiente en la recuperación de objetos administrados no utilizados, pero no puede recuperar objetos no administrados.

{{% /alert %}} 
## **Liberar recursos no administrados del libro**
El siguiente código de ejemplo muestra cómo hacer uso del método [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
