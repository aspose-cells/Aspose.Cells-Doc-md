---
title: Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal ı Uygula
type: docs
weight: 20
url: /tr/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel Formülleri farklı yerel ayarlar, bölgeler veya dillerde farklı adlara sahip olabilir. Örneğin, *SUM* işlevi *Almanca* dilinde *SUMME* olarak adlandırılır. Aspose.Cells, diğer dillerdeki işlev adlarıyla çalışamaz. *Microsoft Excel VBA* içinde* *Range.FormulaLocal* özelliği, işlevin dil veya bölgeye göre adını döndürür. Aspose.Cells ayrıca bu amaçla [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) özelliğini sağlar. Ancak bu özellik, [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) yöntemini uyguladığınızda çalışacaktır. 
## **Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal'ı uygulamanın nasıl olduğunu aşağıdaki örnek kod açıklar. Metod, standart fonksiyonun yerel adını döndürür. Standart fonksiyon adı **SUM** ise **UserFormulaLocal_SUM** döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını döndürebilirsiniz, örneğin **SUM** Almanca'da **SUMME** ve Rusça'da **TEXT** için **ТЕКСТ** olur. Lütfen aşağıdaki örnek kodun konsol çıktısını inceleyin.**
Aşağıdaki örnek kod, [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) yöntemini nasıl uygulayacağınızı açıklamaktadır. Bu yöntem, standart işlevin yerel adını döndürür. Eğer standart işlev adı *SUM* ise, *UserFormulaLocal_SUM* olarak döner. Kodu ihtiyacınıza göre değiştirebilir ve doğru yerel işlev adlarını döndürebilirsiniz, örneğin *SUM*, *Almanca* dilinde *SUMME* ve *TEXT*, *Rusça* dilinde *ТЕКСТ* olarak adlandırılır. Lütfen referans için aşağıdaki örnek kodun konsol çıktısına da bakınız.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsol Çıktısı**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
