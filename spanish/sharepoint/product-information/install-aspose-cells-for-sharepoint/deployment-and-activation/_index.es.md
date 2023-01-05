---
title: Despliegue y Activación
type: docs
weight: 20
url: /es/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[Instalación Aspose.Cells for SharePoint](/cells/es/sharepoint/installing-aspose-cells-for-sharepoint/) lo guía a través del proceso de instalación. Este artículo explica cuál es el proceso de instalación que se implementa y activa.

{{% /alert %}} 
### **Despliegue**
Aspose.Cells for SharePoint realiza las siguientes acciones durante la implementación:

1.  Instalaciones**Aspose.Cells.SharePoint.dll** en la Caché de ensamblados global y agrega una entrada de SafeControl a la**web.config** expediente.
1. Instala el manifiesto de características y otros archivos necesarios en los directorios correspondientes.
1. Registra la función en la base de datos de SharePoint y la pone a disposición para su activación en el ámbito de la función.
### **Activación**
 Aspose.Cells for SharePoint está empaquetado como una función de nivel de sitio (colección de sitios) y se puede activar y desactivar en las colecciones de sitios.

Durante la activación, la función realiza algunos cambios en el directorio virtual de la aplicación web principal de la colección de sitios:

1. Agrega la página de configuración de conversión al archivo del mapa del sitio.
1. Copia los archivos de recursos necesarios a la carpeta App_GlobalResources en el directorio virtual.
