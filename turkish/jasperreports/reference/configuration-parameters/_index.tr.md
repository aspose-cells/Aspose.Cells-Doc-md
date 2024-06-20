---
title: Yapılandırma Parametreleri
type: docs
weight: 10
url: /tr/jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

Aşağıdaki tablo, yapılandırma parametrelerini listeler. 

{{% /alert %}} 

|**Parametre adı** |**Açıklama** |
| :- | :- |
|FORMAT_TYPE | Microsoft Excel 79 0 2003 veya Excel 2007 format dosyalarını oluşturmak için "EXCEL97TO2003" veya "EXCEL2007" olarak ayarlanabilir. |
|IS_ONE_PAGE_PER_SHEET | Satırlar arasında görünebilecek boşlukların kaldırılıp kaldırılmayacağını belirleyen Boolean bir değer. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS | Satırlar arasında görünebilecek boşlukların kaldırılıp kaldırılmayacağını belirleyen bir Boolean değeri. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS | Sütunlar arasında oluşabilecek boşlukların kaldırılıp kaldırılmayacağını belirleyen bir Boolean değeri. |
|IS_WHITE_PAGE_BACKGROUND | Sayfa arka planının beyaz olup olmayacağını veya varsayılan XLS arka plan renginin ne olduğunu belirleyen Boolean bir değer. XLS arka plan rengi, XLS görüntüleyici özelliklerine veya işletim sistemi renk şemasına bağlı olarak değişebilir. |
|IS_DETECT_CELL_TYPE | Dışa aktarıcının, orijinal metin alanı ifadelerinin türünü dikkate alıp hücre tiplerini ve değerlerini buna göre ayarlamasının gerekip gerekmediğini belirtmek için kullanılan bayrak. |
|SHEET_NAMES | Tek Sayfa Başına - IS_ONE_PAGE_PER_SHEET parametresiyle birlikte kullanıldığında, özel sayfa adlarını temsil eden bir dizi dize. |
|IS_FONT_SIZE_FIX_ENABLED | Metin belirtilen hücre yüksekliğine uyması için font boyutunu azaltma bayrağı. |
|MAXIMUM_ROWS_PER_SHEET | Bir sayfada gösterilebilecek maksimum satır sayısını belirten tamsayı değeri. Ayarlandığında, gösterilmek istenen kalan satırlar için yeni bir sayfa oluşturulur. Negatif değerler veya sıfır, herhangi bir sınırın belirlenmediği anlamına gelir. |
|IS_IGNORE_GRAPHICS | Grafiksel öğeleri yok sayma ve yalnızca metin öğelerini dışa aktarma için bayrak. |
|IS_COLLAPSE_ROW_SPAN | Satır aralığını aksatma ve satırlar arasında hücreleri birleştirmeyi önleme bayrağı. |
|IS_IGNORE_CELL_BORDER | Hücre sınırını yok sayma bayrağı. |
|IS_USE_EXCEL_CHART | Statik resimler yerine Microsoft Excel biçiminde düzenlenebilir grafik kullanma bayrağı. Varsayılan değer true'dur. |

