---
title: Aspose.Cells kullanarak C++ ile Özel XML Parçaları Kullanma
linktitle: Özel XML Parçalarını Kullanma
type: docs
weight: 390
url: /tr/cpp/use-custom-xml-parts-in-aspose-cells/
description: Aspose.Cells kullanarak C++ ile Excel dosyalarında programatik olarak özel XML parçalarını nasıl kullanacağınızı öğrenin.
---

## Aspose.Cells'te Özel XML Parçalarını Kullanma

Özel XML Parçaları, SharePoint gibi farklı uygulamalar tarafından bir Excel dosyası içinde saklanan XML verileridir. Bu veriler, ihtiyaç duyan çeşitli uygulamalar tarafından kullanılır. Microsoft Excel bu veriyi kullanmaz, bu nedenle ona eklemek için GUI yoktur. Bu veriyi görmek için, **.xlsx** uzantısını **.zip** olarak değiştirip **WinZip** ile açabilirsiniz. Ayrıca, ZIP dosyasını herhangi bir üçüncü taraf Windows zip aracıyla (örneğin WinRAR veya WinZip) da açabilirsiniz. Veri, **customXml** klasörü içinde bulunur.

Aspose.Cells kullanarak [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) yöntemiyle özel XML parçaları ekleyebilirsiniz.

Aşağıdaki örnek kod, **Book Catalog XML**'yi eklemek için [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) yöntemi kullanır ve adı **BookStore**'dır. Bu kodun sonucu, aşağıdaki görüntüde gösterilmektedir. Görüldüğü gibi, Book Catalog XML, **BookStore** düğümü içine eklenmiştir; bu, bu özelliğin adıdır.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Özel XML Parçalarını Kullanmak için C++ Kodu

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

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## İlgili Makale

- [Belge Bilgisi Panelinde Görünen Özel Özellikleri Ekleme](/cells/tr/cpp/adding-custom-properties-visible-inside-document-information-panel/)
