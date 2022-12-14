---
title: lisanslama
type: docs
weight: 50
url: /tr/java/licensing/
---
{{% alert color="primary" %}} 

 değerlendirme sürümünü indirebilirsiniz.**Aspose.Cells** for Java gelen[indirme sayfası](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven deposu. Değerlendirme sürümü, ürünün lisanslı sürümüyle kesinlikle aynı yetenekleri sağlar. Ayrıca, bir lisans satın aldığınızda ve lisansı uygulamak için birkaç satır kod eklediğinizde, değerlendirme sürümü kolayca lisanslanır.

 Değerlendirmenizden memnun olduğunuzda**Aspose.Cells** , yapabilirsiniz[lisans satın al](https://purchase.aspose.com)Aspose web sitesinde. Sunulan farklı abonelik türleri hakkında bilgi sahibi olun. Herhangi bir sorunuz varsa, Aspose satış ekibiyle iletişime geçmekten çekinmeyin.

Her Aspose lisansı, bu süre içinde çıkan tüm yeni sürümlere veya düzeltmelere ücretsiz yükseltmeler için bir yıllık abonelik içerir. Teknik destek ücretsiz ve sınırsızdır ve hem lisanslı hem de değerlendirme kullanıcılarına sağlanır.

{{% /alert %}} {{% alert color="primary" %}} 

 test etmek istersen**Aspose.Cells** değerlendirme sürümü sınırlamaları olmadan, 30 günlük bir geçici lisans talep edin. Bakınız[Geçici Lisans nasıl alınır?](https://purchase.aspose.com/temporary-license) daha fazla bilgi için.

{{% /alert %}}

## **Değerlendirme Sürümü Sınırlamaları**

 değerlendirme versiyonu**Aspose.Cells** ürün (belirtilen bir lisans olmadan), tam ürün işlevselliği sağlar, ancak bir programda 100 dosya ve değerlendirme filigranlı fazladan bir çalışma sayfası açmakla sınırlıdır.

Sınırlamalar aşağıda gösterilmiştir:

### **1. Sınırlama: Açılan Dosya Sayısı**

Programınızı çalıştırırken sadece 100 Excel dosyası açabilirsiniz. Uygulamanız bu sayıyı aşarsa bir istisna atılır.

### **2. Sınırlama: Değerlendirme Filigranlı Çalışma Sayfası**

![yapılacaklar:resim_alternatif_Metin](licensing_1.png)

Bu çalışma sayfası her zaman etkin çalışma sayfası olarak gösterilir. Yalnızca lisanslı sürümde, aktif çalışma sayfasını diğer çalışma sayfalarına ayarlayabilirsiniz.

## **Lisans Ayarlama**

Lisans, ürün adı, lisanslandığı geliştirici sayısı, abonelik bitiş tarihi gibi ayrıntıları içeren düz metin bir XML dosyasıdır. Dosya dijital olarak imzalanmıştır, bu nedenle dosyayı değiştirmeyin; dosyaya yanlışlıkla fazladan bir satır sonu eklenmesi bile dosyayı geçersiz kılacaktır.

Değerlendirme sınırlamalarından kaçınmak istiyorsanız, Aspose.Cells'i kullanmadan önce bir lisans ayarlamanız gerekir. Uygulama veya işlem başına yalnızca bir kez lisans ayarlamanız gerekir.

Lisans, aşağıdaki konumlardaki bir akıştan veya dosyadan yüklenebilir:

1. Açık yol.
1. Aspose.Cells.jar dosyasını içeren klasör.

 Kullan[Lisans.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) bileşeni lisanslama yöntemi. Genellikle bir lisans ayarlamanın en kolay yolu, lisans dosyasını Aspose.Cells.jar ile aynı klasöre koymak ve aşağıdaki örnekte gösterildiği gibi yolsuz sadece dosya adını belirtmektir:

### **örnek 1**

 Bu örnekte**Aspose.Cells** uygulamanızın JAR'larını içeren klasörde lisans dosyasını bulmaya çalışacaktır.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Örnek 2**

Akıştan bir lisans başlatır.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Aspose.Cells.GridWeb'de Lisans Uygulamaya İlişkin Notlar**

Lisans kodunu web uygulamanızda ilk olarak işlenmesi gereken bir yere koymanız önerilir.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Tarifeli Lisansı Uygulama**

Aspose.Cells, geliştiricilerin ölçülü anahtar uygulamasına izin verir. Yeni bir lisanslama mekanizmasıdır. Yeni lisanslama mekanizması, mevcut lisanslama yöntemiyle birlikte kullanılacaktır. API özelliğinin kullanımına göre faturalandırılmak isteyen müşterilerimiz tarifeli lisanslamayı kullanabilirler. Daha fazla ayrıntı için lütfen bkz.[Ölçülü Lisanslama SSS](https://purchase.aspose.com/faqs/licensing/metered)bölüm.

yeni bir sınıf[ölçülü](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)ölçülü anahtarı uygulamak için tanıtıldı. Ölçülü genel ve özel anahtarın nasıl ayarlanacağını gösteren örnek kod aşağıdadır.

{{< highlight "java" >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
