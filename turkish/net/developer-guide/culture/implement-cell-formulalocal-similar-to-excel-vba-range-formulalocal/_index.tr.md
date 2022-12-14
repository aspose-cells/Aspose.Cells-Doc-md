---
title: Cell.FormulaLocal'ı Excel VBA Range.FormulaLocal'a benzer şekilde uygulayın
type: docs
weight: 30
url: /tr/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Olası Kullanım Senaryoları**

 Microsoft Excel Formülleri, farklı yerel ayarlarda veya bölgelerde veya dillerde farklı adlara sahip olabilir. Örneğin,**TOPLAM**işlev denir**SÜME** Almanca'da. Aspose.Cells, İngilizce olmayan işlev adlarıyla çalışamaz. Microsoft Excel VBA'da var**Range.FormulaLocal**işlevin adını diline veya bölgesine göre döndüren özellik. Aspose.Cells ayrıca sağlar[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)Bu amaçla mülk. Ancak, bu özellik yalnızca uygulayacağınız zaman çalışacaktır.[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)yöntem.

## **Cell.FormulaLocal'ı Excel VBA Range.FormulaLocal'a benzer şekilde uygulayın**

 Aşağıdaki örnek kod, nasıl uygulanacağını açıklar[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) yöntem. Yöntem, standart işlevin yerel adını döndürür. Standart işlev adı ise**TOPLAM** , geri döner**UserFormulaLocal_SUM** Kodu ihtiyaçlarınıza göre değiştirebilir ve örneğin doğru yerel işlev adlarını döndürebilirsiniz.**TOPLAM** dır-dir**SÜME** Almanca ve**METİN** dır-dir**ТЕКСТ**Rusça. Lütfen referans için aşağıda verilen örnek kodun konsol çıktısına da bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
