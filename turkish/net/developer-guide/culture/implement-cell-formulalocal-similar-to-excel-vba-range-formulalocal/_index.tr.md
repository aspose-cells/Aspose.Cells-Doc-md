---
title: Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal ı Uygula
type: docs
weight: 30
url: /tr/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel Formülleri farklı yerel ayarlar, bölgeler veya dillerde farklı adlara sahip olabilir. Örneğin, **SUM** fonksiyonu Almanca'da **SUMME** olarak adlandırılır. Aspose.Cells, diğer dillerdeki fonksiyon adlarıyla çalışamaz. Microsoft Excel VBA'da, dil veya bölgeye göre işlevin adını döndüren **Range.FormulaLocal** özelliği bulunmaktadır. Aspose.Cells aynı amaç için [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) özelliğini sağlar. Ancak bu özellik, sadece [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) metodunu uyguladığınızda çalışacaktır.

## **Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal'ı uygulamanın nasıl olduğunu aşağıdaki örnek kod açıklar. Metod, standart fonksiyonun yerel adını döndürür. Standart fonksiyon adı **SUM** ise **UserFormulaLocal_SUM** döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını döndürebilirsiniz, örneğin **SUM** Almanca'da **SUMME** ve Rusça'da **TEXT** için **ТЕКСТ** olur. Lütfen aşağıdaki örnek kodun konsol çıktısını inceleyin.**

Aşağıdaki örnek kod, [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) yöntemini uygulamanın nasıl yapıldığını açıklar. Bu yöntem, standart işlevin yerel adını döndürür. Standart işlev adı **SUM** ise **UserFormulaLocal_SUM**'ı döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel işlev adlarını döndürebilirsiniz. Örneğin; **SUM** Almanca'da **SUMME** ve **TEXT** Rusça'da **ТЕКСТ** tarafından değiştirilir. Ayrıca aşağıdaki örneğin konsol çıktısını referans için aşağıdaki örnek kodu görün.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
