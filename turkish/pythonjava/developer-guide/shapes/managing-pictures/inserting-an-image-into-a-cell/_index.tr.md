---
title: Hücreye Resim Ekleme
linktitle: Hücreye Resim Ekleme
description: Aspose.Cells for Python via Java, elektronik tablo dosyalarıyla çalışmak için kullanılan bir kütüphanedir. Bu makale, bir resmi hücrenin üzerine kayan resim yerleştirerek veya görüntüyü doğrudan hücreye gömerek tam olarak tek bir hücreye sığdırmayı açıklamaktadır.
keywords: Aspose.Cells, Python via Java kütüphanesi, elektronik tablo, resim ekleme, görüntü gömme, hücrede resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/python-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir görüntüyü tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanında bir hücre aralığının üzerine görsel olarak yerleştirilen bir şekildir; gömülü görüntü ise hücrenin kendisinin içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.

## **Giriş**
Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan dizinleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlanırken sıkça karşılaşılan bir gereksinimdir. Görüntüyü birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahibi olan hücreyle hizalı kalan, temiz ve hücreye bağlı bir görüntü isteyebilirsiniz.
Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:
- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `setPlacement` özelliğini `MOVE_AND_SIZE` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için çapa hücrelerini (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Görüntüyü doğrudan bir hücreye gömün.** Hücrenin `setEmbeddedImage` özelliğine görüntü baytlarını atayın. Görüntü, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.
Bu makalenin geri kalanı her iki yaklaşımı da adım adım açıklar, ilgili API'leri tanımlar ve bunların kodda nasıl kullanılacağını gösterir.

## **Yaklaşım 1: Hücrenin Üzerine Resim Yerleştirme**
Kayan resim, çalışma sayfası çizim katmanında yaşayan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına tutturulur. Resmin çapa hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kaplar.
Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:
1. Resmi `Worksheet.getPictures().add(int row, int column, InputStream stream)` kullanarak ekleyin; bu yeni resmi belirtilen hücreye tutturur.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört çapa özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `Picture.setPlacement` özelliğini `PlacementType.MOVE_AND_SIZE` olarak ayarlayın.

### **Resmi Tek Bir Hücreye Sabitleme**
Resmin çapası dört sıfır tabanlı indis özelliğiyle tanımlanır:
- `setUpperLeftRow` — resmin üst kenarının satır indisi.
- `setUpperLeftColumn` — resmin sol kenarının sütun indisi.
- `setLowerRightRow` — resmin alt kenarının satır indisi. Resmin alt kenarının `r` satırının altına oturması için bunu `r + 1` olarak ayarlayın.
- `setLowerRightColumn` — resmin sağ kenarının sütun indisi. Resmin sağ kenarının `c` sütununun sağına oturması için bunu `c + 1` olarak ayarlayın.

{{% alert color="primary" %}}
Aspose.Cells'te satır ve sütun indisleri **sıfır tabanlıdır**. C6 hücresinin satır indisi 5, sütun indisi 2'dir. Sağ alt çapadaki bir-bir kayma hataları, resimlerin bitişik hücreye taşmış gibi görünmesinin en yaygın nedenidir.

### **Yerleştirme Davranışını Kontrol Etme**
`getPlacement`, kullanıcı alttaki satır veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir numaralandırmadır. Tek hücrelik bir resim için önerilen değer `PlacementType.MOVE_AND_SIZE`'dır; bu, resmin alttaki hücreyle birlikte hareket etmesini ve yeniden boyutlandırılmasını sağlayarak tam sığmayı korur.

### **Adım Adım Talimatlar**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.getWorksheets().get(0)` üzerinden erişin.
3. Görüntü dosyasını diskten bir `InputStream` olarak (tipik olarak `FileInputStream`) açın, böylece akış düzgün bir şekilde kapatılır.
4. C6 hücresine tutturulmuş bir resim eklemek için `worksheet.getPictures().add(5, 2, stream)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört çapa koordinatını ayarlayın: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalması için `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diske bir `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod tüm yaklaşımı göstermektedir.

## **Yaklaşım 2: Görüntüyü Doğrudan Bir Hücreye Gömme**
Aspose.Cells ayrıca hücreye bağlı görüntüler için daha basit bir mekanizma sunar: `Cell.setEmbeddedImage` özelliği. Bu özelliğe görüntü baytlarını atamak, görüntüyü sanki satır içi içerikmiş gibi hücrenin kendisine ekler.

### **Gömülü Görüntüler Nasıl Çalışır**
- Görüntü, çizim katmanındaki bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Görüntü, hücrenin işlenmiş sınırları içine sığacak şekilde otomatik olarak ölçeklenir. Çapa koordinatları veya yerleştirme ayarları gerekmez.
- Hücre, formüller tarafından başvurulabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen gerçek bir adresle gerçek bir hücre olarak kalır.
Bu, amacınız basitçe "bu hücrenin içinde yaşayan bir görüntü" olduğunda `Cell.setEmbeddedImage`'ı en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.getWorksheets().get(0)` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını diskten bir `byte[]` dizisine okuyun (örneğin `java.nio.file.Files`'tan bir `Files.readAllBytes` çağrısı kullanarak).
4. Hedef hücreye bir referans alın — `worksheet.getCells().get("C6")` veya `worksheet.getCells().get(5, 2)` aracılığıyla.
5. Bayt dizisini hücrenin `setEmbeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü görüntüye daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diske bir `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod tüm yaklaşımı göstermektedir.

## **Doğru Yaklaşımı Seçme**
Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı konusunda farklılık gösterir:
- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı denetime ihtiyacınız olduğunda.
  - Resmin diğer şekillerle birlikte seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil gibi davranmasını istediğinizde.
  - Zaten `PictureCollection` ile çalışan kodla eski sürüm uyumluluğuna ihtiyaç duyduğunuzda.
  - Çalışma sayfası düzenine göre çapa koordinatlarını dinamik olarak hesaplamanız gerektiğinde.
- **Şu durumlarda gömülü görüntü kullanın (Yaklaşım 2):**
  - Bir görüntüyü bir hücreye mümkün olan en basit şekilde eklemek istediğinizde.
  - Görüntünün diğer hücre içerikleri gibi hücreyle birlikte taşınması gerektiğinde.
  - Görüntüyü bir şekil olarak işlemenize gerek olmadığında.
{{% /alert %}}

{{% /alert %}}

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

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Get the target cell C6
cell = worksheet.getCells().get("C6")
# Read the image file into a byte array
imageData = open("logo.png", "rb").read()
# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

{{< app/cells/assistant language="python" >}}