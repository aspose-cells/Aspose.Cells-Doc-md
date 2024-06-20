---
title: Lisans Dosyası Artık Çalışmıyor
type: docs
weight: 60
url: /tr/net/license-file-not-working-anymore/
---

## **Belirti**

Bazı durumlarda, kullanıcılar lisans dosyalarının artık yeni bir sunucuya taşıdıklarında / yayınladıklarında artık çalışmadığından dolayı sinir bozucu hale gelebilirler. Lisans dosyalarının önceki (eski) sunucularında düzgün çalıştığını hissederler, ancak şimdi yeni sunucu ortamında yeni **Değerlendirme Telif Uyarısı** filigran Levhası (bileşeni kullanarak raporlar oluşturduklarında her zaman) alırlar.

### **Senaryo**

"ASP.NET web projemizde Aspose.Cells'i kullanarak Excel raporları oluşturduk / düzenledik, kullandığımız geçerli bir lisans aldık. Birkaç gün önce web sitesini yeni bir sunucuya taşıdık; herhangi bir yükseltme veya değişiklik yapılmadı, emin olduk ve sadece her dosyayı yeni sunucuya taşıdık, Aspose.Cells.dll ve ilgili .lic dosyaları da dahil olmak üzere. Şimdi yeni sunucu ortamında Excel raporları oluşturmaya çalıştığımızda raporlarımızda **Değerlendirme Telif Uyarısı** filigranı aldık. Sitenin bin klasörüne Aspose.Cells.lic dosyasını ve ilgili Aspose.Cells.dll bileşen dosyasını yerleştirerek lisansı uyguladık, ki, bahsettiğim gibi, eski sunucuda hiçbir sorun olmadan çalışıyordu."

### **Çözüm**

Aspose'un temiz ve güvenilir lisans mekanizması vardır. Genellikle sorun, dağıtım sorunu ile ilgili olmalıdır. Bir lisans dosyası (bir sunucuda) iyi çalışıyorsa, diğer sunucularda / ortamlarda da aynı şekilde çalışmalıdır. Normalde, kullanıcılar genellikle li­sans kodunu yerleştirmek için global.asax dosyasında Application_Start veya Session_Start olaylarını kullanır. Bu nedenle, Application_Start / Session_Start olaylarının lisans kodunu işlemek üzere tetiklenmediği yeni konum(lar)ı için sorun olursa, bu oldukça olasıdır. Burada belirtilmeli, Aspose.Cells, lisans dosyasını bir yol üzerinde bulamıyorsa her zaman bir istisna fırlatacaktır. Kullanıcılar yerleştirdikleri herhangi bir yere lisans kodunun işlenmesi ve olayların lisans kodunu yerleştirdikleri yerde tetiklenmesi konusunda emin olmalıdır. Kullanıcı atfın ilgili servisi yeniden başlatabilir, yani, "Dünya Çapında Web Yayınlama" ve projelerini ziyaret ettiklerinde Application_Start  / Session_Start olaylarının tetiklenip tetiklenmediğini izleyebilirler.

### **Onay**

Lütfen ayrıca şunu emin olun...

- Projende geçerli bir lisans dosyası kullanıyor olmanız.
- Siz veya başkası lisans dosyasını düzenlememiş / değiştirmemiş olmalı, aksi takdirde lisans dosyası çalışmayacaktır.
- Lisans abonelik süresinin bitiş tarihini bilmelisiniz (basitçe lic dosyasını not defterine açarak son kullanma tarihini kontrol edebilirsiniz).
- Lisans aboneliği sürenizden sonra yayınlanan bir sürüm (Aspose.Cells.dll) kullanmadığınızdan emin olmalısınız. Burada belirtilmelidir ki, bir lisans dosyası asla süresi doldurmaz, ancak abonelik sürenizden sonraki sürümleri kullanıyorsanız, her excel dosyası oluşturduğunuzda ekstra **Değerlendirme Telif Uyarısı** filigranı alırsınız.

### **Referanslar**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
