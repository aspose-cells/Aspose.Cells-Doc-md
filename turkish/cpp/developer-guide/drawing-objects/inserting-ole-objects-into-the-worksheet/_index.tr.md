---
title: OLE Nesnelerini Çalışma Sayfasına Ekleme
type: docs
weight: 20
url: /tr/cpp/inserting-ole-objects-into-the-worksheet/
---
## **Olası Kullanım Senaryoları**
 Aspose.Cells, çalışma sayfasına bir OLE nesnesi eklemenizi sağlar. Lütfen kullan[IWorksheet->GetIOleObjects()->Add()](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object_collection#af230dd65a00cefabcc4b9f165b5dc7ba)Bu amaç için yöntem. OLE nesnesini çalışma sayfasına eklemek için kullanılacak bir görüntü bayt dizisine ve Ole nesnesini çalışma sayfasına eklemek için asıl nesneniz olacak Ole nesnesi veri baytlarına ihtiyacınız olacak.
## **OLE Nesnelerini Çalışma Sayfasına Ekleme**
 Aşağıdaki örnek kod, çalışma kitabı nesnesini oluşturur ve Ole nesnesini ilk çalışma sayfasının içine ekler ve şu şekilde kaydeder:[çıktı excel dosyası](66519074.xlsx) . Lütfen bkz[Aspose logosu](66519075.png) görüntü baytları olarak kullanılır ve[Excel dosyası girişi](66519081.xlsx) referans için kod içinde Ole nesnesi verileri olarak kullanılır.
## **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet.cpp" >}}
