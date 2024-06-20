---
title: Especificar Separadores de Números Decimales y de Grupo Personalizados para Libro de Trabajo
type: docs
weight: 100
url: /es/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Este artículo muestra cómo cambiar el separador decimal y de grupo en MS Excel y con código Java mediante el API Aspose.Cells for Java.
keywords: especificar separador decimal personalizado excel, especificar separador decimal personalizado excel java, especificar separador de grupo personalizado excel, especificar separador de grupo personalizado excel java, especificar separador decimal y de grupo personalizado excel, especificar separador decimal y de grupo personalizado excel java, cambiar separador decimal y de grupo excel java, cambiar separador decimal y de grupo excel, cambiar separador decimal excel, cambiar separador decimal excel java, cambiar separador de grupo excel, cambiar separador de grupo excel java
---

{{% alert color="primary" %}}

En Microsoft Excel, puedes especificar los Separadores de Decimales y Miles Personalizados en lugar de usar Separadores de Sistema de las **Opciones Avanzadas de Excel** como se muestra en la captura de pantalla a continuación.

Aspose.Cells proporciona las propiedades [**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) y [WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) para establecer los separadores personalizados para dar formato/analizar números.

{{% /alert %}}

## **Especificar Separadores Personalizados usando Microsoft Excel**

1. Abre **Opciones** en la pestaña **Archivo**.
1. Abre la pestaña **Avanzadas**.
1. Cambia la configuración en la sección **Opciones de Edición**.

La siguiente captura de pantalla muestra las **Opciones Avanzadas de Excel** y destaca la sección para especificar los **Separadores Personalizados**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Especificar Separadores Personalizados usando Aspose.Cells**

El siguiente código de muestra ilustra cómo especificar los Separadores Personalizados usando el API de Aspose.Cells. Especifica los Separadores de Números Decimales y de Grupo Personalizados como punto y espacio respectivamente. Por lo tanto, el número **123,456.789** se mostrará como **123 456.789** como se muestra en la captura de pantalla que muestra el PDF de salida generado por el código.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
