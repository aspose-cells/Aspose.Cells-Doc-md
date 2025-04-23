---
title: Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal ı Uygula
type: docs
weight: 20
url: /tr/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel formüllerinin farklı bölgelerde veya dillerde farklı isimleri olabilir. Örneğin, *SUM* işlevi Almanca'da *SUMME*. Aspose.Cells, İngilizce olmayan fonksiyon adlarıyla çalışamaz. Microsoft Excel VBA'da, *Range.FormulaLocal* özelliği, fonksiyon adını dil veya bölgeye göre döndürür. Aspose.Cells, bunun amacıyla [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) özelliği sağlar. Ancak, bu özellik yalnızca [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) yöntemini uygularsanız çalışır. 
## **Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal'ı uygulamanın nasıl olduğunu aşağıdaki örnek kod açıklar. Metod, standart fonksiyonun yerel adını döndürür. Standart fonksiyon adı **SUM** ise **UserFormulaLocal_SUM** döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını döndürebilirsiniz, örneğin **SUM** Almanca'da **SUMME** ve Rusça'da **TEXT** için **ТЕКСТ** olur. Lütfen aşağıdaki örnek kodun konsol çıktısını inceleyin.**
Aşağıdaki örnek kod, [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) yönteminin nasıl uygulanacağını açıklar. Bu yöntem, standart fonksiyonun yerel adını döndürür. Örneğin, standart fonksiyon adı *SUM* ise, *UserFormulaLocal_SUM* döner. Kendi ihtiyaçlarınıza göre kodu değiştirebilir ve doğru yerel fonksiyon adlarını döndürebilirsiniz; örneğin, Almanca'da *SUM* *SUMME* ve Rusça'da *TEXT* *ТЕКСТ* olur. Ayrıca, örnek kodun konsol çıktılarını aşağıda görebilirsiniz.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsol Çıktısı**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
