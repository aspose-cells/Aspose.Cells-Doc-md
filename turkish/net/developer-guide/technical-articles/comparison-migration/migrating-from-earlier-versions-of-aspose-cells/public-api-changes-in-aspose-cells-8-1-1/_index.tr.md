---
title: Genel API Aspose.Cells 8.1.1'deki değişiklikler
type: docs
weight: 50
url: /tr/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.1.0'dan 8.1.1'e modül/uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranışlardaki değişikliklerin açıklamasını da içerir.

{{% /alert %}} 
## **HtmlSaveOptions.PresentationPreference Özelliği eklendi**
HtmlSaveOptions sınıfı, elektronik tabloları HTML veya MHTML'ye dışa aktarırken sonuçları daha iyi bir düzende işlemek için kullanılabilen PresentationPreference özelliğine sahiptir. Varsayılan değer yanlıştır. true olarak ayarlanırsa, Aspose.Cells API, çalışma sayfası içeriğini daha iyi sunumla dışa aktarır.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Daha İyi Düzen için PresentationPreference Seçeneğini Kullanın](/cells/tr/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Çalışma Sayfası Senaryoları için Destek Eklendi**
 Bir senaryo, buna göre bir veya daha fazla formülle birbirine bağlanan değişken girdi hücrelerini içeren what-if modeli olarak adlandırılır. Aspose.Cells API, kullanıcıların çalışma sayfalarından senaryo oluşturma, değiştirme ve çıkarma işlemlerini kolaylaştırmak için Worksheet.Scenarios özelliğini aşağıdaki sınıflarla birlikte kullanıma sunmuştur,

1. Senaryo: Tek bir senaryoyu temsil eder.
1. ScenarioCollection: Bir senaryo koleksiyonunu temsil eder.
1. ScenarioInputCellCollection: Belirli bir senaryo için girdi hücrelerinin listesini temsil eder.
1. ScenarioInputCell: Belirli bir senaryo için girdi hücreleri koleksiyonundan bir girdi hücresini temsil eder.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Çalışma Sayfalarından Senaryolar Nasıl Oluşturulur, İşlenir veya Kaldırılır](/cells/tr/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
