---
title: Liberar recursos no administrados del libro
type: docs
weight: 290
url: /es/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells proporciona el método [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) para liberar los recursos no administrados del objeto [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). El patrón dispose se usa solo para objetos que acceden a recursos no administrados, como handles de archivos y tuberías, handles del registro, handles de espera o punteros a bloques de memoria no administrada. Esto se debe a que el recolector de basura es muy eficiente en recuperar objetos gestionados no utilizados, pero no puede recuperar objetos no administrados.

{{% /alert %}} 
## **Liberar recursos no administrados del libro**
El siguiente código de ejemplo muestra cómo hacer uso del método [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}
