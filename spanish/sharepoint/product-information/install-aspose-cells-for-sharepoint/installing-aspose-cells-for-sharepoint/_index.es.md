---
title: Instalación de Aspose.Cells para SharePoint
type: docs
weight: 10
url: /es/sharepoint/installing-aspose-cells-for-sharepoint/
---
{{% alert color="primary" %}} 

 Aspose.Cells para SharePoint se puede descargar como el archivo Aspose.Cells.SharePoint.zip.

{{% /alert %}} 
### **Contenidos del archivo**
El archivo Aspose.Cells.SharePoint.zip contiene:

- Aspose.Cells.SharePoint.wsp: archivo de solución de SharePoint. Aspose.Cells para SharePoint se empaqueta como una solución de SharePoint para facilitar la implementación/retirada y la activación/desactivación de funciones en toda la granja de servidores.
- Aspose_LicenseAgreement.rtf: acuerdo de licencia de usuario final
- Aspose.Cells para SharePoint.pdf – Documentación del usuario
- Aspose.Cells para SharePoint Documentation.chm: documentación de usuario con referencia pública API
- setup.exe – programa de instalación
- setup.exe.config: archivo de configuración de instalación

El programa de instalación verifica las siguientes condiciones antes de continuar con la instalación:

- WSS 3.0, MOSS 2007 o SharePoint 2010 está instalado.
- El usuario tiene permiso para instalar soluciones de SharePoint.
- La base de datos de SharePoint está en línea.
- Se inicia el servicio de administración de WSS.
- Se inicia el servicio de temporizador WSS.

 El servicio de administración WSS y el servicio de temporizador son necesarios porque algunas acciones de configuración dependen de un trabajo de temporizador para propagarse a todos los servidores de la granja de servidores.
#### **Para instalar Aspose.Cells para SharePoint**
1. Descomprima Aspose.Cells.SharePoint zip en la unidad local del servidor MOSS 7.0 o WSS 3.0.
1. Ejecute setup.exe y siga las instrucciones en pantalla.

El programa de instalación realiza las siguientes acciones:

1.  Compruebe los requisitos previos de instalación. La instalación no continuará si falla alguna comprobación.

   **Chequeo del sistema** 

![todo:imagen_alternativa_texto](installing-aspose-cells-for-sharepoint_1.png)




1.  Mostrar Acuerdo de licencia de usuario final. El usuario debe aceptar el acuerdo para continuar.

   **El CLUF** 

![todo:imagen_alternativa_texto](installing-aspose-cells-for-sharepoint_2.png)




1. Mostrar el cuadro de diálogo de selección de destino de implementación. El usuario selecciona las aplicaciones web y las colecciones de sitios donde se activará la característica. Vea la figura a continuación.

   **Destinos de implementación** 

![todo:imagen_alternativa_texto](installing-aspose-cells-for-sharepoint_3.png)




1.  Implemente la función en la granja de servidores.

   **Ejecutando instalación** 

![todo:imagen_alternativa_texto](installing-aspose-cells-for-sharepoint_4.png)




1. Active la función para las colecciones de sitios seleccionadas y configure sus aplicaciones web principales.
1.  Muestre una lista de aplicaciones web y colecciones de sitios donde se implementó y activó la función.

   **Instalación completa** 

![todo:imagen_alternativa_texto](installing-aspose-cells-for-sharepoint_5.png)
