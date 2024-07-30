---
title: Hata Kontrolü Seçeneklerini Kullanma
type: docs
weight: 140
url: /tr/python-net/use-error-checking-options/
description: Bu makalede, Excel çalışma sayfalarının hata denetleme seçeneklerini programatik olarak kullanmak için örnek kodlar bulacaksınız. Örneğin, Aspose.Cells for Python via .NET API sini kullanarak Metin Olarak Saklanan Sayılar gibi hata denetleme seçeneklerini kullanın.
keywords: Python Excel Kütüphanesi, Excel de Metin Olarak Sayı Saklama, Python da hata denetleme excel seçenekleri ile başa çıkma.
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların hata kontrol seçeneklerini ve kurallarını tanımlamalarına izin verir. Kullanıcılar, formüller oluştururken sık ​​sık hata kontrolleri görür, bir hücrenin sağ üst köşesinde küçük bir üçgen, bir hücrede bir sorun olduğunda vurgulanır. Excel, kullanıcılara hücreyle ilgili yaygın problemleri düzeltmelerine yardımcı olacak bilgiler sağlar.

{{% /alert %}}

## **Hata türleri**

Formülün bir sonuç döndüremeyeceği anlamına gelen hatalar - örneğin bir sayıyı sıfıra bölmek gibi - derhal dikkat gerektirir ve hücrede bir hata değeri görüntülenir. Yeşil üçgeni tıklamak, bir ünlem işareti gösterir, buna tıklamak, bir liste seçeneği açar.

Hata, seçenekler kullanılarak çözülebilir veya yok sayılabilir. Bir hatayı yok saymak, o hatanın daha sonra yapılan hata kontrollerinde görünmeyeceği anlamına gelir.

Aspose.Cells for Python via .NET, hata denetleme seçenek özellikleri sağlar. [**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption) sınıfı, metin olarak saklanan sayılar, formül hesaplama hataları ve doğrulama hataları gibi farklı hata denetimleri türlerini yönetir. İstenen hata denetimini ayarlamak için [**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype) numaralı numaralandırmayı kullanın.

## **Metin Olarak Saklanan Sayılar**

Bazen, sayılar hücrelerde metin olarak biçimlendirilmiş ve saklanmış olabilir. Bu, hesaplamalarda sorunlara neden olabilir veya karışık sıralama düzenleri oluşturabilir. Metin olarak biçimlendirilmiş sayılar, hücrede sağa hizalanmış olarak değil, sola hizalanmış olarak bırakılır. Bir hücrelerde matematiksel bir işlem yapması gereken bir formül değeri döndürmezse, formülün başvurduğu hücrelerdeki hizalama kontrol edilmelidir - bu hücrelerin bazıları veya tümü metin olarak biçimlendirilmiş sayılar olabilir.

Metin olarak saklanan sayıları hızlı bir şekilde gerçek sayılara dönüştürmek için hata kontrol seçeneklerini kullanabilirsiniz. Microsoft Excel 2003'te:

1. **Araçlar** menüsünde **Seçenekler**'i tıklayın.
1. Hata Denetimi sekmesini seçin. **Metin Olarak Saklanan Sayılar** seçeneği varsayılan olarak işaretlidir.
1. Bu seçeneği devre dışı bırakın.

Aşağıdaki örnek kod, Aspose.Cells for Python via .NET API'lerini kullanarak bir şablon XLS dosyasında çalışma sayfası için metin olarak saklanan sayılar hata denetim seçeneğini devre dışı bırakmanın nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
