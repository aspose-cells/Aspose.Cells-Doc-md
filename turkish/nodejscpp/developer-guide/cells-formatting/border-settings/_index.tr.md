---  
title: Kenar Ayarları
linktitle: Kenar Ayarları  
description: Node.js de C++ aracılığıyla Aspose.Cells kütüphanesini kullanarak hücre kenarlık stili ve rengini ayarlama. Kenarlığın genişliğini, stilini ve rengini ayarlayarak hücrelerin görünümünü daha iyi kontrol edebilirsiniz.  
keywords: Aspose.Cells, Hücre Kenarı Ayarları, Node.js aracılığıyla C++, Kenarlık Genişliği, Kenarlık Stili, Kenarlık Rengi  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/cells-border-settings/  
---  

## **Hücrelere Kenarlık Eklemek**  

Microsoft Excel, hücreleri kenarlıklar ekleyerek biçimlendirmeye izin verir. Kenarlık tipi, eklendiği konuma göre değişir. Örneğin, üst kenarlık, hücrenin üst konumuna eklenmiş bir kenarlıktır. Kullanıcılar ayrıca kenarlıkların çizgi stilini ve rengini değiştirebilir.  

Aspose.Cells for Node.js via C++ ile geliştiriciler, kenarlıklar ekleyebilir ve onları Microsoft Excel'deki gibi esnek biçimde özelleştirebilir.  

### **Hücrelere Kenarlık Eklemek**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir sayfa, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının bir nesnesini temsil eder.  

Aspose.Cells, [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) metodunu [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfında sağlar. [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) yöntemi, hücre biçimlendirme stilini ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) sınıfı, hücrelere kenarlık eklemek için özellikler sağlar.  

#### **Bir Hücreye Sınır Ekleme**  

Geliştiriciler, bir hücreye kenarlık eklemek için [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) koleksiyonunu kullanabilir. Kenarlık türü, [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) koleksiyonuna indeks olarak geçirilir. Tüm kenarlık türleri önceden tanımlanmış [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype) enum'unda yer alır.  

**Sınır numaralandırması**  

|**Sınır Türleri**|**Açıklama**|  
| :- | :- |  
|BottomBorder|Alt sınır çizgisi|  
|DiagonalDown|Sol üstten sağ alt köşeye çapraz çizgi|  
|DiagonalUp|Sol alttan sağ üste çapraz çizgi|  
|LeftBorder|Sol sınır çizgisi|  
|RightBorder|Sağ sınır çizgisi|  
|TopBorder|Üst sınır çizgisi|  

[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) koleksiyonu tüm kenarlıkları depolar. [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) koleksiyonundaki her kenarlık, [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) nesnesi tarafından temsil edilir ve bu nesne, sırasıyla [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) ve [**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) özellikleri ile kenarlığın çizgi rengi ve stilini ayarlamayı sağlar.  

Bir sınırın çizgi rengini ayarlamak için, Color enumerasyonunu (Node.js'nin bir parçası) kullanarak bir renk seçin ve bunu Border nesnesinin renk özelliğine atayın.  

Kenarın çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype) enum'undan bir çizgi stili seçilerek ayarlanır.  

**HücreSınırTürü numaralandırması**  

|**Çizgi Stilleri**|**Açıklama**|  
| :- | :- |  
|DashDot|İnce tireli kesikli çizgi|  
|DashDotDot|İnce tireli kesik noktalı çizgi|  
|Dashed|Kesikli çizgi|  
|Dotted|Noktalı çizgi|  
|Double|Çift çizgi|  
|Hair|Saç inceliğinde çizgi|  
|MediumDashDot|Orta tireli kesikli çizgi|  
|MediumDashDotDot|Orta tireli kesik noktalı çizgi|  
|MediumDashed|Orta kesikli çizgi|  
|None|No Line|  
|Medium|Orta Çizgi|  
|SlantedDashDot|Eğik orta kesikli çizgi|  
|Thick|Kalın çizgi|  
|Thin|İnce çizgi|  
Çizgi stillerinden birini seçin ve ardından onu [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) nesnesinin [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) özelliğine atayın.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
Her iki çizgi stili ve rengi aynı anda ayarlamalısınız. İki çapraz kenar çizgisi aynı çizgi stiline ve renge sahip olmalıdır.  
{{% /alert %}}  

#### **Hücre Aralığına Sınırlar Ekleme**  

Sadece bir hücre yerine hücre aralığına da sınırlar eklemek mümkündür. Bunu yapmak için önce, [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) yöntemini çağırarak bir hücre aralığı oluşturun. Aşağıdaki parametreleri alır:  

- İlk Sütun, aralığın ilk sütunu.  
- İlk Sütun, aralığın ilk sütunu.  
- Satır Sayısı, aralıktaki satır sayısı.  
- Sütun Sayısı, aralıktaki sütun sayısı.  

[**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) yöntemi, belirtilen hücre aralığını içeren bir [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) nesnesi döner. [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) nesnesi, aşağıdaki parametreleri alan bir [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-) yöntemi sağlar ve hücre aralığına sınır ekler:  

- **Sınır Türü**, [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype) enumerasyonundan seçilen sınır tipi.  
- **Çizgi Stili**, sınır çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype) enumerasyonundan seçilir.  
- **Renk**, Renk sıralamasından seçilen çizgi rengi.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
