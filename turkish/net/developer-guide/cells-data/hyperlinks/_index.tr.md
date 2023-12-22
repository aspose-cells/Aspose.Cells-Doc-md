---
title: Köprüleri Excel veya OpenOffice'e Ekleme
linktitle: Köprüleri Yönetme
type: docs
weight: 45
url: /tr/net/insert-hyperlinks-to-excel/
description: MS Excel olmadan Aspose.Cells kitaplığıyla Excel dosyasına köprüler nasıl eklenir?
keywords: Insert Hyperlinks into Excel, Add or Insert Hyperlinks, Add or Insert link to a URL, Add or Insert a Link to a Cell, Add a Link to an External File
---
{{% alert color="primary" %}} 

İki varlık arasında bağlantı oluşturmak için köprü kullanılır. Herkes, özellikle web sitelerinde hiper bağlantıların kullanımına aşinadır.
Geliştiriciler, Aspose.Cells'i kullanarak Microsoft Excel dosyalarında farklı türde köprüler oluşturabilir. Bu konu, Aspose.Cells tarafından hangi tür köprülerin desteklendiğini ve bunların Excel dosyalarımızda nasıl kullanılabileceğini açıklamaktadır.

{{% /alert %}} 
##  **Köprü Ekleme**
Aspose.Cells, geliştiricilerin API veya tasarımcı elektronik tablolarını (köprü bağlantılarının manuel olarak oluşturulduğu ve bunları diğer elektronik tablolara aktarmak için Aspose.Cells'in kullanıldığı elektronik tablolar) kullanarak Excel dosyalarına köprüler eklemesine olanak tanır.

 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Bu, Excel dosyasındaki her çalışma sayfasına erişime izin verir. Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıfı, Excel dosyalarına farklı köprüler eklemek için farklı yöntemler sağlar.
##  **Bir URL'ye Bağlantı Ekleme**
[Çalışma kağıdı](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir içerir[Köprüler](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) Toplamak. İçindeki her öğe[Köprüler](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) koleksiyon bir temsil eder[Köprü](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . çağırarak URL'lere köprüler ekleyin.[Köprüler](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Koleksiyonun[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntem.[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)yöntem aşağıdaki parametreleri alır:

- Cell ad, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı
- URL, URL adresi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

Yukarıdaki örnekte, *A1** boş hücresindeki bir URL'ye bir köprü eklenmiştir. Bu gibi durumlarda, eğer bir hücre boşsa URL adresi de o boş hücreye değer olarak eklenir. Hücre boş değilse ve köprü eklenmişse hücrenin değeri düz metin gibi görünür. Köprü gibi görünmesini sağlamak için o hücreye uygun biçimlendirme ayarlarını uygulayın.

{{% /alert %}} 
##  **Aynı Dosyadaki Cell'e Bağlantı Ekleme**
 Aynı Excel dosyasındaki hücrelere köprüleri çağırmak mümkündür.[Köprüler](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Koleksiyonun[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntem.[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)yöntem hem iç hem de dış köprüler için çalışır. Aşırı yüklenmiş yöntemin bir sürümü aşağıdaki parametreleri alır:

- Cell ad,köprü bağlantısının ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
##  **Harici Dosyaya Bağlantı Ekleme**
 çağrılarak harici Excel dosyalarına köprüler eklemek mümkündür.[Köprüler](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Koleksiyonun[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) yöntem.[Eklemek](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)yöntem aşağıdaki parametreleri alır:

- Cell ad, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı.
- URL, hedefin adresi, harici Excel dosyası.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

##  **İleri konular**
- [Resim Köprüleri Ekle](/cells/tr/net/add-image-hyperlinks/)
- [Köprü Türünü Algıla](/cells/tr/net/detect-hyperlink-type/)
- [Çalışma Sayfasının Köprülerini Düzenleme](/cells/tr/net/editing-hyperlinks-of-worksheet/)
- [Menzildeki Köprüleri Alın](/cells/tr/net/get-hyperlinks-in-range/)

