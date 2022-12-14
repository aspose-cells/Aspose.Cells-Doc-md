---
title: Establezca el ancho de columna en una unidad escalable como em o porcentaje
type: docs
weight: 130
url: /es/java/set-column-width-to-scalable-unit-like-em-or-percent/
---
La generación de un archivo HTML a partir de una hoja de cálculo es muy común. El tamaño de las columnas se define en "pt" que funciona en muchos casos. Sin embargo, puede haber un caso en el que este tamaño fijo no sea necesario. Por ejemplo, si el ancho del panel del contenedor es de 600 px, donde se muestra esta página HTML. En este caso, puede obtener una barra de desplazamiento horizontal si el ancho de la tabla generada es mayor. Se requirió que este tamaño fijo se cambiara a una unidad escalable como em o porcentaje para obtener una mejor presentación. Se puede usar el siguiente código de muestra donde[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) se establece en**verdadero** para crear un ancho escalable.

El archivo fuente de muestra y los archivos de salida se pueden descargar desde los siguientes enlaces:

[muestraParaColumnasEscalables.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
