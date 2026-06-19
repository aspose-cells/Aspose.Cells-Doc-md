---
title: Bir Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Python kütüphanesidir. Bu makale, bir resmi tam olarak tek bir hücre boyutuna sığdırmayı iki farklı yaklaşımla açıklar: hücrenin üzerine kayan bir resim yerleştirmek veya resmi doğrudan hücreye gömmek.
keywords: Aspose.Cells, Python kütüphanesi, elektronik tablo, resim ekleme, resim gömme, hücrede resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells, bir resmi tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanında bir hücre aralığının üzerine görsel olarak yerleşen bir şekildir; gömülü resim ise hücrenin kendi içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.

{{% /alert %}}

## **Giriş**

Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan dizinleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlarken yaygın bir gereksinimdir. Bir resmi birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, kendisine sahip olan hücreyle hizalı kalan temiz, hücreye bağlı bir resim isteyebilirsiniz.

Aspose.Cells bu senaryoyu birbirini tamamlayan iki şekilde destekler:

- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `placement` özelliğini `MOVE_AND_SIZE` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için sabitleme hücrelerini (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) ayarlayın.
- **Yaklaşım 2 — Resmi doğrudan bir hücreye gömün.** Görüntü baytlarını hücrenin `embedded_image` özelliğine atayın. Resim, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.

Bu makalenin geri kalanı her iki yaklaşımı da inceler, ilgili API'leri açıklar ve bunların kodda nasıl kullanılacağını gösterir.

## **Yaklaşım 1: Hücrenin Üzerine Bir Resim Yerleştirme**

Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına sabitlenmiştir. Resmin sabitleme hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kaplar.

Kayan bir resmi **tam olarak tek bir hücreyi** kaplayacak şekilde ayarlamak için şunları yapmanız gerekir:

1. Resmi `Worksheet.pictures.add(row, column, stream)` kullanarak ekleyin; bu, yeni resmi belirtilen hücreye sabitler.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört sabitleme özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte taşınması ve yeniden boyutlandırılması için `Picture.placement` özelliğini `PlacementType.MOVE_AND_SIZE` olarak ayarlayın.

### **Resmi Tek Bir Hücreye Sabitleme**

Resmin sabitleme noktası dört sıfır tabanlı dizin özelliği ile tanımlanır:

- `Picture.upper_left_row` — resmin üst kenarının satır dizini.
- `Picture.upper_left_column` — resmin sol kenarının sütun dizini.
- `Picture.lower_right_row` — resmin alt kenarının satır dizini. Resmin alt kenarını `r` satırının altına yerleştirmek için bunu `r + 1` olarak ayarlayın.
- `Picture.lower_right_column` — resmin sağ kenarının sütun dizini. Resmin sağ kenarını `c` sütununun sağına yerleştirmek için bunu `c + 1` olarak ayarlayın.

Örneğin, resmi tam olarak **C6** hücresine (satır dizini `5`, sütun dizini `2`) sığdırmak için `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6` ve `lower_right_column = 3` ayarlayın.

{{% alert color="primary" %}}

Aspose.Cells'de satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt sabitleme noktasındaki bir hane hataları, resimlerin bitişik bir hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

{{% /alert %}}

### **Yerleşim Davranışını Kontrol Etme**

`Picture.placement`, kullanıcı alttaki satırı veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir enum'dur. Tek hücreli bir resim için önerilen değer `PlacementType.MOVE_AND_SIZE`'dır; bu, resmin alttaki hücreyle birlikte taşınmasını ve yeniden boyutlandırılmasını sağlayarak tam sığmayı korur.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya var olan birini açın).
2. Hedef `Worksheet`'e `workbook.worksheets[0]` üzerinden erişin.
3. Görüntü dosyasını diskten bir dosya akışına (veya `BytesIO` nesnesine) açın, akışın düzgün şekilde kapatılması için bir `with` bloğu kullanın.
4. `worksheet.pictures.add(5, 2, stream)` çağrısını yaparak resmi C6 hücresine sabitlenmiş şekilde ekleyin. Döndürülen `Picture` referansını yakalayın.
5. Dört sabitleme koordinatını, resmin yalnızca C6 hücresini kaplayacağı şekilde ayarlayın: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalmasını sağlamak için `picture.placement = PlacementType.MOVE_AND_SIZE` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, eksiksiz yaklaşımı gösterir.

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

