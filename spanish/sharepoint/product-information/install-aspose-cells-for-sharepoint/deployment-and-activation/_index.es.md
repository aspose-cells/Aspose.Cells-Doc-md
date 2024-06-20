---
title: Despliegue y activación
type: docs
weight: 20
url: /es/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[La instalación de Aspose.Cells for SharePoint](/cells/es/sharepoint/installing-aspose-cells-for-sharepoint/) le guía a través del proceso de instalación. Este artículo explica cómo se despliega y activa el proceso de instalación.

{{% /alert %}} 
### **Despliegue**
Aspose.Cells for SharePoint realiza las siguientes acciones durante el despliegue:

1. Instala **Aspose.Cells.SharePoint.dll** en la Global Assembly Cache y añade una entrada SafeControl al archivo **web.config**.
1. Instala el manifiesto de la característica y otros archivos necesarios en los directorios correspondientes.
1. Registra la característica en la base de datos de SharePoint y la hace disponible para activación en el alcance de la característica.
### **Activación**
Aspose.Cells for SharePoint está empaquetado como una característica a nivel de sitio (colección de sitios) y puede ser activado y desactivado en las colecciones de sitios. 

Durante la activación, la característica realiza algunos cambios en el directorio virtual de la aplicación web principal de la colección de sitios:

1. Añade la página de configuración de conversión al archivo del mapa del sitio.
1. Copia los archivos de recursos necesarios a la carpeta App_GlobalResources en el directorio virtual.
