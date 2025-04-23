---  
title: Cómo prevenir que los usuarios impriman archivos Excel con C++  
linktitle: Cómo Prevenir que los Usuarios Impriman un Archivo de Excel  
type: docs  
weight: 600  
url: /es/cpp/how-to-prevent-printing-excel/  
description: Aprenda cómo prevenir que los usuarios impriman Excel mediante la API Aspose.Cells for C++.  
keywords: impresión de excel, evitar la impresión de excel, cómo evitar que los usuarios impriman excel, excel evitar impresión, evitar impresión del libro de trabajo, Evitar que los usuarios impriman el libro completo con VBA.  
---  

## **Escenarios de uso posibles**  
En nuestro trabajo diario, puede haber información importante en el archivo de Excel; para proteger los datos internos de la difusión, la empresa no nos permitirá imprimirlos. Este documento le dirá cómo evitar que otros impriman archivos de Excel.  

## **Cómo evitar que los usuarios impriman archivos en MS-Excel**  
Puede aplicar el siguiente código VBA para proteger su archivo específico de ser impreso.  
1. Abra su libro de trabajo que no permite que otros lo impriman.  
1. Seleccione la pestaña "Desarrollador" en la cinta de opciones de Excel y haga clic en el botón "Ver código" en la sección "Controles". Alternativamente, puede mantener presionadas las teclas ALT + F11 para abrir la ventana de Microsoft Visual Basic para Aplicaciones.  
<br>  
<img src="1.png" width=70% />  
1. Luego, en el Explorador de proyectos de la izquierda, doble clic en ThisWorkbook para abrir el módulo y agregar algunos códigos VBA.  
<br>  
<img src="2.png" width=70% />  
1. Luego, guarde y cierre este código, regrese al libro en blanco, y ahora cuando imprima el archivo de muestra, no se permitirá imprimir, y recibirá el siguiente cuadro de advertencia:  
<br>  
<img src="3.png" width=70% />  

## **Cómo prevenir que los usuarios impriman archivos Excel usando Aspose.Cells for C++**  

El siguiente código de muestra ilustra cómo prevenir que los usuarios impriman un archivo de Excel:  

1. Cargar el [archivo de muestra](sample.xlsx).  
1. Obtenga el objeto VbaModuleCollection desde la propiedad VbaProject del libro.  
1. Obtenga el objeto VbaModule mediante el nombre "ThisWorkbook".  
1. Establezca la propiedad de códigos de VbaModule.  
1. Guarde el archivo de muestra en [formato xlsm](out.xlsm).  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook from existing Excel file
    Workbook workbook(u"Sample.xlsx");

    // Access VBA project modules
    VbaModuleCollection modules = workbook.GetVbaProject().GetModules();

    // Set VBA code for 'ThisWorkbook' module
    modules.Get(u"ThisWorkbook").SetCodes(u"Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

    // Save the workbook as macro-enabled Excel file
    workbook.Save(u"out.xlsm");

    std::cout << "VBA code added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
