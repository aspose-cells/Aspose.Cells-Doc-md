---
title: Çalışma Kitabının Formül Hesaplama Modunu Ayarlama
type: docs
weight: 110
url: /tr/net/setting-formula-calculation-mode-of-workbook/
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

 Aspose.Cells ayrıca**Formül Hesaplama Modu** kullanarak[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) mod özelliği. atayabilirsiniz[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)Aşağıdaki değerlerden birine sahip numaralandırma:

- CalcModeType.Otomatik
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
