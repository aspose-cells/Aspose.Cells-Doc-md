---
title: Response Nesnesine Dosya Kaydetme C++ ile
linktitle: Yanıt Nesnesine Dosya Kaydet
type: docs
weight: 50
url: /tr/cpp/saving-file-to-response-object/
description: Aspose.Cells for C++ kullanarak dosyaları dinamik şekilde kaydetmeyi ve doğrudan istemci tarayıcısına göndermeyi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, dosyaların manipüle edilmesini mümkün kılar. Bu makale, dosyaların bir yanıt nesnesine nasıl kaydedilebileceğini açıklar.

{{% /alert %}}

## **Yanıt Nesnesine Dosya Kaydetme**

Ayrıca, bir dosya dinamik olarak oluşturulup doğrudan istemci tarayıcısına gönderilmesi de mümkündür. Bunun için aşağıdaki parametreleri kabul eden [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yönteminin özel aşırı yüklenmiş sürümünü kullanın:

- **HttpResponse** nesnesi.
- Dosya adı.
- Çıktı dosyasının içerik düzeni türü olan [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/).
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/), dosya biçim tipi.

[**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) numaralandırması, tarayıcıya gönderilen dosyanın doğrudan tarayıcıda kendisi veya .xls/.xlsx veya başka bir uzantıyla ilişkilendirilmiş bir uygulamada açılıp açılmamasının seçeneğini belirler.

Numaralama aşağıdaki önceden tanımlanmış kaydetme türlerini içerir:

|**Tür**|**Açıklama**|
| :- | :- |
|Ek|Elektronik tabloyu tarayıcıya gönderir ve .xls/.xlsx veya diğer uzantılarla ilişkilendirilmiş bir uygulamada bir eki olarak açar|
|İçeride|Belgeyi tarayıcıya gönderir ve elektronik tabloyu diske kaydetme veya tarayıcı içinde açma seçeneği sunar|

### **XLS Dosyaları**

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

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **XLSX Dosyaları**

```cpp
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PDF Dosyaları**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Not**

Sistemi içermeyen "System.Web.HttpResponse" nesnesi sebebiyle,
Bu durum, Aspose.Cells .NET5 ve .Netstandard sürümlerinde bulunmadığı için, dosyayı akıma kaydetme işlemini yapmak için aşağıdaki kodlara başvurabilirsiniz.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
