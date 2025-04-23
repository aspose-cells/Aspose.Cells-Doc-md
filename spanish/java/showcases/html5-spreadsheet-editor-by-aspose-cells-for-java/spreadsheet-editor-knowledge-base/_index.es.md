---
title: Base de Conocimientos del Editor de Hojas de Cálculo
type: docs
weight: 30
url: /es/java/spreadsheet-editor-knowledge-base/
---

## **Incrusta el Editor de Hojas de Cálculo HTML5 en cualquier lugar**

El Editor de Hojas de Cálculo HTML5 se puede incrustar en cualquier sitio web, blog y foros para compartir hojas de cálculo a través de Internet. Puede ser incrustado como un editor independiente o puedes cargarlo con un archivo de hoja de cálculo.

**Incrustar como editor independiente**

Para incrustar como editor independiente, usa la etiqueta IFRAME de HTML para agregarlo al sitio web. Por ejemplo:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**Incrustar con una hoja de cálculo**

Para cargar una hoja de cálculo en un editor incrustado, utilice el parámetro **url**. Por ejemplo:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
