---
title: Golang aracılığıyla C++ ile Excel VBA Range.FormulaLocal a benzer Cell.FormulaLocal uygulayın
linktitle: Cell.FormulaLocal ı uygula
type: docs
weight: 30
url: /tr/go-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aspose.Cells kullanarak Golang ile C++ aracılığıyla Excel VBA Range.FormulaLocal e benzer Cell.FormulaLocal uygulamasını öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel Formülleri farklı yerel ayarlar, bölgeler veya dillerde farklı adlara sahip olabilir. Örneğin, **SUM** fonksiyonu Almanca'da **SUMME** olarak adlandırılır. Aspose.Cells, diğer dillerdeki fonksiyon adlarıyla çalışamaz. Microsoft Excel VBA'da, dil veya bölgeye göre işlevin adını döndüren **Range.FormulaLocal** özelliği bulunmaktadır. Aspose.Cells aynı amaç için [**Cell.FormulaLocal**](https://reference.aspose.com/cells/go-cpp/cell/getformulalocal/) özelliğini sağlar. Ancak bu özellik, sadece [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) metodunu uyguladığınızda çalışacaktır.

## **Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal'ı uygulamanın nasıl olduğunu aşağıdaki örnek kod açıklar. Metod, standart fonksiyonun yerel adını döndürür. Standart fonksiyon adı **SUM** ise **UserFormulaLocal_SUM** döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını döndürebilirsiniz, örneğin **SUM** Almanca'da **SUMME** ve Rusça'da **TEXT** için **ТЕКСТ** olur. Lütfen aşağıdaki örnek kodun konsol çıktısını inceleyin.**

Aşağıdaki örnek kod, [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getlocalfunctionname/) yöntemini uygulamanın nasıl yapıldığını açıklar. Bu yöntem, standart işlevin yerel adını döndürür. Standart işlev adı **SUM** ise **UserFormulaLocal_SUM**'ı döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel işlev adlarını döndürebilirsiniz. Örneğin; **SUM** Almanca'da **SUMME** ve **TEXT** Rusça'da **ТЕКСТ** tarafından değiştirilir. Ayrıca aşağıdaki örneğin konsol çıktısını referans için aşağıdaki örnek kodu görün.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCellFormulalocalSimilarToExcelVbaRangeFormulalocal.go" >}}
## **Konsol Çıktısı**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
