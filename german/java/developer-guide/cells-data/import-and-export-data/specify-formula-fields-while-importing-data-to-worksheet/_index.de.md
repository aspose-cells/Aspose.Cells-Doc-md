---
title: Formelfelder beim Importieren von Daten in das Arbeitsblatt angeben
type: docs
weight: 220
url: /de/java/specify-formula-fields-while-importing-data-to-worksheet/
---

## **Mögliche Verwendungsszenarien**

Sie können Formelfelder angeben, wenn Sie Daten in Ihr Arbeitsblatt importieren, indem Sie die [**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas)-Methode verwenden. Diese Methode nimmt das Boolesche Array entgegen, in dem der Wert **true** bedeutet, dass das Feld ein Formelfeld ist. Wenn beispielsweise das dritte Feld ein Formelfeld ist, ist der dritte Wert im Array **true**.

## **Formelfelder beim Import von Daten in ein Arbeitsblatt angeben**

Bitte beachten Sie den folgenden Beispielcode, der erklärt, wie das Formelfeld beim Importieren von Daten in ein Arbeitsblatt angegeben wird. Bitte sehen Sie sich die [Ausgabedatei Excel](61767850.xlsx) an, die durch den Code generiert wurde, sowie den Screenshot, der die Auswirkung des Codes auf die Ausgabedatei Excel zeigt.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
