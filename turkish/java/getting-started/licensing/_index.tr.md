---
title: Lisanslama
type: docs
weight: 50
url: /tr/java/licensing/
description: Aspose.Cells for JAVA, Java da Lisanslama ve Abonelik politikalarını kullanarak satın alma için farklı planlar sunar veya Değerlendirme için Ücretsiz Deneme ve 30 günlük Geçici Lisans sunar.
keywords: Java Diskten veya Akıştan Lisans Uygula. Java Diskten veya Akıştan Lisans Belirle. Aspose.Cells for Java de Lisans Uygulama.
---

## **Aspose.Cells Bileşeninde Lisans Nasıl Uygulanır**

Lisans, ürün adı, lisanslanan geliştiricilerin sayısı, abonelik bitiş tarihi gibi detayları içeren düz metin XML dosyasıdır. Dosya dijital olarak imzalanmıştır, bu nedenle dosyayı değiştirmeyin; hatta dosyaya yanlışlıkla ek bir satır aralığı eklemek bile geçersiz kılacaktır.

Aspose.Cells kullanmadan önce lisansı ayarlamanız gerekmektedir. Bir uygulama veya işlem başına yalnızca bir kez lisans ayarlamanız gerekmektedir.

Lisans bir akıştan veya dosyadan aşağıdaki konumlardan yüklenebilir:

1. Açık yol.
1. Aspose.Cells.jar içeren klasör.

Bileşimi lisanslamak için [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) yöntemini kullanın. Genellikle lisansı ayarlamanın en kolay yolu, lisans dosyasını Aspose.Cells.jar ile aynı klasöre koymak ve sadece dosya adını belirtmektir, örnek aşağıda gösterildiği gibi:

### **Dandan Uygulaması**

Bu örnekte **Aspose.Cells**, uygulamanın JAR'larını içeren klasörde lisans dosyasını bulmaya çalışacaktır.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Akıştan Lisans Uygulama**

Bir akıştan lisansı başlatır.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Aspose.Cells.GridWeb'de Lisans Uygulama**

Lisanslama kodunu web uygulamanızın en öncelikli işleyeceği bir yere koymak önerilir.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Saatlik Lisansın Uygulanması**

Aspose.Cells, geliştiricilere saatlik anahtar uygulama imkanı tanır. Bu yeni bir lisanslama mekanizmasıdır. Yeni lisanslama mekanizması, mevcut lisanslama yöntemi ile birlikte kullanılacaktır. API özelliklerinin kullanımına göre faturalandırılmak isteyen müşteriler, saatlik lisanslamayı kullanabilir. Daha fazla bilgi için lütfen [Saatlik Lisanslama SSY](https://purchase.aspose.com/faqs/licensing/metered) bölümüne başvurun.

Metrik genel ve özel anahtarları ayarlamayı gösteren örnek kod şu şekildedir.

{{< highlight java >}}

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
