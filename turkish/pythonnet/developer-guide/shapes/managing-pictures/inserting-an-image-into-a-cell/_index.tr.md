---
title: Hücreye Resim Ekleme
linktitle: Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir Python kütüphanesidir. Bu makale, bir resmi hücrenin üzerine kayan resim olarak yerleştirerek veya görseli doğrudan hücreye gömerek tam olarak tek bir hücreye sığdırmayı açıklar.
keywords: Aspose.Cells, Python kütüphanesi, elektronik tablo, resim ekle, görsel göm, hücredeki resim, resmi hücreye sığdır, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir görseli tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfasının çizim katmanındaki bir şekildir ve bir hücre aralığının üzerine görsel olarak yerleştirilir; gömülü görsel ise hücrenin kendi içinde depolanır ve hücrenin görüntü alanına otomatik olarak ölçeklenir. Yerleşim gereksinimlerinize en uygun yaklaşımı seçin.
{{% /alert %}}

## **Introduction**
Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlarken yaygın bir gereksinimdir. Görseli birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahip olduğu hücreyle hizalı kalan temiz, hücreye bağlı bir görsel isteyebilirsiniz.
Aspose.Cells bu senaryoyu birbirini tamamlayan iki şekilde destekler:
- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `placement` özelliğini `MOVE_AND_SIZE` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için bağlantı hücrelerini (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) ayarlayın.
- **Yaklaşım 2 — Görseli doğrudan bir hücreye gömün.** Görsel baytlarını hücrenin `embedded_image` özelliğine atayın. Görsel otomatik olarak hücrenin görüntü alanına sığacak şekilde ölçeklenir ve hücreyle birlikte taşınır.
Bu makalenin geri kalanı her iki yaklaşımı da ele alır, ilgili API'leri açıklar ve kodda nasıl kullanılacağını gösterir.

## **Approach 1: Place a Picture Over a Cell**
Kayan resim, çalışma sayfasının çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına bağlanır. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kapsar.
Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:
1. `Worksheet.pictures.add(row, column, stream)` kullanarak resmi ekleyin; bu, yeni resmi verilen hücreye bağlar.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört bağlantı özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte taşınması ve yeniden boyutlandırılması için `Picture.placement` özelliğini `PlacementType.MOVE_AND_SIZE` olarak ayarlayın.

### **Anchoring the Picture to a Single Cell**
Resmin bağlantısı dört sıfır tabanlı dizin özelliğiyle tanımlanır:
- `Picture.upper_left_row` — resmin üst kenarının satır dizini.
- `Picture.upper_left_column` — resmin sol kenarının sütun dizini.
- `Picture.lower_right_row` — resmin alt kenarının satır dizini. Resmin alt kenarının `r` satırının altında olmasını sağlamak için bunu `r + 1` olarak ayarlayın.
- `Picture.lower_right_column` — resmin sağ kenarının sütun dizini. Resmin sağ kenarının `c` sütununun sağında olmasını sağlamak için bunu `c + 1` olarak ayarlayın.

{{% alert color="primary" %}}
Aspose.Cells'deki satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt bağlantı noktasındaki bir-ofset hataları, resimlerin bitişik bir hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

### **Controlling Placement Behavior**
`Picture.placement`, kullanıcı alttaki satırı veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir enum'dur. Tek hücreli bir resim için önerilen değer `PlacementType.MOVE_AND_SIZE`'dir; bu, resmin alttaki hücreyle birlikte taşınmasını ve yeniden boyutlandırılmasını sağlayarak tam sığmayı korur.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Görsel dosyasını diskten bir dosya akışına (veya `BytesIO` nesnesine) `with` bloğu kullanarak açın; böylece akış düzgün şekilde kapatılır.
4. C6 hücresine bağlı bir resim eklemek için `worksheet.pictures.add(5, 2, stream)` çağrısını yapın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört bağlantı koordinatını ayarlayın: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalmasını sağlamak için `picture.placement = PlacementType.MOVE_AND_SIZE` olarak ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod tam yaklaşımı gösterir.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells ayrıca hücreye bağlı görseller için daha basit bir mekanizma sunar: `Cell.embedded_image` özelliği. Görsel baytlarını bu özelliğe atamak, görseli sanki satır içi içerikmiş gibi hücrenin kendisine ekler.

### **How Embedded Images Work**
- Görsel, çizim katmanındaki bir şekil olarak değil, hücre içeriğinin bir parçası olarak depolanır.
- Görsel, hücrenin işlenmiş sınırlarının içine sığacak şekilde otomatik olarak ölçeklenir. Bağlantı koordinatları veya yerleştirme ayarları gerekmez.
- Hücre, formüller tarafından referans alınabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyindeki işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.
Bu, amacınız basitçe 'bu hücrenin içinde yaşayan bir görsel' olduğunda `Cell.embedded_image` özelliğini en özlü seçenek haline getirir.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Görsel dosyasını diskten bir `bytes` nesnesine okuyun (örneğin, dosyayı ikili modda açıp `.read()` çağırarak).
4. Hedef hücrenin referansını alın — `worksheet.cells["C6"]` veya `worksheet.cells[5, 2]` aracılığıyla.
5. Bayt nesnesini hücrenin `embedded_image` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü görsele daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod tam yaklaşımı gösterir.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells["C6"]
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Choosing the Right Approach**
Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl depolandığı ve nasıl davrandığı açısından farklılık gösterir:
- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı kontrol gerektiğinde.
  - Resmin seçilebilen, yeniden sıralanabilen veya diğer şekillerle gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten `pictures` koleksiyonlarıyla çalışan kodla eski sürüm uyumluluğu gerektirdiğinde.
  - Çalışma sayfası düzenine göre bağlantı koordinatlarını dinamik olarak hesaplamanız gerektiğinde.
- **Şu durumlarda gömülü görsel kullanın (Yaklaşım 2):**
  - Bir hücreye mümkün olan en basit görsel eklemeyi istediğinizde.
  - Görsel, diğer hücre içerikleri gibi hücreyle birlikte taşınmalıdır.
{{% /alert %}}

## Related Articles
- [Aspose.Cells for Python via .NET'te Excel Camera](/cells/tr/python-net/excel-camera/)
- [Aspose.Cells for Python via .NET'te Bir Pivot Tablosuna Filtre Alanları Ekleme](/cells/tr/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET'te Pivot Tablolarına Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/python-net/change-page-field-layout/)
- [Aspose.Cells for Python via .NET'te Sparkline'ı Görsele ve HTML'e Dönüştürme](/cells/tr/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python" >}}