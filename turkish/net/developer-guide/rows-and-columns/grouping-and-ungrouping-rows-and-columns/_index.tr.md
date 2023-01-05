---
title: Satırları ve Sütunları Gruplandırma ve Grubu Çözme
type: docs
weight: 50
url: /tr/net/grouping-and-ungrouping-rows-and-columns/
---
## **Giriş**

Bir Microsoft Excel dosyasında, tek bir fare tıklamasıyla ayrıntı düzeylerini göstermenize ve gizlemenize olanak tanıyan veriler için bir ana hat oluşturabilirsiniz.

 Tıkla**Anahat Sembolleri**, 1,2,3, + ve - yalnızca bir çalışma sayfasındaki bölümler için özetler veya başlıklar sağlayan satırları veya sütunları hızlı bir şekilde görüntülemek için veya aşağıdaki şekilde gösterildiği gibi ayrıntıları tek bir özet veya başlık altında görmek için sembolleri kullanabilirsiniz. :

|**Satırları ve Sütunları Gruplandırma.**|
|:- |
|![yapılacaklar:resim_alternatif_metin](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Satır ve Sütunların Grup Yönetimi**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 bu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar; bunlardan birkaçı aşağıda daha ayrıntılı olarak ele alınmıştır.

### **Satırları ve Sütunları Gruplama**

 çağırarak satırları veya sütunları gruplandırmak mümkündür.[**GrupSatırları**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) ve[**Grup Sütunları**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) yöntemleri[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun dizini, gruptaki ilk satır veya sütun.
- Son satır/sütun dizini, gruptaki son satır veya sütun.
- Gizlidir, gruplamadan sonra satırların/sütunların gizlenip gizlenmeyeceğini belirten bir Boolean parametresidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Grup Ayarları**

Microsoft Excel, aşağıdakileri görüntülemek için grup ayarlarını yapılandırmanıza izin verir:

- Ayrıntıların altındaki özet satırları.
- Ayrıntıların sağındaki özet sütunları.

 Geliştiriciler, bu grup ayarlarını[**Anahat**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) mülkiyeti[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf.

### **Ayrıntı Altına Özet Satırları**

 Ayarlayarak özet satırlarının ayrıntıların altında görüntülenip görüntülenmediğini kontrol etmek mümkündür.[**Anahat**](https://reference.aspose.com/cells/net/aspose.cells/outline) sınıf'[**ÖzetSatırAşağıda**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) mülkiyet**doğru** veya**YANLIŞ**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Ayrıntı Sağındaki Özet Sütunları**

 Geliştiriciler ayrıca, ayrıntının sağında özet sütunlarının görüntülenmesini ayarlayarak kontrol edebilir.[**ÖzetSütunuSağ**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) mülkiyet[**Anahat**](https://reference.aspose.com/cells/net/aspose.cells/outline) sınıf**doğru** veya**YANLIŞ**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Satırları ve Sütunları Çözme**

 Gruplanmış herhangi bir satır veya sütunun grubunu çözmek için,[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonun[**Satırları Çöz**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) ve[**Sütunların Grubunu Çöz**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)yöntemler. Her iki yöntem de iki parametre alır:

- İlk satır veya sütun dizini, grubu çözülecek ilk satır/sütun.
- Son satır veya sütun dizini, grubu çözülecek son satır/sütun.

[**Satırları Çöz**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) bir Boole üçüncü parametresi alan bir aşırı yüke sahiptir. ayarlanıyor**doğru**gruplandırılmış tüm bilgileri kaldırır. Aksi takdirde sadece dış grup bilgisi kaldırılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
