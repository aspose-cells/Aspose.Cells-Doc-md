---
title: Gömülü OLE Nesnesinin Sınıf Kimliğini Alın veya Ayarlayın
type: docs
weight: 920
url: /tr/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, gömülü bir ole nesnesinin sınıf kimliğini almak veya ayarlamak için kullanabileceğiniz [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier) özelliğini sağlar. Ole Nesne Sınıf Kimlikleri aslında GUID'lerdir, yani Global Benzersiz Tanımlayıcılar. GUID her zaman 16 bayt uzunluğunda olduğundan, Sınıf Kimlikleri de 16 bayt uzunluğundadır. Sıklıkla Windows Kayıt defterinde bulunurlar ve barındırma uygulamasına gömülü kaynakları içeren gömülü ole nesnesini nasıl açacağı hakkında bilgi sağlarlar.
## **Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla**
Aşağıdaki ekran görüntüsü, gömülü PowerPoint ole nesnesini içeren [örnek excel dosyasından](5473378.xls) okunan Ole Nesne Sınıf Kimliğini, yani GUID'i göstermektedir.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Örnek Kod**
Lütfen [örnek excel dosyasıyla](5473378.xls) çalıştırılmış aşağıdaki örnek kodu ve *Ole Nesne* 'nin *Sınıf Kimliği*’ni yani GUID'ini içeren konsol çıktısını yazdıran konsol çıktısını inceleyin. Yazdırılan GUID, ekran görüntüsünde gösterildiği gibi tamamen aynıdır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Konsol Çıktısı**
Bu, [örnek excel dosyasıyla](5473378.xls) çalıştırıldığında yukarıdaki örnek kodun konsol çıktısıdır.

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
