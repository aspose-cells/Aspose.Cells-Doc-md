---
title: Katıştırılmış OLE Nesnesinin Sınıf Tanımlayıcısını Alın veya Ayarlayın
type: docs
weight: 920
url: /tr/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **Olası Kullanım Senaryoları**
 Aspose.Cells şunları sağlar:[OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier)katıştırılmış bir ole nesnesinin sınıf tanımlayıcısını almak veya ayarlamak için kullanabileceğiniz özellik. Ole Nesne Sınıfı Tanımlayıcıları aslında GUID'lerdir, yani Global Olarak Benzersiz Tanımlayıcılardır. GUID her zaman 16 bayt uzunluğundadır, bu nedenle Sınıf Tanımlayıcıları da 16 bayt uzunluğundadır. Genellikle Windows Kayıt Defterinde bulunurlar ve istemci uygulamasında çeşitli gömülü kaynakları içeren gömülü ole nesnesinin nasıl açılacağı hakkında ana uygulamaya bilgi sağlarlar.
## **Katıştırılmış OLE Nesnesinin Sınıf Tanımlayıcısını Alın veya Ayarlayın**
 Aşağıdaki ekran görüntüsü, Ole Nesne Sınıfı Tanımlayıcısını, yani kullanıcıdan okunan GUID'yi gösterir.[örnek excel dosyası](5473378.xls) katıştırılmış PowerPoint ole nesnesini içeren.

![yapılacaklar:resim_alternatif_Metin](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Basit kod**
 Lütfen ile yürütülen aşağıdaki örnek koda bakın.[örnek excel dosyası](5473378.xls) ve yazdıran konsol çıktısı*Sınıf Tanımlayıcı*Ole Nesnesi, yani GUID. Yazdırılan GUID, ekran görüntüsünde gösterilenle tamamen aynıdır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Konsol Çıkışı**
 Bu, yukarıdaki örnek kodun aşağıdaki kodla yürütüldüğünde konsol çıktısıdır:[örnek excel dosyası](5473378.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
