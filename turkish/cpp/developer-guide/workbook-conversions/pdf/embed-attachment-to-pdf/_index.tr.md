---
title: C++ ile PDF ye Ek Dosya Gölgelendirme
linktitle: Ekli Dosya Ekle PDF ye
type: docs
weight: 380
url: /tr/cpp/embed-attachment-to-pdf/
description: Aspose.Cells kullanarak C++ ile PDF ye ek dosya gömlemeyi öğrenin.
---

Excel'de, kaynağı verilerle Ole Nesnesi ekleyebilirsiniz ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Ole Nesnesine çift tıklayınca gömülü dosya açılır.

Genellikle, PDF'ye dönüştürürken Ole Nesnesi simge veya önizleme olarak gösterilir, Ole Nesnesi kaynağı veriler olmadan. [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/) seçeneği ile, Ole Nesnesi kaynağı verilerini PDF'ye ek bağlantısı olarak gömebilirsiniz. PDF'deki simge veya önizleme üzerine çift tıklayarak Ole Nesnesinin kaynağını açabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template file
    Workbook workbook(u"embedded-attachments-example.xlsx");

    // Set to embed Ole Object attachment.
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetEmbedAttachments(true);

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF saved successfully with embedded attachments!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="cpp" >}}
