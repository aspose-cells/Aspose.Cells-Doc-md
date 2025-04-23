---
title: Aspose.Cells te FormulaText Fonksiyonu Kullanma
description: Bu makale, Aspose.Cells kitaplığını kullanarak Microsoft Excel deki formülleri işlemek için FormulaText fonksiyonunun nasıl kullanılacağını tanıtır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemi kullanarak hücrenin formül metnini alabilir ve ayarlayabilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, FormulaText fonksiyonları
type: docs
weight: 60
url: /tr/net/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText, Excel 2013 ve sonrası bir fonksiyondur. Önceki sürümler, Excel 2010 veya 2007 gibi, tarafından desteklenmez. Adından da anlaşılacağı gibi, belirli bir hücrede bulunan formülün metnini yazdırır. Bu makale, Aspose.Cells kullanarak bu fonksiyonun nasıl kullanılacağını gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, Aspose.Cells ile FormulaText kullanımını gösterir. Kod önce hücre A1'e bir formül yazar ve sonra A2 hücresinde FormulaText'i kullanarak formülün metnini yazdırır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
