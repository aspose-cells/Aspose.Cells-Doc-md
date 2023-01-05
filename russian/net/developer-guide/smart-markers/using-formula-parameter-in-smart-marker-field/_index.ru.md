---
title: Использование параметра Formula в поле Smart Marker
type: docs
weight: 40
url: /ru/net/using-formula-parameter-in-smart-marker-field/
---
## **Возможные сценарии использования**
Иногда вы хотите встроить формулу в поле смарт-маркера. В этой статье описывается, как использовать*Формула*параметр для встраивания формулы в поле смарт-маркера.
## **Использование параметра Formula в поле Smart Marker**
 В следующем примере кода формула встраивается в поле интеллектуального маркера с именем TestFormula, а имя источника данных — MyDataSource, поэтому полное поле с параметром формулы выглядит как &=MyDataSource.TestFormula(formula) и после выполнения кода[окончательный выходной файл Excel](46465047.xlsx) будут иметь формулы в ячейках от A1 до A5.
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
