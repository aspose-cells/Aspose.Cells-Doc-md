---
title: Preguntas más frecuentes
type: docs
weight: 400
url: /es/net/grid-faq/
---
## **¿Existe alguna limitación en la versión de evaluación de Aspose.Cells Grid Controls?**
 No, no hay limitación de funciones en la versión de evaluación de Aspose.Cells Grid Controls. La versión de evaluación proporciona funciones completas de la versión con licencia, excepto que agrega una hoja de trabajo adicional (que contiene**Evaluación Advertencia de derechos de autor** ) a los archivos de salida.
## **Hay tantos controles Grid disponibles en el mercado. ¿Por qué debería comprar Aspose.Cells Grid Controls?**
 Bueno, Aspose.Cells Grid Controls tienen un precio muy bueno para ser asequible para todo tipo de usuarios. A un precio muy razonable, le brinda un conjunto de dos controles para trabajar en Windows y aplicaciones web. Además, no es solo una simple cuadrícula, es su**Visor, editor y creador de hojas de cálculo** al mismo tiempo. No solo puede vincularlo con cualquier tipo de fuente de datos (como los controles de cuadrícula normales), sino también crear y administrar archivos de Excel. También proporciona un fuerte y rico**Motor de cálculo de fórmulas** para calcular no solo funciones integradas (compatibles con Aspose.Cells Grid Controls), sino también fórmulas personalizadas definidas por usted. Hay muchas más características de Aspose.Cells Grid Suite que no se pueden cubrir aquí, consulte la página Tipos de edición para obtener una lista de características más detallada.
## **Recientemente compré mi licencia para Aspose.Cells Grid Controls. ¿Cómo puedo usar esa licencia en mi aplicación con Aspose.Cells Grid Control?**
por favor refiérase a[Licencia](/cells/es/net/licensing/) página de Aspose.Cells Grid Controls. Proporciona detalles completos sobre cómo usar la licencia con Aspose.Cells Grid Controls en sus aplicaciones.
## **¿Se admiten los controles de cuadrícula Aspose.Cells en Visual Studio.NET 2005?**
Sí, Aspose.Cells Grid Controls son totalmente compatibles con Visual Studio.NET 2005 y versiones posteriores.
## **Estoy usando el control Aspose.Cells.GridWeb en mi sitio web usando Visual Studio.NET 2005. Pero no funciona en absoluto. ¿Cuál es el problema?**
 Aspose.Cells. GridWeb admite ambos**Sistema de archivos** y**HTTP** modos de Visual Studio.NET 2005. Si todavía está confundido, consulte la guía paso a paso para Trabajar con Aspose.Cells.GridWeb usando Visual Studio.NET 2005.
## **¿Cómo puedo implementar mi proyecto/solución web basado en Aspose.Cells.GridWeb en el servidor?**
Si necesita implementar la aplicación web con el control de GridWeb, debe copiar el archivo "acw_client" en la carpeta de su proyecto, al menos su aplicación web (implementada en el servidor) no pudo encontrarlo. Siempre puede especificar la ruta de secuencias de comandos agregando las siguientes líneas de código en la sección de configuración (por ejemplo, en el archivo web.config en su Proyecto VS.NET). El "acw_client" es una carpeta que contiene archivos y Aspose.Cells. GridWeb usa esta carpeta para administrar su configuración interna, tiene archivos de secuencias de comandos, archivos de imagen y otros archivos para especificar el comportamiento de GridWeb y establecer otras operaciones. El archivo de configuración se usa para evitar que el control utilizando los recursos del cliente incorporados (imágenes, scripts, etc.), lo cual es útil en algunos casos/escenarios.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

La ruta siempre está relacionada con el directorio del proyecto. No debe usar ningún directorio que esté fuera del directorio del proyecto. Por lo tanto, es necesario copiar el directorio "acw_client" (@ su carpeta de instalación de GridWeb) en el directorio del proyecto.

{{% /alert %}} 
## **Ejecutando Aspose.Cell.GridWeb en Internet Explorer 10 u 11**
 Actualmente, Aspose.Cells.GridWeb no funciona muy bien en Internet Explorer 10 u 11, por lo que debe usar el modo de compatibilidad de IE8/9 para trabajar con él en el tipo de navegador IE10/11. Debe agregar la siguiente línea de**<meta>** etiqueta en la sección de encabezado en**.aspx** página:



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

