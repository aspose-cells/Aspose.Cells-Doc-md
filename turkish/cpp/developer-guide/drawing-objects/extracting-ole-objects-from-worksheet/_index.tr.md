---
title: OLE Nesnelerini Çalışma Sayfasından Çıkarma
type: docs
weight: 10
url: /tr/cpp/extracting-ole-objects-from-worksheet/
---
## **Olası Kullanım Senaryoları**
 Aspose.Cells, çalışma sayfasından her türden OLE nesnesini çıkarmanıza olanak tanır. Lütfen kullan[IWorksheet->GetIOleObjects()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728) çalışma sayfasındaki tüm OLE nesnelerine erişme yöntemi. Her OLE nesnesinin sahip olduğu[ProgID](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752) ve[Nesne Verileri](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)OLE nesnesinin türünü tanımlamanıza ve başarıyla ayıklamanıza yardımcı olabilecek özellikler.
## **OLE Nesnelerini Çalışma Sayfasından Çıkarma**
 Aşağıdaki örnek kod,[örnek excel dosyası](66519077.xlsx) üç OLE nesnesi olan. Kod, OLE nesnelerinin türlerini tanımlar ve bunları aşağıdaki dosyalar olarak birer birer çıkarır.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
