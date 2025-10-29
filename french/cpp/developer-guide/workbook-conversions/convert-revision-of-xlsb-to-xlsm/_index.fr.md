---
title: Convertir la révision de XLSB en XLSM avec C++
linktitle: Convertir la révision des XLSB en XLSM
type: docs
weight: 290
url: /fr/cpp/convert-revision-of-xlsb-to-xlsm/
description: Apprenez à convertir les révisions des fichiers XLSB en format XLSM en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}} 

Aspose.Cells prend désormais en charge la conversion complète des révisions des fichiers XLSB en fichiers XLSM. Les révisions se trouvent dans le chemin \xl\revisions. Vous pouvez les voir en changeant l'extension de votre fichier XLSB en ZIP. Le chemin \xl\revisions contient des fichiers se terminant par l'extension .bin.

Lorsque vous convertissez votre fichier XLSB en fichier XLSM à l'aide d'Aspose.Cells, ces fichiers .bin se convertissent avec succès en fichiers .xml, comme le montrent ces deux captures d'écran.

{{% /alert %}} 

L'exemple de code ci-dessous vous montre comment convertir le fichier XLSB en format XLSM en utilisant Aspose.Cells.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
