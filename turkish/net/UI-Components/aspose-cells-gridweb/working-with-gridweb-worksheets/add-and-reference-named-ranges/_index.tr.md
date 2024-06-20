---
title: Isimlendirilmiş Aralıkları Ekleme ve Referans Verme
type: docs
weight: 120
url: /tr/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: Bu makale, GridWeb de adlandırılmış aralıklarla çalışmanın nasıl yapılacağını tanıtmaktadır. 
---

{{% alert color="primary" %}} 

Genellikle, sütun ve satır etiketleri hücrelere benzersiz bir şekilde başvurmak için kullanılır. Ancak, hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil etmek için açıklayıcı isimler oluşturabilirsiniz. **Ad** kelimesi, hücreyi, hücre aralığını, formülü veya sabit değeri temsil eden bir karakter dizisine atıfta bulunabilir. Örneğin, Satış!C20:C30 gibi anlaşılması zor aralıklara başvurmak için Products gibi anlaşılması kolay isimler kullanın. Formüllerde, aynı çalışma sayfasındaki verilere başvuran etiketler kullanılabilir; başka bir çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız bir isim kullanabilirsiniz. **Adlandırılmış aralıklar**, Microsoft Excel'in en güçlü özelliklerinden biridir. Kullanıcılar bir aralığa bir ad atayabilir ve bu adı formüllerde kullanabilir. Aspose.Cells.GridWeb bu özelliği destekler.

{{% /alert %}} 
## **Formüllerde İsimli Aralıkları Ekleme/Başvuru Yapma**
GridWeb denetimi, adlandırılmış aralıklarla çalışmak için iki sınıf (GridName ve GridNameCollection) sağlar. Aşağıdaki kod parçası, Adlandırılmış Aralık oluşturmayı ve bu formüllerde erişmeyi anlamanıza yardımcı olacaktır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
