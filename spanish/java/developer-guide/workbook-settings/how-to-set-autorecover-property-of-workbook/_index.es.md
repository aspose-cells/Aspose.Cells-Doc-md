---
title: Cómo configurar la propiedad Autorrecuperación de Workbook
type: docs
weight: 160
url: /es/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

Puede usar Aspose.Cells para establecer la propiedad Autorrecuperación del libro de trabajo. El valor predeterminado de esta propiedad es**verdadero** . cuando lo configuras**falso** en un libro de trabajo, Microsoft Excel deshabilita la Recuperación automática (Guardado automático) en ese archivo de Excel.

 Aspose.Cells proporciona[**Libro de trabajo.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) propiedad para habilitar o deshabilitar esta opción.

{{% /alert %}}

## Java código para establecer la propiedad Autorrecuperación del libro de trabajo

 El siguiente código explica cómo usar[**Libro de trabajo.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) propiedad del libro de trabajo. El código primero lee el valor predeterminado de esta propiedad que es**verdadero** , entonces lo establece como**falso** y guarda el libro de trabajo. Luego lee el libro de trabajo nuevamente y lee el valor de esta propiedad que es falsa en este momento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Salida generada por código de muestra

Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
