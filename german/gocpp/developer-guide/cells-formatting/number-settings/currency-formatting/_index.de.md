---
title: Zahl als Währung formatieren mit Golang über C++
linktitle: So formatiert man Zahlen als Währung
type: docs
weight: 10
url: /de/go-cpp/format-number-to-currency/
description: Dieser Artikel führt in die Formatierung von Zahlen als Währung mit der API Aspose.Cells for C++ ein.
keywords: Zahl als Währung formatieren, Zelleinstellungen, Zahl in Währung formatieren, Währungseinstellungen, Währungsformat.
---

## **Mögliche Verwendungsszenarien**
Das Formatieren von Zahlen in Währung in Excel ist aus mehreren Gründen wichtig, insbesondere bei der Arbeit mit Finanzdaten. Hier ist, warum das Währungsformat vorteilhaft ist:

1. **Klarheit bei Finanzwerten**: Das Formatieren einer Zahl als Währung macht deutlich, dass der Wert Geld darstellt. Zum Beispiel zeigt $1.000,00 klar an, dass es sich um einen Geldbetrag handelt, im Gegensatz zu 1000, was alles bedeuten könnte.
1. **Enthält Währungssymbole**: Bei internationalen oder mehreren Währungen macht das Formatieren mit dem entsprechenden Währungssymbol (z.B. $, €, £) die verwendete Währung deutlich und reduziert Verwirrung in multinationale Finanzberichte oder Transaktionen.
1. **Verbessert Professionelles Erscheinungsbild**: Gut formatierte Währungswerte wirken gepflegt und professionell, was besonders bei Berichten, Präsentationen und Geschäftsdokumenten wichtig ist. $10.000,00 wirkt glaubwürdiger und organisierter als eine einfache Zahl 10000.
1. **Verbessert Lesbarkeit**: Das Währungsformat fügt Tausendertrennzeichen und Dezimalstellen hinzu, was große Zahlen leichter lesbar macht. Zum Beispiel wird 1000000 zu $1.000.000,00, was auf einen Blick besser verständlich ist.
1. **Sichert Konsistenz**: Durch die Anwendung eines einheitlichen Währungsformats stellen Sie sicher, dass alle Geldwerte in einem Datensatz im selben Format angezeigt werden. Diese Konsistenz ist wichtig für finanzielle Genauigkeit und professionelle Kommunikation, insbesondere in großen Tabellen mit vielen Zahlen.
1. **Zeigt Präzision**: Das Währungsformat umfasst typischerweise zwei Dezimalstellen, um genaue Geldbeträge anzuzeigen. Zum Beispiel ist $100.50 deutlich verschieden von $100.00, was in Finanzberichten, in denen Genauigkeit wichtig ist, relevant ist.
1. **Vereinfachte Finanzberechnungen**: Beim Durchführen von Finanzberechnungen (wie Summe bilden oder Kosten mitteln) hilft das Währungsformat Excel und den Nutzern zu verstehen, dass die Daten in Geldangaben bestehen. Es hilft Excel, das geeignete Format in Formeln und Funktionen anzuwenden, und sorgt für konsistente Ergebnisse.
1. **Reduziert Fehlinterpretationen**: Ohne Währungsformat könnten Zahlen als allgemeine numerische Werte missverstanden werden, nicht als Geldbeträge. Zum Beispiel könnte 500 fälschlicherweise als Stückzahl interpretiert werden, während $500.00 eindeutig einen Finanzbetrag darstellt.
1. **Funktioniert mit Buchhaltungsfunktionen**: Das Währungsformat passt gut zu Buchhaltungsfunktionen in Excel, wie Bilanz- oder Cashflow-Berichten. Es macht die Werte leichter nutzbar in Finanzberichten, in denen Geld im Mittelpunkt steht.
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

Um Zahlen in der Bibliothek Aspose.Cells for C++ für die Arbeit mit Excel-Dateien als Währung zu formatieren, können Sie die Währungsformatierung programmatisch auf Zellen anwenden. Hier erfahren Sie, wie Sie es mit C++ und Aspose.Cells machen:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CurrencyFormatting.go" >}}
