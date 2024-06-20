---
title: Excel i NumPy e Dönüştür
type: docs
weight: 30
url: /tr/python-net/convert-excel-to-numpy/
description: Aspose.Cells for Python via .NET API sını kullanarak Excel i NumPy e dönüştürme.
keywords: Python da Excel i NumPy dizisine dönüştürme, Python da Çalışma Kitabını NumPy dizisine dönüştürme via NET, Python da Satırı NumPy dizisine dönüştürme, Python da Tabloyu NumPy dizisine dönüştürme, Python da ListObject i NumPy dizisine dönüştürme via NET, Python da Aralığı NumPy dizisine dönüştürme, Python da Sütunu NumPy dizisine dönüştürme.
---

## **NumPy'ya Giriş**
NumPy (Sayısal Python), Python'un açık kaynaklı sayısal hesaplama uzantısıdır. Bu araç, büyük matrisleri depolamak ve işlemek için kullanılabilir ve Python'un iç içe liste yapısından (matrisleri temsil etmek için de kullanılabilir) çok daha verimlidir. Büyük sayıda boyutlu dizileri ve matris işlemlerini destekler ve ayrıca dizi işlemleri için geniş bir matematiksel işlev kütüphanesi sağlar. 

NumPy'nın temel işlevleri:
1. Ndarray, hızlı, esnek ve yer tasarrufu sağlayan çok boyutlu dizi nesnesidir.
1. Matris çarpımı, transpozisyon, ters çevirme vb. içeren lineer cebir işlemleri.
1. Fourier dönüşümü, bir dizide hızlı Fourier dönüşümü yapma.
1. Kayan noktalı dizilerin hızlı işlemi.
1. Python içine C dil kodunu entegre ederek daha hızlı çalışmasını sağlama.

Aspose.Cells for Python via .NET API'sini kullanarak Excel, TSV, CSV, Json ve birçok farklı formatı Numpy dizisine dönüştürebilirsiniz.

## **Excel Çalışma Kitabını NumPy dizisine Dönüştürme**
Aspose.Cells for Python via .NET kullanarak excel verisini NumPy dizisine aktarmayı gösteren örnek kod parçası:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. Excel verilerini dolaşın ve Aspose.Cells for Python via .NET kullanarak veriyi NumPy dizisine aktarın.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

Çıktı sonucu:
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **Çalışma Sayfasını NumPy dizisine Nasıl Dönüştürülür**
Aspose.Cells for Python'i kullanarak elektronik tablo verilerini Numpy ndarray'e nasıl dışa aktarılacağını gösteren örnek bir kod parçacığıdır via .NET:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. Aspose.Cells for Python Excel kütüphanesi kullanarak çalışma sayfası verilerini Numpy ndarray'e dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

Çıktı sonucu:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **Excel'den Numpy ndarray'e bir aralığı nasıl dönüştürürsünüz**
Aspose.Cells for Python'i kullanarak aralık verilerini Numpy ndarray'e nasıl dışa aktarılacağını gösteren örnek bir kod parçacığıdır via .NET:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. Aralık oluşturun.
1. Aspose.Cells for Python Excel kütüphanesi kullanarak aralık verilerini Numpy ndarray'e dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

Çıktı sonucu:
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **Excel'in bir ListObject'ini Numpy ndarray'e nasıl dönüştürürsünüz**
Aspose.Cells for Python'i kullanarak ListObject verilerini Numpy ndarray'e nasıl dışa aktarılacağını gösteren örnek bir kod parçacığıdır via .NET:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. ListObject nesnesi oluşturun.
1. Aspose.Cells for Python Excel kütüphanesi kullanarak ListObject verilerini Numpy ndarray'e dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

Çıktı sonucu:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **Excel'in bir satırını Numpy ndarray'e nasıl dönüştürürsünüz**
Aspose.Cells for Python'i kullanarak Satır verilerini Numpy ndarray'e nasıl dışa aktarılacağını gösteren örnek bir kod parçacığıdır via .NET:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. Satır endeksine göre Satır nesnesini alın.
1. Aspose.Cells for Python Excel kütüphanesi kullanarak Satır verilerini Numpy ndarray'e dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

Çıktı sonucu:
```
['Detroit' 'Central' '3074']
```

## **Excel'in bir sütununu Numpy ndarray'e nasıl dönüştürürsünüz**
Aspose.Cells for Python'i kullanarak Sutun verilerini Numpy ndarray'e nasıl dışa aktarılacağını gösteren örnek bir kod parçacığıdır via .NET:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. Sütun dizinine göre Sütun nesnesini alın.
1. Aspose.Cells for Python Excel kütüphanesini kullanarak Sütun verisini NumPy ndarray'ına dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

Çıktı sonucu:
```
['Store' '3055' '3036' '3074']
```
