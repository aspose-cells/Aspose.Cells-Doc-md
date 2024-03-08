---
title: Limitaciones de la versión de evaluación
type: docs
weight: 110
url: /es/net/evaluation-version-limitations/
description: Aspose.Cells for .NET proporciona diferentes planes de compra u ofrece una prueba gratuita y una licencia temporal de 30 días para evaluación utilizando las políticas de Licencia y Suscripción en C#.
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---
##  **Cómo obtener la versión de evaluación de Aspose.Cells**

 Puede descargar una versión de evaluación de**Aspose.Cells** para NET de[su página de descarga](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repositorios. La versión de evaluación proporciona absolutamente las mismas capacidades que la versión con licencia del producto. Además, la versión de evaluación simplemente adquiere la licencia cuando usted compra una licencia y agrega un par de líneas de código para aplicar la licencia.

 Una vez que esté satisfecho con su evaluación de *Aspose.Cells**, puede[comprar una licencia](https://purchase.aspose.com) en el sitio web Aspose. Familiarícese con los diferentes tipos de suscripción que se ofrecen. Si tiene alguna pregunta, no dude en comunicarse con el equipo comercial Aspose.

Cada licencia Aspose incluye una suscripción de un año para actualizaciones gratuitas de cualquier nueva versión o corrección que surja durante este tiempo. El soporte técnico es gratuito e ilimitado y se proporciona tanto a usuarios con licencia como a usuarios de evaluación.

##  **Cómo probar Aspose.Cells sin limitaciones de la versión de evaluación**

 Si quieres probar**Aspose.Cells**sin limitaciones de versión de evaluación, solicite una licencia temporal de 30 días. Por favor refiérase a[¿Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license) para más información.


##  **Limitaciones de la versión de evaluación**

 Versión de evaluación de**Aspose.Cells** El producto (sin una licencia especificada) proporciona la funcionalidad completa del producto, pero está limitado a abrir 100 archivos en un programa y una hoja de trabajo adicional con marca de agua de evaluación.

Las limitaciones se muestran a continuación:

###  **Primera limitación: número de archivos abiertos**

Al ejecutar su programa, solo puede abrir 100 archivos de Excel. Si su aplicación excede este número, se generará una excepción.

###  **Segunda limitación: hoja de trabajo con marca de agua de evaluación**
Esta hoja de trabajo siempre se mostrará como la hoja de trabajo activa. Sólo en la versión con licencia, puede configurar la hoja de trabajo activa para otras hojas de trabajo.
<br>
<image src="1.png" width="70%" />
<br>

###  **3ª Limitación: Texto plano con información de evaluación**
En el archivo de texto sin formato de salida de Aspose.Cells, se agregaría información de evaluación al final del documento.
<br>
<image src="2.png" width="70%" />
<br>

###  **4ta Limitación: PDF e Imagen con Marca de Agua de Evaluación**
En la salida PDF o el archivo de imagen de Aspose.Cells, se pegará una marca de agua de evaluación en la parte superior del documento/imagen. No puede ocultar la Advertencia de derechos de autor de evaluación (la hoja de trabajo adicional) en el control GridWeb, siempre se agregará (al final en las pestañas de la hoja de trabajo) en el control.
<br>
<image src="3.png" width="70%" />
<br>

###  **Quinta limitación: configuración del archivo de configuración (Aspose.Cells.GridWeb)**
No puede volver a especificar la ruta del script agregando las siguientes líneas de código en la sección de configuración (por ejemplo, en el archivo web.config). acw_client es una carpeta que contiene archivos y Aspose.Cells.GridWeb usa esta carpeta para administrar su configuración interna, tiene archivos de script, archivos de imágenes y otros archivos para especificar el comportamiento de GridWeb y establecer otras operaciones. El archivo de configuración se utiliza para evitar que el control utilice los recursos del cliente integrados (imágenes, scripts, etc.), lo cual es útil en algunos casos/escenarios. Además, estos ajustes de configuración en el archivo web.config solo tendrán efecto con la versión CON LICENCIA del control.

**XML**
{{< highlight "csharp" >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Esta configuración puede ser obligatoria en algunos casos/escenarios si está utilizando el control Aspose.Cells.GridWeb en sitios web del sistema de archivos o extensiones de MS Ajax, etc.

{{% /alert %}}