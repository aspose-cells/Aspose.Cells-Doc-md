---
title: lisanslama
type: docs
weight: 50
url: /tr/cpp/licensing/
---
## **Değerlendirme Sürümü Sınırlamaları**
 Aspose.Cells for C++'in ücretsiz değerlendirme sürümü, Aspose'in şu adresteki web sitesindeki indirmeler bölümünden indirilebilir:<https://downloads.aspose.com/cells/cpp>.
## **Dosya veya Akış Nesnesi Kullanarak Lisansı Uygulayın**
Lisans bir dosyadan veya akış nesnesinden yüklenebilir. Aspose.Cells for C++ aşağıdaki konumlarda lisansı bulmaya çalışacak:

1. Açık yol.
1. Aspose.Cells.dll dosyasını içeren klasör.
1. Aspose.Cells.dll adlı derlemeyi içeren klasör.
1. Giriş derlemesini içeren klasör (.exe'niz).
1. Derlemede Aspose.Cells.dll olarak adlandırılan katıştırılmış bir kaynak.

Lisans ayarlamanın en kolay yolu, lisans dosyasını Aspose.Cells.dll dosyasıyla aynı klasöre koymak ve aşağıdaki örnekte gösterildiği gibi dosya adını yolsuz olarak belirtmektir.
### **Dosyadan Lisans Yükleme**
Bir lisansı uygulamanın en kolay yolu, lisans dosyasını Aspose.Cells.dll dosyasıyla aynı klasöre koymak ve yolsuz sadece dosya adını belirtmektir.

{{% alert color="primary" %}} 

SetLicense yöntemini çağırdığınızda, ilettiğiniz lisans adı, lisans dosyasının adı olmalıdır. Örneğin, lisans dosyası adını "Aspose.Cells.lic.xml" olarak değiştirirseniz, bu dosya adını Cells->SetLicense(…) yöntemine iletin.

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License> license = new License();

license->SetLicense(new String("Aspose.Cells.lic"));

{{< /highlight >}}
### **Akış Nesnesinden Lisans Yükleme**
Aşağıdaki örnek, bir akıştan bir lisansın nasıl yükleneceğini gösterir.

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License>license = new License();

intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.Cells.lic"), FileMode_Open);

license->SetLicense(myStream);

{{< /highlight >}}
