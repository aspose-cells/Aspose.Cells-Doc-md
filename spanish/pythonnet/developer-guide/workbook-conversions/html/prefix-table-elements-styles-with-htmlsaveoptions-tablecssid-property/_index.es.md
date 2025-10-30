---
title: Prefijo de estilos de elementos de tabla con la propiedad HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /es/python-net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **Escenarios de uso posibles**

Aspose.Cells le permite prefijar los estilos de los elementos de tabla con la propiedad [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id). Supongamos que define esta propiedad con algún valor como **MyTest_TableCssId**, entonces encontrará estilos de elementos de tabla como se muestra a continuación

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

La siguiente captura de pantalla muestra el efecto de usar la propiedad [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id) en la salida de HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Prefijo de estilos de elementos de tabla con la propiedad HtmlSaveOptions.TableCssId**

El siguiente código de ejemplo demuestra cómo hacer uso de la propiedad [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id). Revise el [HTML de salida](60489790.zip) generado por el código como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.py" >}}
{{< app/cells/assistant language="python-net" >}}
