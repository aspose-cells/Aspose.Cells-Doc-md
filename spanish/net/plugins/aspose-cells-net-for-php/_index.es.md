---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /es/net/aspose-cells-net-for-php/
---

## **Empezando**

### **Introducción**

### **Requisitos del sistema y plataformas compatibles**

#### **Requisitos del sistema**

**A continuación se presentan los requisitos del sistema para usar Aspose.Cells .NET para PHP:**

- IIS con PHP y PHP Manager instalado.
- Aspose.Total APIs.
- Aspose.Cells, el archivo dll e tlb de Interop.

#### **Plataformas compatibles**

**A continuación se presentan las plataformas compatibles:**

- PHP 5.3 o superior
- Sistema operativo Windows

### **Descargar y Configurar**

#### **Descargar Bibliotecas Requeridas**

Descargar las bibliotecas requeridas mencionadas a continuación. Estas son necesarias para ejecutar ejemplos de Aspose.Cells Java para PHP.

- [Descargar archivos Aspose.Cells for .NET (DLL o MSI) desde la sección de descargas](https://downloads.aspose.com/cells/net)
- [Descargar Aspose.Cells for .NET interop dll](https://downloads.aspose.com/cells/net)

Si descarga la versión MSI, encontrará Aspose.Cells.dll en la ubicación instalada, que es C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 por defecto.
Sin embargo, en caso de que haya descargado la versión DLL, puede extraerla y luego copiar Aspose.Cells.dll desde la carpeta .NET 2.0 a su carpeta c:\temp para mayor comodidad de uso.
De manera similar, extraiga el archivo zip de Interop y copie Aspose.Inteop.dll a c:\temp

#### **Descargar Ejemplos de Sitios de Codificación Social**

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Cómo configurar el código fuente en la Plataforma Windows**

Por favor, siga estos sencillos pasos para abrir y extender el código fuente al usar:

##### **1. Registre tanto los archivos dll como interop.dll, por ejemplo Aspose.Cells.dll y Aspose.Cells.Interop.dll.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Habilitar las extensiones COM y DOTNET en PHP.**

En IIS, abra el Administrador de PHP y luego haga clic en 'Habilitar o deshabilitar y Extensión'. Encuentre php_com_dotnet.dll y asegúrese de que esté habilitado.

##### **3. Configurar Ejemplos de Aspose.Cells .NET para PHP**

###### **Método 1**

Clonar Ejemplos de PHP desde [github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
y ejecutar el siguiente comando

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **Método 2**

En el archivo composer.json de su proyecto PHP, agregue las siguientes líneas

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

y ejecute el comando de instalación

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **Soporte Ampliar y Contribuir**

#### **Soporte**

Desde los primeros días de Aspose, supimos que simplemente proporcionar buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que resulta cuando un problema técnico o una peculiaridad en el software le impide hacer lo que necesita. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquier persona que use nuestro producto, ya sea que los haya comprado o esté usando una evaluación, merece nuestra completa atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con Aspose.Cells .NET para PHP utilizando cualquiera de las siguientes plataformas:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Ampliar y Contribuir**

Aspose.Cells .NET para PHP es de código abierto y su código fuente está disponible en los principales sitios web de codificación social enumerados a continuación. Se anima a los desarrolladores a descargar el código fuente y contribuir sugiriendo o agregando nuevas funciones o mejorando las existentes, para que otros también puedan beneficiarse de él.

#### **Código Fuente**

Puede obtener el último código fuente en una de las siguientes ubicaciones

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Ejemplos de Código de Muestra**

Esta sección incluye los siguientes temas

- [Guía de Programadores de PHP](/cells/es/net/php-programmers-guide/)
  - [Trabajo con Archivos en PHP](/cells/es/net/working-with-files-in-php/)
    - [Funciones de Manipulación de Archivos en PHP](/cells/es/net/file-handling-features-in-php/)
      - [Apertura de Archivos en PHP](/cells/es/net/opening-files-in-php/)
      - [Guardado de Archivos en PHP](/cells/es/net/saving-files-in-php/)
    - [Funciones de Utilidad en PHP](/cells/es/net/utility-features-in-php/)
      - [Cifrado de Archivos en PHP](/cells/es/net/encrypting-files-in-php/)
      - [Conversión de Excel a PDF en PHP](/cells/es/net/excel-to-pdf-conversion-in-php/)
      - [Gestión de Propiedades de Documentos en PHP](/cells/es/net/managing-document-properties-in-php/)
      - [Conversión de Hoja de Cálculo a Imagen en PHP](/cells/es/net/worksheet-to-image-conversion-in-php/)
  - [Trabajo con Fórmulas en PHP](/cells/es/net/working-with-formulas-in-php/)
    - [Cálculo de Fórmulas en PHP](/cells/es/net/calculating-formulas-in-php/)
  - [Trabajo con Hojas de Cálculo en PHP](/cells/es/net/working-with-worksheets-in-php/)
    - [Funciones de Gestión en PHP](/cells/es/net/management-features-in-php/)
      - [Gestionar Hojas de Cálculo en PHP](/cells/es/net/managing-worksheets-in-php/)
        - [Agregar Hojas de Cálculo a Archivo de Excel Existente en PHP](/cells/es/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Agregar Hojas de Cálculo a Nuevo Archivo de Excel en PHP](/cells/es/net/add-worksheets-to-new-excel-file-in-php/)
        - [Eliminar Hojas de Cálculo Usando Índice de Hoja en PHP](/cells/es/net/removing-worksheets-using-sheet-index-in-php/)
        - [Eliminar Hojas de Cálculo Usando Nombre de Hoja en PHP](/cells/es/net/removing-worksheets-using-sheet-name-in-php/)
