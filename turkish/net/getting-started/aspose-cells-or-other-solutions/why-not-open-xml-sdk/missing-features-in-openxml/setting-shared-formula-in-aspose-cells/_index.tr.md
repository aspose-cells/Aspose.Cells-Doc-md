---
title: Aspose.Cells'de Paylaşılan Formülü Ayarlama
type: docs
weight: 110
url: /tr/net/setting-shared-formula-in-aspose-cells/
---
{{% alert color="primary" %}} 

Verilerle dolu bir çalışma sayfanız olduğunu varsayalım.

 B2'de ilk veri satırı için satış vergisini hesaplayacak bir işlev eklemek istiyorsunuz. vergi**9%** . Satış vergisini hesaplayan formül şu şekildedir:**"=A2*0,09"**. Bu makalede, bu formülün Aspose.Cells ile nasıl uygulanacağı açıklanmaktadır.

{{% /alert %}} 

Aspose.Cells, Cell.Formula özelliğini kullanarak bir formül belirlemenizi sağlar.

Sütundaki diğer hücrelere (B3, B4, B5 vb.) formül eklemek için iki seçenek vardır.

Ya ilk hücre için yaptığınızı yapın, her hücre için formülü etkili bir şekilde ayarlayın, hücre referansını buna göre güncelleyin (A3*0,09, A4*0,09, A5*0,09 vb.). Bu, her satır için hücre başvurularının güncellenmesini gerektirir. Ayrıca, Aspose.Cells'in her bir formülü ayrı ayrı ayrıştırmasını gerektirir; bu, büyük elektronik tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca fazladan kod satırları ekler, ancak döngüler bunları bir şekilde azaltabilir.

 Başka bir yaklaşım, bir**paylaşılan formül**. Paylaşılan bir formül ile, verginin doğru bir şekilde hesaplanması için formüller her satırdaki hücre referansları için otomatik olarak güncellenir. Cell.SetSharedFormula yöntemi, ilk yöntemden daha etkilidir.

Aşağıdaki örnek nasıl kullanılacağını göstermektedir.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Çalışan Örneği İndirin**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
