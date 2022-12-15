---
title: Empezando
type: docs
weight: 10
url: /es/cpp/getting-started/
description: Cómo instalar Aspose Cells for C++ y crear una aplicación Hello World.
---
{{% alert color="primary" %}} 

Esta página le mostrará cómo instalar Aspose Cells for C++ y crear una aplicación Hello World.

{{% /alert %}}

## **Instalación**

### **Instalar Aspose Cells a NuGet**

NuGet es la forma más fácil de descargar e instalar Aspose.Cells for C++.
1. Cree un proyecto de Visual Studio Microsoft for C++.
2. Incluya el archivo de encabezado "Aspose.Cells.h".
3. Abra Microsoft Visual Studio y NuGet administrador de paquetes.
 4. Busque "aspose.cells.cpp" para encontrar el Aspose.Cells for C++ deseado.
5. Haga clic en "Instalar", Aspose.Cells for C++ se descargará y se hará referencia en su proyecto.

**![Instalar Aspose Cells a NuGet](Instalar a través deNuget.png)**

 También puede descargarlo desde la página web nuget para aspose.cells:
[Aspose.Cells for C++ NuGet Paquete](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Más pasos para detalles](/cells/es/cpp/installation/)

### **Una demostración para usar Aspose.Cells for C++ en Windows**

1. Descarga Aspose.Cells for C++ de la siguiente página:
[Descargar Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Descomprima el paquete y encontrará una demostración sobre cómo usar Aspose.Cells for C++.
3. Abra Demo.sln con Visual Studio 2017 o una versión superior
4. main.cpp: este archivo muestra cómo codificar para probar Aspose.Cells for C++
 5. sourceFile/resultFile: estas dos carpetas son directorios de almacenamiento utilizados en main.cpp

### **Cómo usar Aspose.Cells for C++ en el sistema operativo Linux**

1. Descarga Aspose.Cells for C++ de la siguiente página:
[Descargar Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. Descomprima el paquete y encontrará una demostración sobre cómo usar Aspose.Cells for C++ para Linux.
3. Ejecute "cd Demo" en su línea de comandos de Linux
4. Ejecute "rm -rf build;mkdir build;cd build"
5. Ejecute "cmake .." creará un Makefile por CMakeLists.txt en la carpeta Demo
6. Ejecute "make" para compilar
 7. Ejecute "./demo" verá el resultado

## **Creación de la aplicación Hello World**

Los pasos a continuación crean la aplicación Hello World usando el Aspose.Cells API:

1.  Crear una instancia de la[Libro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) clase.
1.  Si tiene una licencia, entonces[apliquelo](/cells/es/cpp/licensing/).
 Si está utilizando la versión de evaluación, omita las líneas de código relacionadas con la licencia.
1. Acceda a cualquier celda deseada de una hoja de trabajo en el archivo de Excel.
1. Inserta las palabras "**Hello World!**" en una celda a la que se accedió.
1. Genere el archivo de Excel Microsoft modificado.

La implementación de los pasos anteriores se demuestra en los siguientes ejemplos.

### **Ejemplo de código: creación de un nuevo libro de trabajo**

El siguiente ejemplo crea un nuevo libro de trabajo desde cero, inserta "**Hello World!**" en la celda A1 de la primera hoja de cálculo y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **Ejemplo de código: abrir un archivo existente**

El siguiente ejemplo abre un archivo de plantilla de Excel Microsoft existente, obtiene una celda y verifica el valor en la celda A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
