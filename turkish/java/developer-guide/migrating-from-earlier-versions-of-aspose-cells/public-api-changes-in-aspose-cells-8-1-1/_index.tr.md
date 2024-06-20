---
title: Aspose.Cells 8.1.1 Kamu API Değişiklikleri
type: docs
weight: 60
url: /tr/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sındaki 8.1.0'dan 8.1.1'e kadar olan değişiklikleri açıklar, modül ve uygulama geliştiricilerin ilgisini çekebilecek. Sadece [yeni ve güncellenmiş kamusal yöntemleri](/cells/tr/java/public-api-changes-in-aspose-cells-8-1-1/) değil, aynı zamanda Aspose.Cells'in arka plandaki davranışında herhangi bir [değişikliği](/cells/tr/java/public-api-changes-in-aspose-cells-8-1-1/) de içerir.

{{% /alert %}} 
## **Özellikler ve Özellikler Eklendi**
### **HtmlSaveOptions.PresentationPreference Özelliği Eklendi**
HtmlSaveOptions sınıfı, HTML veya MHTML'ye elektronik tabloları dışa aktarırken sonuçları daha iyi düzen ile görüntülemek için kullanılacak PresentationPreference özelliğinin getter/setter'ını açığa çıkardı. Varsayılan değer false'tur. true olarak ayarlansa, Aspose.Cells API çalışma sayfası içeriğini daha iyi sunar.

{{% alert color="primary" %}} 

Daha İyi Düzen için PresentationPreference Seçeneğini Kullanma hakkındaki detaylı makaleyi inceleyin

{{% /alert %}} 
### **Çalışma Sayfası Senaryoları için Destek Eklendi**
Senaryo, bir veya daha fazla formül tarafından birbirine bağlı değişken giriş hücrelerini içeren bir ne olur modelidir. Aspose.Cells, geliştiricilerin senaryolar oluşturmalarına, manipüle etmelerine ve kaldırmalarına yardımcı olmak için Worksheet.Scenarios özelliği için bir get ve set erişimi ile birlikte aşağıdaki sınıfları ortaya çıkartmıştır.

1. Senaryo: Bireysel bir senaryoyu temsil eder.
1. SenaryoKoleksiyonu: Senaryoların bir koleksiyonunu temsil eder.
1. SenaryoGirişHücresiKoleksiyonu: Belirli bir senaryo için giriş hücrelerinin listesini temsil eder.
1. SenaryoGirişHücresi: Belirli bir senaryo için giriş hücresini temsil eder.

{{% alert color="primary" %}} 

Çalışma Sayfalarından Senaryo Oluşturma, Manipüle Etme veya Kaldırma hakkındaki detaylı makaleyi inceleyin

{{% /alert %}}
## **CellsException için Davranış Değişikliği**
Önceki Aspose.Cells for Java API sürümlerinde, hasar görmüş bir elektronik tablo bir Workbook örneğinde yüklendiğinde, API genellikle sorunun nerede olabileceğini belirtmeden genel bir mesaj fırlatma eğilimindeydi. 8.1.1 için bu davranışı değiştirdik, böylece API, şablon dosyasını okurken hangi hücrede ve hangi formül ifadesinin istisnaya neden olduğunu belirten anlamlı bir mesajla istisna fırlatır.
