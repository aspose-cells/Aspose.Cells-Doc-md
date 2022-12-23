---
title: Sayısal tuş takımından ondalık ayırıcıyı değiştirme
type: docs
weight: 150
url: /tr/net/change-the-decimal-separator-from-numeric-keypad/
---
## **Olası Kullanım Senaryoları**
Varsayılan olarak Aspose.Cells.GridWeb, makinedeki yerel/bölgesel ayarlara göre sayısal verileri görüntüler. Aspose.Cells.GridWeb API'i kullanarak Sayısal tuş takımından ondalık ayırıcıyı programlı olarak değiştirebilirsiniz. Bu nedenle, bir dosya GridWeb matrisine içe aktarıldığında veya yeni bir çalışma sayfası hücresine bazı sayısal veriler (sayısal tuş takımından) girdiğinizde, istediğiniz ondalık sayıya sahip olmalıdır. ayırıcı görsel olarak ayarlanır.
## **Sayısal tuş takımından ondalık ayırıcıyı değiştirme**
Kullanmak**GridWorksheetCollection.NumberDecimalSeparator**özelliğini kullanarak, ondalık ayırıcıyı Sayısal tuş takımından programlı olarak değiştirebilirsiniz. Lütfen nasıl çalıştığını gösteren ekran görüntülerine bakın

![yapılacaklar:resim_alternatif_metin](change-the-decimal-separator-from-numeric-keypad_1.png)

![yapılacaklar:resim_alternatif_metin](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Lütfen ondalık ayırıcı değişikliğinin yalnızca kullanıcıların GridWeb'deki görsel deneyimi için olduğunu unutmayın. Çalışma kitabınızı düzenlediğinizde ve kaydettiğinizde, yerel/bölgesel ondalık ayırıcınıza göre sayısal değerleri (e-tabloda) depolamaya devam edecektir.

{{% /alert %}}
