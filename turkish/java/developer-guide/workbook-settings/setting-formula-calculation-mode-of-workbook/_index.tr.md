---
title: Çalışma Kitabının Formül Hesaplama Modunu Ayarlama
type: docs
weight: 130
url: /tr/java/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel, formül hesaplama modunu, yani formüllerin hesaplanma şeklini ayarlamanıza olanak tanır. Üç olası değer vardır:

- Otomatik - bir şey değiştiğinde ve bir çalışma kitabı her açıldığında yeniden hesaplayın.
- Veri tabloları dışında otomatik - bir şey değiştiğinde yeniden hesaplayın, ancak veri tablolarını dışarıda bırakın.
- El ile - yalnızca kullanıcı F9 veya CTRL+ALT+F9 tuşlarına basarak açıkça istediğinde veya çalışma kitabı kaydedildiğinde yeniden hesaplayın.

{{% /alert %}}

Microsoft Excel'de formül hesaplama modunu ayarlamak için:

1.  Seçme**formüller** ve sonra**Hesaplama Seçenekleri**.
1. Seçeneklerden birini seçin.

 Aspose.Cells ayrıca**Formül Hesaplama Modu** kullanmak[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) Emlak. atayabilirsiniz[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)Aşağıdaki değerlerden birine sahip numaralandırma:

- [**CalcModeType.OTOMATİK**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

Aşağıdaki örnek kod önce bir çalışma kitabı oluşturur, ardından formül hesaplama modunu şu şekilde ayarlar:**Manuel** ve çalışma kitabını çıktı Excel dosyası olarak diske kaydeder.

**Çıkış dosyası. Formül hesaplama modunu not edin.**

![yapılacaklar:resim_alternatif_metin](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
