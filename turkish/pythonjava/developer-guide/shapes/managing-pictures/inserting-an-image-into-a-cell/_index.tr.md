---
title: Bir Hücreye Görüntü Ekleme
description: Aspose.Cells for Python via Java, elektronik tablo dosyalarıyla çalışmak için bir kütüphanedir. Bu makale, resmi tam olarak tek bir hücre boyutuna sığdırmayı iki farklı yaklaşımla açıklar: hücrenin üzerine kayan bir resim yerleştirmek veya görüntüyü doğrudan hücrenin içine gömmek.
keywords: Aspose.Cells, Python via Java kütüphanesi, elektronik tablo, görüntü ekleme, görüntü gömme, hücredeki resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells, bir görüntüyü tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanında bulunan ve bir hücre aralığının üzerine görsel olarak yerleşen bir şekildir; gömülü görüntü ise hücrenin içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.

{{% /alert %}}

## **Giriş**

Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan dizinleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlanırken sık karşılaşılan bir gereksinimdir. Görüntüyü birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahibi olan hücreyle hizalı kalan, temiz ve hücreye bağlı bir görüntü isteyebilirsiniz.

Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:

- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `setPlacement` özelliğini `MOVE_AND_SIZE` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için bağlantı hücrelerini (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Görüntüyü doğrudan bir hücreye gömün.** Görüntü baytlarını hücrenin `setEmbeddedImage` özelliğine atayın. Görüntü, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.

Bu makalenin geri kalanı her iki yaklaşımı da adım adım açıklar, ilgili API'leri anlatır ve bunların kodda nasıl kullanılacağını gösterir.

## **Yaklaşım 1: Hücrenin Üzerine Bir Resim Yerleştirme**

Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına bağlanır. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreye yayılır.

Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:

1. Resmi `Worksheet.getPictures().add(int row, int column, InputStream stream)` kullanarak ekleyin; bu, yeni resmi verilen hücreye bağlar.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört bağlantı özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte taşınması ve yeniden boyutlandırılması için `Picture.setPlacement` özelliğini `PlacementType.MOVE_AND_SIZE` olarak ayarlayın.

### **Resmi Tek Bir Hücreye Bağlama**

Resmin bağlantısı, sıfır tabanlı dört dizin özelliği tarafından tanımlanır:

- `setUpperLeftRow` — resmin üst kenarının satır dizini.
- `setUpperLeftColumn` — resmin sol kenarının sütun dizini.
- `setLowerRightRow` — resmin alt kenarının satır dizini. Resmin alt kenarını `r` satırının altına yerleştirmek için bunu `r + 1` olarak ayarlayın.
- `setLowerRightColumn` — resmin sağ kenarının sütun dizini. Resmin sağ kenarını `c` sütununun sağına yerleştirmek için bunu `c + 1` olarak ayarlayın.

Örneğin, resmi tam olarak **C6** hücresine (satır dizini `5`, sütun dizini `2`) sığdırmak için `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` ve `setLowerRightColumn(3)` ayarlayın.

{{% alert color="primary" %}}

Aspose.Cells'teki satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt bağlantı noktasındaki off-by-one hataları, resimlerin bitişik hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

{{% /alert %}}

### **Yerleştirme Davranışını Kontrol Etme**

`getPlacement`, kullanıcı alttaki satırı veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir numaralandırmadır. Tek hücreli resim için önerilen değer `PlacementType.MOVE_AND_SIZE`'dır; bu, resmin alttaki hücreyle birlikte taşınmasına ve yeniden boyutlandırılmasına neden olarak tam sığdırmayı korur.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.getWorksheets().get(0)` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını disk üzerinden bir `InputStream`'e açın (genellikle akışın düzgün şekilde kapatılması için bir `FileInputStream`).
4. Resmi C6 hücresine bağlı olarak eklemek için `worksheet.getPictures().add(5, 2, stream)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört bağlantı koordinatını ayarlayın: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalmasını sağlamak için `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, yaklaşımın tamamını göstermektedir.



```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()

workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Yaklaşım 2: Görüntüyü Doğrudan Bir Hücreye Gömme**

Aspose.Cells ayrıca hücreye bağlı görüntüler için daha basit bir mekanizma sunar: `Cell.setEmbeddedImage` özelliği. Görüntü baytlarını bu özelliğe atamak, görüntüyü hücrenin kendisine satır içi içerikmiş gibi ekler.

### **Gömülü Görüntüler Nasıl Çalışır**

- Görüntü, çizim katmanındaki bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Görüntü, hücrenin işlenmiş sınırları içine sığacak şekilde otomatik olarak ölçeklenir. Bağlantı koordinatları veya yerleştirme ayarları gerekmez.
- Hücre, formüller tarafından başvurulabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.

Bu, amacınız yalnızca "bu hücrenin içinde yaşayan bir görüntü" olduğunda `Cell.setEmbeddedImage`'ı en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.getWorksheets().get(0)` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını diskten bir `byte[]` dizisine okuyun (örneğin, `java.nio.file.Files` üzerinden bir `Files.readAllBytes` çağrısı kullanarak).
4. Hedef hücreye bir referans alın — `worksheet.getCells().get("C6")` veya `worksheet.getCells().get(5, 2)` aracılığıyla.
5. Bayt dizisini hücrenin `setEmbeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü görüntüye daha belirgin bir görünüm kazandırmak için hedef satır ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, yaklaşımın tamamını göstermektedir.



```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# buraya taşınan kod
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Hedef hücre C6'yı al
cell = worksheet.getCells().get("C6")

# Görüntü dosyasını bir bayt dizisine oku
imageData = open("logo.png", "rb").read()

# Görüntüyü doğrudan hücreye göm
cell.setEmbeddedImage(imageData)

# İsteğe bağlı olarak satır yüksekliğini ve sütun genişliğini ayarla, böylece gömülü görüntü daha görünür olur
worksheet.getCells().setColumnWidth(2, 30)   # Sütun C (indeks 2)
worksheet.getCells().setRowHeight(5, 100)    # Satır 6 (indeks 5)

# Ortaya çıkan çalışma kitabını .xlsx dosyası olarak kaydet
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Doğru Yaklaşımı Seçme**

Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı konusunda farklılık gösterir:

- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı bir kontrole ihtiyacınız olduğunda.
  - Resmin diğer şekillerle birlikte seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil gibi davranmasını istediğinizde.
  - Zaten `PictureCollection` ile çalışan kodla eski uyumluluk gerektirdiğinizde.
  - Çalışma sayfası düzenine dayalı olarak bağlantı koordinatlarını dinamik olarak hesaplamanız gerektiğinde.

- **Şu durumlarda gömülü görüntü kullanın (Yaklaşım 2):**
  - Bir hücreye görüntü eklemenin en basit olası yolunu istediğinizde.
  - Görüntünün diğer hücre içerikleri gibi hücreyle birlikte taşınması gerektiğinde.
  - Görüntüyü bir şekil olarak işleme ihtiyacınız olmadığında.

{{% alert color="primary" %}}

Her iki yaklaşım da aynı çalışma kitabında birlikte var olabilir. İki mekanizma dosyada farklı depolama katmanları kullandığından, bir hücre kümesinin üzerine kayan resimler yerleştirebilir ve görüntüleri doğrudan diğer hücrelere gömebilirsiniz.

{{% /alert %}}



{{< app/cells/assistant language="python" >}}