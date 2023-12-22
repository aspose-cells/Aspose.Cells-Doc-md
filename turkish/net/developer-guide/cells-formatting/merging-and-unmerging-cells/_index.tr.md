---
title: Birleştirme ve Ayrılma Cells
description: Aspose.Cells, hücrelerin birleştirilmesini ve ayrılmasının desteklenmesini destekleyen, elektronik tablo dosyalarıyla çalışmaya yönelik bir .NET kitaplığıdır. Bu makalede, Aspose.Cells kitaplığı kullanılarak hücrelerin nasıl birleştirilip ayrılacağı ve birleştirilmiş hücre stilinin nasıl özelleştirileceği anlatılacaktır.
keywords: Aspose.Cells, NET library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /tr/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells bu özelliği destekler ve ayrıca çalışma sayfasındaki hücreleri birleştirebilir. Birleştirilmiş hücreleri de ayırabilir veya bölebilirsiniz. Birleştirilmiş bir hücrenin hücre referansı, orijinal seçilen aralıktaki sol üst hücrenin referansıdır.

{{% /alert %}} 
##  **giriiş**
Her satır veya sütunda her zaman aynı sayıda hücre olmasını istemezsiniz. Örneğin, birden fazla sütuna yayılan bir hücreye başlık koymak isteyebilirsiniz. Veya fatura oluşturuyorsanız toplam için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre oluşturmak için bunları birleştirin. Microsoft Excel, kullanıcıların dosyaları seçmelerine ve elektronik tabloyu istedikleri gibi yapılandırmak için bunları birleştirmelerine olanak tanır.

{{% alert color="primary" %}} 

Hücreler birleştirildiğinde yalnızca sol üst hücrelerdeki verilerin korunacağını unutmayın. Aralıktaki diğer hücrelerde veri varsa bu veriler silinir.
Biçimlendirme de aynı şekilde referans hücreyi temel alır; böylece hücreleri birleştirdiğinizde aralıktaki sol üst hücrenin biçimlendirme ayarları birleştirilmiş hücreye uygulanır. Hücre bölündüğünde yeni hücreler orijinal format ayarlarını korur.

{{% /alert %}} 
##  **Cells'i Çalışma Sayfasında Birleştirme**
###  **Cells'i Microsoft Excel'de birleştirme**
Aşağıdaki adımlarda MS Excel kullanılarak çalışma sayfasındaki hücrelerin nasıl birleştirileceği açıklanmaktadır.

1. İstediğiniz verileri aralığın en sol üst hücresine kopyalayın.
1. Birleştirmek istediğiniz hücreleri seçin.
1.  Bir satır veya sütundaki hücreleri birleştirmek ve hücre içeriğini ortalamak için**Birleştir ve Ortala** üzerindeki simge**Biçimlendirme** araç çubuğu.
###  **Cells'in Aspose.Cells ile birleştirilmesi**
Aspose.Cells.Cells Sınıfının bu görev için bazı yararlı yöntemleri vardır. Örneğin Merge() yöntemi, hücreleri belirli bir aralıktaki tek bir hücrede birleştirir.

Aşağıdaki örnek, bir çalışma sayfasındaki hücrelerin (C6:E7) nasıl birleştirileceğini gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
##  **Ayrılıyor (Bölünüyor) Birleştirildi Cells**
###  **Microsoft Excel'i kullanma**
Aşağıdaki adımlarda, birleştirilmiş hücrelerin Microsoft Excel kullanılarak nasıl bölüneceği açıklanmaktadır.

1. Birleştirilmiş hücreyi seçin.
 Hücreler birleştiğinde**Birleştir ve Ortala** üzerinde seçilir**Biçimlendirme** araç çubuğu.
1.  Tıklamak**Birleştir ve Ortala** üzerinde**Biçimlendirme** araç çubuğu.
###  **Aspose.Cells'i kullanma**
Aspose.Cells.Cells sınıfı, hücreleri orijinal durumlarına bölen UnMerge() adında bir yönteme sahiptir. Yöntem, birleştirilmiş hücre aralığındaki hücrenin referansını kullanarak hücreleri ayırır.

Aşağıdaki örnek, birleştirilmiş hücrelerin (C6) nasıl bölüneceğini gösterir. Örnek, önceki örnekte oluşturulan dosyayı kullanır ve birleştirilmiş hücreleri böler.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


##  **İleri konular**
- [Bir Çalışma Sayfasındaki Birleştirilmiş Cells'i Algıla](/cells/tr/net/detect-merged-cells-in-a-worksheet/)
