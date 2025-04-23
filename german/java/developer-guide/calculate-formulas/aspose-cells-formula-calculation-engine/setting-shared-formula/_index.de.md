---
title: Einstellung gemeinsamer Formel
type: docs
weight: 10
url: /de/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

Angenommen, Sie haben ein Arbeitsblatt mit Daten im Format, das wie das folgende Beispieldatenblatt aussieht.

**Eingabedatei mit einer Spalte oder Daten** 

![todo:image_alt_text](setting-shared-formula_1.png)

Sie möchten eine Funktion in B2 hinzufügen, die die Umsatzsteuer für die erste Datensatzreihe berechnet. Die Steuer beträgt **9%**. Die Formel zur Berechnung der Umsatzsteuer lautet: **"=A2*0,09"**. In diesem Artikel wird erläutert, wie diese Formel mit Aspose.Cells angewendet wird.

{{% /alert %}} 

Mit Aspose.Cells können Sie eine Formel mithilfe der Eigenschaft [Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula), speziell [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) und [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) angeben.

Es gibt zwei Möglichkeiten, Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte hinzuzufügen.

Entweder tun Sie das, was Sie für die erste Zelle getan haben, und setzen die Formel für jede Zelle, wobei der Zellbezug entsprechend aktualisiert wird (`A3*0,09`, `A4*0,09`, `A5*0,09` usw.). Dies erfordert, dass die Zellbezüge für jede Zeile aktualisiert werden. Es erfordert auch, dass Aspose.Cells jede Formel einzeln analysiert, was bei großen Tabellenkalkulationen und komplexen Formeln zeitaufwändig sein kann. Es fügt auch zusätzliche Codezeilen hinzu, obwohl Schleifen sie etwas reduzieren können.

Ein weiterer Ansatz ist die Verwendung einer **gemeinsamen Formel**. Mit einer gemeinsamen Formel werden die Formeln automatisch für die Zellreferenzen in jeder Zeile aktualisiert, sodass die Steuer korrekt berechnet wird. Die Methode [Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula-java.lang.String-int-int-) ist effizienter als die erste.

Das folgende Beispiel zeigt, wie sie verwendet wird. Der folgende Screenshot zeigt die Ausgabedatei.

**Ausgabedatei: gemeinsame Formel angewendet** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
