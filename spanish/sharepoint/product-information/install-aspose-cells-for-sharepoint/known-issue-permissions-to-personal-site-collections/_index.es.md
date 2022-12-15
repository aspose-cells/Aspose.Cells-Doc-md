---
title: "Problema conocido: permisos para colecciones de sitios personales"
type: docs
weight: 40
url: /es/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

SharePoint, de forma predeterminada, no otorga permisos completos para administrar sitios personales a los administradores del portal. Es por eso que la activación y desactivación en una colección de sitios personales puede fallar cuando la realizan los administradores del portal. Esto incluye la activación y desactivación durante la configuración.

{{% /alert %}} 
### **Conceder permiso a sitios personales**
Cuando se produce este problema durante la instalación, se registra una UnauthorizedAccessException en Microsoft.SharePoint.SPFeature.Activate() en el registro de seguimiento de SharePoint. Cuando la desactivación falla como parte de la desinstalación, se muestra una excepción UnauthorizedAccessException en la última pantalla de configuración para las desactivaciones fallidas.

Para evitar este problema, otorgue a los administradores del portal el permiso para administrar la aplicación web MySite:

1.  Ir**Administración central de SharePoint** seleccione el**Gestión de aplicaciones** pestaña.
1.  Elegir**Política para la aplicación web** bajo la**Seguridad de la aplicación** grupo.
1.  Asegúrese de seleccionar la aplicación web correcta para su "Mi sitio" en el**Aplicación web** lista de la derecha.
1.  Seleccione**Agregar usuarios** en la parte superior izquierda.
1.  Elegir**Todas las zonas** por defecto en el**Agregar usuarios** pantalla y haga clic**próximo**.
1. Agregue los usuarios apropiados o el grupo de directorio activo que desea tener control sobre su aplicación web "Mi sitio".
1.  Seleccione el nivel de control.

   **Adición de usuarios y configuración del nivel de control** 

![todo:imagen_alternativa_texto](known-issue-permissions-to-personal-site-collections_1.png)




1.  Hacer clic**Finalizar**.
