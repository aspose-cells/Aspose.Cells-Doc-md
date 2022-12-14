---
title: Aspose.Cells'de Çalışma Kitabının Formül Hesaplama Modunu Ayarlama
type: docs
weight: 100
url: /tr/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel, formül hesaplama modunu, yani formüllerin hesaplanma şeklini ayarlamanıza olanak tanır. Üç olası değer vardır:

- Otomatik - bir şey değiştiğinde ve bir çalışma kitabı her açıldığında yeniden hesaplayın.
- Veri tabloları dışında otomatik - bir şey değiştiğinde yeniden hesaplayın, ancak veri tablolarını dışarıda bırakın.
- El ile - yalnızca kullanıcı F9 veya CTRL+ALT+F9 tuşlarına basarak açıkça istediğinde veya çalışma kitabı kaydedildiğinde yeniden hesaplayın.

{{% /alert %}} 

Microsoft Excel'de formül hesaplama modunu ayarlamak için:

1.  Seçme**formüller** ve daha sonra**Hesaplama Seçenekleri**.
1. Seçeneklerden birini seçin.

 Aspose.Cells ayrıca**Formül Hesaplama Modu** FormulaSettings.CalculationMode modu özelliğini kullanarak. Ona, aşağıdaki değerlerden birine sahip olan CalcModeType numaralandırmasını atayabilirsiniz:

- CalcModeType.Otomatik
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

 Aşağıdaki örnek kod önce bir çalışma kitabı oluşturur, ardından formül hesaplama modunu şu şekilde ayarlar:**Manuel** ve çalışma kitabını çıktı Excel dosyası olarak diske kaydeder.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Çalışan Örneği İndirin**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
