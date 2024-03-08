---
title: Licensing
type: docs
weight: 50
url: /tr/java/licensing/
description: JAVA için Aspose.Cells, farklı satın alma planları sağlar veya Licensing'i ve Java'deki Abonelik politikalarını kullanarak değerlendirme için Ücretsiz Deneme ve 30 günlük Geçici Lisans sunar.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **Aspose.Cells Bileşeninde Lisans Nasıl Başvurulur**

Lisans, ürün adı, lisanslandığı geliştirici sayısı, aboneliğin sona erme tarihi vb. ayrıntıları içeren düz metinli bir XML dosyasıdır. Dosya dijital olarak imzalanmıştır; dolayısıyla dosyayı değiştirmeyin; dosyaya yanlışlıkla fazladan bir satır sonu eklenmesi bile dosyayı geçersiz kılacaktır.

Değerlendirme sınırlamalarından kaçınmak istiyorsanız Aspose.Cells'i kullanmadan önce bir lisans ayarlamanız gerekir. Her uygulama veya işlem için yalnızca bir kez lisans ayarlamanız gerekir.

Lisans aşağıdaki konumlardaki bir akıştan veya dosyadan yüklenebilir:

1. Açık yol.
1. Aspose.Cells.jar dosyasını içeren klasör.

 Kullan[Lisans.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)bileşeni lisanslama yöntemi. Genellikle lisans ayarlamanın en kolay yolu, lisans dosyasını Aspose.Cells.jar ile aynı klasöre koymak ve aşağıdaki örnekte gösterildiği gibi yol olmadan yalnızca dosya adını belirtmektir:

###  **Diskten Lisans Nasıl Başvurulur**

 Bu örnekte**Aspose.Cells** Uygulamanızın JAR'larını içeren klasördeki lisans dosyasını bulmaya çalışacaktır.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **Akıştan Lisans Nasıl Başvurulur**

Bir akıştan bir lisans başlatır.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **Aspose.Cells.GridWeb'de Lisans Nasıl Başvurulur**

Lisans kodunu web uygulamanızda ilk işleneceği yere koymanız tavsiye edilir.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Ölçülü Lisans Nasıl Başvurulur**

Aspose.Cells, geliştiricilerin ölçülü anahtar uygulamasına olanak tanır. Yeni bir lisanslama mekanizmasıdır. Yeni lisanslama mekanizması mevcut lisanslama yöntemiyle birlikte kullanılacaktır. API özelliğinin kullanımına göre faturalandırılmak isteyen müşterilerimiz, ölçülü lisanslamayı kullanabilirler. Daha fazla ayrıntı için lütfen bkz.[Ölçülü Licensing SSS](https://purchase.aspose.com/faqs/licensing/metered)bölüm.

Yeni bir sınıf[Ölçülü](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)ölçülü anahtarı uygulamak için tanıtıldı. Ölçülü genel ve özel anahtarın nasıl ayarlanacağını gösteren örnek kod aşağıda verilmiştir.

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
