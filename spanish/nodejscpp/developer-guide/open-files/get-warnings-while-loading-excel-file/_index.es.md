---
title: Obtener advertencias al cargar archivo de Excel con Node.js vía C++
linktitle: Obtener advertencias al cargar archivo de Excel
type: docs
weight: 110
url: /es/nodejs-cpp/get-warnings-while-loading-excel-file/
description: Aprenda cómo capturar advertencias al cargar un archivo de Excel usando Aspose.Cells for Node.js via C++. Maneje eficazmente libros de trabajo corruptos pero cargables.
---

## **Escenarios de uso posibles**

A veces, el usuario intenta cargar un libro de trabajo que está algo corrupto pero es cargable. En tales casos, Aspose.Cells genera advertencias al cargar el libro. Puede capturar estas advertencias implementando la interfaz [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback) y configurando la propiedad [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--).

## **Obtener advertencias al cargar archivo de Excel**

El siguiente código de ejemplo explica cómo obtener advertencias al cargar un archivo de Excel. El código carga el [archivo de Excel de muestra](sampleDuplicateDefinedName.xlsx) que genera una advertencia [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype) al cargar. Esta advertencia se captura mediante el método [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-) que imprime los mensajes de advertencia en la consola. Luego, guarda el libro en el [archivo de Excel de salida](outputDuplicateDefinedName.xlsx). Si abre el archivo de Excel de muestra en Microsoft Excel, también mostrará esta advertencia como se muestra en esta captura de pantalla. También puede revisar la salida en la consola del código a continuación para mayor comprensión.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **Salida de la consola**

Aquí está la salida de la consola del código anterior cuando se ejecuta con el [archivo de Excel de muestra proporcionado](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
