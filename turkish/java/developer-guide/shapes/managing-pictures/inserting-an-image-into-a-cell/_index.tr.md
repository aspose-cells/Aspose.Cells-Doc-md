---
title: Bir Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir Java kütüphanesidir. Bu makale, bir resmi iki farklı yaklaşımla tam olarak tek bir hücre boyutuna sığdırmayı açıklar, hücrenin üzerine kayan bir resim yerleştirmek veya resmi doğrudan hücrenin içine gömmek.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, resim ekleme, resmi gömme, hücredeki resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells, bir resmi tek bir hücreyle ilişkilendirmenin iki farklı yolunu sunar. Kayan resim, çalışma sayfası çizim katmanında bulunan ve bir hücre aralığının üzerinde görsel olarak yer alan bir şekildir; gömülü resim ise hücrenin kendisinin içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Yerleşim gereksinimlerinize en uygun yaklaşımı seçin.

{{% /alert %}}

## **Giriş**

Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlanırken sık karşılaşılan bir gereksinimdir. Resmi birçok hücreye yayarak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahip olduğu hücreyle hizalı kalan temiz, hücreye bağlı bir resim isteyebilirsiniz.

Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:

- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `Placement` özelliğini `MOVE_AND_SIZE` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için bağlantı hücrelerini (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Bir resmi doğrudan bir hücreye gömün.** Resim baytlarını hücrenin `getEmbeddedImage()` ayarlayıcısına atayın. Resim, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.

Bu makalenin geri kalanı her iki yaklaşımı da adım adım açıklar, ilgili API'leri anlatır ve bunların kodda nasıl kullanılacağını gösterir.

## **Yaklaşım 1: Hücrenin Üzerine Bir Resim Yerleştirme**

Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına bağlıdır. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kapsar.

Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:

1. `Worksheet.getPictures().add(int row, int column, InputStream stream)` kullanarak resmi ekleyin; bu yöntem, yeni resmi verilen hücreye bağlar.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört bağlantı özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `Picture.setPlacement()` özelliğini `PlacementType.MOVE_AND_SIZE` olarak ayarlayın.

### **Resmi Tek Bir Hücreye Bağlama**

Resmin bağlantısı, sıfır tabanlı dört dizin özelliği ile tanımlanır:

- `Picture.getUpperLeftRow()` — resmin üst kenarının satır dizini.
- `Picture.getUpperLeftColumn()` — resmin sol kenarının sütun dizini.
- `Picture.getLowerRightRow()` — resmin alt kenarının satır dizini. Resmin alt kenarını `r` satırının altına yerleştirmek için bunu `r + 1` olarak ayarlayın.
- `Picture.getLowerRightColumn()` — resmin sağ kenarının sütun dizini. Resmin sağ kenarını `c` sütununun sağına yerleştirmek için bunu `c + 1` olarak ayarlayın.

Örneğin, resmi tam olarak **C6** hücresine (satır dizini `5`, sütun dizini `2`) sığdırmak için `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` ve `setLowerRightColumn(3)` ayarlayın.

{{% alert color="primary" %}}

Aspose.Cells'deki satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt bağlantı noktasındaki bir-bir-fazla hataları, resimlerin bitişik hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

{{% /alert %}}

### **Yerleşim Davranışını Kontrol Etme**

`Picture.getPlacement()`, kullanıcı alttaki satırı veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir enum döndürür. Tek hücreli bir resim için önerilen değer `PlacementType.MOVE_AND_SIZE`'dır; bu değer, resmin alttaki hücreyle birlikte hareket etmesini ve yeniden boyutlandırılmasını sağlayarak tam sığdırmayı korur.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.getWorksheets().get(0)` üzerinden erişin.
3. Akışın düzgün bir şekilde kapatılması için try-with-resources bloğu kullanarak görüntü dosyasını diskten bir `InputStream`'e (örneğin bir `FileInputStream`) açın.
4. Resmi C6 hücresine bağlı olarak eklemek için `worksheet.getPictures().add(5, 2, stream)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört bağlantı koordinatını ayarlayın: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalması için `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resim içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, tüm yaklaşımı gösterir.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

try (FileInputStream fs = new FileInputStream("logo.png"))
{
    int picIndex = worksheet.getPictures().add(5, 2, fs);
    Picture picture = worksheet.getPictures().get(picIndex);
    picture.setUpperLeftRow(5);
    picture.setUpperLeftColumn(2);
    picture.setLowerRightRow(6);
    picture.setLowerRightColumn(3);
    picture.setPlacement(PlacementType.MOVE_AND_SIZE);
}

workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Yaklaşım 2: Bir Resmi Doğrudan Bir Hücreye Gömme**

Aspose.Cells ayrıca hücreye bağlı resimler için daha basit bir mekanizma sunar: `Cell.setEmbeddedImage(byte[])` yöntemi. Bu özelliğe resim baytları atamak, resmi satır içi içerikmiş gibi hücrenin kendisine ekler.

### **Gömülü Resimler Nasıl Çalışır**

- Resim, çizim katmanında bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Resim, hücrenin oluşturulan sınırlarının içine sığacak şekilde otomatik olarak ölçeklenir. Herhangi bir bağlantı koordinatı veya yerleşim ayarı gerekmez.
- Hücre, formüller tarafından başvurulabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen, gerçek bir adrese sahip gerçek bir hücre olarak kalır.

Bu, amacınızın yalnızca "bu hücrenin içinde yaşayan bir resim" olduğu durumlarda `setEmbeddedImage()` yöntemini en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.getWorksheets().get(0)` üzerinden erişin.
3. Görüntü dosyasını diskten bir `byte[]` dizisine okuyun (örneğin, `java.nio.file` üzerinden `Files.readAllBytes()` ile dosyayı okuyarak).
4. Hedef hücreye bir referans alın — `worksheet.getCells().get("C6")` veya `worksheet.getCells().get(5, 2)` üzerinden.
5. Bayt dizisini `cell.setEmbeddedImage(bytes)` kullanarak hücreye atayın.
6. İsteğe bağlı olarak, gömülü resme daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, tüm yaklaşımı gösterir.

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// C6 hedef hücresini al
Cell cell = worksheet.getCells().get("C6");

// Görüntü dosyasını bir bayt dizisine oku
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));

// Görüntüyü doğrudan hücreye göm
cell.setEmbeddedImage(imageData);

// Gömülü görüntünün daha görünür olması için isteğe bağlı olarak satır yüksekliğini ve sütun genişliğini ayarla
worksheet.getCells().setColumnWidth(2, 30);   // C Sütunu (indeks 2)
worksheet.getCells().setRowHeight(5, 100);     // 6. Satır (indeks 5)

// Elde edilen çalışma kitabını .xlsx dosyası olarak kaydet
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Doğru Yaklaşımı Seçme**

Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı konusunda farklılık gösterir:

- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleşim, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı kontrol gerektiğinde.
  - Resmin diğer şekillerle birlikte seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten `PictureCollection` ile çalışan kodlarla eski uyumluluk gerektiğinde.
  - Çalışma sayfası düzenine göre bağlantı koordinatlarını dinamik olarak hesaplamanız gerektiğinde.

- **Şu durumlarda gömülü resim kullanın (Yaklaşım 2):**
  - Bir hücreye resim eklemenin en basit olası yolunu istediğinizde.
  - Resim, diğer hücre içerikleri gibi hücreyle birlikte taşınmalıdır.
  - Resmi bir şekil olarak değiştirmeniz gerekmiyorsa.

{{% alert color="primary" %}}

Her iki yaklaşım da aynı çalışma kitabında birlikte var olabilir. İki mekanizma dosyada farklı depolama katmanları kullandığından, bir hücre kümesinin üzerine kayan resimler yerleştirebilir ve diğer hücrelere doğrudan resim gömebilirsiniz.

{{% /alert %}}



{{< app/cells/assistant language="java" >}}