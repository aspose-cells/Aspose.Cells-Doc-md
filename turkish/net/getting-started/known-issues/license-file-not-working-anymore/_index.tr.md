---
title: Lisans Dosyası Artık Çalışmıyor
type: docs
weight: 60
url: /tr/net/license-file-not-working-anymore/
---
## **Belirti**

 Bazen, kullanıcılar web projelerini yeni bir sunucuya taşıdıklarında / yayınladıklarında lisans dosyalarının artık çalışmaması nedeniyle hayal kırıklığına uğrarlar. Lisans dosyaları önceki (eski) sunucularında düzgün çalıştığı için üzülüyorlar, ancak şimdi fazladan bir lisans alıyorlar.**Değerlendirme Telif Hakkı Uyarısı** filigran Çalışma Sayfası (bileşeni kullanarak raporlar oluşturduklarında) yeni sunucu ortamında.

### **Bir Senaryo**

"Excel raporları oluşturmak/değiştirmek için ASP.NET web projemizde Aspose.Cells kullanıyoruz, kullandığımız geçerli bir lisansımız var. Birkaç gün önce web sitesini yeni bir sunucuya taşıdık; herhangi bir yükseltme veya değişiklik olmadı. Aspose.Cells.dll ve ilgili .lic dosya(lar) dahil olmak üzere her dosyayı yeni sunucuya taşıdık.Artık yeni sunucu ortamında Excel raporları oluşturmaya çalıştığımızda,**Değerlendirme Telif Hakkı Uyarısı** raporlarımızda filigran sayfası. Sitenin Siparişlerim bölümünden yeni bir lisans dosyası indirip yüklemeyi denedik, ancak sorunu hiçbir şekilde çözmedi. Bilginize, Aspose.Cells.lic dosyasını sitenin bin klasörüne, belirttiğim gibi eski sunucuda sorunsuz çalışan Aspose.Cells.dll bileşen dosyasıyla birlikte yerleştirerek lisansı uyguluyoruz."

### **Çözüm**

Aspose temiz ve güvenilir bir lisanslama mekanizmasına sahiptir. Genel olarak, sorun dağıtım sorunu ile ilgili olmalıdır. Bir lisans dosyası (bir sunucuda) iyi çalışıyorsa, diğer sunucularda/ortamlarda da eşit derecede iyi çalışmalıdır. Normalde kullanıcılar Uygulamayı kullanır_Başlangıç veya Oturum_Lisans kodunu oraya yerleştirmek için global.asax dosyasında olayları vb. başlatın. Bu nedenle, Uygulamanın oldukça olasıdır_Başlangıç / Oturum_Yeni konum(lar)ında lisans kodunu işlemek için başlatma olay(lar)ı tetiklenmez. Burada not edilmelidir, bileşen lisans dosyasını bir yolda bulamazsa Aspose.Cells her zaman bir istisna atar. Kullanıcılar, lisans kodunun (yerleştirdikleri her yerde) işlendiğinden ve lisans kodunun girildiği olayların tetiklendiğinden emin olmalıdır. Kullanıcı, "World Wide Web Publishing" gibi ilgili hizmeti yeniden başlatabilir ve Uygulamanın yayınlanıp yayınlanmadığını izlemeye çalışabilir._Başlangıç / Oturum_Başlangıç etkinlikleri, yeni sunucu ortamında projelerini ziyaret ettiklerinde tetiklenir.

### **Onayla**

Lütfen şundan da emin olun…

- Projenizde geçerli bir lisans dosyası kullanıyorsunuz.
- Siz veya bir başkası lisans dosyasını düzenlememeli / değiştirmemelisiniz, en azından lisans dosyası çalışmayacaktır.
- Lisans aboneliğinizin sona erme süresinin farkında olmalısınız (lisans dosyasını not defterinde açıp son kullanma tarihini kontrol edebilirsiniz).
-  Lisans aboneliğiniz sona erdikten sonra yayınlanan bir sürümü (Aspose.Cells.dll) kullanmıyorsunuz. Burada not edilmelidir, bir lisans dosyasının süresi asla dolmaz, ancak abonelik süreniz sona erdikten sonra yayınlanan bileşen sürümünü kullanıyorsanız, ekstra bir ücret alırsınız.**Değerlendirme Telif Hakkı Uyarısı** bir excel dosyası oluşturduğunuzda filigran sayfası.

### **Referanslar**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
