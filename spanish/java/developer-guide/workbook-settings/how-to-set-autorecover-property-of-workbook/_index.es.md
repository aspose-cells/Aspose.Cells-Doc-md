---
title: Cómo establecer la propiedad AutoRecover del Libro de trabajo
type: docs
weight: 160
url: /es/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Puedes usar Aspose.Cells para establecer la propiedad AutoRecover del libro de trabajo. El valor predeterminado de esta propiedad es **verdadero**. Cuando lo estableces en **falso** en un libro de trabajo, Microsoft Excel deshabilita la Autorecuperación (Guardado automático) en ese archivo de Excel.

Aspose.Cells proporciona la propiedad [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) para activar o desactivar esta opción.

{{% /alert %}}

## Código Java para establecer la propiedad AutoRecover del libro de trabajo

El siguiente código explica cómo usar la propiedad [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) del libro de trabajo. El código primero lee el valor predeterminado de esta propiedad que es **true**, luego lo establece como **false** y guarda el libro de trabajo. Luego lee el libro nuevamente y lee el valor de esta propiedad que en ese momento es false.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Salida generada por el código de ejemplo

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
