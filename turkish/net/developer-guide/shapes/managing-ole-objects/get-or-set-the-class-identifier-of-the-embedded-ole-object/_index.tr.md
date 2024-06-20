---
title: Gömülü OLE Nesnesinin Sınıf Kimliğini Alın veya Ayarlayın
type: docs
weight: 200
url: /tr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, gömülü ole nesnesinin sınıf kimliğini almak veya ayarlamak için [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier) özelliğini sağlar. Ole Nesne Sınıf Kimlikleri aslında GUID'lerdir, yani Küresel Benzersiz Kimliklerdir. GUID her zaman 16 bayt uzunluğundadır, bu nedenle Sınıf Kimlikleri de 16 bayt uzunluğundadır. Genellikle Windows Kaydı içinde bulunurlar ve istemci uygulaması içinde çeşitli gömülü kaynaklar içeren gömülü ole nesnesini nasıl açacağı hakkında bilgi sağlarlar.
## **Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla**
Aşağıdaki ekran görüntüsü, gömülü PowerPoint ole nesnesini içeren [örnek excel dosyasından](5115190.xls) okunmuş olan Ole Nesne Sınıf Kimliğini yani GUID'i göstermektedir.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Örnek Kod**
Lütfen [örnek excel dosyası](5115190.xls) ile yapılan örnek kodu ve konsol çıktısını aşağıda görebilirsiniz. Çıktılanan GUID, ekran görüntüsünde gösterilenle tam olarak aynıdır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Konsol Çıktısı**
Yukarıdaki örnek kod çalıştırıldığında [örnek excel dosyası](5115190.xls) ile konsol çıktısıdır.

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
