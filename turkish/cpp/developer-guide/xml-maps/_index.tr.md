---
title: XML i C++ ile Excel Çalışma Kitabına İçe Aktarın
linktitle: XML Haritaları
type: docs
weight: 210
url: /tr/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Bir XML veri dosyasından verileri Microsoft Excel e Aspose.Cells kullanarak import edin.
---

{{% alert color="primary" %}}

Aspose.Cells, [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/) yöntemi kullanılarak çalışma kitabı içindeki XML haritasını içe aktarmanıza olanak tanır. XML Map'i aşağıdaki adımlarla Microsoft Excel kullanarak içe aktarabilirsiniz:

- **Developer** sekmesini seçin.
- XML bölümünde **İçe Aktar**'ı tıklayın ve gerekli adımları izleyin.

İçe aktarma işlemini tamamlamak için XML verilerinizi sağlamanız gerekecektir. Test için kullanabileceğiniz [örnek XML verileri](5115037.txt) burada bulunmaktadır.

{{% /alert %}}

## **Microsoft Excel kullanarak XML Haritası İçe Aktarma**

Aşağıdaki ekran görüntüsü, Microsoft Excel kullanarak XML Haritası İçe Aktarma işlemini göstermektedir.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cells kullanarak XML Haritası İçe Aktarma**

Aşağıdaki örnek kod, [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/) metodunun nasıl kullanılacağını gösterir. Bu, bu ekran görüntüsünde gösterilen [çıktı Excel dosyasını](5115036.xlsx) oluşturur.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

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

    // Create a workbook
    Workbook workbook;

    // URL that contains your XML data for mapping
    U16String XML(u"http://www.aspose.com/docs/download/attachments/434475650/sampleXML.txt");

    // Import your XML Map data starting from cell A1
    workbook.ImportXml(XML, u"Sheet1", 0, 0);

    // Save workbook
    U16String outputPath = outDir + u"output_out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully with imported XML data!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [XmlMapCollection.Add yöntemini kullanarak İçine 'XmlMap' ekleyin](/cells/tr/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Çalışma Kitabı içinde XML Haritasına bağlı XML Verilerini Dışa Aktar](/cells/tr/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [XML Haritasının Kök Eleman Adını Bul](/cells/tr/cpp/find-the-root-element-name-of-xml-map/)
- [Hücreleri XML Haritası Elemanlarına Bağla](/cells/tr/cpp/link-cells-to-xml-map-elements/)
