---
title: Noktalama işaretinin değiştirilmesi
type: docs
weight: 150
url: /tr/net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb,ondalık,ondalık ayırıcı
description: Bu makale, GridWeb de ondalık ayırıcısını nasıl değiştireceğini tanıtır.
---

## **Olası Kullanım Senaryoları**
Varsayılan olarak, Aspose.Cells.GridWeb, makinedeki yerel/bölgesel ayarlara göre sayısallaştırılmış verileri uygun bir şekilde görüntüler. Aspose.Cells.GridWeb API'sını kullanarak programlı olarak Numeric keypad'den ondalık ayırıcıyı değiştirebilirsiniz. Bu nedenle, bir dosya GridWeb matrisine veya yeni bir çalışma sayfası hücresine (Numeric keypad'den) bazı sayısal verileri (giriş) içine alırken, istenen ondalık ayırıcıyı görsel olarak ayarlı olması gerekmektedir. 
## **Numeric keypad'den ondalık ayırıcıyı değiştirme**
**GridWorksheetCollection.NumberDecimalSeparator** özelliğini kullanarak, programlı olarak Numeric keypad'den ondalık ayırıcıyı değiştirebilirsiniz. Bu nasıl çalıştığını gösteren ekran görüntülerini görmek için lütfen bakınız

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Lütfen dikkat, ondalık ayırıcı değişikliği sadece GridWeb'de kullanıcıların görsel deneyimi içindir. Çalışma kitabınızı düzenlediğinizde ve kaydettiğinizde, hücrelere, yerel/bölgesel ondalık ayırıcıya göre sayısal değerlerin hala saklanacaktır.

{{% /alert %}}
