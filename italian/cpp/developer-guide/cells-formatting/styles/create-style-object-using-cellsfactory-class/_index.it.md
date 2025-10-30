---  
title: Creare un oggetto Style usando la classe CellsFactory con C++  
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo che fornisce un oggetto stile per stilizzare le celle. Questo articolo introdurrà come creare un oggetto stile della cella usando la classe CellsFactory nella libreria Aspose.Cells in modo che gli utenti possano personalizzare l aspetto delle celle secondo le proprie esigenze.  
keywords: Aspose.Cells, libreria C++, foglio di calcolo elettronico, oggetto stile, stile cella, personalizzazione  
type: docs  
weight: 70  
url: /it/cpp/create-style-object-using-cellsfactory-class/  
---  

## **Crea un oggetto Style utilizzando la classe CellsFactory**  
Il seguente esempio di codice crea un oggetto [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) usando la classe [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory) e quindi imposta lo stile predefinito del workbook. Scarica il [file excel di output](5115153.xlsx) per vedere i risultati di questo codice di riferimento.  

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

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
