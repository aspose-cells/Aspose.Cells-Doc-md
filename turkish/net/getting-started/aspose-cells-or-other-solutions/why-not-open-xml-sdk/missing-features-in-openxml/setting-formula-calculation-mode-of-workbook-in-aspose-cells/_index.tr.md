---
title: Aspose.Cells te Çalışma Kitabının Formül Hesaplama Modunu Ayarlamak
type: docs
weight: 100
url: /tr/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
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

Aspose.Cells ayrıca FormulaSettings.CalculationMode özelliği kullanarak **Formül Hesaplama Modunu** ayarlamanıza izin verir. Ona CalcModeType numaralandırmasını atayabilirsiniz ki bu şu değerlerden birine sahiptir:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

Aşağıdaki örnek kod önce bir çalışma kitabı oluşturur, sonra formül hesaplama modunu **Manuel** olarak ayarlar ve çalışma kitabını diskte çıktı Excel dosyası olarak kaydeder.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Örnek Çalışmayı İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
