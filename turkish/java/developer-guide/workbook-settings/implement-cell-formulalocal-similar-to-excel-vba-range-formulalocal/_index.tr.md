---
title: Cell.FormulaLocal'ı Excel VBA Range.FormulaLocal'a benzer şekilde uygulayın
type: docs
weight: 20
url: /tr/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Olası Kullanım Senaryoları**
Microsoft Excel Formülleri, farklı yerel ayarlarda veya bölgelerde veya dillerde farklı adlara sahip olabilir. Örneğin,*TOPLAM*işlev denir*SÜME*içinde*Almanca*. Aspose.Cells, İngilizce olmayan işlev adlarıyla çalışamaz. İçinde*Microsoft Excel VBA'sı*, var* *a*Range.FormulaLocal*işlevin adını diline veya bölgesine göre döndüren özellik. Aspose.Cells ayrıca sağlar[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)Bu amaçla mülk. Ancak, bu özellik yalnızca uygulayacağınız zaman çalışacaktır.[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) yöntem.
## **Cell.FormulaLocal'ı Excel VBA Range.FormulaLocal'a benzer şekilde uygulayın**
Aşağıdaki örnek kod, nasıl uygulanacağını açıklar[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) yöntem. Yöntem, standart işlevin yerel adını döndürür. Standart işlev adı ise*TOPLAM*, geri döner*UserFormulaLocal_SUM*. Kodu ihtiyaçlarınıza göre değiştirebilir ve örneğin doğru yerel işlev adlarını döndürebilirsiniz.*TOPLAM*dır-dir*SÜME*içinde*Almanca*ve*METİN*dır-dir*ТЕКСТ*içinde*Rusça*. Lütfen referans için aşağıda verilen örnek kodun konsol çıktısına da bakın.
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsol Çıkışı**
{{< highlight "java" >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
