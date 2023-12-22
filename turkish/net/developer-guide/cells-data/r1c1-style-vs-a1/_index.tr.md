---
title: Excel – R1C1 Referans Stili ve A1
type: docs
weight: 30
url: /tr/net/r1c1-reference-style-vs-a1/
description: R1C1 Referans Stili VS. Aspose.Cells for Python via .NET API'i kullanarak A1 stilini kullanın.
keywords: R1C1 Reference Style VS. A1 style, R1C1 Reference Style, How to switch between R1C1 Reference Style and A1 Reference Style, A1 Reference style.
---
{{% alert color="primary" %}}

Excel'de R1C1 ve A1, çalışma sayfasındaki hücreleri tanımlamak için kullanılan iki farklı referans stilidir. A1 ve R1C1 arasındaki seçimin büyük ölçüde kişisel tercih meselesi olduğunu unutmayın. Çoğu kullanıcı A1 stiline daha aşinadır ancak R1C1 belirli durumlarda, özellikle formüller ve hesaplamalarla çalışırken yararlı olabilir.

{{% /alert %}}

##  **A1 Referans Stili**

Bu, Excel'deki varsayılan referans stilidir. A1 stilinde sütunlar harflerle (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...), satırlar ise sayılarla (1, 2, 3, ...).
Örneğin birinci sütun ve ikinci satırdaki hücreye A2 adı verilir.

##  **R1C1 Referans Stili**

R1C1 stilinde hem satırlar hem de sütunlar sayılarla tanımlanır. "R" harfi satır numarasını, "C" harfi ise sütun numarasını temsil etmektedir. Örneğin R2C1, ikinci satır ve birinci sütundaki hücreyi ifade eder.

Köşeli parantez içindeki sayılar mevcut hücreye olan göreceli mesafeyi belirtir. Sıra numarasının takip ettiği sütunları ifade eden A1'den farklı olarak, R1C1 bunun tersini yapar: satırların ardından sütunlar gelir (buna alışmak biraz zaman alır). Pozitif sayılar aşağıdaki ve/veya sağ taraftaki hücreleri ifade eder. Negatif sayılar yukarıdaki ve/veya soldaki hücreleri ifade eder.

Örneğin R[2]C[3] 2 satır aşağı ve 3 sütun sağdaki bir hücredir. R[-1]C[-4] 1 satır yukarıda ve 4 sütun solda bir hücredir. Parantez içinde hiçbir sayı gösterilmiyorsa aynı satır veya sütuna atıfta bulunuyorsunuz demektir; yani R[3]C, aynı sütundaki mevcut hücrenin 3 satır altındaki bir hücre olacaktır.
<br>
<image src="2.png" width="70%" />

##  **R1C1 Referans Stili ve A1 Referans Stili Karşılaştırması**
İşte hızlı bir karşılaştırma:
|**A1 Stili**|**R1C1 Stili**|
| :- | :- |
|A1|
|B3|
|G10|
|AA25|

##  **R1C1 Referans Stili ile A1 Referans Stili arasında nasıl geçiş yapılır?**
Excel ayarlarında bu referans stilleri arasında geçiş yapabilirsiniz. Referans stilini değiştirmek için:

1. "Dosya" sekmesine gidin.
1. Alt kısımdaki "Seçenekler"i seçin.
1. Excel Seçenekleri iletişim kutusunda "Formüller" kategorisine gidin.
1. "Formüllerle çalışma" bölümünün altında "R1C1 referans stili" seçeneğini işaretleyin veya işaretini kaldırın.
1. Değişiklikleri uygulamak için "Tamam"ı tıklayın.
<br>
<image src="1.png" width="70%" />

##  **Excel'de R1C1 Referans Stili ve A1 Referans Stili nasıl kullanılır?**
Aşağıdaki örnek, iki hücre değerinin toplamının iki stilde nasıl hesaplanacağını gösterir.
<br>
A1 Referans Stili:
<br>
<image src="4.png" width="70%" />

R1C1 Referans Stili:
<br>
<image src="3.png" width="70%" />
