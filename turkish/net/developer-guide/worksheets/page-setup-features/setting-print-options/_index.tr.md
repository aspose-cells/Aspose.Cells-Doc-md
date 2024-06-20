---
title: Baskı Seçeneklerini Ayarlama
type: docs
weight: 40
url: /tr/net/setting-print-options/
description: Bu makale, C# API ve .NET Kütüphanesi kullanarak Excel Çalışma Sayfası Düzeni özelliğinin Baskı Seçeneklerini programlı olarak nasıl ayarlayacağınızı göstermektedir. Baskı Alanı, Baskı Başlıkları ve Sayfa Sırası ayarlayabilirsiniz.
keywords: excel baskı alanı ayarla c#, excel baskı başlıklarını ayarlayın c#, excel sayfa sırasını ayarlayın c#
---

{{% alert color="primary" %}}

Microsoft Excel'in sayfa düzeni ayarları, kullanıcıların çalışma sayfalarının nasıl basılacağını kontrol etmelerini sağlayan birkaç baskı seçeneği (ayrıca sayfa seçenekleri olarak da adlandırılır) sunar.

{{% /alert %}}

## **Baskı Seçeneklerini Ayarlama**

Bu baskı seçenekleri, kullanıcıların şunları yapmalarını sağlar:

- Çalışma sayfasında belirli bir baskı alanı seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.

Aspose.Cells, Microsoft Excel tarafından sunulan tüm baskı seçeneklerini destekler ve geliştiriciler, bu seçenekleri [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfının sunduğu özellikleri kolayca yapılandırabilirler. Bu özelliklerin nasıl kullanıldığı aşağıda daha ayrıntılı olarak tartışılmaktadır.

### **Baskı Alanı Belirle**

Varsayılan olarak, baskı alanı veri içeren çalışma sayfasının tüm alanlarını içerir. Geliştiriciler, çalışma sayfasının belirli bir baskı alanını belirleyebilirler.

Belirli bir baskı alanı seçmek için, [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfının [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea) özelliğini kullanın. Bu özelliğe, baskı alanını tanımlayan bir hücre aralığı atayın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Başlıkları Yazdırma**

Aspose.Cells, basılı bir çalışma sayfasının tüm sayfalarında tekrar edecek şekilde satır ve sütun başlıklarını belirlemenize olanak tanır. Bunu yapmak için [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfının [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) ve [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows) özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Diğer Yazdırma Seçeneklerini Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfı ayrıca aşağıdaki gibi genel yazdırma seçeneklerini ayarlamak için birkaç başka özellik sunar:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): Izgaraları yazdırmak veya yazdırmamak konusunda tanımlı olan bir Boolean özelliği.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): Satır ve sütun başlıklarını yazdırmak veya yazdırmamak konusunda tanımlı olan bir Boolean özelliği.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): Çalışsayıyı siyah-beyaz moda yazdırmak veya yazdırmamak konusunda tanımlı olan bir Boolean özelliği.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): Çalışma sayfasındaki yazdırma yorumlarını veya çalışma sayfasının sonunda yer alan yorumları gösterip göstermemeyi tanımlar.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): Grafiksiz olarak çalışsayıyı yazdırmayı tanımlayan bir boolean özelliği.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): Hücre hatalarını, görüntülendiği gibi, boş, çizgi veya N/A olarak yazdırmayı tanımlar.

[**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) ve [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) özelliklerini ayarlamak için Aspose.Cells, respectively [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) ve [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) özelliklerine atanan önceden tanımlanmış değerleri içeren iki numaralamayı, [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) ve [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype), sağlar.

[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) numaralamasındaki önceden tanımlanmış değerler aşağıda açıklamalarıyla listelenmiştir.

|**Yazdırma Yorumları Türleri**|**Açıklama**|
| :- | :- |
|PrintInPlace| Çalışma sayfasında görüntülenen yorumları yazdırmayı belirtir.
|PrintNoComments| Yorumları yazdırmamayı belirtir.
|PrintSheetEnd| Yorumları çalışma sayfasının sonunda yazdırmayı belirtir.

[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) numaralamasındaki önceden tanımlanmış değerler aşağıda açıklamalarıyla listelenmiştir.



|**Yazdırma Hataları Türleri**|**Açıklama**|
| :- | :- |
|PrintErrorsBlank| Hataları yazdırmamayı belirtir.
|PrintErrorsDash| Hataları "--" olarak yazdırmayı belirtir.
|PrintErrorsDisplayed| Hataları görüntülendiği gibi yazdırmayı belirtir.
|PrintErrorsNA| Hataları "#N/A" olarak yazdırmayı belirtir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Sayfa Sırasını Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfı, çalışma sayfasının birden fazla sayfasını yazdırmak için kullanılan [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) özelliğini sağlar. Sayfaların sıralaması aşağıdaki gibi iki olasılığı sağlar.

- **Aşağıdan önce ardından:** herhangi bir sayfayı sağa yazdırmadan önce tüm sayfaları aşağıya yazdırır.
- **Ardından aşağıdan önce:** sayfaları aşağıya yazdırmadan önce soldan sağa doğru sayfaları yazdırır.

Aspose.Cells, tüm önceden tanımlanmış sıralama tiplerini içeren [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) numaralaması sağlar.

[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) numaralamasındaki önceden tanımlanmış değerler aşağıda listelenmiştir.

|**Yazdırma Sıralama Türleri**|**Açıklama**|
| :- | :- |
|DownThenOver|Aşağıdan önce ardından sıralama temsil eder.
|OverThenDown|Ardından aşağıdan önce sıralama temsil eder.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
