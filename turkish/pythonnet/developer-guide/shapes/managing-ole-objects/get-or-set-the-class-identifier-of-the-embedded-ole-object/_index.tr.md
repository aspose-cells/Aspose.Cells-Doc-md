---
title: Gömülü OLE Nesnesinin Sınıf Kimliğini Alın veya Ayarlayın
type: docs
weight: 200
url: /tr/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for Python via .NET, gömülü ole nesnesinin sınıf tanımlayıcısını almak veya ayarlamak için kullanılabilecek [OleObject.class_identifier](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier) özelliğini sağlar. Ole Nesne Sınıf Tanımlayıcıları aslında GUID’lerdir, yani Küresel Benzersiz Tanımlayıcılar. GUID her zaman 16 bayt uzunluğundadır, bu nedenle Sınıf Tanımlayıcıları da 16 bayt uzunluğundadır. Bunlar genellikle Windows Kayıt Defteri içinde bulunur ve çeşitli gömülü kaynaklar içeren gömülü ole nesnesini açmak için ana uygulamaya bilgi sağlar.

## **Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla**
Aşağıdaki ekran görüntüsü, gömülü PowerPoint ole nesnesini içeren [örnek excel dosyasından](5115190.xls) okunmuş olan Ole Nesne Sınıf Kimliğini yani GUID'i göstermektedir.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Örnek Kod**
Lütfen [örnek excel dosyası](5115190.xls) ile yapılan örnek kodu ve konsol çıktısını aşağıda görebilirsiniz. Çıktılanan GUID, ekran görüntüsünde gösterilenle tam olarak aynıdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-GetSetClassIdentifierEmbedOleObject.py" >}}

### **Konsol Çıktısı**
Yukarıdaki örnek kod çalıştırıldığında [örnek excel dosyası](5115190.xls) ile konsol çıktısıdır.

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
