---
title: Problema conocido  Permisos para colecciones de sitios personales
type: docs
weight: 40
url: /es/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

SharePoint, de forma predeterminada, no otorga permisos completos para administrar sitios personales a los administradores del portal. Es por eso que la activación y desactivación en una colección de sitios personales podría fallar cuando es realizada por administradores del portal. Esto incluye la activación y desactivación durante la configuración.

{{% /alert %}} 
### **Concesión de permiso para sitios personales**
Cuando este problema ocurre durante la instalación, se registra una UnauthorizedAccessException en Microsoft.SharePoint.SPFeature.Activate() en el registro de seguimiento de SharePoint. Cuando la desactivación falla como parte de la desinstalación, se muestra una UnauthorizedAccessException en la pantalla de configuración final para las desactivaciones fallidas.

Para evitar este problema, otorgue a los administradores del portal el permiso para administrar la aplicación web de Mis sitios:

1. Vaya a **Administración central de SharePoint** y seleccione la pestaña **Administración de aplicaciones**.
1. Elija **Política para la aplicación web** en el grupo **Seguridad de la aplicación**.
1. Asegúrese de seleccionar la Aplicación Web correcta para su "Mi sitio" en la lista de **Aplicación web** a la derecha.
1. Seleccione **Agregar usuarios** en la parte superior izquierda.
1. Elija **Todas las zonas** de forma predeterminada en la pantalla **Agregar usuarios** y haga clic en **Siguiente**.
1. Agregue el(los) usuario(s) o grupo de Active Directory apropiado que desee tener control sobre su Aplicación Web 'Mi sitio'.
1. Seleccione el nivel de control. 

   **Añadir usuarios y establecer nivel de control** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. Haga clic en **Terminar**.
