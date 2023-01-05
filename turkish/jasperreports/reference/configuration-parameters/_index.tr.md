---
title: Yapılandırma Parametreleri
type: docs
weight: 10
url: /tr/jasperreports/configuration-parameters/
---
{{% alert color="primary" %}} 

 Aşağıdaki tablo yapılandırma parametrelerini listeler.

{{% /alert %}} 

|**Parametre adı** |**Açıklama** |
|:- |:- |
| FORMAT_TYPE| Microsoft Excel 79 0 2003 veya Excel 2007 formatındaki dosyaları oluşturmak için "EXCEL97TO2003" veya "EXCEL2007" olarak ayarlanabilir.|
|DIR-DİR_BİR TANE_SAYFA_BAŞINA_ ÇARŞAF| Her rapor sayfasının farklı bir XLS çalışma sayfasına yazılması gerekip gerekmediğini belirten bir Boolean değeri.|
|DIR-DİR_KALDIRMAK_BOŞ_UZAY_ ARASINDA_SATIRLAR| Satır aralarında oluşabilecek boşlukların kaldırılıp kaldırılmayacağını belirten bir Boolean değeri.|
|DIR-DİR_KALDIRMAK_BOŞ_UZAY_ BETWEEN_COLUMNS ARASINDA|Sütunlar arasında oluşabilecek boşlukların kaldırılıp kaldırılmayacağını belirten bir Boolean değeri.|
|DIR-DİR_BEYAZ_ SAYFA ARKAPLANI| Sayfa arka planının beyaz mı yoksa varsayılan XLS arka plan rengi mi olacağını belirten bir Boole değeri. XLS arka plan renginin ne olduğu, XLS görüntüleyici özelliklerine veya işletim sistemi renk şemasına göre değişebilir.|
|DIR-DİR_TESPİT ETMEK_ HÜCRE_TİPİ| Dışa aktarıcının orijinal metin alanı ifadelerinin türünü dikkate alması ve hücre türlerini ve değerlerini buna göre ayarlaması gerekip gerekmediğini belirtmek için kullanılan bayrak.|
| SHEET_NAMES|Özel sayfa adlarını temsil eden bir dizi dize. Bu, IS ile birlikte kullanıldığında kullanışlıdır._BİR TANE_SAYFA_BAŞINA_ SHEET parametresi.|
|DIR-DİR_YAZI TİPİ_BOY_DÜZELTMEK_ ETKİNLEŞTİRİLMİŞ| Metnin belirtilen hücre yüksekliğine sığması için yazı tipi boyutunu azaltmak için işaretleyin.|
|MAKSİMUM_SATIRLAR_ PER_SHEET|Bir sayfada gösterilmesine izin verilen maksimum satır sayısını belirten bir tamsayı değeri. Ayarlandığında, kalan satırların görüntülenmesi için yeni bir sayfa oluşturulur. Negatif değerler veya sıfır, herhangi bir limitin ayarlanmadığı anlamına gelir.|
|DIR-DİR_GÖZ ARDI ETMEK_ GRAFİKLER| Grafik öğeleri yok saymak ve yalnızca metin öğelerini dışa aktarmak için işaretleyin.|
|DIR-DİR_ÇÖKÜŞ_ ROW_SPAN| Daralan satır aralığı için işaretleyin ve satırlar arasında hücreleri birleştirmekten kaçının.|
|DIR-DİR_GÖZ ARDI ETMEK_ HÜCRE_SINIR| Hücre kenarlığını yok saymak için işaretleyin.|
|DIR-DİR_KULLANMAK_ EXCEL_CHART| Statik resimler yerine Microsoft Excel formatında düzenlenebilir grafiğin kullanılması için işaret. Varsayılan değer doğrudur.|

