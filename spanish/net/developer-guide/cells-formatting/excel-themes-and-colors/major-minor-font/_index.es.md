---
title: Fuente de tema para encabezados y cuerpo
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Admite el ajuste de las fuentes de tema para encabezados y cuerpo en documentos de Excel, lo que permite a los usuarios personalizar la apariencia y el estilo del documento. Este artículo introducirá cómo utilizar la biblioteca Aspose.Cells para trabajar con las fuentes de tema para encabezados y cuerpo en documentos de Excel.
keywords: Aspose.Cells, Documento de Excel, Encabezado, Cuerpo, Fuente de tema, Apariencia, Estilo
type: docs
weight: 120
url: /es/net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La fuente predeterminada cambiará automáticamente cuando se cambie la configuración de la región. 

Si se cambia la fuente predeterminada, también se cambiará la altura de la fila y el ancho de la columna e incluso puede desconfigurar el diseño de la página.

¿Qué causó el cambio de la fuente predeterminada?

Si se establece una fuente de tema de Excel, Excel cambiará automáticamente entre fuentes diferentes según el entorno de idioma actual.


{{% /alert %}}

## **Fuente de tema para encabezados y cuerpo en Excel**

En Excel, selecciona la pestaña Inicio, haz clic en el cuadro desplegable de fuente, verás "Fuentes del tema" con dos fuentes de tema: Calibri Light (Encabezados) y Calibri (Cuerpo) en la parte superior con la configuración de región en inglés.

**![Fuentes del tema](Theme-Fonts.png)**

Si se selecciona la Fuente del tema, el nombre de la fuente se mostrará de manera diferente en diferentes regiones.
Si no quieres que la fuente cambie automáticamente en diferentes regiones, no selecciones las dos Fuentes del tema.


## **Cambiar las fuentes de encabezados y cuerpo de forma programática**
Con Aspose.Cells para .Net, podemos verificar si la fuente predeterminada es una fuente del tema o establecer la fuente del tema con la propiedad [**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/).

El siguiente código de muestra muestra cómo manipular la fuente del tema de forma programática.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **Obtención dinámica de la fuente del tema local de forma programática**
A veces, nuestros servidores y las máquinas de los usuarios no están en la misma región. ¿Cómo podemos obtener la misma fuente que los usuarios desean para el procesamiento de archivos?

Tenemos que establecer la configuración regional del sistema antes de cargar el archivo con la propiedad [**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/).

El siguiente código de muestra muestra cómo obtener la fuente del tema local.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
{{< app/cells/assistant language="csharp" >}}
