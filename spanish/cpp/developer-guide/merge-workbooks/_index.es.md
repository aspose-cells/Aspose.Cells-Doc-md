---
title: Combinar múltiples libros de trabajo en uno solo con C++
linktitle: Combinar libros de trabajo
type: docs
weight: 66
url: /es/cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aprenda cómo combinar múltiples libros de trabajo en uno solo usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, necesitas combinar libros de trabajo con diferentes contenidos, como imágenes, gráficos y datos, en un solo libro de trabajo. Aspose.Cells soporta esta función. Este artículo muestra cómo crear una aplicación de consola en Visual Studio y combinar libros de trabajo con unas pocas líneas de código usando Aspose.Cells.

{{% /alert %}}

## **Combinar libros de trabajo con imágenes y gráficos**

El código de ejemplo combina dos libros de trabajo en un único libro utilizando Aspose.Cells. El código carga los libros de trabajo de origen, utiliza el método [**Workbook::Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) para combinarlos y guarda el libro de trabajo de salida.

### **Libros de trabajo de origen**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Libros de trabajo de salida**

- [combined.xlsx](5473095.xlsx)

### **Capturas de pantalla**

A continuación se muestran capturas de pantalla de los libros de trabajo de origen y de salida.

{{% alert color="primary" %}}

Puede utilizar cualquier libro de trabajo de origen. Estas imágenes son solo con fines ilustrativos.

{{% /alert %}}

**La primera hoja de cálculo del libro de trabajo de gráficos: apilada** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Segunda hoja de cálculo del libro de trabajo de gráficos: línea** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primera hoja de cálculo del libro de trabajo de imagen: imagen** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Las tres hojas de cálculo en el libro de trabajo combinado: apilada, línea, imagen** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

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

    // Path of the first source excel file
    U16String sourceFile1 = srcDir + u"SampleChart.xlsx";

    // Path of the second source excel file
    U16String sourceFile2 = srcDir + u"SampleImage.xlsx";

    // Open the first excel file.
    Workbook sourceBook1(sourceFile1);

    // Open the second excel file.
    Workbook sourceBook2(sourceFile2);

    // Combining the two workbooks
    sourceBook1.Combine(sourceBook2);

    // Define the output file path
    U16String outputFilePath = srcDir + u"Combined.out.xlsx";

    // Save the target book file.
    sourceBook1.Save(outputFilePath);

    std::cout << "Workbooks combined and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Combinar múltiples hojas de cálculo en una sola hoja de cálculo](/cells/es/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionar archivos](/cells/es/cpp/merge-files/)
