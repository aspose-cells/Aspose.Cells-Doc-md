---
title: Использование параметра Formula в умном маркере
type: docs
weight: 30
url: /ru/java/using-formula-parameter-in-smart-marker-field/
---

## **Возможные сценарии использования**
Иногда вы хотите вставить формулу в поле умного маркера. В этой статье описано, как использовать параметр Formula для вставки формулы в поле умного маркера.
## **Использование параметра Formula в умном маркере**
В следующем образце кода встраивается формула в переменную умного маркера с именем Test, а имя источника данных также Test, поэтому поле с параметром формулы выглядит как **&=$Test(formula)**, а после выполнения кода [финальный файл Excel](47153156.xlsx) будет содержать формулы в ячейках с A1 по A5.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
