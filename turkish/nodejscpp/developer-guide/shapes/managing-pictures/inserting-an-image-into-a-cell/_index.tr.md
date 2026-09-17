---
title: Bir Hücreye Resim Ekleme
linktitle: Bir Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için Node.js via C++ kitaplığıdır. Bu makale, bir resmi hücrenin üzerine kayan bir resim yerleştirerek veya görüntüyü doğrudan hücreye gömerek tam olarak tek bir hücreye sığdırmayı açıklar.
keywords: Aspose.Cells, Node.js via C++ kitaplığı, elektronik tablo, resim ekleme, görüntü gömme, hücredeki resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/nodejs-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir görüntüyü tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanında hücre aralığının üzerine görsel olarak yerleşen bir şekildir; gömülü görüntü ise hücrenin kendisinin içinde depolanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.
{{% /alert %}}

## **Introduction**
Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlarken yaygın bir gereksinimdir. Görüntüyü birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahibi olan hücreyle hizalı kalan temiz, hücreye bağlı bir görüntü isteyebilirsiniz.
Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:
- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `placement` özelliğini `MoveAndSize` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için bağlantı hücrelerini (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Görüntüyü doğrudan bir hücreye gömün.** Görüntü baytlarını hücrenin `embeddedImage` özelliğine atayın. Görüntü, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte hareket eder.
Bu makalenin geri kalanı her iki yaklaşımı da ele alır, ilgili API'leri açıklar ve bunları kodda nasıl kullanacağınızı gösterir.

## **Approach 1: Place a Picture Over a Cell**
Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına sabitlenir. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kapsar.
Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:
1. Resmi `worksheet.pictures.add(row, column, stream)` kullanarak ekleyin; bu, yeni resmi verilen hücreye sabitler.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört bağlantı özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `picture.placement` özelliğini `PlacementType.MoveAndSize` olarak ayarlayın.

### **Anchoring the Picture to a Single Cell**
Resmin bağlantısı dört sıfır tabanlı dizin özelliği ile tanımlanır:
- `picture.upperLeftRow` — resmin üst kenarının satır dizini.
- `picture.upperLeftColumn` — resmin sol kenarının sütun dizini.
- `picture.lowerRightRow` — resmin alt kenarının satır dizini. Resmin alt kenarının `r` satırının altına yerleşmesini sağlamak için bunu `r + 1` olarak ayarlayın.
- `picture.lowerRightColumn` — resmin sağ kenarının sütun dizini. Resmin sağ kenarının `c` sütununun sağına yerleşmesini sağlamak için bunu `c + 1` olarak ayarlayın.

{{% alert color="primary" %}}
Aspose.Cells'teki satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt bağlantı noktasındaki bir birimlik sapma hataları, resimlerin bitişik bir hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

### **Controlling Placement Behavior**
`picture.placement`, kullanıcı alttaki satırı veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir numaralandırmadır. Tek hücreli bir resim için önerilen değer `PlacementType.MoveAndSize`'dır; bu, resmin alttaki hücreyle birlikte hareket etmesine ve yeniden boyutlandırılmasına neden olarak tam sığmayı korur.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.worksheets[0]` üzerinden erişin.
3. Görüntü dosyasını diskten bir akışa açın ve akışın kullanımdan sonra düzgün bir şekilde kapatıldığından emin olun.
4. C6 hücresine sabitlenmiş bir resim eklemek için `worksheet.pictures.add(5, 2, stream)` çağrısı yapın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört bağlantı koordinatını ayarlayın: `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalmasını sağlamak için `picture.placement = PlacementType.MoveAndSize` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod, eksiksiz yaklaşımı gösterir.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const fs_stream = fs.createReadStream("logo.png");
const picIndex = worksheet.getPictures().add(5, 2, fs_stream);
const picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells ayrıca hücreye bağlı görüntüler için daha basit bir mekanizma sunar: `cell.embeddedImage` özelliği. Görüntü baytlarını bu özelliğe atamak, görüntüyü sanki satır içi içerikmiş gibi hücrenin kendisine ekler.

### **How Embedded Images Work**
- Görüntü, çizim katmanındaki bir şekil yerine hücre içeriğinin bir parçası olarak depolanır.
- Görüntü, hücrenin işlenmiş sınırlarına sığacak şekilde otomatik olarak ölçeklenir. Herhangi bir bağlantı koordinatı veya yerleşim ayarı gerekmez.
- Hücre, formüller tarafından referans alınabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyindeki işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.
Bu, amacınız yalnızca "bu hücrenin içinde yaşayan bir görüntü" olduğunda `cell.embeddedImage`'ı en özlü seçenek haline getirir.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.worksheets[0]` üzerinden erişin.
3. Görüntü dosyasını Node.js dosya sistemi API'lerini kullanarak (örneğin, `fs.readFileSync`) diskten bir Buffer veya bayt dizisine okuyun.
4. Hedef hücreye bir referans alın — `worksheet.cells["C6"]` veya `worksheet.cells[5, 2]` aracılığıyla.
5. Bayt dizisini hücrenin `embeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü görüntüye daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod, eksiksiz yaklaşımı gösterir.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Get the target cell C6
var cell = worksheet.getCells().get("C6");
// Read the image file into a byte array
var imageData = fs.readFileSync("logo.png");
// Embed the image directly into the cell
cell.setEmbeddedImage(imageData);
// Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30);   // Column C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Row 6 (index 5)
// Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Choosing the Right Approach**
Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl depolandığı ve nasıl davrandığı açısından farklılık gösterir:
- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleşim, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı denetime ihtiyacınız olduğunda.
  - Resmin seçilebilen, yeniden sıralanabilen veya diğer şekillerle gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten resim koleksiyonuyla çalışan kodla eski sürüm uyumluluğu gerektirdiğinizde.
  - Çalışma sayfası düzenine göre bağlantı koordinatlarını dinamik olarak hesaplamanız gerektiğinde.
- **Şu durumlarda gömülü görüntü kullanın (Yaklaşım 2):**
  - Bir hücreye mümkün olan en basit görüntü eklemeyi istediğinizde.
  - Görüntü, diğer tüm hücre içerikleri gibi hücreyle birlikte hareket etmelidir.
{{% /alert %}}

## Related Articles
- [Excel Camera in Aspose.Cells for Node.js via C++](/cells/tr/nodejs-cpp/excel-camera/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via C++](/cells/tr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via C++](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/tr/nodejs-cpp/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Node.js via C++](/cells/tr/nodejs-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript" >}}