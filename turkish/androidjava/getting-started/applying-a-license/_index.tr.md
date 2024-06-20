---
title: Lisans Başvurusu
type: docs
weight: 40
url: /tr/java/applying-a-license/
---

{{% alert color="primary" %}}

Aspose.Cells'in değerlendirmesinden memnunsanız, Aspose web sitesinden [lisans satın al](https://purchase.aspose.com/buy). Sunulan farklı [lisans türleriyle](https://purchase.aspose.com/policies/license-types/) tanışın. Herhangi bir sorunuz varsa, çekinmeden [Aspose satış ekibiyle iletişime geçin](https://about.aspose.com/contact).

Her Aspose lisansı, bu süre zarfında ortaya çıkan yeni sürümlere veya düzeltmelere ücretsiz yükseltmeler için bir yıllık abonelik içerir. Teknik destek, lisanslı ve değerlendirme kullanıcılara ücretsiz ve sınırsız olarak sağlanır.

Lisans, ürün adı, lisanslı geliştiricilerin sayısı, abonelik sona erme tarihi vb. gibi ayrıntıları içeren düz metin XML dosyasıdır. Dosya dijital olarak imzalanmıştır, bu nedenle dosyayı değiştirmeyin: dosyaya ek bir satır kesme bile onu geçersiz kılacaktır.

Belgelerle herhangi bir işlem yapmadan önce bir lisans ayarlamanız gerekir. Bu işlemi bir kez uygulamanız veya işlem başına bir kez uygulamanız yeterlidir.

{{% /alert %}}

## **Lisans dosyasını yüklemeniz gerekmektedir**

Aspose.Cells için Android via Java'te lisans, [bir kaynak olarak gömülü](/cells/tr/java/applying-a-license/#applying-a-license-from-an-embedded-resource) veya bir akıştan yüklenebilir:

1. Lisans dosyasını **/mnt/sdcard/** dizinine yerleştirin.
1. Dosyayı referans alan bir akış oluşturun.
1. (Lisans dosyasını içeren) akışı SetLicense yöntemine iletebilirsiniz.

**Java**

{{< highlight java >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Gömülü Bir Kaynaktan Lisans Başvurusu**

Android paket dosyasından bir kaynak olarak lisansa erişmek için:

1. Lisans dosyasını uygulamanızın **res/raw** klasörüne bir kaynak olarak ekleyin.
   Lisans dosyası **res/raw** klasöründe görünür olmalıdır.
1. Aşağıdaki kod örneği ile kaynaktan lisansa erişin/yükleyin.

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
