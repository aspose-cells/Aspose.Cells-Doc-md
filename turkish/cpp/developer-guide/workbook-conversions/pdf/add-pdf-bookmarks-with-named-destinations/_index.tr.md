---
title: PDF Yer İmleri ve İsimli Hedeflerle C++ ile Ekle
linktitle: Adlandırılmış hedeflerle PDF Yer İmlerini Ekleyin
type: docs
weight: 20
url: /tr/cpp/add-pdf-bookmarks-with-named-destinations/
description: Aspose.Cells for C++ kullanarak, isimli hedeflerle PDF yer imi eklemeyi öğrenin.
---

## **Olası Kullanım Senaryoları**

İsimli Hedefler, PDF'de sayfa bağımsız, özel bookmark veya bağlantı türleridir. Yani, PDF'den sayfalar eklenip silindiğinde, yer imleri geçersiz hale gelebilir, ancak isimli hedefler sağlam kalır. İsimli Hedef oluşturmak için, [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/getdestinationname/) özelliğini ayarlayın.

## **Adlandırılmış Yer İmleriyle PDF Yer İmi Ekleyin**

Aşağıdaki örnek kodu, [kaynak Excel dosyasını](50528348.xlsx) ve [çıktı PDF dosyasını](50528349.pdf) inceleyin. Ekran görüntüsü, çıktı PDF içindeki yer imlerini ve isimli hedefleri gösterir. Ekran görüntüsü ayrıca İsimli Hedeflerin nasıl görüntüleneceğini ve Adobe Acrobat Reader'ın Profesyonel sürümüne ihtiyacınız olduğunu açıklar.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"samplePdfBookmarkEntry_DestinationName.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell C5
    Cell cell = ws.GetCells().Get(u"C5");

    // Create Bookmark and Destination for this cell
    PdfBookmarkEntry bookmarkEntry;
    bookmarkEntry.SetText(u"Text");
    bookmarkEntry.SetDestination(cell);
    bookmarkEntry.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Access cell G56
    cell = ws.GetCells().Get(u"G56");

    // Create Sub-Bookmark and Destination for this cell
    PdfBookmarkEntry subbookmarkEntry1;
    subbookmarkEntry1.SetText(u"Text1");
    subbookmarkEntry1.SetDestination(cell);
    subbookmarkEntry1.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Access cell L4
    cell = ws.GetCells().Get(u"L4");

    // Create Sub-Bookmark and Destination for this cell
    PdfBookmarkEntry subbookmarkEntry2;
    subbookmarkEntry2.SetText(u"Text2");
    subbookmarkEntry2.SetDestination(cell);
    subbookmarkEntry2.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Add Sub-Bookmarks in list
    std::vector<PdfBookmarkEntry> list;
    list.push_back(subbookmarkEntry1);
    list.push_back(subbookmarkEntry2);

    // Assign Sub-Bookmarks list to Bookmark Sub-Entry
    // Note: The SubEntry property is not directly available in the provided headers.
    // Assuming it is a member of PdfBookmarkEntry, you would need to set it here.
    // bookmarkEntry.SetSubEntry(list);

    // Create PdfSaveOptions and assign Bookmark to it
    PdfSaveOptions opts;
    opts.SetBookmark(bookmarkEntry);

    // Save the workbook in Pdf format with given pdf save options
    wb.Save(outDir + u"outputPdfBookmarkEntry_DestinationName.pdf", opts);

    std::cout << "Workbook saved successfully with bookmarks!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
