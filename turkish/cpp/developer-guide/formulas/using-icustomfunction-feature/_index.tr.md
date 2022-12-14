---
title: ICustomFunction Özelliğini Kullanma
type: docs
weight: 20
url: /tr/cpp/using-icustomfunction-feature/
---
## **giriiş**
Bu makale, Aspose.Cells API'leri ile özel işlevleri uygulamak için ICustomFunction özelliğinin nasıl kullanılacağına ilişkin bir anlayış sağlar.

ICustomFunction arabirimi, belirli gereksinimleri karşılamak üzere Aspose.Cells temel hesaplama motorunu genişletmek için özel formül hesaplama işlevleri eklemenize olanak tanır. Bu özellik, bir şablon dosyasında veya bir kodda özel (kullanıcı tanımlı) işlevleri tanımlamak için kullanışlıdır; burada özel işlev, diğer herhangi bir varsayılan Microsoft Excel işlevi gibi Aspose.Cells API'leri kullanılarak uygulanıp değerlendirilebilir.
## **ICustomFunction Özelliğini Kullanma**
Aşağıdaki örnek kod, MySampleFunc() ve YourSampleFunc() gibi iki özel işlevin değerlerini değerlendiren ve döndüren ICustomFunction arabirimini uygular. Bu özel işlevler, sırasıyla A1 ve A2 hücrelerinin içindedir. Ardından, ICustomFunction.CalculateCustomFunction() yönteminin uygulanmasını çağırmak için IWorkbook.CalculateFormula(false, ICustomFunction) yöntemini çağırır. Ardından, aslında ICustomFunction.CalculateCustomFunction() tarafından döndürülen değerler olan A1 ve A2 değerlerini konsola yazdırır. Daha fazla yardım için lütfen aşağıdaki örnek kodun Konsol Çıktısına bakın.
## **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **Konsol Çıkışı**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
