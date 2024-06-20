---
title: Akıllı İmleç alanında Formül parametresini kullanma
type: docs
weight: 40
url: /tr/net/using-formula-parameter-in-smart-marker-field/
---


## **Olası Kullanım Senaryoları**
Bazen akıllı işaretçi alanına formül gömebilmek istersiniz. Bu makale, formülü akıllı işaretçi alanına gömmek için *Formula* parametresini nasıl kullanacağınızı açıklar.
## **Akıllı İşaretçi Alanında Formula Parametresi Kullanımı**
Aşağıdaki örnek kod, TestFormula adlı akıllı işaretçi alanına formül gömülü veri kaynağı adının MyDataSource olduğunu gösterir, bu nedenle formül parametreli tam alan şu şekilde görünür: &=MyDataSource.TestFormula(formula) ve kodun çalıştırılmasından sonra [son çıktı Excel dosyası](46465047.xlsx) A1'den A5'e kadar olan hücrelerde formülleri içerecektir.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
