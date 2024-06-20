---
title: Soporte para el diseño de etiquetas DIV al cargar HTML en un libro de trabajo de Excel
type: docs
weight: 50
url: /es/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

Normalmente, el diseño de las etiquetas div se ignora al cargar HTML en un objeto de libro de trabajo de Excel. Sin embargo, si desea que el diseño de las etiquetas div no se ignore, establezca la propiedad [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) en **true**. El valor predeterminado de esta propiedad es **false**.

{{% /alert %}} 

El siguiente código de ejemplo ilustra el uso de la propiedad [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag). Descargue el [logotipo de Aspose](5115218.png) utilizado dentro del HTML de entrada y el [archivo de Excel de salida](5115220.xlsx) generado por el código.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
