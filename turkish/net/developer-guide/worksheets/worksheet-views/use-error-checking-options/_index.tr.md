---
title: Hata Kontrolü Seçeneklerini Kullanma
type: docs
weight: 140
url: /tr/net/use-error-checking-options/
description: Bu makalede, C# API veya .NET Kütüphanesi ni kullanarak Excel çalışma sayfasının hata kontrol seçeneklerini (örneğin metin olarak saklanan sayılar) programlı olarak kullanacak örnek kod bulacaksınız.
keywords: c# ile excel de metin olarak sayı saklama, hata kontrolü excel seçenekleri c#
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların hata kontrol seçeneklerini ve kurallarını tanımlamalarına izin verir. Kullanıcılar, formüller oluştururken sık ​​sık hata kontrolleri görür, bir hücrenin sağ üst köşesinde küçük bir üçgen, bir hücrede bir sorun olduğunda vurgulanır. Excel, kullanıcılara hücreyle ilgili yaygın problemleri düzeltmelerine yardımcı olacak bilgiler sağlar.

{{% /alert %}}

## **Hata türleri**

Formülün bir sonuç döndüremeyeceği anlamına gelen hatalar - örneğin bir sayıyı sıfıra bölmek gibi - derhal dikkat gerektirir ve hücrede bir hata değeri görüntülenir. Yeşil üçgeni tıklamak, bir ünlem işareti gösterir, buna tıklamak, bir liste seçeneği açar.

Hata, seçenekler kullanılarak çözülebilir veya yok sayılabilir. Bir hatayı yok saymak, o hatanın daha sonra yapılan hata kontrollerinde görünmeyeceği anlamına gelir.

Aspose.Cells, hata kontrolü seçeneği özellikleri sağlar. Örneğin, metin olarak saklanan sayılar, formül hesaplama hataları ve doğrulama hataları gibi farklı türde hata kontrollerini yöneten [**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption) sınıfı. İstenen hata kontrolünü ayarlamak için [**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype) numarasını kullanın.

## **Metin Olarak Saklanan Sayılar**

Bazen, sayılar hücrelerde metin olarak biçimlendirilmiş ve saklanmış olabilir. Bu, hesaplamalarda sorunlara neden olabilir veya karışık sıralama düzenleri oluşturabilir. Metin olarak biçimlendirilmiş sayılar, hücrede sağa hizalanmış olarak değil, sola hizalanmış olarak bırakılır. Bir hücrelerde matematiksel bir işlem yapması gereken bir formül değeri döndürmezse, formülün başvurduğu hücrelerdeki hizalama kontrol edilmelidir - bu hücrelerin bazıları veya tümü metin olarak biçimlendirilmiş sayılar olabilir.

Metin olarak saklanan sayıları hızlı bir şekilde gerçek sayılara dönüştürmek için hata kontrol seçeneklerini kullanabilirsiniz. Microsoft Excel 2003'te:

1. **Araçlar** menüsünde **Seçenekler**'i tıklayın.
1. Hata Kontrolü sekmesini seçin.
   **Metin olarak saklanan sayı** seçeneği varsayılan olarak işaretlidir.
1. Bu seçeneği devre dışı bırakın.

Aşağıdaki örnek kod, Aspose.Cells API'lerini kullanarak bir çalışma sayfasındaki metin olarak saklanan sayılar hata kontrol seçeneğini devre dışı bırakmanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
