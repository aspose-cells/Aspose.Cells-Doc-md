---
title: Formül Listesi
type: docs
weight: 10
url: /tr/reportingservices/formula-list/
---

**Rapor alanları**

|**Ad Kümesi**|**Formül Adı**|**Açıklama**|
| :- | :- | :- |
|Global alanlar |ExecutionTime |Raporun çalışmaya başladığı tarih ve saat. |
| |ReportServerUrl |Raporun çalıştırıldığı rapor sunucusunun URL'si. |
| |ReportName |Raporun rapor sunucusu veritabanında depolandığı ad. |
| |ReportFolder |Raporu içeren klasörün tam yolu. Bu, rapor sunucusu URL'sini içermez. |
|Kullanıcı |UserID |Raporu çalıştıran kullanıcının kimlik numarası. |
| |Language |Raporu çalıştıran kullanıcının dil kimliği. |
**Rapor alanları**

|**Ad Kümesi**|**Açıklama**|
| :- | :- |
|Parameters |Parametreler koleksiyonu, raporun içindeki rapor parametrelerini içerir. Parametreler sorgulara iletilerek, filtrelerde kullanılarak veya parametreye bağlı olarak raporun görünümünü değiştiren diğer işlevlerde kullanılabilir. |
|Alanlar |Geçerli veri kümesindeki alanları içeren Alanlar koleksiyonu. |
|Veri Seti ||
**Operatörler**
Aritmetik operatörler, başka bir sayı elde etmek için sayıları, sayısal değişkenleri, sayısal alanları ve sayısal işlevleri birleştirmek için kullanılır. Karşılaştırma operatörleri genellikle bir If ifadesi gibi bir kontrol yapısındaki koşul için operatlarları karşılaştırmak için kullanılır. Boolean operatörler genellikle kontrol yapıları için koşullar oluşturmak için karşılaştırma operatörleri ile birlikte kullanılır.

|**Ad Kümesi**|**Formül adı**|**Açıklama**|
| :- | :- | :- |
|Aritmetik |^ |Üs alma, örneğin 2^3. |
| |* |Çarpma, örneğin 2*3. |
| |/ |Bölme, örneğin 2/3. |
| |\\\ |Tam bölme, örneğin 2\\\3. |
| |Mod |Modulus, örneğin 4 Mod 3. |
| |+ |Toplama, örneğin 4 + 3. |
| |- |Çıkarma, örneğin 4 – 3. |
|Karşılaştırma |< |Daha az, örneğin 4 < 3 yanlış. |
| |<= |Daha az veya eşit, örneğin 4 <= 3 yanlış. |
|>| |Örneğin 4 > 3 doğrudur. |
|>=| |Örneğin 4 >= 3 doğrudur. |
|=| |Örneğin 4 = 3 yanlıştır. |
|<>| |Örneğin 4 <> 3 doğrudur. |
|Like| |Bir dizeyi desene karşılaştırır. Örneğin sonuç = dize desen. |
|Is| |İki nesne referans değişkenini karşılaştırır, örneğin asp aspose'dur. |
|Concatenation|& |İki ifadenin bir dize birleşimi oluşturur. |
|+| |İki sayıyı ekler veya sayısal bir ifadenin pozitif değerini döndürür. Ayrıca iki dize ifadesini birleştirmek için de kullanılabilir. |
Mantıksal/Bit Düzeyinde |And| |İki Boolean ifadesinde mantıksal birleşme veya iki sayısal ifadede bit düzeyinde birleşme yapar. |
|Not| |Bir Boolean ifadesinde mantıksal değillemeyi gerçekleştirir veya sayısal ifadede bit düzeyinde değillemeyi gerçekleştirir. |
|Or| |İki Boolean ifadesinde mantıksal ayrıma veya iki sayısal ifadede bit düzeyinde ayrıma yapar. |
|Xor| |İki Boolean ifadesinde mantıksal dışlama veya iki sayısal ifadede bit düzeyinde dışlama yapar. |
|AndAlso| |İki ifadede kısa devre mantıksal birleşme gerçekleştirir. |
|OrElse| |İki ifadede kısa devre dahil mantıksal ayrım yapar. |
Bit Kaydırma |>>| |Bir bit deseninde aritmetik sola kaydırma gerçekleştirir. |
|<<| |Bir bit deseninde aritmetik sağa kaydırma gerçekleştirir. |

