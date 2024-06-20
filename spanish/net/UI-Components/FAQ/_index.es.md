---
title: Preguntas frecuentes (FAQ)
type: docs
weight: 400
url: /es/net/grid-faq/
---

## **¿Hay alguna limitación en la versión de evaluación de los controles de cuadrícula de Aspose.Cells?**
No, no hay limitación de funciones en la versión de evaluación de esos controles.

La versión de evaluación proporciona todas las funciones de la versión con licencia excepto que agrega una hoja de cálculo adicional (que contiene **Advertencia de Derechos de Autor de Evaluación**) a los archivos de salida.


## **Hay tantos controles de cuadrícula disponibles en el mercado. ¿Por qué debería comprar los controles de cuadrícula de Aspose.Cells?**
Bueno, los controles de cuadrícula de Aspose.Cells tienen un precio muy razonable para ser asequible para todo tipo de usuarios. Por un precio muy asequible,

proporciona un conjunto de dos controles para trabajar en aplicaciones de Windows y Web. 

Además, no es simplemente una cuadrícula, es su **Visor, Editor y Creador de Hojas de Cálculo** al mismo tiempo. 

No solo puedes vincularlo con cualquier tipo de fuente de datos (como los controles de cuadrícula normales) sino también crear y gestionar archivos de Excel. También proporciona un **Motor de Cálculo de Fórmulas** sólido y rico para calcular no solo funciones integradas (compatibles con los controles de cuadrícula de Aspose.Cells) sino también fórmulas personalizadas definidas por ti. Hay muchas más características del conjunto de cuadrícula de Aspose.Cells que no se pueden detallar aquí, por favor consulta la página de Tipos de Edición para obtener una lista de características más detallada.

## **Recientemente compré mi licencia para los controles de cuadrícula de Aspose.Cells. ¿Cómo puedo usar esa licencia en mi aplicación con el Control de Cuadrícula de Aspose.Cells?**
Consulta la página de [Licencias](/cells/es/net/licensing/) de los controles de cuadrícula de Aspose.Cells. 

Proporciona detalles completos sobre cómo utilizar la licencia con los controles de cuadrícula de Aspose.Cells en tus aplicaciones.



## **¿Cómo puedo implementar mi proyecto/solución web basado en Aspose.Cells.GridWeb en el servidor?**
Si necesitas implementar la aplicación web con control GridWeb, copiarías el directorio "acw_client" en la carpeta de tu proyecto como mínimo, ya que tu aplicación web (implementada en el servidor) no podría encontrarlo.

Siempre puedes especificar la ruta de scripts agregando las siguientes líneas de código en la sección de configuración (por ejemplo, en el archivo web.config de tu proyecto VS.NET). El "acw_client" es una carpeta que contiene archivos y Aspose.Cells.GridWeb utiliza esta carpeta para gestionar su configuración interna, tiene archivos de scripts, archivos de imagen y otros archivos para especificar el comportamiento de GridWeb y configurar otras operaciones. El archivo de configuración se utiliza para evitar que el control utilice los recursos del cliente incrustados (imágenes, scripts, etc.), lo cual es útil en algunos casos o escenarios.

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

La ruta siempre está relacionada con el directorio del proyecto. No debe usar ningún directorio que esté fuera del directorio del proyecto. Por lo tanto, es necesario copiar el directorio "acw_client" (en su carpeta de instalación de GridWeb) en el directorio del proyecto.

{{% /alert %}} 
## **Ejecutando Aspose.Cell.GridWeb en Internet Explorer**
Actualmente, Aspose.Cells.GridWeb ya no es compatible con Internet Explorer, es un navegador muy antiguo. 
Soportamos Chrome, Edge, Firefox, Safari, Opera



