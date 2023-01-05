---
title: Aspose.Cells'i Windows'e yükleyin
type: docs
weight: 20
url: /tr/net/installing-aspose-cells-on-windows/
---
{{% alert color="primary" %}} 

 Bazen kurulumda bazı problemlerle karşılaşabilirsiniz.**Aspose.Cells** kurulum paketini (Aspose.Cells.msi...Windows Kurulum Paketi) kullanarak**Windows manzara** . Bu belge, bununla nasıl başa çıkabileceğimizi ve bileşenin başarılı kurulumunu nasıl uygulayabileceğimizi açıklar. Aslında**Aspose.Cells**yükleyicinin, Web Demolarını (Asp.NET Demoları) makinenize dağıtmak için IIS üzerinde sanal bir klasör oluşturması gerekir, bu nedenle yüklemeden önce bir Yönetim Ayrıcalıklarına sahip olmanız gerekir**Aspose.Cells** yükleyicisini kullanarak. Yükleyici, sisteme yönetici düzeyinde erişim talep ediyorsa, bunu yapmasına açıkça izin verilmelidir.

{{% /alert %}} 
## **Olası Faktörler**
 Normalde, içinde**Windows manzara** , yüklediğiniz/kullandığınız ürünler/bileşenler, siz bir kullanıcı olsanız bile her zaman "normal kullanıcı" izinleri altında uygulanır.**yönetici** . olarak oturum açmış olsanız bile, programların dosya sistemine yalnızca sınırlı erişimine izin verilir.**yönetici** . Bunun, bir kullanıcı olarak oturum açtığınızda Windows XP'de normalde karşılaşmayacağınız bazı talihsiz yan etkileri vardır.**yönetici**.
## **UAC (Kullanıcı Hesabı Denetimi)**
**UAC** parçası mı**Windows manzara** senden izin isteyen. bu**UAC** modu (olarak da bilinir)**Yönetici Onay Modu** ), (öncelikle) yönetici hesaplarının çalışma şeklini etkileyen bir işlem modudur. Ne zaman**UAC**açıksa (varsayılan olarak açıktır), "yönetici" yetkilerini kullanmak isteyen herhangi bir programa açıkça izin vermelisiniz. İzniniz olmadan yönetici yetkilerini kullanmaya çalışan herhangi bir programın erişimi reddedilecektir.**UAC** diğer güvenlik özellikleri için de gereklidir.**Windows manzara** , dahil olmak üzere**Korumalı mod** Internet Explorer'da. Internet Explorer Korumalı Modu, bilgisayarınızı hileli web sayfalarından ve bilinmeyenler de dahil olmak üzere web ile ilgili diğer güvenlik açıklarından korur.

 Ne zaman**UAC** modu etkinleştirildiğinde, çalıştırdığınız her programa, yönetici olarak oturum açmış olsanız bile sisteme yalnızca "standart kullanıcı" erişimi verilecektir.**Windows manzara** sistemdeki güvenlik ihlalleri olasılığını otomatik olarak azaltmak için yerleşik bir yeteneğe sahiptir. Bunu, adı verilen bu özelliği otomatik olarak etkinleştirerek yapar.**Kullanıcı Hesap Denetimi** (veya**UAC** kısaca). bu**UAC**yerel yöneticiler grubunun parçası olan kullanıcıları yönetici ayrıcalıkları olmayan normal kullanıcılar gibi çalışmaya zorlar. Rağmen**UAC** üzerindeki güvenliği açıkça artırır**Windows manzara** , bazı senaryolarda, örneğin bir seyirci önünde demolar yaparken (örneğin, güvenlikle ilgili olmayan demolar) devre dışı bırakmak isteyebilirsiniz. Bazı ev kullanıcıları devre dışı bırakmak isteyebilir**UAC** sistemlerinin ek kaynaklarının kullanımı nedeniyle.
## **Bileşenin Başarılı Kurulumu İçin İlgili Adımlar**
-  Lütfen yüklemeden önce Vista'nızda IIS'nin yüklü olduğundan emin olun**Aspose.Cells** . Zorunlu çünkü**Aspose.Cells** yükleyicinin Web Demolarının (Asp.NET Demoları) dağıtımı için IIS üzerinde bir sanal klasör oluşturması gerekir.
-  devre dışı bırakmanız gerekiyor**UAC** (Kullanıcı Hesap Denetimi). sahip olduğunuzdan emin olmalısınız.**Yönetici ayrıcalıkları** kurulumdan önce sistemin tam kontrolü ile**Aspose.Cells** . Aksi takdirde kurulum sırasında # 2869 hatası alabilirsiniz.**Aspose.Cells**yükleyicisini kullanarak.

Bunu başarmanın bazı yolları aşağıdadır.
### **Komut Satırını Kullanma**
1.  Windows dizininizde cmd.exe'yi arayın, ardından sağ tıklayın ve Farklı çalıştır'ı seçin...**yönetici**
 2. Şimdi, komut isteminde şu komutu çalıştırın: msiexec /i<your path>/Aspose.Cells.msi ve Enter.
### **Kontrol Panelini Kullanma**
- Başlat'ı tıklayın
- Denetim Masası'nı tıklayın
- Kullanıcı Hesapları ve Aile Güvenliği'ni tıklayın.
- Kullanıcı Hesapları'na tıklayın
- Kullanıcı Hesabı Denetimini Aç veya Kapat'a tıklayın
- onay kutusunun işaretini kaldırın
- Tamam'ı tıklayın

{{% alert color="primary" %}} 

Değişikliğin etkili olması için bilgisayarınızı yeniden başlatmanız gerekecek. Bu değişiklik, yalnızca sizinkini değil, bilgisayardaki tüm hesapları etkiler.

{{% /alert %}}
