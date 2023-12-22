---
title: Licensing
type: docs
weight: 50
url: /tr/cpp/licensing/
---
##  **Değerlendirme Sürümü Sınırlamaları**
 Aspose.Cells for C++'in ücretsiz değerlendirme sürümü, Aspose'in web sitesinin indirmeler bölümünden indirilebilir:<https://downloads.aspose.com/cells/cpp>.
##  **Dosya veya Akış Nesnesini Kullanarak Lisans Uygulayın**
Lisans bir dosyadan veya akış nesnesinden yüklenebilir. Aspose.Cells for C++, lisansı aşağıdaki konumlarda bulmaya çalışacaktır:

1. Açık yol.
1. Aspose.Cells.dll dosyasını içeren klasör.
1. Aspose.Cells.dll adlı derlemeyi içeren klasör.
1. Giriş derlemesini içeren klasör (.exe'niz).
1. Derlemede Aspose.Cells.dll adlı katıştırılmış bir kaynak.

Lisans ayarlamanın en kolay yolu, lisans dosyasını Aspose.Cells.dll dosyasıyla aynı klasöre koymak ve aşağıdaki örnekte gösterildiği gibi dosya adını yol olmadan belirtmektir.
###  **Dosyadan Lisans Yükleme**
Lisans uygulamanın en kolay yolu, lisans dosyasını Aspose.Cells.dll dosyasıyla aynı klasöre koymak ve yol olmadan yalnızca dosya adını belirtmektir.

{{% alert color="primary" %}} 

SetLicense yöntemini çağırdığınızda aktardığınız lisans adı, lisans dosyasının adı olmalıdır. Örneğin, lisans dosyası adını "Aspose.Cells.lic.xml" olarak değiştirirseniz, bu dosya adını Cells->SetLicense(…) yöntemine iletin.

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
###  **Akış Nesnesinden Lisans Yükleme**
Aşağıdaki örnek, bir akıştan lisansın nasıl yükleneceğini gösterir.

**C++**

{{< highlight "csharp" >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
