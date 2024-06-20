---
title: Establezca el ancho de columna en una unidad escalable como em o porcentaje
type: docs
weight: 130
url: /es/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

Generar un archivo HTML desde una hoja de cálculo es muy común. El tamaño de las columnas está definido en "pt" que funciona en muchos casos. Sin embargo, puede darse el caso de que este tamaño fijo no sea necesario. Por ejemplo, si el ancho del panel contenedor es de 600px donde se muestra esta página HTML. En este caso, puede aparecer una barra de desplazamiento horizontal si el ancho de la tabla generada es mayor. Se requería que este tamaño fijo se cambiara a una unidad escalable como em o porcentaje para obtener una mejor presentación. El siguiente código de ejemplo puede utilizarse donde [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) está configurado como **true** para crear un ancho escalable.

Se pueden descargar archivos fuente de muestra y archivos de salida desde los siguientes enlaces:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
