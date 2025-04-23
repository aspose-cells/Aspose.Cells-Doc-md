---
title: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /de/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel-Formeln können in verschiedenen Regionen oder Sprachen unterschiedliche Namen haben. Zum Beispiel wird die **SUM**-Funktion auf Deutsch als **SUMME** bezeichnet. Aspose.Cells kann nicht mit Funktionen, die nicht in englischer Sprache angegeben sind, arbeiten. In Microsoft Excel VBA gibt es die **Range.FormulaLocal**-Eigenschaft, die den Namen der Funktion je nach Sprache oder Region zurückgibt. Aspose.Cells bietet auch die Eigenschaft [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) für diesen Zweck. Diese Eigenschaft funktioniert jedoch nur, wenn Sie die [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)-Methode implementiert haben.

## **Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal**

Der folgende Beispielcode erläutert die Implementierung der Methode [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname). Die Methode gibt den lokalen Namen der Standardfunktion zurück. Wenn der Standardfunktionsname **SUM** ist, wird **UserFormulaLocal_SUM** zurückgegeben. Sie können den Code entsprechend Ihren Bedürfnissen ändern und die korrekten lokalen Funktionsnamen zurückgeben, z.B. ist **SUM** auf Deutsch **SUMME** und **TEXT** im Russischen **ТЕКСТ**. Bitte beachten Sie auch die Konsolenausgabe des untenstehenden Beispielcodes zur Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
