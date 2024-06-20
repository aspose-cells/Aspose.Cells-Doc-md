---
title: Archivo de Licencia que ya no Funciona
type: docs
weight: 60
url: /es/net/license-file-not-working-anymore/
---

## **Síntoma**

A veces, los usuarios se frustran porque sus archivos de licencia ya no funcionan cuando mueven/publican sus proyectos web a un nuevo servidor. Se sienten molestos ya que sus archivos de licencia funcionaban correctamente en su servidor anterior, pero ahora obtienen una marca de agua de **Advertencia de Copyright de Evaluación** adicional en la hoja de cálculo (cada vez que generan informes utilizando el componente) en el nuevo entorno del servidor.

### **Un Escenario**

"Hemos estado utilizando Aspose.Cells en nuestro proyecto web ASP.NET para generar/manipular informes de Excel, obtuvimos una licencia válida que estamos utilizando. Hace unos días, movimos el sitio web a un nuevo servidor; no hubo actualizaciones ni cambios en absoluto, nos hemos asegurado y simplemente movimos cada archivo al nuevo servidor, incluido el Aspose.Cells.dll y los archivos .lic relacionados. Ahora, cuando intentamos generar informes de Excel en el nuevo entorno del servidor, obtenemos una hoja de cálculo con una marca de agua de **Advertencia de Copyright de Evaluación** en nuestros informes. Intentamos descargar e instalar un nuevo archivo de licencia desde la sección Mis Pedidos del sitio, pero no solucionó el problema en absoluto. Para su información, implementamos la licencia colocando el archivo Aspose.Cells.lic en la carpeta bin del sitio junto con el archivo del componente Aspose.Cells.dll, que, como mencioné, funcionaba sin problemas en el servidor anterior."

### **Solución**

Aspose tiene un mecanismo de licencia limpio y confiable. Generalmente, el problema debería estar relacionado con un problema de implementación. Si un archivo de licencia funciona bien (en un servidor), debería funcionar igual de bien en otros servidores/entornos también. Normalmente, los usuarios utilizan eventos Application_Start o Session_Start, etc. en el archivo global.asax para colocar el código de licencia allí. Por lo tanto, es muy posible que el evento Application_Start / Session_Start no se ejecute para procesar el código de licencia en sus nuevas ubicaciones. Cabe destacar aquí que Aspose.Cells siempre lanzará una excepción si el componente no puede encontrar el archivo de licencia en una ruta. Los usuarios deben asegurarse de que el código de licencia (donde sea que lo coloquen) se procese y los eventos se desencadenen en los que colocan el código de licencia. El usuario puede reiniciar el servicio relacionado, es decir, "Publicación Web en Todo el Mundo" e intentar rastrear si los eventos Application_Start / Session_Start se activan cuando visitan sus proyectos en el nuevo entorno del servidor.

### **Confirmación**

Por favor, asegúrese también de que…

- Está utilizando un archivo de licencia válido en su proyecto.
- Tú o alguien más no debe editar / modificar el archivo de licencia al menos que el archivo de licencia no funcione.
- Debes estar al tanto de la fecha de vencimiento de tu suscripción de licencia (puedes simplemente abrir el archivo lic en el Bloc de notas y verificar la fecha de vencimiento).
- No estás utilizando una versión (Aspose.Cells.dll) que se haya lanzado después de la expiración de tu suscripción de licencia. Cabe destacar que un archivo de licencia nunca expira, pero si estás utilizando la versión del componente que se lanzó después de la expiración de tu suscripción, obtendrás una hoja adicional de advertencia de Copyright de Evaluación cuando crees un archivo de Excel.

### **Referencias**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
