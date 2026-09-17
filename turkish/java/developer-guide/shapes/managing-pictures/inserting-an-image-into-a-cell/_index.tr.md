---
title: Bir Hücreye Resim Ekleme
linktitle: Bir Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir Java kütüphanesidir. Bu makale, bir hücrenin üzerine kayan bir resim yerleştirerek veya görüntüyü doğrudan hücreye gömerek, bir resmi tam olarak tek bir hücreye sığdırmayı açıklar.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, resim ekleme, resim gömme, hücrede resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir görüntüyü tek bir hücreyle ilişkilendirmenin iki farklı yolunu sunar. Kayan resim, çalışma sayfasının çizim katmanında bir hücre aralığının üzerine görsel olarak yerleşen bir şekildir, gömülü görüntü ise hücrenin kendisinin içinde depolanır ve hücrenin görüntü alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.
{{% /alert %}}

## **Introduction**
Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan dizinleri, panolar veya envanter listeleri gibi elektronik tablolar tasarlarken yaygın bir gereksinimdir. Bir görüntüyü birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahibi olan hücreyle hizalı kalan temiz, hücreye bağlı bir resim isteyebilirsiniz.
Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:
- **Yaklaşım 1 — Bir hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `Placement` özelliğini `MOVE_AND_SIZE` olarak ayarlayın ve bağlantı hücrelerini (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) resmin tam olarak bir hücreyi kaplayacağı şekilde ayarlayın.
- **Yaklaşım 2 — Bir görüntüyü doğrudan bir hücreye gömün.** Görüntü baytlarını hücrenin `getEmbeddedImage()` ayarlayıcısına atayın. Görüntü, hücrenin görüntü alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte hareket eder.
Bu makalenin geri kalanı her iki yaklaşımı adım adım açıklar, ilgili API'leri anlatır ve bunların kodda nasıl kullanılacağını gösterir.

## **Approach 1: Place a Picture Over a Cell**
Kayan resim, çalışma sayfasının çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da, bir hücre aralığına bağlıdır. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreye yayılır.
Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:
1. Resmi `Worksheet.getPictures().add(int row, int column, InputStream stream)` kullanarak ekleyin; bu yöntem yeni resmi verilen hücreye bağlar.
2. Resmin sınırlayıcı dikdörtgeninin hedef hücreyle çakışması için dört bağlantı özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin temel alınan hücreyle birlikte taşınması ve yeniden boyutlandırılması için `Picture.setPlacement()` değerini `PlacementType.MOVE_AND_SIZE` olarak ayarlayın.

### **Anchoring the Picture to a Single Cell**
Resmin bağlantısı, sıfır tabanlı dört indeks özelliğiyle tanımlanır:
- `Picture.getUpperLeftRow()` — resmin üst kenarının satır indeksi.
- `Picture.getUpperLeftColumn()` — resmin sol kenarının sütun indeksi.
- `Picture.getLowerRightRow()` — resmin alt kenarının satır indeksi. Resmin alt kenarının `r` satırının alt kısmında bitmesini sağlamak için bunu `r + 1` olarak ayarlayın.
- `Picture.getLowerRightColumn()` — resmin sağ kenarının sütun indeksi. Resmin sağ kenarının `c` sütununun sağ kısmında bitmesini sağlamak için bunu `c + 1` olarak ayarlayın.

{{% alert color="primary" %}}
Aspose.Cells'deki satır ve sütun indisleri **sıfır tabanlıdır**. C6 hücresinin satır indeksi 5, sütun indeksi 2'dir. Sağ alt bağlantı noktasındaki bir-bir dışı hatalar, resimlerin bitişik bir hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

### **Controlling Placement Behavior**
`Picture.getPlacement()`, kullanıcı alttaki satırı veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir enum döndürür. Tek hücreli resim için önerilen değer `PlacementType.MOVE_AND_SIZE`'dir; bu değer, resmin temel alınan hücreyle birlikte taşınmasına ve yeniden boyutlandırılmasına neden olarak tam sığmayı korur.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.getWorksheets().get(0)` üzerinden erişin.
3. Görüntü dosyasını diskten bir `InputStream`'e (örneğin bir `FileInputStream`) try-with-resources bloğu kullanarak açın; böylece akış düzgün şekilde kapatılır.
4. C6 hücresine bağlı bir resim eklemek için `worksheet.getPictures().add(5, 2, stream)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kapsaması için dört bağlantı koordinatını ayarlayın: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalması için `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resim içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod, tam yaklaşımı gösterir.

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

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells ayrıca hücreye bağlı görüntüler için daha basit bir mekanizma sunar: `Cell.setEmbeddedImage(byte[])` yöntemi. Bu özelliğe görüntü baytları atamak, görüntüyü satır içi içerikmiş gibi hücrenin kendisine ekler.

### **How Embedded Images Work**
- Görüntü, çizim katmanındaki bir şekil yerine hücre içeriğinin bir parçası olarak depolanır.
- Görüntü, hücrenin işlenmiş sınırlarına sığacak şekilde otomatik olarak ölçeklenir. Hiçbir bağlantı koordinatı veya yerleştirme ayarı gerekmez.
- Hücre, formüller tarafından başvurulabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.
Bu, amacınız yalnızca "bu hücrenin içinde yaşayan bir görüntü" olduğunda `setEmbeddedImage()` yöntemini en kısa seçenek haline getirir.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.getWorksheets().get(0)` üzerinden erişin.
3. Görüntü dosyasını diskten bir `byte[]` dizisine okuyun (örneğin, `java.nio.file`'dan `Files.readAllBytes()` aracılığıyla dosyayı okuyarak).
4. Hedef hücreye bir referans alın — `worksheet.getCells().get("C6")` veya `worksheet.getCells().get(5, 2)` aracılığıyla.
5. Bayt dizisini `cell.setEmbeddedImage(bytes)` kullanarak hücreye atayın.
6. İsteğe bağlı olarak, gömülü görüntüye daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod, tam yaklaşımı gösterir.

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Get the target cell C6
Cell cell = worksheet.getCells().get("C6");
// Read the image file into a byte array
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));
// Embed the image directly into the cell
cell.setEmbeddedImage(imageData);
// Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30);   // Column C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Row 6 (index 5)
// Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Choosing the Right Approach**
Her iki yaklaşım da tek bir hücreye sığan bir resim üretir, ancak resmin nasıl depolandığı ve nasıl davrandığı konusunda farklılık gösterir:
- **Aşağıdaki durumlarda kayan resim (Yaklaşım 1) kullanın:**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı denetime ihtiyacınız olduğunda.
  - Resmin diğer şekillerle birlikte seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - `PictureCollection` ile zaten çalışan kodla eski sürüm uyumluluğu gerektirdiğinizde.
  - Çalışma sayfası düzenine göre bağlantı koordinatlarını dinamik olarak hesaplamanız gerektiğinde.
- **Aşağıdaki durumlarda gömülü görüntü (Yaklaşım 2) kullanın:**
  - Bir hücreye bir görüntünün mümkün olan en basit şekilde eklenmesini istediğinizde.
  - Görüntü, diğer tüm hücre içerikleri gibi hücreyle birlikte hareket etmelidir.
{{% /alert %}}

## Related Articles
- [Aspose.Cells for Java'da Excel Camera](/cells/tr/java/excel-camera/)
- [Aspose.Cells for Java'da Bir Pivot Tablosuna Filtre Alanları Ekleme](/cells/tr/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java'da Pivot Tablolarına Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/java/change-page-field-layout/)
- [Aspose.Cells for Java'da Sparkline'ı Görüntüye ve HTML'ye Dönüştürme](/cells/tr/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}