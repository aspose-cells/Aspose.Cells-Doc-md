---
title: Aspose.Cells te Paylaşılan Formül Ayarlama
type: docs
weight: 110
url: /tr/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

Varsayalım ki veriyle dolu bir çalışsayfanız var.

Bir fonksiyon eklemek istiyorsunuz ve bu fonksiyon, verinin ilk satırı için satış vergisini hesaplayacak. Vergi **%9**. Satış vergisini hesaplayan formül şudur: **"=A2*0.09"**. Bu makale, bu formülü Aspose.Cells ile nasıl uygulayacağınızı açıklar.

{{% /alert %}} 

Aspose.Cells, Cell.Formula özelliğini kullanarak bir formül belirtmenize izin verir.

Sütunun diğer hücrelerine formül eklemek için iki seçenek bulunmaktadır.

Her bir hücre için yaptığınızı yaparak her bir hücre için formülü ayarlamak, hücre başvurusunu güncellemek (A3*0.09, A4*0.09, A5*0.09 vb.) gerektirir. Bu, her satır için hücre başvurularının güncellenmesini gerektirir. Aynı zamanda Aspose.Cells'in her formülü ayrı ayrı ayrıştırmasını gerektirir, bu da büyük elektronik tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca, döngüler onları azaltabilse de ekstra kod satırları ekler.

Başka bir yaklaşım, bir **paylaşılan formül** kullanmaktır. Paylaşılan bir formülle, her satırdaki hücre başvuruları için formüller otomatik olarak güncellenir, böylece vergi uygun şekilde hesaplanır. Cell.SetSharedFormula yöntemi, ilk yönteme göre daha verimlidir.

Aşağıdaki örnek, bunu nasıl kullanacağınızı göstermektedir.

**C#**

{{< highlight csharp >}}

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
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Örnek Çalışmayı İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
