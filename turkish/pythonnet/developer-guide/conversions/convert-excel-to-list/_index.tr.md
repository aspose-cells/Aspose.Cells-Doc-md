---
title: Excel i Python Verisine Dönüştürme
type: docs
weight: 30
url: /tr/python-net/convert-excel-to-list/
description: Aspose.Cells for Python via .NET API sini kullanarak Excel i Liste Dönüştürme.
keywords: Python Excel Kütüphanesi Kullanarak Excel i Sözlüğe Dönüştürme, Çalışma Kitabını Python Excel Kütüphanesi Kullanarak Sözlüğe Dönüştürme, Python Excel Kütüphanesi Kullanarak Satır Nesnesini Listeye Dönüştürme, Liste Nesnesini Listeye Dönüştürme, Python Excel Kütüphanesi Kullanarak Sütun Nesnesini Listeye Dönüştürme, Aralığı Liste Olarak Döndürme, Python Excel Kütüphanesi Kullanarak Çalışma Sayfasını Listeye Dönüştürme.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET API'si kullanarak, Çalışma Kitabı, Çalışma Sayfası, Aralık, Satır, Sütun ve diğer excel verilerini Python liste şekline dönüştürebilirsiniz.

{{% /alert %}}

## **Excel Çalışma Kitabını Sözlüğe Nasıl Dönüştürülür**
Aspose.Cells for Python via .NET kullanarak excel verilerini sözlüğe nasıl aktaracağınızı gösteren örnek bir kod parçası aşağıda verilmiştir:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. Tüm çalışma sayfalarını gezin ve Aspose.Cells for Python Excel kütüphanesini kullanarak çalışma kitabını sözlüğe dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

Çıktı sonucu:
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **Excel Çalışma Kitabını Listeye Nasıl Dönüştürülür**
Excel verilerini liste olarak dışa aktarmak için Aspose.Cells for Python via .NET kullanarak örnek kod parçası:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. Tüm çalışma sayfalarını gezin ve Aspose.Cells for Python Excel kütüphanesini kullanarak çalışma kitabını listede dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

Çıktı sonucu:
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **Excel Çalışma Sayfasını Listeye Nasıl Dönüştürülür**
Excel çalışma sayfası verilerini liste olarak dışa aktarmak için Aspose.Cells for Python via .NET kullanarak örnek kod parçası:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. Aspose.Cells for Python Excel kütüphanesini kullanarak çalışma sayfası verilerini liste olarak dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

Çıktı sonucu:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **Excel ListObject'ini Listeye Nasıl Dönüştürülür**
Aspose.Cells for Python via .NET kullanarak ListObject verilerini liste olarak dışa aktarmak için örnek kod parçası:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. ListObject nesnesi oluşturun.
Aspose.Cells for Python Excel kütüphanesini kullanarak ListObject verilerini liste olarak dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

Çıktı sonucu:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **Excel Satırını Listeye Nasıl Dönüştürülür**
Aspose.Cells for Python via .NET kullanarak Satır verilerini liste olarak dışa aktarmak için örnek kod parçası:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. Satır endeksine göre Satır nesnesini alın.
Aspose.Cells for Python Excel kütüphanesini kullanarak Satır verilerini liste olarak dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

Çıktı sonucu:
```
['Detroit', 'Central', 3074]
```

## **Excel Sütununu Listeye Nasıl Dönüştürülür**
Aspose.Cells for Python via .NET kullanarak Sütun verilerini liste olarak dışa aktarmak için örnek kod parçası:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. Sütun dizinine göre Sütun nesnesini alın.
1. Aspose.Cells for Python Excel kütüphanesini kullanarak Sütun verisini listeye dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

Çıktı sonucu:
```
['Store', 3055, 3036, 3074]
```

## **Excel'den Listeye Nasıl Dönüştürülür**
Aspose.Cells for Python via .NET kullanarak aralık verisini listeye nasıl aktaracağınızı gösteren örnek kod parçası:
1. [Örnek dosyayı](sample_data.xlsx) yükleyin.
1. İlk elektronik tabloyu alın.
1. Aralık oluşturun.
1. Aspose.Cells for Python Excel kütüphanesini kullanarak Aralık verisini listeye dönüştürün.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

Çıktı sonucu:
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
