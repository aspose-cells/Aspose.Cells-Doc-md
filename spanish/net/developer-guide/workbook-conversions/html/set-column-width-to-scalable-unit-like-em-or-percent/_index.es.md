---
title: Establezca el ancho de columna en una unidad escalable como em o porcentaje
type: docs
weight: 130
url: /es/net/set-column-width-to-scalable-unit-like-em-or-percent/
---

Generar un archivo HTML a partir de una hoja de cálculo es muy común. El tamaño de las columnas está definido en "pt", lo cual funciona en muchos casos. Sin embargo, puede haber casos en los que no se requiera este tamaño fijo. Por ejemplo, si el ancho de un panel contenedor es de 600px donde se muestra esta página HTML. En este caso, es posible que aparezca una barra de desplazamiento horizontal si el ancho de la tabla generada es mayor. Es necesario cambiar este tamaño fijo a una unidad escalable como em o porcentaje para obtener una mejor presentación. El siguiente código de ejemplo se puede utilizar donde [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) se establece como **true** para crear un ancho escalable.

Se pueden descargar archivos fuente de muestra y archivos de salida desde los siguientes enlaces:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
