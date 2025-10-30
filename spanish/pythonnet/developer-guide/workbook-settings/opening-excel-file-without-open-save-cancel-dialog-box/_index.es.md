---
title: Abrir archivo de Excel sin mostrar el cuadro de diálogo de Abrir Guardar Cancelar
type: docs
weight: 150
url: /es/python-net/opening-excel-file-without-open-save-cancel-dialog-box/
---

{{% alert color="primary" %}} 

Este documento explica cómo abrir un archivo de Microsoft Excel en un navegador sin mostrar el cuadro de diálogo Abrir-Guardar-Cancelar. 

Cabe señalar aquí que la restricción de seguridad que no permite la descarga directa de un archivo es impuesta por Microsoft (u otros proveedores de navegadores), no por Aspose. Se impone para bloquear y restringir la descarga de archivos potencialmente dañinos a las máquinas locales. 

Es arriesgado para el sistema local del cliente permitir la descarga sin mostrar el cuadro de diálogo Abrir-Guardar-Cancelar para solicitar la descarga. No hay opción o solución disponible desde Aspose ya que sería un riesgo de seguridad muy grande.

{{% /alert %}} 
## **¿Por qué es un riesgo de seguridad?**
La siguiente imagen muestra el cuadro de diálogo Abrir-Guardar-Cancelar mostrado por Internet Explorer al intentar descargar un archivo.

|**El cuadro de diálogo Abrir-Guardar-Cancelar**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
Como se explicó anteriormente, permitir que un archivo se abra o se ejecute en tu sistema sin confirmar que realmente lo deseas es un riesgo de seguridad. Algunos archivos contienen virus y algunos sitios intentarán descargar archivos dañinos a tu máquina sin preguntarte. Por lo tanto, no se recomienda permitir la descarga de archivos sin el aviso de descarga para que los usuarios tengan que verificar el archivo y su origen antes de descargarlo o ejecutarlo. Deshabilitar el cuadro de diálogo de descarga hace que el sistema sea vulnerable a virus, troyanos y hackers que puedan afectar silenciosamente tu sistema. 
## **Abrir un archivo sin el cuadro de diálogo Abrir-Guardar-Cancelar**
Si bien es una gran preocupación de seguridad, Microsoft todavía proporciona configuraciones de Internet Explorer que permiten a los usuarios deshabilitar el aviso Abrir-Guardar-Cancelar para la descarga de archivos. 

En el Explorador de Windows:

1. En el menú **Herramientas**, selecciona **Opciones de carpeta**.
1. Haz clic en la pestaña Tipos de archivo en el cuadro de diálogo Opciones de carpeta.
1. Selecciona el tipo de archivo de extensión XLS.
1. Haz clic en **Avanzado**. 
   Se muestra un cuadro de diálogo. Tiene tres opciones en la parte inferior.
1. Desmarcar **Confirmar abrir después de la descarga**.
1. Seleccione la tercera opción - **Navegar en la misma ventana** - para ver el archivo de Excel en Internet Explorer sin iniciar Microsoft Excel de forma independiente. 

|**Opciones de tipo de archivo**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
Esta configuración permite que los archivos se ejecuten directamente en el navegador web, sin que se muestre el cuadro de diálogo Abrir-Guardar-Cancelar al descargar o abrir el archivo.

{{< app/cells/assistant language="python-net" >}}
