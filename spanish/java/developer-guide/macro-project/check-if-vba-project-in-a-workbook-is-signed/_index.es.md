---
title: Compruebe si el proyecto de VBA en un libro de trabajo está firmado
type: docs
weight: 40
url: /es/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

 Puede verificar si su proyecto VBA está firmado o no usando Microsoft Excel a través de**Herramientas > Firmas digitales...** comando de menú. Del mismo modo, puede verificarlo mediante programación usando Aspose.Cells[**Libro de trabajo.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) método.

{{% /alert %}}

## **Compruebe si el proyecto de VBA en un libro de trabajo está firmado**

 El siguiente código carga el libro de trabajo y verifica si su proyecto VBA está firmado usando[**Libro de trabajo.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) propiedad. La propiedad volverá**verdadero** si el proyecto está firmado de lo contrario se devolverá**falso**.

## Código de muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