## **Yaklaşım 2: Resmi Doğrudan Bir Hücreye Gömme**

Aspose.Cells ayrıca hücreye bağlı resimler için daha basit bir mekanizma sunar: `Cell.embedded_image` özelliği. Görüntü baytlarını bu özelliğe atamak, resmi hücrenin kendisine, satır içi içerikmiş gibi ekler.

### **Gömülü Resimler Nasıl Çalışır**

- Resim, çizim katmanındaki bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Resim, hücrenin işlenmiş sınırlarına sığacak şekilde otomatik olarak ölçeklenir. Sabitleme koordinatları veya yerleşim ayarları gerekmez.
- Hücre, formüller tarafından referans verilebilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyindeki işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.

Bu, amacınız yalnızca "bu hücrenin içinde yaşayan bir resim" olduğunda `Cell.embedded_image`'ı en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya var olan birini açın).
2. Hedef `Worksheet`'e `workbook.worksheets[0]` üzerinden erişin.
3. Görüntü dosyasını diskten bir `bytes` nesnesine okuyun (örneğin, dosyayı ikili modda açıp `.read()` çağırarak).
4. Hedef hücreye bir referans alın — `worksheet.cells["C6"]` veya `worksheet.cells[5, 2]` aracılığıyla.
5. Bytes nesnesini hücrenin `embedded_image` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü resme daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, eksiksiz yaklaşımı gösterir.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Hedef hücre C6'yı al
cell = worksheet.cells["C6"]

# Görüntü dosyasını bir bayt dizisine oku
with open("logo.png", "rb") as f:
    imageData = f.read()

# Görüntüyü doğrudan hücreye yerleştir
cell.embedded_image = imageData

# Yerleştirilen görüntünün daha görünür olması için isteğe bağlı olarak satır yüksekliğini ve sütun genişliğini ayarla
worksheet.cells.set_column_width(2, 30)   # Sütun C (indeks 2)
worksheet.cells.set_row_height(5, 100)     # Satır 6 (indeks 5)

# Elde edilen çalışma kitabını .xlsx dosyası olarak kaydet
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Doğru Yaklaşımı Seçme**

Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı açısından farklılık gösterir:

- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleşim, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı kontrole ihtiyaç duyduğunuzda.
  - Resmin, seçilebilen, yeniden sıralanabilen veya diğer şekillerle gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten `pictures` koleksiyonlarıyla çalışan kodla eski sürüm uyumluluğuna ihtiyaç duyduğunuzda.
  - Sabitleme koordinatlarını çalışma sayfası düzenine göre dinamik olarak hesaplamanız gerektiğinde.

- **Şu durumlarda gömülü resim kullanın (Yaklaşım 2):**
  - Bir hücreye mümkün olan en basit resim eklemeyi istediğinizde.
  - Resim, diğer hücre içerikleri gibi hücreyle birlikte taşınmalıdır.
  - Resmi bir şekil olarak düzenlemeniz gerekmiyorsa.

{{% alert color="primary" %}}

Her iki yaklaşım aynı çalışma kitabında bir arada bulunabilir. İki mekanizma dosyada farklı depolama katmanları kullandığından, bir hücre kümesinin üzerine kayan resimler yerleştirebilir ve diğer hücrelere doğrudan resim gömebilirsiniz.

{{% /alert %}}

## **İlgili Makaleler**

- [Hücreye Resim Nasıl Yerleştirilir](/cells/tr/python-net/how-to-place-image-to-cell/)
- [Görüntü Köprüleri Ekleme](/cells/tr/python-net/add-image-hyperlinks/)
- [URL'den Bir Web Resmini Excel Çalışma Sayfasına Yükleme](/cells/tr/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Konum, Boyut ve Tasarımcı Grafiğini Değiştirme](/cells/tr/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}