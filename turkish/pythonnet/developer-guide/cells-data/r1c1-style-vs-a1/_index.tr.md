---
title: Excel – R1C1 Referans Stili vs. A1
type: docs
weight: 30
url: /tr/python-net/r1c1-reference-style-vs-a1/
description: Aspose.Cells for Python via .NET API sını kullanarak R1C1 Referans Stili VS. A1 stili.
keywords: Python Excel Kütüphanesi, Python R1C1 Referans Stili VS. A1 stili, Python R1C1 Referans Stili, Python R1C1 Referans Stili ve A1 Referans Stili Arasında Nasıl Geçiş Yapılır?, Python A1 Referans stili.
---

{{% alert color="primary" %}}

Excel'de, R1C1 ve A1, bir çalışma sayfasındaki hücreleri tanımlamak için kullanılan iki farklı referans stili. A1 ve R1C1 arasındaki seçim büyük ölçüde kişisel tercih meselesidir. Çoğu kullanıcı A1 stiliyle daha fazla aşina olsa da, R1C1 özellikle formüller ve hesaplamalarla çalışırken belirli durumlarda kullanışlı olabilir.

{{% /alert %}}

## **A1 Referans Stili**

Excel'de varsayılan referans stili budur. A1 stili, sütunları harflerle (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...) ve satırları sayılarla (1, 2, 3, ...) tanımlar.
Örneğin, ilk sütunun ve ikinci satırın hücresi A2 olarak anılır.

## **R1C1 Referans Stili**

R1C1 stili ile hem satırlar hem de sütunlar sayılarla tanımlanır. Harf "R" satır numarasını temsil eder ve harf "C" sütun numarasını temsil eder. Örneğin, R2C1 ikinci satırın ve ilk sütunun hücresine atıfta bulunur.

Köşeli parantez içindeki herhangi bir sayı, mevcut hücreden göreli uzaklığı ifade eder. A1'in sütunlarından sonra satır numarasına atıfta bulunurken, R1C1 tam tersini yapar: sütunlarından sonra satırları (bu alışkanlık edinmek için biraz zaman alabilir). Pozitif sayılar aşağıdaki hücrelere ve/veya sağa doğru olanlara atıfta bulunur. Negatif sayılar yukarıdaki hücrelere ve/veya sola doğru olanlara atıfta bulunur.

Örneğin, R[2]C[3] 2 satır aşağıdaki ve 3 sağdaki hücredir. R[-1]C[-4] 1 satır yukarıdaki ve 4 sola doğru olan hücredir. Eğer köşeli parantez içinde herhangi bir sayı gösterilmiyorsa, o zaman aynı satır veya sütuna atıfta bulunuyorsunuz demektir, yani R[3]C, aynı sütundaki mevcut hücreden 3 satır aşağıdaki hücredir.
<br>
<image src="2.png" width="70%" />

## **R1C1 Referans Stili ve A1 Referans Stili Karşılaştırması**
İşte hızlı bir karşılaştırma:
|**A1 Stili**|**R1C1 Stili**|
| :- | :- |	
|A1|R1C1
|B3|R3C2
|G10|R10C7
|AA25|R25C27

## **R1C1 Referans Stili ve A1 Referans Stili Arasında Nasıl Geçiş Yapılır**
Bu referans stilleri arasında Excel ayarlarında geçiş yapabilirsiniz. Referans stili değiştirmek için:

1. "Dosya" sekmesine gidin.
1. Alt kısımda "Seçenekler" seçeneğini seçin.
1. Excel Seçenekleri iletişim kutusunda, "Formüller" kategorisine gidin.
1. "Formüllerle çalışma" bölümünde, "R1C1 referans stili" seçeneğini işaretleyin ya da kaldırın.
1. Değişiklikleri uygulamak için "Tamam"a tıklayın.
<br>
<image src="1.png" width="70%" />

## **Excel'de R1C1 ve A1 Referans Stilleri Nasıl Kullanılır**
Aşağıdaki örnek, iki hücre değerinin toplamını iki stilde nasıl hesaplayacağınızı gösterir.
<br>
A1 Referans Stili:
<br>
<image src="4.png" width="70%" />

R1C1 Referans Stili:
<br>
<image src="3.png" width="70%" />
