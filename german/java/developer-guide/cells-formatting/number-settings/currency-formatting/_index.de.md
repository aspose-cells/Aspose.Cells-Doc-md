---
title: So formatiert man Zahlen als Währung
type: docs
weight: 10
url: /de/java/format-number-to-currency/
description: Dieser Artikel führt die Formatierung von Zahlen als Währung mit der API Aspose.Cells for Java ein.
keywords: Zahl als Währung formatieren, Zelleinstellungen, Zahl in Währung formatieren, Währungseinstellungen, Währungsformat.
---

## **Mögliche Verwendungsszenarien**
Das Formatieren von Zahlen in Währung in Excel ist aus mehreren Gründen wichtig, insbesondere bei der Arbeit mit Finanzdaten. Hier ist, warum das Währungsformat vorteilhaft ist:

1. Klare Finanzwerte: Das Formatieren einer Zahl als Währung macht deutlich, dass der Wert Geld darstellt. Zum Beispiel zeigt 1000, was auch immer es bedeuten mag, mit $, € oder £, dass es sich um einen Geldbetrag handelt.
1. Einschluss von Währungssymbolen: Bei internationalen oder mehreren Währungen macht die Formatierung der Zahlen mit dem entsprechenden Währungssymbol (z.B. $, €, £) klar, um welche Währung es sich handelt, und verringert Verwirrung in multinationalen Finanzberichten oder Transaktionen.
1. Professionelle Präsentation: Gut formatierte Währungswerte wirken gepflegt und professionell, was insbesondere bei Berichten, Präsentationen und Geschäftsdokumenten wichtig ist. $10.000,00 wirkt glaubwürdiger und organisierter als eine einfache 10000.
1. Verbesserte Lesbarkeit: Die Währungsformatierung fügt Kommas als Tausendertrennzeichen und Dezimalstellen hinzu, was große Zahlen leichter lesbar macht. Zum Beispiel wird aus 1000000, $1.000.000,00, was auf einen Blick verständlicher ist.
1. Konsistenzsicherung: Durch das Anwenden eines einheitlichen Währungsformats gewährleisten Sie, dass alle Geldwerte in einem Datensatz im gleichen Format angezeigt werden. Diese Konsistenz ist wichtig für finanzielle Genauigkeit und professionelle Kommunikation, vor allem in großen Tabellen mit vielen Zahlen.
1. Zeigt Präzision: Das Währungsformat umfasst typischerweise zwei Dezimalstellen und ermöglicht es, exakte Geldbeträge zu sehen. Zum Beispiel ist $100,50 deutlich anders als $100,00, was in Finanzberichten mit genauerer Angabe wichtig ist.
1. Vereinfachte Finanzberechnungen: Bei der Durchführung finanzieller Berechnungen (wie Summen oder Durchschnittskosten) hilft die Währungsformatierung Excel und Benutzern, zu verstehen, dass die Daten in monetären Beträgen vorliegen. Es hilft Excel, die passende Formatierung in Formeln und Funktionen anzuwenden, um eine Konsistenz zu gewährleisten.
1. Missverständnisse reduzieren: Ohne Währungsformatierung könnten Zahlen als allgemeine numerische Werte interpretiert werden, anstatt als Geldbeträge. Zum Beispiel kann 500 fälschlicherweise als Stückzahl oder Einheit interpretiert werden, während $500,00 eindeutig einen finanziellen Betrag darstellt.
1. Funktioniert mit Buchhaltungsfunktionalitäten: Die Währungsformatierung passt gut zu Buchhaltungsfunktionen in Excel, z. B. Bilanzen oder Cashflow-Berichte. Sie macht die Werte einfacher in Finanzberichten nutzbar, in denen Geld im Mittelpunkt steht.
<br>
Zusammenfassend hilft das Formatieren von Zahlen als Währung, Geldwerte von anderen Zahlenarten zu unterscheiden, die Klarheit zu erhöhen und die Daten interpretierbarer zu machen, insbesondere im Finanzkontext.

## **So formatiert man Zahlen in Excel als Währung**
Um Zahlen in Excel als Währung zu formatieren, folgen Sie diesen Schritten:

### **Verwendung der Option für Währungsformat**
1. Wählen Sie die Zellen aus, die Sie als Währung formatieren möchten.
1. Gehen Sie auf die Registerkarte Start im Menüband.
1. Klicken Sie im Zahlenbereich auf den Dropdown-Pfeil neben dem Zahlenformatfeld (dies zeigt möglicherweise standardmäßig "Allgemein").
<br>
<img src="1.png" width=60% />
1. Wählen Sie Währung aus der Liste.

### **Verwenden des Dialogfelds Zellen formatieren**
1. Wählen Sie die Zellen aus, die Sie formatieren möchten.
1. Klicken Sie mit der rechten Maustaste auf die ausgewählten Zellen und wählen Sie "Zellen formatieren", um das Dialogfeld Zellen formatieren zu öffnen.
1. Im Register Zahl, wählen Sie Währung aus der Liste auf der linken Seite aus.
<br>
<img src="2.png" width=60% />
1. Sie können die folgenden Optionen anpassen: Dezimalstellen, Symbol, Negative Zahlen.
1. Klicken Sie auf OK, um die Formatierung anzuwenden.

## **So formatieren Sie Zahlen als Währung in Aspose.Cells**

Um Zahlen in der Aspose.Cells for Java-Bibliothek zum Arbeiten mit Excel-Dateien als Währung zu formatieren, können Sie die Währungsformatierung programmgesteuert auf Zellen anwenden. So funktioniert es mit Aspose.Cells for Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Cells-Formatting-FormatNumberToCurrency.java" >}}
{{< app/cells/assistant language="java" >}}
