---
title: İsimli Aralıkları Kullanmak
type: docs
weight: 110
url: /tr/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop,isimli aralıklar,isimler
description: Bu makale, GridDesktop taki isimli aralıkları tanıtır.
---

{{% alert color="primary" %}} 

Normalde, bir çalışma sayfasındaki sütun ve satır etiketlerini o sütun ve satırlardaki hücrelere başvurmak için kullanırsınız. Ancak, hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil eden açıklayıcı isimler oluşturabilirsiniz. **Ad**, bir hücre, hücre aralığı, formül veya sabit değeri temsil eden karakterler dizisine atıfta bulunan bir dize olabilir. Örneğin, Satış!C20:C30 gibi anlaşılması zor aralıklara başvurmak için Ürünler gibi anlaşılması kolay isimler kullanın. Formüllerde aynı çalışma sayfasındaki verilere başvurmak için etiketler kullanılabilir; başka bir çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız bir isim kullanabilirsiniz. **İsimli Aralıklar**, Microsoft'un en güçlü özelliklerinden biridir. Kullanıcılar, bu bir adla adlandırılmış aralığa bir ad atayabilir, böylece bu hücrelerin aralığı formüllerde adıyla başvurulabilir. **Aspose.Cells.GridDesktop**, bu özelliği destekler.

{{% /alert %}} 
## **Formüllerde İsimli Aralıkları Ekleme/Başvuru Yapma**
GridDesktop kontrolü, Excel dosyalarında isimli aralıkları içe/dışa aktarmayı destekler, bu işlemler için isimli aralıklar ile çalışmak için iki sınıf (**Name** ve **NameCollection**) sağlar.

Aşağıdaki kod parçası, onları nasıl kullanacağınızı size yardımcı olacaktır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
