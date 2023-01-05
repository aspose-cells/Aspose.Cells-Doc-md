---
title: İlk Başvurunuz Aspose.Cells - Hello World
type: docs
weight: 30
url: /tr/python-java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Bu yeni başlayanlar için konu, geliştiricilerin Aspose.Cells' basit API'i kullanarak basit bir ilk uygulamayı (Hello World) nasıl oluşturabileceklerini gösterir. Uygulama, bir çalışma sayfasının belirli bir hücresinde Hello World sözcükleriyle bir Microsoft Excel dosyası oluşturur.

{{% /alert %}}

### **Hello World Uygulamasını Oluşturma**

Hello World uygulamasını Aspose.Cells API kullanarak oluşturmak için:

1.  örneğini oluşturun**[Çalışma Kitabı](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**sınıf.
1. Lisansı uygula:
1. Bir lisans satın aldıysanız, Aspose.Cells'in tüm işlevlerine erişmek için uygulamanızdaki lisansı kullanın.
 1. Bileşenin değerlendirme sürümünü kullanıyorsanız (Aspose.Cells'i lisanssız kullanıyorsanız), bu adımı atlayın.
1. Yeni bir Microsoft Excel dosyası oluşturun veya metin eklemek/güncellemek istediğiniz mevcut bir dosyayı açın.
1. Microsoft Excel dosyasındaki bir çalışma sayfasının herhangi bir hücresine erişin.
1.  kelimeleri ekle**Hello World!** erişilen bir hücreye
1. Değiştirilen Microsoft Excel dosyasını oluşturun.

Aşağıdaki örnekler yukarıdaki adımları göstermektedir.

#### **Çalışma Kitabı Oluşturma**

Aşağıdaki örnek, sıfırdan yeni bir çalışma kitabı oluşturur, "Hello World!" ilk çalışma sayfasındaki A1 hücresine girer ve dosyayı kaydeder.

**Oluşturulan e-tablo** 

![yapılacaklar:resim_alternatif_metin](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFile.py" >}}

#### **Mevcut Bir Dosyayı Açmak**

 Aşağıdaki örnek, adlı mevcut bir Microsoft Excel şablon dosyasını açar.**kitap1.xls**, "Hello World!" ilk çalışma sayfasındaki A1 hücresinde bulunur ve çalışma kitabını yeni bir dosya olarak kaydeder.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpeningExistingFile.py" >}}
