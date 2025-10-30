---
title: Fuente de tema para encabezados y cuerpo
linktitle: Fuente de tema para encabezados y cuerpo
description: Aspose.Cells es una biblioteca para Node.js que permite trabajar con archivos de hojas de cálculo. Soporta configurar las fuentes del tema para encabezados y cuerpo en documentos de Excel, permitiendo a los usuarios personalizar la apariencia y estilo del documento. Este artículo presentará cómo usar la biblioteca Aspose.Cells para trabajar con fuentes del tema en encabezados y cuerpos de documentos de Excel.
keywords: Aspose.Cells, Documento de Excel, Encabezado, Cuerpo, Fuente del tema, Apariencia, Estilo, Node.js vía C++
type: docs
weight: 120
url: /es/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La fuente predeterminada cambiará automáticamente cuando se modifique la configuración regional.

Si se cambia la fuente predeterminada, también se cambiará la altura de la fila y el ancho de la columna e incluso puede desconfigurar el diseño de la página.

¿Qué causó el cambio de la fuente predeterminada?

Si se establece una fuente de tema de Excel, Excel cambiará automáticamente entre fuentes diferentes según el entorno de idioma actual.

{{% /alert %}}

## **Fuente de tema para encabezados y cuerpo en Excel**

En Excel, selecciona la pestaña Inicio, haz clic en la lista desplegable de fuente, verás "Fuentes del tema" con dos fuentes del tema: Calibri Light (Encabezados) y Calibri (Cuerpo) en la parte superior con la configuración regional en inglés.

**![Fuentes del tema](Theme-Fonts.png)**

Si se selecciona Fuente del tema, el nombre de la fuente se mostrará de manera diferente en distintas regiones. Si no deseas que la fuente cambie automáticamente en diferentes regiones, no selecciones las dos Fuentes del tema.

## **Cambiar fuentes de encabezados y cuerpo de forma programática**
Con Aspose.Cells for Node.js via C++, podemos verificar si la fuente predeterminada es una fuente de tema o establecer la fuente de tema con el método [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-).

El siguiente código de ejemplo muestra cómo manipular la fuente del tema.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **Obtiene dinámicamente la fuente del tema local de forma programática**
A veces, nuestros servidores y las máquinas de los usuarios no están en la misma región. ¿Cómo podemos obtener la misma fuente que los usuarios desean para el procesamiento de archivos?

Debemos establecer la configuración regional del sistema antes de cargar el archivo con el método [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-).

El siguiente código de muestra muestra cómo obtener la fuente del tema local.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
