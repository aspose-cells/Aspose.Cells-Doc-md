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

##  **Instalación**

###  **Instalar Aspose Cells a NuGet**

 NuGet es la forma más sencilla de descargar e instalar Aspose.Cells for C++.
1. Cree un proyecto de Visual Studio Microsoft for C++.
2. Incluya el archivo de encabezado "Aspose.Cells.h".
3. Abra Microsoft Visual Studio y el administrador de paquetes NuGet.
 4. Busque "aspose.cells.cpp" para encontrar el Aspose.Cells for C++ deseado.
5. Haga clic en "Instalar", se descargará Aspose.Cells for C++ y se hará referencia a él en su proyecto.

**![Instalar Aspose Cells a NuGet](InstallThroughNuget.png)**

 También puedes descargarlo desde la página web nuget para aspose.cells:
[Aspose.Cells for C++ NuGet Paquete](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Más pasos para más detalles](/cells/es/cpp/installation/)

###  **Una demostración para usar Aspose.Cells for C++ en Windows**

1. Descarga Aspose.Cells for C++ de la siguiente página:
[Descargar Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Descomprima el paquete y encontrará un ejemplo sobre cómo utilizar Aspose.Cells for C++.
3. Abra el archivo example.sln con Visual Studio 2017 o una versión superior.
4. main.cpp: este archivo muestra cómo codificar para probar Aspose.Cells for C++

###  **Una demostración para usar Aspose.Cells for C++ en Linux**

1. Descarga Aspose.Cells for C++ de la siguiente página:
[Descargar Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. Descomprima el paquete y encontrará un ejemplo sobre cómo usar Aspose.Cells for C++ para Linux.
3. Asegúrate de estar en la ruta donde se encuentra el ejemplo.
4. Ejecute "cmake -S ejemplo -B ejemplo/compilación -DCMAKE_BUILD_TYPE=Release"
5. Ejecute "cmake --build ejemplo/build"

###  **Una demostración para usar Aspose.Cells for C++ en Mac OS**

1. Descarga Aspose.Cells for C++ de la siguiente página:
[Descargar Aspose.Cells for C++ (MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Descomprima el paquete y encontrará un ejemplo sobre cómo usar Aspose.Cells for C++ para MacOS.
3. Asegúrate de estar en la ruta donde se encuentra el ejemplo.
4. Ejecute "cmake -S ejemplo -B ejemplo/compilación -DCMAKE_BUILD_TYPE=Release"
5. Ejecute "cmake --build ejemplo/build"

##  **Creando la aplicación Hello World**

Los pasos siguientes crean la aplicación Hello World utilizando Aspose.Cells API:

1.  Crear una instancia del[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) clase.
1.  Si tiene una licencia, entonces[apliquelo](/cells/es/cpp/licensing/).
 Si está utilizando la versión de evaluación, omita las líneas de código relacionadas con la licencia.
1. Acceda a cualquier celda deseada de una hoja de trabajo en el archivo de Excel.
1. Inserte las palabras "**Hello World!**" en una celda a la que acceda.
1. Genere el archivo Excel Microsoft modificado.

La implementación de los pasos anteriores se demuestra en los ejemplos siguientes.

###  **Ejemplo de código: creación de un nuevo libro de trabajo**

El siguiente ejemplo crea un nuevo libro desde cero, inserta "**Hello World!**" en la celda A1 de la primera hoja de cálculo y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

###  **Ejemplo de código: abrir un archivo existente**

El siguiente ejemplo abre un archivo de plantilla de Excel Microsoft existente, obtiene una celda y verifica el valor en la celda A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
