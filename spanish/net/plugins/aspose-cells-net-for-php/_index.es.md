---
title: Aspose.Cells .NET para PHP
type: docs
weight: 40
url: /es/net/aspose-cells-net-for-php/
---
## **Empezando**

### **Introducción**

### **Requisitos del sistema y plataformas compatibles**

#### **Requisitos del sistema**

**Los siguientes son los requisitos del sistema para usar Aspose.Cells .NET para PHP:**

- IIS con PHP y PHP Manager instalado.
- Aspose.Total API.
- Aspose.Cells el archivo Interop dll y tlb.

#### **Plataformas compatibles**

**Las siguientes son las plataformas compatibles:**

- PHP 5.3 o superior
- Windows sistema operativo

### **Descargar y configurar**

#### **Descargar bibliotecas requeridas**

Descargue las bibliotecas necesarias que se mencionan a continuación. Estos son los necesarios para ejecutar Aspose.Cells Java para ejemplos de PHP.

- [Descargue los archivos Aspose.Cells for .NET (DLL o MSI) de la sección de descargas](https://downloads.aspose.com/cells/net)
- [Descargar Aspose.Cells for .NET dll de interoperabilidad](https://downloads.aspose.com/cells/net)

Si descarga la versión MSI, encontrará Aspose.Cells.dll en la ubicación instalada, que es la carpeta C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 de forma predeterminada.
Sin embargo, en caso de que haya descargado la versión DLL, puede extraerla y luego copiar Aspose.Cells.dll de la carpeta .NET 2.0 a su carpeta c:\temp para facilitar su uso.
Del mismo modo, extraiga el archivo zip de interoperabilidad y copie Aspose.Inteop.dll en c:\temp

#### **Descargar ejemplos de sitios de codificación social**

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

-----

##### **GitHub**

- **Aspose.Cells .NET para ejemplos de PHP**

  - [Aspose.Cells .NET para PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Cómo configurar el código fuente en la plataforma Windows**

Siga estos sencillos pasos para abrir y ampliar el código fuente mientras usa:

##### **1. Registre los archivos dll e interop.dll, por ejemplo, Aspose.Cells.dll y Aspose.Cells.Interop.dll.**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Habilite las extensiones COM y DOTNET en PHP.**

En IIS, abra PHP Manager y luego haga clic en 'Habilitar para deshabilitar y extensión'. encontrar php_com_dotnet.dll y asegúrese de que esté habilitado.

##### **3. Configure Aspose.Cells .NET para ejemplos de PHP**

###### **Método 1**

 Clonar ejemplos de PHP de[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
y ejecuta el siguiente comando

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **Método 2**

En el archivo composer.json de su proyecto PHP, agregue las siguientes líneas

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

y ejecuta el comando de instalación

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

 Para leer sobre el compositor visita<https://getcomposer.org/>

### **Apoyar Extender y Contribuir**

#### **Apoyo**

Desde los primeros días de Aspose, sabíamos que solo dar buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software le impiden hacer lo que debe hacer. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquiera que use nuestro producto, ya sea que lo haya comprado o esté usando una evaluación, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con Aspose.Cells .NET para PHP utilizando cualquiera de las siguientes plataformas:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Extender y contribuir**

Aspose.Cells .NET para PHP es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se alienta a los desarrolladores a descargar el código fuente y contribuir sugiriendo o agregando nuevas funciones o mejorando las existentes, para que otros también puedan beneficiarse de ellas.

#### **Código fuente**

Puede obtener el código fuente más reciente de una de las siguientes ubicaciones

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Ejemplos de código de muestra**

Esta sección incluye los siguientes temas

- [Guía de programadores de PHP](/cells/es/net/php-programmers-guide/)
  - [Trabajar con archivos en PHP](/cells/es/net/working-with-files-in-php/)
    - [Funciones de manejo de archivos en PHP](/cells/es/net/file-handling-features-in-php/)
      - [Abrir archivos en PHP](/cells/es/net/opening-files-in-php/)
      - [Guardar archivos en PHP](/cells/es/net/saving-files-in-php/)
    - [Funciones de utilidad en PHP](/cells/es/net/utility-features-in-php/)
      - [Cifrado de archivos en PHP](/cells/es/net/encrypting-files-in-php/)
      - [Conversión de Excel a PDF en PHP](/cells/es/net/excel-to-pdf-conversion-in-php/)
      - [Gestión de propiedades de documentos en PHP](/cells/es/net/managing-document-properties-in-php/)
      - [Conversión de hoja de trabajo a imagen en PHP](/cells/es/net/worksheet-to-image-conversion-in-php/)
  - [Trabajar con fórmulas en PHP](/cells/es/net/working-with-formulas-in-php/)
    - [Cálculo de fórmulas en PHP](/cells/es/net/calculating-formulas-in-php/)
  - [Trabajar con hojas de trabajo en PHP](/cells/es/net/working-with-worksheets-in-php/)
    - [Funciones de gestión en PHP](/cells/es/net/management-features-in-php/)
      - [Manejo de hojas de trabajo en PHP](/cells/es/net/managing-worksheets-in-php/)
        - [Agregue hojas de trabajo a un archivo de Excel existente en PHP](/cells/es/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Agregar hojas de trabajo a un nuevo archivo de Excel en PHP](/cells/es/net/add-worksheets-to-new-excel-file-in-php/)
        - [Eliminar hojas de trabajo usando el índice de hojas en PHP](/cells/es/net/removing-worksheets-using-sheet-index-in-php/)
        - [Eliminar hojas de trabajo usando el nombre de la hoja en PHP](/cells/es/net/removing-worksheets-using-sheet-name-in-php/)
