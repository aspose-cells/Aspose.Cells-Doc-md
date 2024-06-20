---
title: Verifique si el proyecto VBA en un Libro de Trabajo está firmado
type: docs
weight: 40
url: /es/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Puede verificar si su proyecto VBA está firmado o no utilizando Microsoft Excel a través del comando del menú **Herramientas > Firmas Digitales...**. De manera similar, puede verificarlo programáticamente utilizando el método [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) de Aspose.Cells.

{{% /alert %}}

## **Comprobar si el proyecto de VBA en un libro de Excel está firmado**

El siguiente código carga el libro de trabajo y verifica si su proyecto VBA está firmado utilizando la propiedad [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned). La propiedad devolverá **verdadero** si el proyecto está firmado, de lo contrario devolverá **falso**.

## Código de Muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
