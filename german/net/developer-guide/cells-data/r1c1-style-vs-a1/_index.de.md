---
title: Excel – R1C1-Referenzstil vs. A1
type: docs
weight: 30
url: /de/net/r1c1-reference-style-vs-a1/
description: R1C1 Referenzstil VS. A1-Stil mit Aspose.Cells for Python via .NET API.
keywords: R1C1 Reference Style VS. A1 style, R1C1 Reference Style, How to switch between R1C1 Reference Style and A1 Reference Style, A1 Reference style.
---
{{% alert color="primary" %}}

In Excel sind R1C1 und A1 zwei verschiedene Referenzstile, die zum Identifizieren von Zellen in einem Arbeitsblatt verwendet werden. Beachten Sie, dass die Wahl zwischen A1 und R1C1 weitgehend eine Frage der persönlichen Präferenz ist. Die meisten Benutzer sind mit dem A1-Stil besser vertraut, aber R1C1 kann in bestimmten Situationen nützlich sein, insbesondere beim Arbeiten mit Formeln und Berechnungen.

{{% /alert %}}

##  **A1-Referenzstil**

Dies ist der Standardreferenzstil in Excel. Im A1-Stil werden Spalten durch Buchstaben (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...) und Zeilen durch Zahlen (1, 2, 3, ...).
Beispielsweise wird die Zelle in der ersten Spalte und der zweiten Zeile als A2 bezeichnet.

##  **R1C1-Referenzstil**

Im R1C1-Stil werden sowohl Zeilen als auch Spalten durch Nummern gekennzeichnet. Der Buchstabe „R“ steht für die Zeilennummer und der Buchstabe „C“ für die Spaltennummer. R2C1 bezieht sich beispielsweise auf die Zelle in der zweiten Zeile und der ersten Spalte.

Alle Zahlen in eckigen Klammern beziehen sich auf den relativen Abstand von der aktuellen Zelle. Im Gegensatz zu A1, das sich auf Spalten gefolgt von der Zeilennummer bezieht, macht R1C1 das Gegenteil: Zeilen gefolgt von Spalten (was etwas gewöhnungsbedürftig ist). Positive Zahlen beziehen sich auf Zellen darunter und/oder rechts davon. Negative Zahlen beziehen sich auf Zellen darüber und/oder links.

Zum Beispiel ist R[2]C[3] eine Zelle 2 Zeilen tiefer und 3 Spalten rechts. R[-1]C[-4] ist eine Zelle 1 Zeile oben und 4 Spalten links. Wenn in Klammern keine Zahl angezeigt wird, beziehen Sie sich auf dieselbe Zeile oder Spalte, dh R[3]C ist eine Zelle 3 Zeilen unter der aktuellen Zelle in derselben Spalte.
<br>
<image src="2.png" width="70%" />

##  **Vergleich für R1C1-Referenzstil und A1-Referenzstil**
Hier ein kurzer Vergleich:
|**A1-Stil**|**R1C1-Stil**|
| :- | :- |
|A1|
|B3|
|G10|
|AA25|

##  **So wechseln Sie zwischen dem R1C1-Referenzstil und dem A1-Referenzstil**
Sie können in den Excel-Einstellungen zwischen diesen Referenzstilen wechseln. So ändern Sie den Referenzstil:

1. Gehen Sie zur Registerkarte „Datei“.
1. Wählen Sie unten „Optionen“.
1. Gehen Sie im Dialogfeld „Excel-Optionen“ zur Kategorie „Formeln“.
1. Aktivieren oder deaktivieren Sie im Abschnitt „Mit Formeln arbeiten“ die Option „R1C1-Referenzstil“.
1. Klicken Sie auf „OK“, um die Änderungen zu übernehmen.
<br>
<image src="1.png" width="70%" />

##  **So verwenden Sie den R1C1-Referenzstil und den A1-Referenzstil in Excel**
Das folgende Beispiel zeigt, wie die Summe zweier Zellwerte in zwei Stilen berechnet wird.
<br>
A1-Referenzstil:
<br>
<image src="4.png" width="70%" />

R1C1-Referenzstil:
<br>
<image src="3.png" width="70%" />
