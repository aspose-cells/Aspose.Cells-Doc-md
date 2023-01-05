---
title: Genel API Aspose.Cells 8.1.1'deki değişiklikler
type: docs
weight: 60
url: /tr/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürüm 8.1.0'dan 8.1.1'e modül ve uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Sadece içermez[yeni ve güncellenmiş genel yöntemler](/cells/tr/java/public-api-changes-in-aspose-cells-8-1-1/) , aynı zamanda herhangi birinin açıklaması[davranış değişiklikleri](/cells/tr/java/public-api-changes-in-aspose-cells-8-1-1/) Aspose.Cells'de kamera arkası.

{{% /alert %}} 
## **Eklenen Özellikler ve Özellikler**
### **HtmlSaveOptions.PresentationPreference Özelliği eklendi**
HtmlSaveOptions sınıfı, e-tabloları HTML veya MHTML'e dışa aktarırken sonuçları daha iyi düzende işlemek için kullanılabilen PresentationPreference özelliği için getter/setter özelliğini kullanıma sundu. Varsayılan değer false'tur. true olarak ayarlanırsa, Aspose.Cells API, çalışma sayfası içeriğini daha iyi sunumla dışa aktarır.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Daha İyi Düzen için PresentationPreference Seçeneğini Kullanın](/cells/tr/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Çalışma Sayfası Senaryoları için Destek Eklendi**
Senaryo, bir veya daha fazla formülle birbirine bağlanan değişken girdi hücrelerini içeren bir ne olursa olsun modelidir. Aspose.Cells, geliştiricilerin senaryoları oluşturmasına, değiştirmesine ve kaldırmasına yardımcı olmak için Worksheet.Scenarios özelliği için bir alıcı ve ayarlayıcıyı aşağıdaki sınıflarla birlikte kullanıma sunmuştur.

1. Senaryo: Tek bir senaryoyu temsil eder.
1. ScenarioCollection: Bir senaryo koleksiyonunu temsil eder.
1. ScenarioInputCellCollection: Belirli bir senaryo için girdi hücrelerinin listesini temsil eder.
1. ScenarioInputCell: Belirli bir senaryo için girdi hücreleri koleksiyonundan bir girdi hücresini temsil eder.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Çalışma Sayfalarından Senaryolar Nasıl Oluşturulur, İşlenir veya Kaldırılır](/cells/tr/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **CellsException için Davranışta Değişiklik**
Aspose.Cells for Java API'in önceki sürümlerinde, bir Çalışma Kitabı örneğine zarar görmüş olma olasılığı bulunan bir elektronik tablo yüklendiğinde, API, sorunun nerede olabileceğinden bahsetmeden genel bir mesaj atma eğilimindeydi. 8.1.1 için bu davranışı değiştirdik, böylece API, şablon dosyasını okurken nerede (hangi hücre) ve neyin (formül ifadesi) istisnaya neden olduğunu gösteren anlamlı bir mesajla bir istisna atar.
