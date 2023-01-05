---
title: Adlandırılmış Aralıkları Ekleme ve Referans Alma
type: docs
weight: 120
url: /tr/net/add-and-reference-named-ranges/
---
{{% alert color="primary" %}} 

 Normalde sütun ve satır etiketleri, hücrelere benzersiz bir şekilde atıfta bulunmak için kullanılır. Ancak hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil etmek için açıklayıcı adlar oluşturabilirsiniz. Kelime**İsim**bir hücreyi, hücre aralığını, formülü veya sabit değeri temsil eden bir karakter dizisine atıfta bulunabilir. Örneğin, Satış!C20:C30 gibi anlaşılması zor aralıklara atıfta bulunmak için Ürünler gibi anlaşılması kolay adlar kullanın. Etiketler, aynı çalışma sayfasındaki verilere atıfta bulunan formüllerde kullanılabilir; başka bir çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız, bir ad kullanabilirsiniz.**Adlandırılmış aralıklar** Microsoft Excel'in en güçlü özelliklerinden biridir. Kullanıcılar bir aralığa bir ad atayabilir ve bu adı formüllerde kullanabilir. Aspose.Cells.GridWeb bu özelliği destekler.

{{% /alert %}} 
## **Formüllerde Adlandırılmış Aralıkları Ekleme/Başvuruda Bulunma**
GridWeb denetimi, adlandırılmış aralıklarla çalışmak için iki sınıf (GridName ve GridNameCollection) sağlar. Aşağıdaki kod parçacığı, Adlandırılmış Aralık'ı nasıl oluşturacağınızı ve ona formüllerden nasıl erişeceğinizi anlamanıza yardımcı olacaktır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
