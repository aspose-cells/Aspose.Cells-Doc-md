---
title: Çalışma Sayfaları Eklemek
type: docs
weight: 20
url: /tr/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: Bu makale, GridWeb e çalışma sayfası (GridWorksheet) eklemenin nasıl yapılacağını tanıtmaktadır.
---

{{% alert color="primary" %}} 

Çalışma sayfaları, Aspose.Cells.GridWeb'in ayrılmaz bir parçasıdır. Tüm veriler çalışma sayfaları şeklinde yönetilir ve depolanır. Aspose.Cells.GridWeb, geliştiricilere Aspose.Cells.GridWeb denetimine bir veya daha fazla çalışma sayfası eklemelerine olanak tanır.

{{% /alert %}} 
## **Çalışma Sayfası Ekleme**
### **Sayfa Adı Belirtmeden**
Aspose.Cells.GridWeb'e çalışma sayfası eklemenin en basit yolu, GridWeb denetimindeki GridWorksheetCollection koleksiyonunun Add yöntemini çağırmaktır. Bu, varsayılan adlar (yani Sheet1, Sheet2, Sheet3 vb.) kullanan çalışma sayfaları oluşturur ve bunları GridWeb denetimine ekler.

**Çıktı: varsayılan adlı bir çalışma sayfası, GridWeb'e eklenmiştir** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

Add yöntemi, yeni çalışma sayfasının dizinini döndürür, bu dizin, bu çalışma sayfasının örneğine erişmek için kullanılabilir. Çalışma sayfalarına nasıl erişileceğiyle ilgili daha fazla bilgi için [Çalışma Sayfalarına Erişim](/cells/tr/net/aspose-cells-gridweb/access-worksheets/) bölümünü okuyun.

{{% /alert %}} 
### **Belirtilen Sayfa Adıyla**
Varsayılan adlandırma şeması yerine GridWeb denetimine belirli bir isimle bir çalışma sayfası eklemek için Add yönteminin aşırı yüklenmiş bir sürümünü çağırmak gerekmektedir. Örneğin, aşağıdaki örnek, Invoice adında bir çalışma sayfası ekler.

**Çıktı: belirtilen adlı bir çalışma sayfası, GridWeb'e eklenmiştir** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Dize olarak çalışma sayfası adını alan Add yöntemi, GridWorksheet'in bir örneğini döndürür.

{{% /alert %}}
