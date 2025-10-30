---
title: Elektronik Tablodan OLE Nesneleri Çıkarma
type: docs
weight: 10
url: /tr/cpp/extracting-ole-objects-from-worksheet/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, elektronik tablodaki tüm türde OLE nesnelerini çıkarmaya olanak tanır. Lütfen [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) metodunu kullanarak elektronik tablo içindeki tüm OLE nesnelerine erişin. Her OLE nesnesinin [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) ve [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) özellikleri, OLE nesnesinin türünü tanımlamanıza ve başarılı bir şekilde çıkarmanıza yardımcı olabilir.
## **Çalışma Sayfasından OLE Nesneleri Çıkarma**
Aşağıdaki örnek kod, üç OLE nesnesine sahip olan [örnek Excel dosyasını](66519077.xlsx) yükler. Kod, OLE nesnelerinin türlerini belirler ve bunları sırasıyla aşağıdaki dosyalara çıkarır.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
