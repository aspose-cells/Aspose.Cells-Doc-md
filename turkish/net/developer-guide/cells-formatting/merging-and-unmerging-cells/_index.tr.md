---
title: Hücreleri Birleştirme ve Ayırma
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir .NET kitaplığıdır ve hücreleri birleştirme ve ayırma işlemlerini destekler. Bu makale, Aspose.Cells kitaplığını kullanarak hücreleri nasıl birleştirip ayıracağınızı ve birleştirilmiş hücre stili nasıl özelleştireceğinizi tanıtacaktır.
keywords: Aspose.Cells, NET kitaplığı, elektronik tablo, hücreleri birleştirme, hücreleri ayırma, stil ayarları, özel stiller
type: docs
weight: 190
url: /tr/net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells, bu özelliği destekler ve çalışsheet'lerde hücreleri birleştirebilir. Birleştirilmiş hücreleri de ayırabilir veya bölebilirsiniz. Birleştirilmiş bir hücrenin hücre referansı, orijinal seçilen aralıktaki sol üst hücrenin referansıdır.

{{% /alert %}} 
## **Giriş**
Her zaman her satır veya sütunda aynı hücre sayısını istemezsiniz. Örneğin, birkaç sütunu kapsayan bir hücreye başlık koymak isteyebilirsiniz. Veya, bir fatura oluştururken toplam için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre yapmak için hücreleri birleştirin. Microsoft Excel, kullanıcılara dosyaları seçme ve istedikleri şekilde elektronik tabloyu yapılandırmak için birleştirmelerine izin verir.

{{% alert color="primary" %}} 

Hücreler birleştirildiğinde, aralıktaki sol üst hücredeki veriler yalnızca korunur. Aralıktaki diğer hücrelerde veri varsa, bu veri silinir.
Benzer şekilde, biçimlendirme, birleştirme hücresinin referans hücresine dayalı olduğundan, hücreleri birleştirdiğinizde, aralıktaki sol üst hücrenin biçimlendirme ayarları birleştirilmiş hücreye uygulanır. Hücre bölündüğünde, yeni hücreler özgün biçim ayarlarını korur.

{{% /alert %}} 
## **Çalışsheet'te Hücreleri Birleştirme**
### **Microsoft Excel'de Hücreleri Birleştirme**
Aşağıdaki adımlar, MS Excel kullanarak çalışsheet'te hücreleri birleştirmeyi açıklar.

1. İstenen veriyi aralıktaki en sol üst hücreye kopyalayın.
2. Birleştirmek istediğiniz hücreleri seçin.
3. Bir satır veya sütunda hücreleri birleştirmek ve hücre içeriğini ortalamak için, **Biçimlendirme** araç çubuğundaki **Birleştir ve Ortala** simgesine tıklayın.
### **Aspose.Cells ile Hücreleri Birleştirmek**
Aspose.Cells.Cells Sınıfı, görev için bazı kullanışlı yöntemlere sahiptir. Örneğin, Merge() yöntemi belirtilen aralıkta hücreleri tek bir hücrede birleştirir.

Aşağıdaki örnek, bir çalışsheet'te (C6:E7) hücrelerin nasıl birleştirileceğini göstermektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Hücreleri Ayırma (Birleştirmeyi Bölmek)**
### **Microsoft Excel Kullanımı**
Aşağıdaki adımlar, Microsoft Excel kullanarak birleştirilmiş hücreleri nasıl ayıracağınızı açıklar.

1. Birleştirilmiş hücreyi seçin.
   Hücreler birleştirildiğinde, **Birleştir ve Ortala**, **Biçimlendirme** araç çubuğunda seçilidir.
1. **Biçimlendirme** araç çubuğunda **Birleştir ve Ortala**'ya tıklayın.
### **Aspose.Cells Kullanımı**
Aspose.Cells.Cells sınıfının UnMerge() adında bir yöntemi vardır; bu yöntem, hücreleri birleştirdiği hücre referansını kullanarak ayırır.

Aşağıdaki örnek, birleştirilmiş hücreleri (C6) nasıl ayıracağınızı göstermektedir. Örnek, önceki örnekte oluşturulan dosyayı kullanır ve birleştirilmiş hücreleri ayırır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Gelişmiş Konular**
- [Çalışsheet'teki Birleştirilmiş Hücreleri Bulma](/cells/tr/net/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="csharp" >}}
