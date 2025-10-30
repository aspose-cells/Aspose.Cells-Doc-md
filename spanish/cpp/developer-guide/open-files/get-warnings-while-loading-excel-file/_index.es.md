---
title: Obtener advertencias al cargar archivos de Excel con C++
linktitle: Obtener advertencias al cargar archivo de Excel
type: docs
weight: 110
url: /es/cpp/get-warnings-while-loading-excel-file/
description: Aprenda cómo capturar y manejar advertencias al cargar archivos de Excel usando el Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

A veces, el usuario intenta cargar un libro de trabajo que está algo corrupto pero aún cargable. En tales casos, Aspose.Cells genera advertencias al cargar el libro. Puede capturar estas advertencias implementando la interfaz [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/) y configurando la propiedad [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/).

## **Obtener advertencias al cargar archivo de Excel**

El siguiente código de ejemplo explica cómo obtener advertencias al cargar un archivo de Excel. El código carga el [archivo de Excel de muestra](sampleDuplicateDefinedName.xlsx), que genera una advertencia [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/) al cargar. Esta advertencia es posteriormente capturada por el método [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/), que imprime los mensajes de advertencia en la consola. Luego, el código guarda el libro en un [archivo de Excel de salida](outputDuplicateDefinedName.xlsx). Si abre el archivo de Excel de muestra en Microsoft Excel, también mostrará esta advertencia, como se muestra en la captura de pantalla a continuación. Por favor, revise también la salida de la consola del código a continuación para mayor comprensión.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class WarningCallback : public IWarningCallback {
public:
    void Warning(WarningInfo& warningInfo) override {
        if (warningInfo.GetType() == ExceptionType::DefinedName) {
            std::cout << "Defined Name Warning: " << warningInfo.GetDescription().ToUtf8() << std::endl;
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    LoadOptions options;
    WarningCallback callback;
    options.SetWarningCallback(&callback);

    U16String inputFilePath = srcDir + u"sampleDuplicateDefinedName.xlsx";
    Workbook book(inputFilePath, options);

    U16String outputFilePath = outDir + u"outputDuplicateDefinedName.xlsx";
    book.Save(outputFilePath);

    std::cout << "Workbook saved successfully with warning handling!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**

Aquí está la salida de la consola del código anterior cuando se ejecuta con el [archivo de Excel de muestra proporcionado](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
