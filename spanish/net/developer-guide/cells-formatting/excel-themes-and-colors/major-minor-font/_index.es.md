---
title: Fuente del tema de encabezados y cuerpo
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Admite la configuración de fuentes de temas de encabezado y cuerpo en documentos de Excel, lo que permite a los usuarios personalizar la apariencia y el estilo del documento. Este artículo presentará cómo utilizar la biblioteca Aspose.Cells para trabajar con fuentes de temas de encabezado y cuerpo en documentos de Excel.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /es/net/headings-and-body-theme-font/
---
{{% alert color="primary" %}}

 La fuente predeterminada cambiará automáticamente cuando se cambie la configuración de reinicio.

Si se cambia la fuente predeterminada, la altura de la fila y el ancho de la columna también cambian, e incluso puede estropear el diseño de la página.

¿Qué causó que cambiara la fuente predeterminada?

Si se configura la fuente del tema de Excel, Excel cambiará automáticamente entre diferentes fuentes según el entorno de idioma actual.


{{% /alert %}}

##  **Fuente de tema de encabezados y cuerpo en Excel**

En Excel, seleccione la pestaña Inicio, haga clic en el cuadro desplegable de fuentes y verá "Fuentes de tema" con dos fuentes de tema: Calibri Light (encabezados) y Calibri (cuerpo) en la parte superior con la configuración de región en inglés.

**![Fuentes del tema](Theme-Fonts.png)**

Si se selecciona Fuente del tema, el nombre de la fuente se mostrará diferente en diferentes regiones.
Si no desea que la fuente cambie automáticamente en diferentes regiones, no seleccione las dos fuentes del tema.


##  **Cambiar la fuente de los títulos y el cuerpo de forma programática**
 Con Aspose.Cells para .Net, podemos verificar si la fuente predeterminada es la fuente del tema o establecer la fuente del tema con[**Tipo de esquema de fuente**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) propiedad.

El siguiente código de muestra muestra cómo manipular la fuente del tema.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


##  **Obtiene dinámicamente la fuente del tema local de forma programática**
A veces, nuestros servidores y las máquinas de los usuarios no se encuentran en la misma región. ¿Cómo podemos obtener la misma fuente que los usuarios desean para el procesamiento de archivos?

 Tenemos que configurar la configuración regional del sistema antes de cargar el archivo con[**Opciones de carga.Región**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) propiedad

El siguiente código de muestra muestra cómo obtener la fuente del tema local.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}