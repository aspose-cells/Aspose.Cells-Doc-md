---
title: Çalışma Sayfaları Ekle
type: docs
weight: 20
url: /tr/net/add-worksheets/
---
{{% alert color="primary" %}} 

Çalışma sayfaları, Aspose.Cells.GridWeb'in ayrılmaz bir parçasıdır. Tüm veriler çalışma sayfaları biçiminde yönetilir ve saklanır. Aspose.Cells.GridWeb, geliştiricilerin Aspose.Cells.GridWeb denetimine bir veya daha fazla çalışma sayfası eklemesine olanak tanır. Bu konuda, Aspose.Cells.GridWeb'e çalışma sayfası eklemeye yönelik basit yaklaşımlar gösterilmektedir.

{{% /alert %}} 
## **Çalışma Sayfası Ekleme**
### **Sayfa Adını Belirtmeden**
Aspose.Cells.GridWeb'e bir çalışma sayfası eklemenin en basit yolu, GridWeb denetiminde GridWorksheetCollection koleksiyonunun Add yöntemini çağırmaktır. Bu, varsayılan adları (Sayfa1, Sayfa2, Sayfa3 vb.) kullanan çalışma sayfaları oluşturur ve bunları GridWeb denetimine ekler.

**Çıktı: GridWeb'e varsayılan ada sahip bir çalışma sayfası eklendi** 

![yapılacaklar:resim_alternatif_metin](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 Add yöntemi, bu çalışma sayfasının örneğine erişmek için kullanılabilecek yeni çalışma sayfasının dizinini döndürür. Çalışma sayfalarına nasıl erişileceği hakkında daha fazla bilgi için, okuyun[Çalışma Sayfalarına Erişim](/cells/tr/net/access-worksheets/).

{{% /alert %}} 
### **Belirtilen Sayfa Adıyla**
Varsayılan adlandırma düzenini kullanmak yerine GridWeb denetimine belirli bir ada sahip bir çalışma sayfası eklemek için, belirtilen SheetName'i alan Add yönteminin aşırı yüklenmiş bir sürümünü çağırın. Örnek olarak, aşağıdaki örnek Fatura adlı bir çalışma sayfası ekler.

**Çıktı: Belirtilen ada sahip bir çalışma sayfası GridWeb'e eklendi** 

![yapılacaklar:resim_alternatif_metin](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Çalışma sayfası adını dize olarak kabul eden Add yöntemi, GridWorksheet'in bir örneğini döndürür.

{{% /alert %}}
