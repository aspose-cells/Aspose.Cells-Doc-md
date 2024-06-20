---
title: Çalışbook un Formül Hesaplama Modunu Ayarlama
type: docs
weight: 130
url: /tr/java/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel, formül hesaplama modunu, yani formüllerin nasıl hesaplandığını ayarlamanıza izin verir. Üç olası değer bulunmaktadır:

- Otomatik - bir şey değiştirildiğinde ve her bir çalışma kitabı açıldığında yeniden hesapla.
- Otomatik, veri tabloları hariç - bir şey değiştirildiğinde yeniden hesapla, ancak veri tablolarını dışarıda bırak.
- Manuel - kullanıcı açıkça istediğinde (F9 veya CTRL+ALT+F9'a basarak) veya çalışma kitabı kaydedildiğinde sadece yeniden hesapla.

{{% /alert %}}

Microsoft Excel'de formül hesaplama modunu ayarlamak için:

1. **Formüller**'i seçin, ardından **Hesaplama Seçenekleri**'ni seçin.
1. Seçeneklerden birini seçin.

Aspose.Cells ayrıca [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) özelliğini kullanarak **Formül Hesaplama Modunu** ayarlamanıza olanak tanır. Bu özelliğe [**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) numaralı sıralamayı atayabilirsiniz ki bu sıralama aşağıdaki değerlerden birine sahiptir:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

Aşağıdaki örnek kod önce bir çalışma kitabı oluşturur, sonra formül hesaplama modunu **Manuel** olarak ayarlar ve çalışma kitabını diskte çıktı Excel dosyası olarak kaydeder.

**Çıktı dosyası. Formül hesaplama moduna dikkat edin.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
