---
title: Akıllı İşaretleyici alanında Formül parametresini kullanma
type: docs
weight: 40
url: /tr/net/using-formula-parameter-in-smart-marker-field/
---
## **Olası Kullanım Senaryoları**
Bazen formülü akıllı işaretçi alanına gömmek istersiniz. Bu makale, bu özelliğin nasıl kullanılacağını açıklamaktadır.*formül*formülü akıllı işaretleyici alanına gömmek için parametre.
## **Akıllı İşaretleyici alanında Formül parametresini kullanma**
 Aşağıdaki örnek kod, formülü TestFormula adlı akıllı işaretçi alanına katıştırır ve veri kaynağı adı MyDataSource'tur, bu nedenle formül parametresi içeren tam alan &=MyDataSource.TestFormula(formula) gibi görünür ve kodun yürütülmesinden sonra,[nihai çıktı Excel dosyası](46465047.xlsx) A1'den A5'e kadar olan hücrelerde formüller olacaktır.
## **Basit kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
