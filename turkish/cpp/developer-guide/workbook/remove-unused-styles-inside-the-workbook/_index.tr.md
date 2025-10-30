---  
title: Çalışma Kitabındaki Kullanılmayan Stilleri C++ ile Kaldırın  
linktitle: Çalışma Kitabı İçinde Kullanılmayan Stilleri Kaldırma  
type: docs  
weight: 340  
url: /tr/cpp/remove-unused-styles-inside-the-workbook/  
description: Aspose.Cells kullanarak C++ ile Excel çalışma kitabındaki kullanılmayan stilleri kaldırın.  
---  

{{% alert color="primary" %}}  

Excel dosyalarındaki kullanılmayan stiller sadece yer kaplamaz, aynı zamanda PDF, HTML vb. farklı formatlara dönüştürürken performans sorunlarına da neden olur. Aspose.Cells, çalışma kitabındaki tüm kullanılmayan stilleri kaldırmanızı sağlayan [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) sağlar.  

{{% /alert %}}  

Aşağıdaki kod, [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) kullanımını açıklar. Kod, sağlanan bağlantıdan indirilebilecek şablon Excel dosyasını yükler. Bu dosyada **AsposeStyle** adlı kullanılmayan bir stil bulunmaktadır; bu stil ve diğer tüm kullanılmayan stiller, kod yürütüldükten sonra kaldırılacaktır.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
