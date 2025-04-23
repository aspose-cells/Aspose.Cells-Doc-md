---
title: Cómo Prevenir que los Usuarios Impriman un Archivo de Excel
type: docs
weight: 600
url: /es/net/how-to-prevent-printing-excel/
description: Aprende cómo evitar que los usuarios impriman Excel a través de la API Aspose.Cells for .NET.
keywords: impresión de excel, evitar la impresión de excel, cómo evitar que los usuarios impriman excel, excel evitar impresión, evitar impresión del libro de trabajo, Evitar que los usuarios impriman el libro completo con VBA. 
---

## **Escenarios de uso posibles**
En nuestro trabajo diario, puede haber información importante en el archivo de Excel; para proteger la difusión interna de datos, la empresa no nos permitirá imprimirlos. Este documento le dirá cómo evitar que otros impriman archivos de Excel.

## **Cómo evitar que los usuarios impriman archivos en MS-Excel**
Puede aplicar el siguiente código VBA para proteger su archivo específico para que no se imprima.
1. Abra su libro de trabajo que no permite que otros lo impriman.
1. Seleccione la pestaña "Desarrollador" en la cinta de Excel y haga clic en el botón "Ver código" en la sección "Controles". Alternativamente, puede presionar las teclas ALT + F11 para abrir la ventana de Microsoft Visual Basic for Applications.
<br>
<img src="1.png" width=70% />
1. Y luego en el Explorador de proyectos izquierdo, haga doble clic en ThisWorkbook para abrir el módulo y agregar algunos códigos VBA.
<br>
<img src="2.png" width=70% />
1. Luego, guarde y cierre este código, vuelva al libro de trabajo y ahora cuando imprima el archivo de muestra, no estará permitido imprimirlo y recibirá el siguiente cuadro de advertencia:
<br>
<img src="3.png" width=70% />

## **Cómo evitar que los usuarios impriman archivos de Excel usando Aspose.Cells for .NET**

El siguiente código de muestra ilustra cómo evitar que los usuarios impriman un archivo de excel

1. Cargar el [archivo de muestra](sample.xlsx).
1. Obtenga el objeto VbaModuleCollection desde la propiedad VbaProject del Libro.
1. Obtenga el objeto VbaModule a través del nombre "ThisWorkbook".
1. Establezca la propiedad de códigos de VbaModule.
1. Guarde el archivo de muestra en [formato xlsm](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
