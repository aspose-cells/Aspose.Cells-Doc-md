---
title: Formül Listesi
type: docs
weight: 10
url: /tr/reportingservices/formula-list/
---
**Rapor alanları**

|**Set Adı** |**Formül Adı**|**Tanım**|
|:- |:- |:- |
| Küresel alanlar| Uygulama vakti|Raporun çalışmaya başladığı tarih ve saat.|
|| RaporSunucuUrl'si| Raporun çalıştırıldığı rapor sunucusunun URL'si.|
|| Rapor Adı| Raporun, rapor sunucusu veritabanında saklandığı şekliyle adı.|
|| Rapor Klasörü| Raporu içeren klasörün tam yolu. Bu, rapor sunucusu URL'sini içermez.|
| kullanıcı| Kullanıcı kimliği| Raporu çalıştıran kullanıcının kimliği.|
|| Dil| Raporu çalıştıran kullanıcının dil kimliği.|
**Rapor alanları**

|**Set Adı**|**Tanım**|
|:- |:- |
| parametreler| Parametreler koleksiyonu, rapor içindeki rapor parametrelerini içerir. Parametreler sorgulara iletilebilir, filtrelerde kullanılabilir veya parametreye göre raporun görünümünü değiştiren diğer işlevlerde kullanılabilir.|
| alanlar| Fields koleksiyonu, geçerli veri kümesindeki alanları içerir.|
| Veri Kümesi||
**Operatörler**
Aritmetik işleçler, başka bir sayı elde etmek için sayıları, sayısal değişkenleri, sayısal alanları ve sayısal işlevleri birleştirmek için kullanılır. Karşılaştırma işleçleri genellikle If ifadesi gibi bir kontrol yapısındaki bir koşul için işlenenleri karşılaştırmak için kullanılır. Boole işleçleri, genellikle kontrol yapıları için koşullar oluşturmak üzere karşılaştırma işleçleriyle birlikte kullanılır.

|**Set Adı**|**formül adı**|**Tanım**|
|:- |:- |:- |
| Aritmetik|^ | Üs alma, örneğin 2^3.|
||* | Çarpma, örneğin 2*3.|
||/ | Bölme, örneğin 2/3.|
||\\\ | Tamsayı bölümü, örneğin 2\\\3.|
|| mod| Modül, örneğin 4 Mod 3.|
||+ | Toplama, örneğin 4 + 3.|
||- | Çıkarma, örneğin 4 – 3.|
| Karşılaştırmak|< | Daha az, örneğin 4< 3 false. |
||<= | Küçük veya eşittir, örneğin 4<= 3 false. |
||> | Büyüktür, örneğin 4 > 3 doğrudur.|
||>= | Büyüktür veya eşittir, örneğin 4 >= 3 doğru.|
||= | Eşit, örneğin 4 = 3 yanlış.|
||<> | Eşit değil, örneğin 4<> 3 doğru.|
|| Beğenmek|Bir diziyi bir modelle karşılaştırır. Örneğin sonuç = string Benzer kalıp.|
|| Dır-dir| İki nesne referans değişkenini karşılaştırır, örneğin asp Is aspose.|
| birleştirme|& | İki ifadeden oluşan bir dizi birleştirme oluşturur.|
||+ | İki sayı ekler veya bir sayısal ifadenin pozitif değerini döndürür. İki dize ifadesini birleştirmek için de kullanılabilir.|
| Mantıksal/Bitsel| Ve| İki Boole ifadesinde mantıksal bağlaç veya iki sayısal ifadede bit düzeyinde bağlaç gerçekleştirir.|
|| Değil| Bir Boole ifadesinde mantıksal olumsuzlama veya sayısal bir ifadede bit düzeyinde olumsuzlama gerçekleştirir.|
|| Veya| İki Boole ifadesinde mantıksal ayırma veya iki sayısal ifadede bit düzeyinde ayırma gerçekleştirir.|
|| Xor| İki Boole ifadesinde mantıksal bir dışlama veya iki sayısal ifadede bit düzeyinde bir dışlama gerçekleştirir.|
|| Ve ayrıca| İki ifade üzerinde kısa devre yapan mantıksal bağlaç gerçekleştirir.|
|| VeyaBaşka|İki ifade üzerinde kısa devre yapan kapsayıcı mantıksal ayırma gerçekleştirir.|
| Bit Kaydırma|>> | Bir bit modelinde aritmetik bir sola kaydırma gerçekleştirir.|
||<< | Bir bit örüntüsünde aritmetik sağa kaydırma gerçekleştirir.|

