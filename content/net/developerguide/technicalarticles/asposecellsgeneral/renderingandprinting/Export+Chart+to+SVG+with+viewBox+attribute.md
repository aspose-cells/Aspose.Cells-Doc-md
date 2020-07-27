+++
title = "Export Chart to SVG with viewBox attribute" 
description = "" 
weight = 20383 
+++

Aspose.Cells for .NET : Export Chart to SVG with viewBox attribute  

# Aspose.Cells for .NET : Export Chart to SVG with viewBox attribute


By default, when chart is export to svg format, **viewBox** attribute is not included in its xml. However, Aspose.Cells provides `ImageOrPrintOptions.SVGFitToViewPort` property which when set to true exports the chart to svg with viewBox attribute.

# Export Chart to SVG with viewBox attribute

The following sample code exports the chart to svg format with viewBox attribute.

  
  

If you open the chart's svg in notepad, you will find the **viewBox** attribute similar to this.

{{< code lang="cs" >}}
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="100%" height="100%"
     viewBox="0 0 480 288">
{{< /code >}}

