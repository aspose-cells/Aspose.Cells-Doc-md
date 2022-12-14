---
title: Abrir un archivo de Excel sin abrir el cuadro de diálogo Guardar Cancelar
type: docs
weight: 150
url: /es/net/opening-excel-file-without-open-save-cancel-dialog-box/
---
{{% alert color="primary" %}} 

Este documento explica cómo abrir un archivo de Excel Microsoft en un navegador sin mostrar el cuadro de diálogo Abrir-Guardar-Cancelar.

 Cabe señalar aquí que la restricción de seguridad que no permite la descarga directa de un archivo es aplicada por Microsoft (u otros proveedores de navegadores), no por Aspose. Se impone para bloquear y restringir la descarga de archivos potencialmente dañinos a las máquinas locales. .

Es arriesgado que el sistema local del cliente permita la descarga sin mostrar el cuadro de diálogo Abrir-Guardar-Cancelar para solicitar la descarga. No hay ninguna opción o solución alternativa disponible desde Aspose, ya que será un riesgo de seguridad muy grande.

{{% /alert %}} 
## **¿Por qué un riesgo de seguridad?**
La siguiente imagen muestra el cuadro de diálogo Abrir-Guardar-Cancelar que muestra Internet Explorer al intentar descargar un archivo.

|**El cuadro de diálogo Abrir-Guardar-Cancelar**|
|:- |
|![todo:imagen_alternativa_texto](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
Como se explicó anteriormente, permitir que un archivo se abra o se ejecute en su sistema sin confirmar que realmente lo desea es un riesgo de seguridad. Algunos archivos contienen virus y algunos sitios intentarán descargar archivos dañinos a su máquina sin avisarle. Por lo tanto, no se recomienda que permita la descarga de archivos sin el aviso de descarga para que los usuarios tengan que verificar el archivo y su fuente pueda verificarse antes de descargarlo o ejecutarlo. Deshabilitar el cuadro de diálogo de descarga hace que el sistema sea vulnerable a virus, troyanos y piratas informáticos que pueden afectar su sistema de forma silenciosa.
## **Abrir un archivo sin el cuadro de diálogo Abrir-Guardar-Cancelar**
 Si bien es un gran problema de seguridad, Microsoft aún proporciona configuraciones de Internet Explorer que permiten a los usuarios deshabilitar el mensaje Abrir-Guardar-Cancelar para la descarga de archivos.

En Windows Explorador:

1.  Sobre el**Instrumentos** menú, seleccione**Opciones de carpeta**.
1. Haga clic en la pestaña Tipos de archivo en el cuadro de diálogo Opciones de carpeta.
1. Seleccione el tipo de archivo de extensión XLS.
1.  Hacer clic**Avanzado**. 
Se muestra un cuadro de diálogo. Tiene tres opciones en la parte inferior.
1.  Desmarcar**Confirmar apertura después de la descarga**.
1.  Seleccione la tercera opción -**Navegar en la misma ventana** - para ver el archivo de Excel en Internet Explorer sin iniciar Microsoft Excel independiente.

|**Editar opciones de tipo de archivo**|
|:- |
|![todo:imagen_alternativa_texto](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
Esta configuración permite que los archivos se ejecuten directamente en el navegador web, sin que se muestre el cuadro de diálogo Abrir-Guardar-Cancelar al descargar o abrir el archivo.
