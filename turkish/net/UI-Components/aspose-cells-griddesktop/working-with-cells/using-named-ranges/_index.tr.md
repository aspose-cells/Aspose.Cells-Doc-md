---
title: Adlandırılmış Aralıkları Kullanma
type: docs
weight: 110
url: /tr/net/using-named-ranges/
---
{{% alert color="primary" %}} 

 Normalde, bir çalışma sayfasındaki sütunların ve satırların etiketlerini, bu sütunlar ve satırlardaki hücrelere başvurmak için kullanırsınız. Ancak hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil etmek için açıklayıcı adlar oluşturabilirsiniz. Kelime**İsim**bir hücreyi, hücre aralığını, formülü veya sabit değeri temsil eden bir karakter dizisine atıfta bulunabilir. Örneğin, bir hücreyi, hücre aralığını, formülü veya sabit değeri temsil etmek için Sales!C20:C30 gibi anlaşılması zor aralıklara başvurmak için Ürünler gibi anlaşılması kolay adlar kullanın. Etiketler, aynı çalışma sayfasındaki verilere atıfta bulunan formüllerde kullanılabilir; başka bir çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız, bir ad kullanabilirsiniz.**Adlandırılmış Aralıklar** Microsoft'in en güçlü özelliklerinden biridir. Kullanıcılar, adlandırılmış bir aralığa bir ad atayabilir, böylece bu hücre aralığı formüllerde adıyla anılabilir.**Aspose.Cells.GridDesktop** bu özelliği destekler.

{{% /alert %}} 
## **Formüllerde Adlandırılmış Aralıkları Ekleme/Başvuruda Bulunma**
GridDesktop denetimi, Excel dosyalarındaki adlandırılmış aralıkları içe/dışa aktarmayı destekler, iki sınıf sağlar (**İsim** ve**İsim Koleksiyonu**) adlandırılmış aralıklarla çalışmak için.

Aşağıdaki kod parçacığı, bunları nasıl kullanacağınız konusunda size yardımcı olacaktır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
