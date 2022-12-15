---
title: Satırları Gruplandırma ve Ara Toplam Oluşturma
type: docs
weight: 70
url: /tr/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, verileriniz için bir taslak oluşturabilir. Bu, yalnızca bir çalışma sayfasındaki bölümler için özetler veya başlıklar sağlayan satırları görüntülemek için "+" ve "-" anahat simgelerini tıklatarak ayrıntı düzeylerini göstermenizi ve gizlemenizi sağlar. Ayrıntıları ayrı bir özet veya başlık altında görmek için sembolleri kullanabilirsiniz.

Satırları gruplandırırken sadece grubu oluşturan detay satırlarını seçmek önemlidir. İlgili özet satırını dahil etmeyin. Örneğin, 6. satır 3 ile 5 arasındaki veriler için toplamları içeriyorsa, grubu tanımlamak için yalnızca 3 ile 5 arasındaki satırları seçin. Aspose.Cells.GridWeb denetimi,**detayları göster** (+) ve**ayrıntıyı gizle** Çalışma sayfasındaki grupları belirten satır başlıklarının yanındaki (-) simgeleri.

Aspose.Cells.GridWeb, herhangi bir veri alanına dayalı ara toplamlar oluşturmanıza da olanak tanır. Ara toplam mutlaka bir toplam değildir: Ortalama, sayma, minimum, maksimum veya başka bir istatistiksel hesaplama olabilir.

Bu konu, Aspose.Cells.GridWeb API'i kullanarak satırları gruplandırmayı ve alt toplamlar oluşturmayı ele alır. Geliştiriciler, satırları herhangi bir iç içe geçme düzeyiyle gruplayabilir ve kolayca alt toplamlar oluşturabilir.

{{% /alert %}} 
## **Satırları Gruplama**
Belirli sayıda satırı gruplandırmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışma sayfasına erişin.
1. Satırlarda istenen hücre sayısını seçin.
1. Satırları gruplandırın.

Satırlar gruplandığında, satırların Özet Satırı'nın üstünde bir genişlet/daralt düğmesi görüntülenir. Yön ayarını değiştirebilirsiniz. WebWorksheet.IsSummaryRowBelow özelliği bir Boolean özelliğidir. Bunu false (varsayılan) olarak ayarlayın, özet satırı ayrıntı satırlarının üzerinde olacaktır. Bunu true olarak ayarlayın ve özet satırı ayrıntı satırlarının altında olacaktır. Gruplandırılmış satırları genişletmek veya daraltmak için genişlet/daralt düğmesine tıklayın.

Aşağıdaki örnek, satırları 2. sıradan 10. sıraya kadar gruplandırır.

**Satırları gruplama** 

![yapılacaklar:resim_alternatif_Metin](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Gruplandırılmış Satırları İç İçe Yerleştirme**
Bir dizi satırı gruplandırırken organizasyon seviyeleri oluşturabilirsiniz. Gruplandırılmış satırlar arasında satırları gruplandırabilirsiniz. Aşağıdaki örnek, iç içe geçmiş gruplandırılmış satırları göstermektedir.

**Satırları gruplama** 

![yapılacaklar:resim_alternatif_Metin](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Dahili Süreç: Kontrol Nasıl Çalışır?**
Sayfanın her satırının bir anahat numarası vardır. Ana hat numarasının varsayılan değeri sıfırdır. Satırları her grupladığınızda anahat numarası 1 artar. Anahat numarasını GridWorksheet.Cells.GetRowOutlineLevel() yöntemini çağırarak alabilirsiniz.
## **Satırların Grubunu Çöz**
Aspose.Cells.GridWeb, gruplandırılmış satırların grubunu çözmenizi sağlar.

Belirli sayıda satırın grubunu çözmek için:

1. Grubu çözmek için çalışma sayfasındaki satırlarda bir dizi hücre seçin.
1. Satırların grubunu çözün.

Aşağıdaki örnek, 2. satırdan 10. satıra kadar olan satırların grubunu çözer.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

GridWorksheet.Cells.UngroupRows() yöntemini çağırdığınızda, gruplandırılmış satırların anahat numarası sıfır olarak ayarlanır.

{{% /alert %}} 
## **Ara Toplam Oluşturma**
Kontrolün ara toplam özelliği, sayfadaki satırları belirli bir sütunla gruplandırabilir ve sütunların özetini hesaplayabilir. Aspose.Cells.GridWeb, bir liste için ara toplam değerlerini otomatik olarak hesaplayabilir. Alt toplamları uyguladığınızda, kontrol, her bir alt toplam için ayrıntı satırlarını görüntüleyip gizleyebilmeniz için listenin ana hatlarını çizer. Ara toplamları eklemeden önce, ara toplam yapmak istediğiniz alana göre sıralayın. Ara toplamlar oluşturmak için aşırı yüklenmiş WebWorksheet.CreateSubtotal yönteminin herhangi bir sürümünü kullanın.



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **Parametre Listesi**

|**Numara.**|**Parametre adı**|**Tanım**|
|:- |:- |:- |
|1|sütunAdıSatırIndex|Sütun adı satırının satır dizini.|
|2|veriSatırları|Veri satırlarının sayısı.|
|3|groupByColumnIndex|Gruplanacak sütunun sütun dizini.|
|4|ara toplamFonksiyonu|Alt toplam işlev türü sıralaması.|
|5|ara toplamSütunDizinListesi|Alt toplamı alınacak sütun dizinleri.|
### **Özet Fonksiyon Listesi**
{[SubtotalFunction}} numaralandırması tarafından desteklenen birkaç tür özet işlevi vardır:

|**Numara.**|**Fonksiyon adı**|**Tanım**|
|:- |:- |:- |
|1|ORTALAMA|Değerlerin ortalamasını hesaplar.|
|2|SAYMAK|Hücrelerdeki sayısal değerleri sayar.|
|3|SAYI|Hücrelerdeki sayısal olmayan verileri sayar.|
|4|MAKS.|En büyük değeri hesaplar.|
|5|DAK|En küçük değeri hesaplar.|
|6|ÜRÜN|Değerlerin çarpımını hesaplar.|
|7|TOPLAM|Değerlerin toplamını hesaplar.|
Aşağıdaki örnek, çalışma sayfasındaki ikinci sütuna göre gruplandırılmış sayısal olmayan değerleri hesaplayan ara toplamları oluşturur.

**ara toplamlar** 

![yapılacaklar:resim_alternatif_Metin](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Ara Toplamı Kaldırma**
Bir ara toplamı kaldırmak için WebWorksheet.RemoveSubtotal yöntemini kullanın. Aşağıdaki örnek, alt toplamları kaldırır.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **ALT TOPLAM işlevi hakkında**
GridWeb denetimi, ara toplam değerini hesaplamak için ALT TOPLAM formül işlevini kullanır.

Sözdizimi: ALT TOPLAM(işlev_sayısı, başv1, başv2, ...)

işlev_num ara toplam hesaplamasında kullanılan işlevin türünü belirten bir sayıdır.

|**1**|**ORTALAMA**|
|:- |:- |
|2|SAYMAK|
|3|SAYI|
|4|MAKS.|
|5|DAK|
|6|ÜRÜN|
|7|TOPLAM|
ref1, ref2, alt toplamı alınacak alanlardır. ref1, ref2, ... başka ara toplam işlevleri içeriyorsa, yinelenen hesaplamayı önlemek için başvurulan hücreler dikkate alınmaz.
