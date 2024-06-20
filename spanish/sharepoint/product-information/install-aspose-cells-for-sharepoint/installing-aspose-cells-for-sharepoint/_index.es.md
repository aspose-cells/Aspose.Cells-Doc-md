---
title: Instalando Aspose.Cells for SharePoint
type: docs
weight: 10
url: /es/sharepoint/installing-aspose-cells-for-sharepoint/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePoint se puede descargar como el archivo Aspose.Cells.SharePoint.zip. 

{{% /alert %}} 
### **Contenido del Archivo**
El archivo Aspose.Cells.SharePoint.zip contiene:

- Aspose.Cells.SharePoint.wsp – archivo de solución de SharePoint. Aspose.Cells for SharePoint está empaquetado como una solución de SharePoint para facilitar la implementación/retracción y la activación/desactivación de características en la granja de servidores.
- Aspose_LicenseAgreement.rtf – Contrato de licencia de usuario final
- Aspose.Cells for SharePoint.pdf – Documentación del usuario
- Aspose.Cells for SharePoint Documentation.chm – Documentación del usuario con referencia a la API pública
- setup.exe – Programa de configuración
- setup.exe.config – Archivo de configuración de la instalación

El programa de configuración verifica las siguientes condiciones antes de proceder con la instalación:

- WSS 3.0, MOSS 2007 o SharePoint 2010 está instalado.
- El usuario tiene permiso para instalar soluciones de SharePoint.
- La base de datos de SharePoint está en línea.
- El servicio de administración de WSS está iniciado.
- El servicio de temporizador de WSS está iniciado.

El servicio de administración de WSS y el servicio de temporizador son necesarios porque algunas acciones de configuración dependen de una tarea programada para propagarse a todos los servidores en la granja de servidores. 
#### **Para instalar Aspose.Cells for SharePoint**
1. Desempaquete Aspose.Cells.SharePoint zip en la unidad local del servidor MOSS 7.0 o WSS 3.0.
1. Ejecute setup.exe y siga las instrucciones en la pantalla.

El programa de configuración realiza las siguientes acciones:

1. Verificar los requisitos de instalación. La configuración no continuará si alguna verificación falla. 

   **Verificación del sistema** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




1. Mostrar el Contrato de Licencia de Usuario Final. El usuario debe aceptar el acuerdo para poder continuar. 

   **El CLUF** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1. Mostrar el cuadro de diálogo de selección del destino de implementación. El usuario selecciona las aplicaciones web y las colecciones de sitios en las que se activará la característica. Consulte la figura a continuación. 

   **Destinos de implementación** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1. Implementar la característica en la granja de servidores. 

   **Instalación en ejecución** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. Activar la característica para las colecciones de sitios seleccionadas y configurar sus aplicaciones web principales.
1. Mostrar una lista de aplicaciones web y colecciones de sitios donde se implementó y activó la característica. 

   **Instalación completa** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
