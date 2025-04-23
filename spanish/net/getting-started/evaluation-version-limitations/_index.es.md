---
title: Limitaciones de la Versión de Evaluación
type: docs
weight: 110
url: /es/net/evaluation-version-limitations/
description: Aspose.Cells for .NET ofrece diferentes planes para comprar u ofrece un Prueba Gratuita y una Licencia Temporal de 30 días para evaluación utilizando políticas de Licenciamiento y Suscripción en C#.
keywords: Limitaciones de la Versión de Evaluación, Número de Archivos Abiertos en la Versión de Evaluación, Marca de Agua de Evaluación usando la Versión de Evaluación.
---

## **Cómo Obtener la Versión de Evaluación de Aspose.Cells**

Puede descargar una versión de evaluación de **Aspose.Cells** para .NET desde [su página de descarga](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) en repositorios Maven. La versión de evaluación proporciona absolutamente las mismas capacidades que la versión con licencia del producto. Además, la versión de evaluación simplemente se convierte en licenciada cuando compra una licencia y agrega un par de líneas de código para aplicar la licencia.

Una vez que estés satisfecho con tu evaluación de **Aspose.Cells**, puedes [comprar una licencia](https://purchase.aspose.com) en el sitio web de Aspose. Familiarízate con los distintos tipos de suscripción ofrecidos. Si tienes alguna pregunta, no dudes en contactar al equipo de ventas de Aspose.

Cada licencia de Aspose lleva una suscripción de un año para actualizaciones gratuitas a cualquier nueva versión o correcciones que salgan durante este tiempo. El soporte técnico es gratuito e ilimitado y se proporciona tanto a usuarios con licencia como de evaluación.

## **Cómo Probar Aspose.Cells Sin Limitaciones de la Versión de Evaluación**

Si desea probar **Aspose.Cells** sin limitaciones de la versión de evaluación, solicite una licencia temporal de 30 días. Consulte [Cómo obtener una licencia temporal?](https://purchase.aspose.com/temporary-license) para más información.


## **Limitaciones de la versión de evaluación**

La versión de evaluación del producto **Aspose.Cells** (sin una licencia especificada) proporciona funcionalidad completa del producto, pero está limitada a abrir 100 archivos en un programa y una hoja de cálculo adicional con marca de agua de evaluación.

Las limitaciones se muestran a continuación:

### **1ª Limitación: Número de archivos abiertos**

Al ejecutar su programa, solo puede abrir 100 archivos de Excel. Si su aplicación supera este número, se generará una excepción.

### **2ª Limitación: Hoja de cálculo con marca de agua de evaluación**
Esta hoja de cálculo siempre se mostrará como la hoja de cálculo activa. Solo en la versión con licencia, puede establecer la hoja de cálculo activa en otras hojas de cálculo.
<br>
<image src="1.png" width="70%" />
<br>

### **3ra Limitación: Texto Simple con información de Evaluación**
En el archivo de Texto Simple de Aspose.Cells, se agregaría información de evaluación al final del documento.
<br>
<image src="2.png" width="70%" />
<br>

### **4ta Limitación: PDF e Imagen con Marca de Agua de Evaluación**
En el archivo PDF de salida o imagen de Aspose.Cells, se pegaría una marca de agua de evaluación en la parte superior del documento/imagen. No se puede ocultar la Advertencia de Derechos de Autor de Evaluación (la hoja de trabajo adicional) en el control GridWeb, también siempre se agregará (al final en las pestañas de la hoja de trabajo) en el control.
<br>
<image src="3.png" width="70%" />
<br>

### **5ta Limitación: Configuración del archivo de configuración (Aspose.Cells.GridWeb)**
No se puede volver a especificar la ruta del script agregando las siguientes líneas de código en la sección de configuración (por ejemplo, en el archivo web.config). El acw_client es una carpeta que contiene archivos y Aspose.Cells.GridWeb utiliza esta carpeta para gestionar su configuración interna, tiene archivos de script, archivos de imagen y otros archivos para especificar el comportamiento de GridWeb y establecer otras operaciones. El archivo de configuración se utiliza para evitar que el control utilice los recursos del cliente integrados (imágenes, scripts, etc.) que son útiles en algunos casos / escenarios. Además, esta configuración en el archivo web.config solo tendrá efecto con la versión CON LICENCIA del control.

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Estas configuraciones pueden ser obligatorias en algunos casos / escenarios si está utilizando el control Aspose.Cells.GridWeb en sitios web del Sistema de Archivos o extensiones MS Ajax, etc.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
