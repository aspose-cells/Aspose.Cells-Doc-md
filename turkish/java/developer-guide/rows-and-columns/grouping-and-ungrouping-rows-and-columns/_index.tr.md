---
title: Satırları ve Sütunları Gruplandırma ve Grubu Çözme
type: docs
weight: 40
url: /tr/java/grouping-and-ungrouping-rows-and-columns/
---
## **Giriş**
Bir Microsoft Excel dosyasında, tek bir fare tıklamasıyla ayrıntı düzeylerini göstermenize ve gizlemenize olanak tanıyan veriler için bir ana hat oluşturabilirsiniz.

 Tıkla**Anahat Sembolleri**, 1,2,3, + ve - yalnızca bir çalışma sayfasındaki bölümler için özetler veya başlıklar sağlayan satırları veya sütunları hızlı bir şekilde görüntülemek için veya aşağıdaki şekilde gösterildiği gibi ayrıntıları tek bir özet veya başlık altında görmek için sembolleri kullanabilirsiniz. :

 Satırların ve sütunların gruplandırılması

![yapılacaklar:resim_alternatif_metin](grouping-and-ungrouping-rows-and-columns_1.png)
## **Satırlar ve Sütunların Grup Yönetimi**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[çalışma sayfaları](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 bu[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar; bunlardan birkaçı aşağıda daha ayrıntılı olarak ele alınmıştır.
### **Satırları ve Sütunları Gruplama**
 çağırarak satırları veya sütunları gruplandırmak mümkündür.[grupSatırları](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ) ve[grup Sütunları](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) ) yöntemleri[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Toplamak. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun dizini, gruptaki ilk satır veya sütun.
- Son satır/sütun dizini, gruptaki son satır veya sütun.
- Gizlidir, gruplamadan sonra satırların/sütunların gizlenip gizlenmeyeceğini belirten bir Boolean parametresidir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Grup Ayarları**
Microsoft Excel ayrıca aşağıdakileri görüntülemek için grup ayarlarının yapılandırılmasına izin verir:

- Ayrıntıların altındaki özet satırları.
- Ayrıntıların sağındaki özet sütunları.

**Grup ayarları** 

![yapılacaklar:resim_alternatif_metin](grouping-and-ungrouping-rows-and-columns_2.png)

Worksheet sınıfının Outline özelliğini kullanarak bu grup ayarlarını yapılandırmak mümkündür.
### **Detayın Altındaki Özet Satırları**
 Geliştiriciler, ayrıntının altında özet satırlarının görüntülenmesini kontrol edebilir.[Anahat](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) sınıf'[ÖzetSatırAşağıda](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) yöntem.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Ayrıntı Sağındaki Özet Sütunları**
ile detayların sağında özet sütunlarının gösterilip gösterilmeyeceği kontrol edilebilir.[Anahat](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) sınıf'[ÖzetSütunuSağ](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)yöntem.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Satırları ve Sütunları Çözme**
 çağırarak gruplandırılmış satırların veya sütunların grubunu çözün.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[Satırları Çöz](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ) ve[Sütunların Grubunu Çöz](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) yöntemler. Her iki yöntem de aynı parametreleri alır:

- İlk satır veya sütun dizini, grubu çözülecek ilk satır/sütun.
- Son satır veya sütun dizini, grubu çözülecek son satır/sütun.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
