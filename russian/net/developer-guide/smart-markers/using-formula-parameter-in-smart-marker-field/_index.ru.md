---
title: Использование параметра Formula в умном маркере
type: docs
weight: 40
url: /ru/net/using-formula-parameter-in-smart-marker-field/
---


## **Возможные сценарии использования**
Иногда вы хотите вставить формулу в умный маркер. В этой статье описано, как использовать параметр *Formula* для вставки формулы в умный маркер.
## **Использование параметра Formula в умном маркере**
В следующем образце кода встраивается формула в умный маркер с именем TestFormula, и его исходные данные называются MyDataSource, поэтому поле с параметром формулы выглядит как &=MyDataSource.TestFormula(formula), и после выполнения кода [конечный файл Excel](46465047.xlsx) будет содержать формулы в ячейках с A1 по A5.
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
{{< app/cells/assistant language="csharp" >}}
