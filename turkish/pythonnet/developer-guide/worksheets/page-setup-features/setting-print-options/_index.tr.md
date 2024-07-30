---
title: Baskı Seçeneklerini Ayarlama
type: docs
weight: 40
url: /tr/python-net/setting-print-options/
description: Bu makale, Aspose.Cells için Python via .NET API sini kullanarak Excel Çalışma Sayfası Ayarı özelliğinin Yazdırma Seçeneklerini programlı olarak nasıl ayarlayacağınızı göstermektedir. Yazdırma Alanı, Yazdırma Başlıkları ve Sayfa Sırasını ayarlayabilirsiniz.
keywords: Python Excel Kütüphanesi, Python excel yazdırma alanı ayarlamak, Python excel yazdırma başlıklarını ayarlamak, Python excel sayfa sırasını nasıl ayarlarım, Python Nasıl Yazdırma Seçeneklerini Ayarlarım, Python Nasıl Yazdırma Alanı Ayarlarım, Python Nasıl Yazdırma Başlıkları Ayarlarım. 
---

{{% alert color="primary" %}}

Microsoft Excel'in sayfa düzeni ayarları, kullanıcıların çalışma sayfalarının nasıl basılacağını kontrol etmelerini sağlayan birkaç baskı seçeneği (ayrıca sayfa seçenekleri olarak da adlandırılır) sunar.

{{% /alert %}}

## **Yazdırma Seçeneklerini Nasıl Ayarlarım**

Bu baskı seçenekleri, kullanıcıların şunları yapmalarını sağlar:

- Çalışma sayfasında belirli bir baskı alanı seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.

Aspose.Cells için Python via .NET, Microsoft Excel tarafından sunulan tüm yazdırma seçeneklerini destekler ve geliştiriciler bu seçenekleri kolayca yapılandırabilirler. Bu özelliklerin nasıl kullanıldığı daha detaylı olarak aşağıda tartışılmaktadır.

## **Yazdırma Alanını Nasıl Ayarlarım**

Varsayılan olarak, baskı alanı veri içeren çalışma sayfasının tüm alanlarını içerir. Geliştiriciler, çalışma sayfasının belirli bir baskı alanını belirleyebilirler.

Belirli bir baskı alanı seçmek için, [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfının [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) özelliğini kullanın. Bu özelliğe, baskı alanını tanımlayan bir hücre aralığı atayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Yazdırma Başlıklarını Nasıl Ayarlarım**

Aspose.Cells için Python via .NET, yazdırılan bir çalışma sayfasının tüm sayfalarında yinelemesini istediğiniz satır ve sütun başlıklarını belirlemenize izin verir. Bunu yapmak için [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfının [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) ve [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Diğer Yazdırma Seçeneklerini Nasıl Ayarlanır**

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
|YERİNDE YAZDIR|Yorumları çalışma sayfasında göründüğü gibi yazdırmayı belirtir.|
|YORUM YAZDIRMAMA|Yorumları yazdırmamayı belirtir.|
|SAYFA SONUNA YAZDIR|Yorumları çalışma sayfasının sonunda yazdırmayı belirtir.|

[**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) numaralamasındaki önceden tanımlanmış değerler aşağıda açıklamalarıyla listelenmiştir.



|**Yazdırma Hataları Türleri**|**Açıklama**|
| :- | :- |
|HATALARI YAZDIRMA BOŞ|Hataları yazdırmamayı belirtir.|
|HATALARI TİRE YAZDIR|Hataları "--" olarak yazdırmayı belirtir.|
|HATALARI GÖRÜNDÜĞÜ GİBİ YAZDIR|Hataları görüntülendiği gibi yazdırmayı belirtir.|
|HATALARI #YOK YAZDIR|Hataları "#YOK" olarak yazdırmayı belirtir.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Sayfa Sırası Nasıl Ayarlanır**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfı, çalışma sayfasının birden fazla sayfasını yazdırmak için kullanılan [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) özelliğini sağlar. Sayfaların sıralaması aşağıdaki gibi iki olasılığı sağlar.

- **Aşağıdan önce ardından:** herhangi bir sayfayı sağa yazdırmadan önce tüm sayfaları aşağıya yazdırır.
- **Ardından aşağıdan önce:** sayfaları aşağıya yazdırmadan önce soldan sağa doğru sayfaları yazdırır.

Aspose.Cells, tüm önceden tanımlanmış sıralama tiplerini içeren [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) numaralaması sağlar.

[**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) numaralamasındaki önceden tanımlanmış değerler aşağıda listelenmiştir.

|**Yazdırma Sıralama Türleri**|**Açıklama**|
| :- | :- |
|AŞAĞI SONRA ÜSTE|Yazdırma sırasını aşağı sonra üst olarak temsil eder.|
|ÜSTÜ SONRA AŞAĞI|Yazdırma sırasını üst sonra aşağı olarak temsil eder.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
