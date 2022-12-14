---
title: Bir Lisansın Uygulanması
type: docs
weight: 40
url: /tr/java/applying-a-license/
---
{{% alert color="primary" %}}

 Aspose.Cells ile yaptığınız değerlendirmeden memnun kaldığınızda,[lisans satın al](https://purchase.aspose.com/buy) Aspose web sitesinde. Kendinizi farklı olana alıştırın[lisans türleri](https://purchase.aspose.com/policies/license-types/) teklif edildi. Herhangi bir sorunuz varsa, çekinmeyin[Aspose satış ekibiyle iletişime geçin](https://about.aspose.com/contact).

Her Aspose lisansı, bu süre içinde çıkan tüm yeni sürümlere veya düzeltmelere ücretsiz yükseltmeler için bir yıllık abonelik içerir. Teknik destek ücretsiz ve sınırsızdır ve hem lisanslı hem de değerlendirme kullanıcılarına sağlanır.

Lisans, ürün adı, lisanslı geliştirici sayısı, abonelik bitiş tarihi vb. gibi ayrıntıları içeren düz metin bir XML dosyasıdır. Dosya dijital olarak imzalanmıştır, bu nedenle dosyayı değiştirmeyin: dosyaya fazladan bir satır sonu eklemek bile dosyayı geçersiz kılar.

Belgelerle herhangi bir işlem yapmadan önce bir lisans ayarlamanız gerekir. Belge nesnesi oluşturmadan önce bunu yaptığınızdan emin olun. Uygulama veya işlem başına yalnızca bir kez lisans ayarlamanız gerekir.

{{% /alert %}}

## **Lisans dosyasının yüklenmesi**

 Java aracılığıyla Android için Aspose.Cells'de, lisans[kaynak olarak gömülü](/cells/tr/java/applying-a-license/#applying-a-license-from-an-embedded-resource)veya bir akıştan yüklendi:

1.  Lisans dosyasını herhangi bir yere koyun**/mnt/sdkart/**.
1. Dosyaya başvuran bir akış oluşturun.
1. Akışı (lisans dosyasını içeren) SetLicense yöntemine geçirin.

**Java**

{{< highlight "java" >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Gömülü Kaynaktan Lisans Uygulama**

Lisansa bir Android paket dosyasından ada göre kaynak olarak erişmek için:

1.  Lisans dosyasını uygulamanıza bir kaynak olarak ekleyin.**res/ham** dosya.
 Lisans dosyası,**res/ham** dosya.
1. Aşağıdaki kod örneğiyle kaynaktan lisansa erişin/yükleyin.

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
