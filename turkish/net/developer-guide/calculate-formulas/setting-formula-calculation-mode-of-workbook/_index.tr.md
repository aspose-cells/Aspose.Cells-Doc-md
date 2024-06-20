---
title: Çalışbook un Formül Hesaplama Modunu Ayarlama
description: Bu makale, Aspose.Cells kitaplığını kullanarak Microsoft Excel de bir çalışbook un formül hesaplama modunu ayarlamanın nasıl yapıldığını tanıtır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemi kullanarak formül hesaplama modunu ayarlayabilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, çalışbook, formül hesaplama modu, ayarlar
type: docs
weight: 110
url: /tr/net/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells ayrıca, [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) mod özelliğini kullanarak **Formül Hesaplama Modunu** ayarlamanıza izin verir. Bu özelliği, aşağıdaki değerlerden birine sahip olan [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype) numaralandırmasına atayabilirsiniz:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
