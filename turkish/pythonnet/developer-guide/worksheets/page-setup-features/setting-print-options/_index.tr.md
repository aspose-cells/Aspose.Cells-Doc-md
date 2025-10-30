---
title: Baskı Seçeneklerini Ayarlama
type: docs
weight: 40
url: /tr/python-net/setting-print-options/
description: Bu makale, Aspose.Cells for Python via .NET API kullanarak Excel Çalışma Sayfası Sayfa Kurulumu nun Yazdırma Seçeneklerini programlı olarak nasıl ayarlayacağınızı gösterir. Yazdırma Alanı, Yazdırma Başlıkları ve Sayfa Sırasını ayarlayabilirsiniz.
keywords: Python Excel Kütüphanesi, Python da Excel yazdırma alanını ayarlama, Python da Excel yazdırma başlıklarını ayarlama, Python da Excel sayfa sırasını nasıl ayarlarım, Python da Yazdırma Seçenekleri Nasıl Ayarlanır, Python da Yazdırma Alanı Nasıl Ayarlanır, Python da Yazdırma Başlıkları Nasıl Ayarlanır. 
---

{{% alert color="primary" %}}

Microsoft Excel'in sayfa düzeni ayarları, kullanıcıların çalışma sayfalarının nasıl basılacağını kontrol etmelerini sağlayan birkaç baskı seçeneği (ayrıca sayfa seçenekleri olarak da adlandırılır) sunar.

{{% /alert %}}

## **Yazdırma Seçenekleri Nasıl Ayarlanır**

Bu baskı seçenekleri, kullanıcıların şunları yapmalarını sağlar:

- Çalışma sayfasında belirli bir baskı alanı seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.

Aspose.Cells for Python via .NET, Microsoft Excel tarafından sunulan tüm yazdırma seçeneklerini destekler ve geliştiriciler bu seçenekleri [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfının özellikleri aracılığıyla kolayca yapılandırabilir. Bu özelliklerin nasıl kullanıldığı aşağıda detaylı olarak açıklanmıştır.

## **Yazdırma Alanı Nasıl Ayarlanır**

Varsayılan olarak, baskı alanı veri içeren çalışma sayfasının tüm alanlarını içerir. Geliştiriciler, çalışma sayfasının belirli bir baskı alanını belirleyebilirler.

Belirli bir baskı alanı seçmek için, [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfının [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) özelliğini kullanın. Bu özelliğe, baskı alanını tanımlayan bir hücre aralığı atayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Yazdırma Başlıkları Nasıl Ayarlanır**

Aspose.Cells for Python via .NET, satır ve sütun başlıklarının tüm yazdırılan sayfalar üzerinde tekrarlanmasını sağlar. Bunu yapmak için, [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfın [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) ve [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Diğer Yazdırma Seçenekleri Nasıl Ayarlanır**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfı ayrıca aşağıdaki gibi genel yazdırma seçeneklerini ayarlamak için birkaç başka özellik sunar:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): Izgaraları yazdırmak veya yazdırmamak konusunda tanımlı olan bir Boolean özelliği.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): Satır ve sütun başlıklarını yazdırmak veya yazdırmamak konusunda tanımlı olan bir Boolean özelliği.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): Çalışsayıyı siyah-beyaz moda yazdırmak veya yazdırmamak konusunda tanımlı olan bir Boolean özelliği.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): Çalışma sayfasındaki yazdırma yorumlarını veya çalışma sayfasının sonunda yer alan yorumları gösterip göstermemeyi tanımlar.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): Grafiksiz olarak çalışsayıyı yazdırmayı tanımlayan bir boolean özelliği.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): Hücre hatalarını, görüntülendiği gibi, boş, çizgi veya N/A olarak yazdırmayı tanımlar.

[**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) ve [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) özelliklerini ayarlamak için Aspose.Cells, respectively [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) ve [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) özelliklerine atanan önceden tanımlanmış değerleri içeren iki numaralamayı, [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) ve [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype), sağlar.

[**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) numaralamasındaki önceden tanımlanmış değerler aşağıda açıklamalarıyla listelenmiştir.

|**Yazdırma Yorumları Türleri**|**Açıklama**|
| :- | :- |
|YAZDIRİÇİNDE|Yorumların çalışma sayfasında gösterilen şekilde yazdırılmasını belirler.|
|YORUM_YOK|Yorumların yazdırılmamasını sağlar.|
|YAZDIR_SAYFA_SONU|Yorumların çalışma sayfasının sonunda yazdırılmasını sağlar.|

[**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) numaralamasındaki önceden tanımlanmış değerler aşağıda açıklamalarıyla listelenmiştir.



|**Yazdırma Hataları Türleri**|**Açıklama**|
| :- | :- |
|YAZDIR_HATALAR_BOŞ|Hataların yazdırılmamasını sağlar.|
|YAZDIR_HATALAR_GRAFİK|Hataları "--" olarak yazdırır.|
|YAZDIR_HATALAR_GÖRÜNTÜLENİYOR|Hataları görüntülenen şekilde yazdırır.|
|YAZDIR_HATALAR_NA|Hataları "#N/A" olarak yazdırır.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Sayfa Sırasını Nasıl Ayarlarım**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfı, çalışma sayfasının birden fazla sayfasını yazdırmak için kullanılan [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) özelliğini sağlar. Sayfaların sıralaması aşağıdaki gibi iki olasılığı sağlar.

- **Aşağıdan önce ardından:** herhangi bir sayfayı sağa yazdırmadan önce tüm sayfaları aşağıya yazdırır.
- **Ardından aşağıdan önce:** sayfaları aşağıya yazdırmadan önce soldan sağa doğru sayfaları yazdırır.

Aspose.Cells, tüm önceden tanımlanmış sıralama tiplerini içeren [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) numaralaması sağlar.

[**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) numaralamasındaki önceden tanımlanmış değerler aşağıda listelenmiştir.

|**Yazdırma Sıralama Türleri**|**Açıklama**|
| :- | :- |
|AŞAĞI_DİK|Yazdırma sırasını aşağıdan yukarıya doğru temsil eder.|
|YUKARI_DİK|Yazdırma sırasını yukarıdan aşağıya doğru temsil eder.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
