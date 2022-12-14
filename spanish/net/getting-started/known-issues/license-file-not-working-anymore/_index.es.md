---
title: El archivo de licencia ya no funciona
type: docs
weight: 60
url: /es/net/license-file-not-working-anymore/
---
## **Síntoma**

 A veces, los usuarios se frustran porque sus archivos de licencia ya no funcionan cuando mueven/publican sus proyectos web a un nuevo servidor. Se sienten molestos porque sus archivos de licencia funcionaban correctamente en su servidor anterior (antiguo), pero ahora obtienen una licencia adicional.**Evaluación Advertencia de derechos de autor** Hoja de trabajo de marca de agua (siempre que generen informes utilizando el componente) en el nuevo entorno de servidor.

### **un escenario**

"Hemos estado usando Aspose.Cells en nuestro proyecto web ASP.NET para generar/manipular informes de Excel, obtuvimos una licencia válida que estamos usando. Hace algunos días, movimos el sitio web a un nuevo servidor; no hubo actualizaciones ni cambios de ningún tipo, me aseguré y simplemente moví todos y cada uno de los archivos al nuevo servidor, incluido el Aspose.Cells.dll y los archivos .lic relacionados. Ahora, cuando tratamos de generar informes de Excel en el nuevo entorno de servidor, obtenemos un**Evaluación Advertencia de derechos de autor** hoja de marca de agua en nuestros informes. Intentamos descargar e instalar un nuevo archivo de licencia desde la sección Mis pedidos del sitio, pero no solucionó el problema en absoluto. Para su información, implementamos la licencia colocando el archivo Aspose.Cells.lic en la carpeta bin del sitio junto con el archivo del componente Aspose.Cells.dll, que, como mencioné, funcionó sin problemas en el servidor anterior".

### **Solución**

Aspose tiene un mecanismo de licencia limpio y confiable. En general, el problema debe estar relacionado con el problema de implementación. Si un archivo de licencia funciona bien (en un servidor), también debería funcionar igual de bien en otros servidores/entornos. Normalmente los usuarios utilizan la aplicación_Inicio o Sesión_Inicie eventos, etc. en el archivo global.asax para colocar el código de licencia allí. Entonces, es muy posible que la aplicación_Inicio / Sesión_Los eventos de inicio no se activan para procesar el código de licencia en sus nuevas ubicaciones. Cabe señalar aquí que Aspose.Cells siempre generará una excepción si el componente no puede encontrar el archivo de licencia en una ruta. Los usuarios deben asegurarse de que se procese el código de licencia (donde sea que lo coloquen) y se deben activar eventos en los que se coloque el código de licencia. El usuario puede reiniciar el servicio relacionado, es decir, "Publicación en la World Wide Web" e intentar rastrear si la aplicación_Inicio / Sesión_Los eventos de inicio se activan cuando visitan sus proyectos en el nuevo entorno de servidor.

### **Confirmación**

Por favor, también asegúrese de que...

- Está utilizando un archivo de licencia válido en su proyecto.
- Usted u otra persona no debe editar/modificar el archivo de licencia, ya que el archivo de licencia no funcionará.
- Debe tener en cuenta el vencimiento de la suscripción de su licencia (simplemente puede abrir el archivo lic en el bloc de notas y verificar la fecha de vencimiento).
-  No está utilizando una versión (Aspose.Cells.dll) que se lanza después de que caduque la suscripción de su licencia. Cabe señalar aquí que un archivo de licencia nunca caduca, pero si está utilizando la versión del componente que se lanzó después de que caduque su suscripción, obtendrá un archivo adicional**Evaluación Advertencia de derechos de autor** hoja de marca de agua cada vez que crea un archivo de Excel.

### **Referencias**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
