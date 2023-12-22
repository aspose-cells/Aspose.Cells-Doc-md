---
title: Cómo evitar que los usuarios impriman archivos de Excel
type: docs
weight: 600
url: /es/net/how-to-prevent-printing-excel/
description: Aprenda cómo evitar que los usuarios impriman Excel a través del Aspose.Cells for .NET API.
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **Posibles escenarios de uso**
En nuestro trabajo diario, puede haber alguna información importante en el archivo excel, para proteger los datos internos difundidos, la empresa no nos permitirá imprimirlos. Este documento le indicará cómo evitar que otras personas impriman archivos de Excel.

##  **Cómo evitar que los usuarios impriman archivos en MS-Excel**
Puede aplicar el siguiente código VBA para proteger el archivo específico que desea imprimir.
1. Abra su libro de trabajo que no permite que otros impriman.
1. Seleccione la pestaña "Desarrollador" en la cinta de Excel y haga clic en el botón "Ver código" en la sección "Controles". Alternativamente, puede mantener presionadas las teclas ALT + F11 para abrir la ventana Microsoft Visual Basic para Aplicaciones.
<br>
<img src="1.png" width=70% />
1. Y luego, en el Explorador de proyectos de la izquierda, haga doble clic en ThisWorkbook para abrir el módulo y agregue algunos códigos vba.
<br>
<img src="2.png" width=70% />
1. Luego guarde y cierre este código, regrese al libro de trabajo y ahora, cuando imprima el archivo de muestra, no se permitirá imprimirlo y aparecerá el siguiente cuadro de advertencia:
<br>
<img src="3.png" width=70% />

##  **Cómo evitar que los usuarios impriman archivos de Excel usando Aspose.Cells for .NET**

El siguiente código de muestra ilustra cómo evitar que los usuarios impriman archivos de Excel:

1.  Carga el[archivo de muestra](sample.xlsx).
1. Obtenga el objeto VbaModuleCollection de la propiedad VbaProject del libro de trabajo.
1. Obtenga el objeto VbaModule a través del nombre "ThisWorkbook".
1. Establezca la propiedad de códigos de VbaModule.
1.  Guarde el archivo de muestra en[formato xlsm](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}