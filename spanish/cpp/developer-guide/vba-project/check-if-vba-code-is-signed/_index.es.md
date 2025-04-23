---  
title: Verifica si el código VBA está firmado con C++  
linktitle: Verifique si el Código VBA está firmado  
type: docs  
weight: 100  
url: /es/cpp/check-if-vba-code-is-signed/  
description: Aprende cómo verificar si el código VBA en archivos Excel está firmado usando Aspose.Cells con C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells permite al usuario verificar si el proyecto de código VBA está firmado o no. Usa la propiedad [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) para verificar si el proyecto está firmado o no.  

{{% /alert %}}  

El siguiente código explica cómo verificar si el código VBA está firmado usando la propiedad [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/). Puedes usar cualquiera de tus archivos de Excel para probar este código. Para fines de prueba, puedes usar [este archivo de Excel usado en el código](5115032.xlsm).  

## **Verifica si el código VBA está firmado en C++**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## Salida de la consola  

A continuación se muestra la salida de consola del código anterior utilizando el [archivo excel de muestra](5115032.xlsm) proporcionado por el enlace.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
