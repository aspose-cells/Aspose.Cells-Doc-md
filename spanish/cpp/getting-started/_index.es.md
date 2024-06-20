---
title: Empezando
type: docs
weight: 10
url: /es/cpp/getting-started/
description: Cómo instalar Aspose Cells para C++ y crear una aplicación Hello World.
---

{{% alert color="primary" %}} 

Esta página te mostrará cómo instalar Aspose Cells para C++ y crear una aplicación Hello World.

{{% /alert %}}

## **Instalación**

### **Instala Aspose Cells a través de NuGet**

NuGet es la forma más fácil de descargar e instalar Aspose.Cells for C++. 
1. Crea un proyecto de Microsoft Visual Studio para C++.
2. Incluye el archivo de encabezado "Aspose.Cells.h".
3. Abre Microsoft Visual Studio y el administrador de paquetes NuGet.
4. Busque "aspose.cells.cpp" para encontrar el Aspose.Cells for C++ deseado. 
5. Haga clic en "Instalar", se descargará y hará referencia en su proyecto al Aspose.Cells for C++.

**![Instalar Aspose Cells a través de NuGet](InstallThroughNuget.png)**

También puedes descargarlo desde la página web de nuget para aspose.cells: 
[Paquete NuGet Aspose.Cells for C++](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Más pasos para detalles](/cells/es/cpp/installation/)

### **Una demostración para usar Aspose.Cells for C++ en Windows**

1. Descargue Aspose.Cells for C++ desde la siguiente página:
[Descargar Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Descomprima el paquete y encontrará un ejemplo sobre cómo usar Aspose.Cells for C++.
3. Abra el ejemplo.sln con Visual Studio 2017 o una versión superior
4. main.cpp: este archivo muestra cómo codificar para probar Aspose.Cells for C++

### **Una demostración para usar Aspose.Cells for C++ en Linux**

1. Descargue Aspose.Cells for C++ desde la siguiente página:
[Descargar Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. Descomprima el paquete y encontrará un ejemplo sobre cómo usar Aspose.Cells for C++ para Linux.
3. Asegúrese de estar en la carpeta donde se encuentra el ejemplo.
4. Ejecute "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Ejecute "cmake --build example/build"

### **Una demostración para usar Aspose.Cells for C++ en Mac OS**

1. Descargue Aspose.Cells for C++ desde la siguiente página:
[Descargar Aspose.Cells for C++(MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Descomprima el paquete y encontrará un ejemplo que muestra cómo utilizar Aspose.Cells for C++ en MacOS.
3. Asegúrese de estar en la carpeta donde se encuentra el ejemplo.
4. Ejecute "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Ejecute "cmake --build example/build"

## **Creación de la aplicación Hola Mundo**

Los siguientes pasos crean la aplicación Hola Mundo utilizando la API de Aspose.Cells:

1. Cree una instancia de la clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)
1. Si tiene una licencia, entonces [aplíquela](/cells/es/cpp/licensing/)
   Si estás usando la versión de evaluación, omite las líneas de código relacionadas con la licencia.
1. Accede a cualquier celda deseada de una hoja de cálculo en el archivo de Excel.
1. Inserte las palabras "**¡Hola Mundo!**" en una celda accedida.
1. Genere el archivo modificado de Microsoft Excel.

La implementación de los pasos anteriores se muestra en los ejemplos a continuación.

### **Ejemplo de código: Crear un nuevo libro de trabajo**

El siguiente ejemplo crea un nuevo libro desde cero, inserta "**¡Hola Mundo!**" en la celda A1 de la primera hoja de cálculo y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **Ejemplo de código: Abrir un archivo existente**

El siguiente ejemplo abre un archivo de plantilla de Microsoft Excel existente, obtiene una celda y verifica el valor en la celda A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
