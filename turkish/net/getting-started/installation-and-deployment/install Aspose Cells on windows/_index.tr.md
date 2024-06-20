---
title: Windows ta Aspose.Cells Yükle
type: docs
weight: 20
url: /tr/net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

Bazen **Aspose.Cells**'i Windows Vista üzerinde kurarken ek parçalar gerektirmeyen Aspose.Cells dosyasının (Aspose.Cells.msi...Windows Installer Package) başarıyla kurulması için nasıl başa çıkabileceğimizi ve uygulayabileceğimizi açıklayan belgedir. Gerçekte **Aspose.Cells** kurulumunun asp.NET Demoları'nın (Asp.NET Demoları) dağıtımı için IIS üzerinde sanal bir klasör oluşturması gerektiğinden, **Aspose.Cells**'i yüklerken Yönetici Haklarına sahip olmanız gerekir.

{{% /alert %}} 
## **Olası Faktörler**
Normalde **Windows Vista**'da admin olsanız bile kullandığınız ürünler/bileşenler her zaman "normal kullanıcı" izinleri altında uygulanır. Programlar, yönetici olarak oturum açmış olsanız bile dosya sistemine sınırlı erişime izin verilir. Bu, **Windows XP**'de genellikle bir yönetici olarak oturum açtığınızda karşılaşmayacağınız bazı talihsiz yan etkilere sahiptir.
## **Kullanıcı Hesabı Denetimi (UAC)**
**UAC**, izin isteyen **Windows Vista**'nın bir parçasıdır. **UAC** modu (aynı zamanda **Yönetici Onay Modu** olarak da bilinir), (başlıca) yönetici hesaplarının çalışma şeklini etkileyen bir çalışma modudur. Varsayılan olarak **UAC** açık olduğunda "yönetici" yetkilerini kullanan herhangi bir programa açıkça izin vermeniz gerekir. İzin verilmeyen herhangi bir program, izniniz olmadan yönetici yetkilerini kullanmaya çalışırsa erişimi reddedilir. **UAC**, Internet Explorer'da **Korunan Mod** dahil olmak üzere, **Windows Vista**'nın diğer güvenlik özellikleri için de gereklidir. Internet Explorer Korunan Modu, bilgisayarınızı yanlış web sayfaları ve diğer web tabanlı zafiyetler de dahil olmak üzere, bilinmeyen zafiyetler de dahil olmak üzere korur.

**UAC** modu etkin olduğunda, yönetici olarak oturum açtığınızda çalıştırdığınız her program sadece sistemde "standart kullanıcı" erişimi verilecektir. **Windows Vista**, potansiyel güvenlik ihlallerini otomatik olarak azaltma yeteneğine sahiptir. Bu, sistemde otomatik olarak bu özelliği etkinleştirerek yapar ve bu özellik **Kullanıcı Hesabı Denetimi** (veya kısacası **UAC**) olarak adlandırılır. **UAC**, yerel yöneticiler grubunun bir parçası olan kullanıcıları, yönetici izinleri olmayan normal kullanıcılar gibi çalışmaya zorlar. **UAC** açıkça **Windows Vista**'daki güvenliği arttırırken, bazı senaryolarda, örneğin güvenlikle ilgili olmayan demolar (örneğin) için devre dışı bırakmak isteyebilirsiniz. Bazı ev kullanıcıları, sistemin ek kaynaklarını kullanmasından dolayı **UAC**'i devre dışı bırakmak isteyebilir.
## **Bileşenin Başarılı Kurulumu İçin İzlenmesi Gereken Adımlar**
- **Aspose.Cells**'i kurmadan önce Vista'nızda IIS'nin kurulu olduğundan emin olun. Çünkü **Aspose.Cells** kurulumunun asp.NET Demoları'nın (Asp.NET Demoları) dağıtımı için IIS üzerinde sanal bir klasör oluşturması zorunludur.
- **UAC**'i (Kullanıcı Hesabı Denetimi) devre dışı bırakmanız gerekir. **Aspose.Cells**'i kurmadan önce sistemin tam kontrolüne sahip **Yönetici Hakları**'na sahip olduğunuzdan emin olmanız gerekir. Aksi takdirde, **Aspose.Cells**'i yüklerken 2869 hatası alabilirsiniz.

Bunu başarmanın bazı yolları aşağıda belirtilmiştir.
### **Komut Satırı Kullanımı**
1. Windows dizininde cmd.exe'yi arayın, ardından üzerine sağ tıklayıp **Yönetici olarak çalıştır**'ı seçin.
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **Denetim Masası Kullanımı**
- Başlat'a tıklayın
- Denetim Masası'na tıklayın
- Kullanıcı Hesapları ve Aile Koruması'na tıklayın
- Kullanıcı Hesapları'na tıklayın
- Kullanıcı Hesabı Denetimi'ni Açık veya Kapalı Duruma Getir'e tıklayın
- Onay kutusunu kaldırın
- Tamam'a tıklayın

{{% alert color="primary" %}} 

Değişikliğin etkili olması için bilgisayarınızı yeniden başlatmanız gerekecektir. Bu değişiklik sadece sizin değil, bilgisayardaki tüm hesapları etkiler.

{{% /alert %}}
