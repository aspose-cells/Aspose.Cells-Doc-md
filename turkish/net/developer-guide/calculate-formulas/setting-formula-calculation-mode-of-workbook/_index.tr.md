---
title: Çalışma Kitabının Formül Hesaplama Modunu Ayarlama
description: Bu makalede, Microsoft Excel'de Aspose.Cells kitaplığıyla bir çalışma kitabının formül hesaplama modunun nasıl ayarlanacağı anlatılmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells'in sağladığı yöntemi kullanarak formül hesaplama modunu ayarlayabilir ve sonucu alabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /tr/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel, formül hesaplama modunu, yani formüllerin hesaplanma şeklini ayarlamanıza olanak tanır. Üç olası değer vardır:

- Otomatik - bir şey değiştiğinde ve çalışma kitabı her açıldığında yeniden hesaplayın.
- Veri tabloları hariç otomatik - bir şey değiştiğinde yeniden hesaplayın, ancak veri tablolarını dışarıda bırakın.
- El ile - yalnızca kullanıcı F9 veya CTRL+ALT+F9 tuşlarına basarak açıkça istediğinde veya çalışma kitabı kaydedildiğinde yeniden hesaplama yapın.

{{% /alert %}}

Microsoft Excel'de formül hesaplama modunu ayarlamak için:

1.  Seçme**Formüller** ve ardından *Hesaplama Seçenekleri**'ne tıklayın.
1. Seçeneklerden birini seçin.

 Aspose.Cells aynı zamanda**Formül Hesaplama Modu** kullanarak[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) mod özelliği. Bunu atayabilirsiniz[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)aşağıdaki değerlerden birine sahip numaralandırma:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
