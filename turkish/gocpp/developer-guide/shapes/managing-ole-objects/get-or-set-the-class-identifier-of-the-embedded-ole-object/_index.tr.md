---
title: Golang aracılığıyla C++ ile Gömülü OLE Nesnesinin Sınıf Tanımlayıcısını Alma veya Ayarlama
linktitle: Gömülü OLE Nesnesinin Sınıf Kimliğini Alın veya Ayarlayın
type: docs
weight: 200
url: /tr/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Aspose.Cells ile Golang kullanarak Gömülü OLE nesnelerinin sınıf tanımlayıcısını nasıl alacağınızı veya ayarlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, gömülü OLE nesnesinin sınıf tanımlayıcısını almak veya ayarlamak için kullanabileceğiniz [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/) özelliği sağlar. OLE Nesnesi Sınıf Tanımlayıcıları aslında GUID'lerdir, yani Eşsiz Tanımlayıcılar. GUID her zaman 16 bayt uzunluğundadır, bu nedenle Sınıf Tanımlayıcıları da 16 bayt uzunluğundadır. Genellikle Windows Kayıt Defteri içinde bulunurlar ve ana uygulamaya içerisinde çeşitli gömülü kaynaklar içeren gömülü OLE nesnelerini nasıl açacağınıza dair bilgiler sağlarlar.

## **Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla**
Aşağıdaki ekran görüntüsü, gömülü PowerPoint OLE nesnesi içeren [örnek excel dosyasından](5115190.xls) okunmuş olan OLE Nesnesi Sınıf Tanımlayıcısı, yani GUID'yi gösterir.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Örnek Kod**
Lütfen, [örnek excel dosyasını](5115190.xls) çalıştırılarak ve ekran görüntüsünde gösterilenle birebir aynı olan OLE Nesnesinin Sınıf Tanımlayıcısını, yani GUID'yi yazdıran konsol çıktı ile birlikte örnek kodu inceleyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **Konsol Çıktısı**
Yukarıdaki örnek kod çalıştırıldığında [örnek excel dosyası](5115190.xls) ile konsol çıktısıdır.

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
