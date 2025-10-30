---
title: Lisanslama
type: docs
weight: 50
url: /tr/cpp/licensing/
---

## **Değerlendirme Sürümü Kısıtlamaları**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **Dosya veya Akış Nesnesi Kullanarak Lisansı Uygulayın**
Lisans, bir dosyadan veya akış nesnesinden yüklenebilir. Aspose.Cells for C++ aşağıdaki konumlarda lisansı aramaya çalışacaktır:

1. Açık yol.
1. Aspose.Cells.dll içeren klasör.
1. Aspose.Cells.dll'yi çağıran derlemenin bulunduğu klasör.
1. Giriş derlemesini (yani .exe dosyanızı) içeren klasör.
1. Aspose.Cells.dll'yi çağıran derlemede yerleşik bir kaynak.

Lisansı ayarlamak için en kolay yol, lisans dosyasını Aspose.Cells.dll dosyası ile aynı klasöre koymak ve aşağıdaki örnekte gösterildiği gibi dosya adını belirtmek (dizin olmadan).
### **Dosyadan Lisans Yükleme**
Lisansı uygulamanın en kolay yolu, lisans dosyasını Aspose.Cells.dll dosyası ile aynı klasöre koymak ve sadece dosya adını (dizin olmadan) belirtmektir.

{{% alert color="primary" %}} 

SetLicense yöntemini çağırdığınızda geçtiğiniz lisans adı, lisans dosyasının adı olmalıdır. Örneğin, lisans dosyasının adını "Aspose.Cells.lic.xml" olarak değiştirirseniz, bu dosya adını Cells->SetLicense(…) yöntemine geçirin.

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **Akış Nesnesinden Lisans Yükleme**
Aşağıdaki örnek, bir lisansı bir akıştan yüklemenin nasıl yapıldığını göstermektedir.

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
