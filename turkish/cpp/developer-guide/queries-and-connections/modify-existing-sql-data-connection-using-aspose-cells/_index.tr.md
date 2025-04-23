---
title: Aspose.Cells kullanarak mevcut SQL Veri Bağlantısını C++ ile Düzenle
linktitle: Mevcut SQL Veri Bağlantısını değiştir
type: docs
weight: 20
url: /tr/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Aspose.Cells kullanarak Excel dosyalarında mevcut SQL Veri Bağlantısını C++ ile nasıl düzenleyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, mevcut SQL Veri Bağlantısını düzenlemeyi destekler. Bu makale, Aspose.Cells kullanarak SQL Veri Bağlantısının farklı özelliklerini nasıl düzenleyeceğinizi açıklayacaktır.

Microsoft Excel içinde Veri > Bağlantılar menü komutunu kullanarak Veri Bağlantılarını ekleyebilir veya görüntüleyebilirsiniz.

Benzer şekilde, Aspose.Cells `Workbook.DataConnections` koleksiyonunu kullanarak Veri Bağlantılarına erişip düzenleme imkanı sağlar.

{{% /alert %}}

## Aspose.Cells ile Mevcut SQL Veri Bağlantısını Değiştirme

Aşağıdaki örnek, Aspose.Cells'ı kullanarak Excel dosyasının SQL Veri Bağlantısını değiştirmeyi göstermektedir. Kod içinde kullanılan kaynak Excel dosyasını ve kod tarafından oluşturulan çıktı Excel dosyasını aşağıdaki linklerden indirebilirsiniz.

- [Kaynak Excel Dosyası](5112357.xlsx)
- [Çıktı Excel Dosyası](5112356.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataConnection.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Access first Data Connection
    ExternalConnection conn = workbook.GetDataConnections().Get(0);

    // Change the Data Connection Name and Odc file
    conn.SetName(u"MyConnectionName");
    conn.SetOdcFile(u"C:\\Users\\MyDefaulConnection.odc");

    // Change the Command Type, Command and Connection String
    DBConnection dbConn = conn;
    dbConn.SetCommandType(OLEDBCommandType::SqlStatement);
    dbConn.SetCommand(u"Select * from AdminTable");
    dbConn.SetConnectionString(u"Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Data connection updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
