---
title: Satırları Grupla ve Ara Toplam Oluştur
type: docs
weight: 70
url: /tr/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: Bu makale, satırlar/sütunları gruplandırma/ayrıştırma ve GridWeb de ara toplamlarla nasıl çalışılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, verileriniz için bir anahat oluşturabilir. Bu, çalışma sayfasındaki bölümlerin özetlerini veya başlıklarını göstermek ve gizlemek için özet simgelerini tıklatarak ayrıntıların düzeylerini gösterme ve gizleme izni verir. Özet simgelerini kullanarak yalnızca özetlerin veya başlıkların sunulduğu satırları görüntülemek için simgeleri kullanabilirsiniz. İlgili özet satırını dahil etmeyin. Örneğin, 6. satır 3 ile 5 arasındaki verilerin toplamlarını içeriyorsa, grup tanımlamak için yalnızca 3 ile 5 arasındaki satırları seçmelisiniz. Aspose.Cells.GridWeb kontrolü, çalışma sayfasındaki grupları belirten satır başlıklarının yanına **detayları göster** (+) ve **detayları gizle** (-) simgelerini görüntüler.

Satırları grupladığınızda, grup oluşturan ayrıntı satırlarını seçmek önemlidir. İlgili özet satırı dahil etmeyin. Örneğin, 6. satır, 3 ile 5 arasındaki verilerin toplamlarını içeriyorsa, grubu tanımlamak için yalnızca 3 ile 5 arasındaki satırları seçin. Aspose.Cells.GridWeb kontrolü, çalışma sayfasındaki grupları belirten satır başlıklarının yanına **detayları göster** (+) ve **detayları gizle** (-) simgelerini görüntüler.

Aspose.Cells.GridWeb ayrıca herhangi bir veri alanına dayalı olarak ara toplamlar oluşturmanıza olanak tanır. Bir ara toplam mutlaka bir toplam olmak zorunda değildir: Ortalama, sayma, minimum, maksimum veya diğer istatistiksel hesaplama olabilir.

Bu konu, Aspose.Cells.GridWeb API'sını kullanarak satırları gruplama ve ara toplamlar oluşturma üzerine tartışmaktadır. Geliştiriciler, herhangi bir yerleşik seviye ile satırları gruplayabilir ve ara toplamlar oluşturabilirler.

{{% /alert %}} 
## **Satırları Gruplama**
Belirli bir sayıdaki satırları gruplamak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışsayı açın.
1. Satırlardaki istenen hücreleri seçin.
1. Satırları gruplayın.

Satırlar gruplandığında, satır Özet Satırının üstünde genişletme/daraltma düğmesi görüntülenir. Yön ayarını değiştirebilirsiniz. WebWorksheet.IsSummaryRowBelow özelliği bir Boole özelliğidir. Varsayılan olarak false (yanlış) olarak ayarlayın ve özet satır detay satırlarının üstünde olacaktır. True olarak ayarlayın ve özet satır detay satırlarının altında olacaktır. Gruplanmış satırları genişletmek veya daraltmak için genişletme/daraltma düğmesini tıklayın.

Aşağıdaki örnek, 2. sıradan 10. sıraya kadar olan satırları gruplar.

**Satırları Gruplama** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Yerleşik Satırların Gruplanması**
Bir dizi satırı gruplarken düzen seviyeleri oluşturabilirsiniz. Gruplanmış satırlar arasında satırları gruplayabilirsiniz. Aşağıdaki örnek, yerleşik satırların gruplanmasını göstermektedir.

**Satırları Gruplama** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Dahili İşlem: Kontrol Nasıl Çalışır?**
Sayfanın her satırında bir anahat numarası bulunmaktadır. Anahat numarasının varsayılan değeri sıfırdır. Satırları her grupladığınızda, anahat numarası 1 artar. GridWorksheet.Cells.GetRowOutlineLevel() yöntemini çağırarak anahat numarasını alabilirsiniz.
## **Satırları Ayrıştırma**
Aspose.Cells.GridWeb, gruplanmış satırları ayırmanıza olanak tanır.

Belirli bir sayıdaki satırları ayırmak için:

1. Çalışma sayfasındaki satırlardaki hücrelerin belirli bir sayısını seçin.
1. Satırları ayırın.

Aşağıdaki örnek, 2. satırdan 10. satıra kadar olan satırları ayırır.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

GridWorksheet.Cells.UngroupRows() yöntemini çağırdığınızda, gruplanmış satırların anahat numarası sıfırlanır.

{{% /alert %}} 
## **Ara Toplam Oluşturma**
Kontrolün ara toplam özelliği, belirli bir sütuna göre sayfaların satırlarını gruplayabilir ve sütunların özetini hesaplayabilir. Aspose.Cells.GridWeb, bir liste için otomatik olarak ara toplam değerlerini hesaplayabilir. Ara toplamları uygularken kontrol, her bir ara toplam için detay satırlarını göstermek veya gizlemek için listeyi açıklar. Ara toplamları eklemeden önce, ara toplamları oluşturmak istediğiniz alanı sıralayın. Ara toplamları oluşturmak için, WebWorksheet.CreateSubtotal yönteminin herhangi bir yüklenmiş sürümünü kullanın.



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **Parametre Listesi**

|**No.**|**Parametre Adı**|**Açıklama**|
| :- | :- | :- |
|1|columnNameRowIndex|Sütun adı satırının satır indeksi.|
|2|dataRows|Veri satırlarının sayısı.|
|3|groupByColumnIndex|Gruba alınacak sütunun sütun indeksi.|
|4|subtotalFunction|Alt toplam fonksiyonu tipi numaralandırması.|
|5|subtotalColumnIndexList|Alt toplama alınacak sütun indeksleri.|
### **Özet Fonksiyonları Listesi**
{[SubtotalFunction}} numaralandırması tarafından desteklenen çeşitli özet fonksiyon türleri bulunmaktadır:

|**No.**|**Fonksiyon Adı**|**Açıklama**|
| :- | :- | :- |
|1|AVERAGE|Değerlerin ortalamasını hesaplar.|
|2|COUNT|Hücrelerdeki sayısal değerleri sayar.|
|3|COUNTA|Hücrelerdeki sayısal olmayan verileri sayar.|
|4|MAX|En büyük değeri hesaplar.|
|5|MIN|En küçük değeri hesaplar.|
|6|PRODUCT|Değerlerin çarpımını hesaplar.|
|7|SUM|Değerlerin toplamını hesaplar.|
Aşağıdaki örnek, çalışma sayfasındaki ikinci sütuna göre gruplanan sayısal olmayan değerleri hesaplayan alt toplamları oluşturur.

**Alt Toplamlar** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Alt Toplamı Kaldırma**
Bir alt toplamı kaldırmak için WebWorksheet.RemoveSubtotal yöntemini kullanın. Aşağıdaki örnek alt toplamları kaldırır.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **SUBTOTAL işlevi hakkında**
GridWeb kontrolü, alt toplam değerini hesaplamak için formül işlevi SUBTOTAL'i kullanır.

Sözdizimi: SUBTOTAL(fonksiyon_num, ref1, ref2, ...)

function_num, alt toplam hesaplamasında kullanılan fonksiyon türünü belirten bir numaradır.

|**1**|**ORTALAMA**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1, ref2, ..., alt toplam işlevleri içeriyorsa, referans alınan hücreler, çift hesaplama önlemek için yok sayılır.
