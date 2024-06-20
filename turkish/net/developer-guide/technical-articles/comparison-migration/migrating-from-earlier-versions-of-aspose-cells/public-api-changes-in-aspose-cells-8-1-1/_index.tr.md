---
title: Aspose.Cells 8.1.1 Kamu API Değişiklikleri
type: docs
weight: 50
url: /tr/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.1.0'dan 8.1.1'e kadar olan sürümlerdeki değişiklikleri açıklamaktadır, modül/uygulama geliştiricilerinin ilgisini çekebilecek. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'in arka planda olan herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **HtmlSaveOptions.PresentationPreference Özelliği Eklendi**
HtmlSaveOptions sınıfı, elektronik tabloları HTML veya MHTML biçimine dışa aktarırken sonuçları daha iyi düzenleme imkanı sağlamak için PresentationPreference özelliğini açmıştır. Varsayılan değer false'dur. true olarak ayarlandığında Aspose.Cells API, çalışma sayfası içeriğini daha iyi sunum ile dışa aktaracaktır.

{{% alert color="primary" %}} 

[Daha İyi Düzen İçin PresentationPreference Seçeneğini Kullanın] (/hücreler/tr/net/html-için-excel-daha-iyi-düzen-seçeneği-kullanın/)' üzerindeki detaylı makaleyi kontrol edin

{{% /alert %}}
## **Çalışma Sayfası Senaryoları için Destek Eklendi**
Senaryo, değişken giriş hücrelerini bir veya daha fazla formülle bağlayarak adını aldığı bir ne-olur modelidir. Aspose.Cells API, kullanıcıların çalışma sayfaları üzerinde senaryo oluşturmasını, manipüle etmesini ve kaldırmasını kolaylaştırmak için Worksheet.Scenarios özelliğini ve aşağıdaki sınıfları açmıştır. 

1. Senaryo: Bireysel bir senaryoyu temsil eder.
1. SenaryoKoleksiyonu: Senaryoların bir koleksiyonunu temsil eder.
1. ScenarioInputCellCollection: Belirli bir senaryo için giriş hücrelerinin listesini temsil eder.
1. ScenarioInputCell: Belirli bir senaryo için giriş hücrelerinin koleksiyonundan bir giriş hücresini temsil eder.

{{% alert color="primary" %}} 

Lütfen [Çalışma Kitaplarından Senaryolar Oluşturma, Manipüle Etme veya Kaldırma](/cells/tr/net/create-manipulate-or-remove-scenarios-from-worksheets/) hakkında detaylı makaleyi kontrol edin.

{{% /alert %}}
