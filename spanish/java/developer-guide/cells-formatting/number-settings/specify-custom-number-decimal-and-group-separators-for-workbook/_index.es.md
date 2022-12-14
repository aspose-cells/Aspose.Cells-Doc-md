---
title: Especificar separadores de grupos y decimales de números personalizados para el libro de trabajo
type: docs
weight: 100
url: /es/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Este artículo muestra cómo cambiar el número decimal y el separador de grupos en MS Excel y con el código Java usando el Aspose.Cells for Java API.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 En Microsoft Excel, puede especificar los separadores decimales y de miles personalizados en lugar de utilizar los separadores de sistema de la**Opciones Avanzadas de Excel** como se muestra en la captura de pantalla a continuación.

 Aspose.Cells proporciona el[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) y[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) properties para establecer los separadores personalizados para formatear/analizar números.

{{% /alert %}}

## **Especificación de separadores personalizados usando Microsoft Excel**

1.  Abierto**Opciones** en el**Expediente** pestaña.
1. Abre el**Avanzado** pestaña.
1.  Cambie la configuración en el**Opciones de edición** sección.

 La siguiente captura de pantalla muestra la**Opciones Avanzadas de Excel** y resalta la sección para especificar el**Separadores personalizados**.

![todo:imagen_alternativa_texto](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Especificación de separadores personalizados mediante Aspose.Cells**

 El siguiente código de ejemplo ilustra cómo especificar los separadores personalizados mediante Aspose.Cells API. Especifica los separadores decimales y de grupo de números personalizados como punto y espacio respectivamente. entonces el numero**123,456.789** se mostrará como**123 456.789** como se muestra en la captura de pantalla que muestra el PDF de salida generado por el código.

![todo:imagen_alternativa_texto](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
