---  
title: CellsFactory sınıfını kullanarak C++ ile Stil nesnesi oluşturma  
description: Aspose.Cells, hücreleri biçimlendirmek için stil nesnesi sağlayan bir C++ kütüphanesidir. Bu makale, kullanıcıların ihtiyaçlarına göre hücrelerin görünümünü özelleştirmelerine olanak tanımak amacıyla Aspose.Cells kütüphanesindeki CellsFactory sınıfını kullanarak hücre stili nesnesi nasıl oluşturulacağını tanıtacaktır.  
keywords: Aspose.Cells, C++ kütüphanesi, elektronik elektronik tablo, stil nesnesi, hücre stili, özelleştirme  
type: docs  
weight: 70  
url: /tr/cpp/create-style-object-using-cellsfactory-class/  
---  

## **CellsFactory sınıfını kullanarak Stil nesnesi oluşturma**  
Aşağıdaki örnek kod, [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory) sınıfını kullanarak [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) nesnesi oluşturur ve ardından çalışma kitabının Varsayılan Stilini ayarlar. Lütfen bu kodun sonuçlarını görmek için [çıktı Excel dosyasını](5115153.xlsx) indiriniz.  

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
