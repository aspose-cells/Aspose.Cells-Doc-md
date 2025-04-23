---
title: Excel – R1C1 Referenzstil vs. A1
type: docs
weight: 30
url: /de/net/r1c1-reference-style-vs-a1/
description: R1C1 Referenzstil VS. A1 Stil mit Hilfe der Aspose.Cells für Python via .NET API.
keywords: R1C1 Bezugsstil gegen A1 Stil, R1C1 Bezugsstil, Wie man zwischen R1C1 Bezugsstil und A1 Bezugsstil wechselt, A1 Bezugsstil
---

## **Einführung**

In Excel sind A1 und R1C1 zwei verschiedene Referenzstile, die zur Identifizierung von Zellen in einem Arbeitsblatt verwendet werden. Beachten Sie, dass die Wahl zwischen A1 und R1C1 weitgehend eine Frage des persönlichen Geschmacks ist. Die meisten Benutzer sind eher mit dem A1-Stil vertraut, aber R1C1 kann in bestimmten Situationen nützlich sein, insbesondere bei der Arbeit mit Formeln und Berechnungen.

## **A1 Referenzstil**

Dies ist der Standard-Bezugsstil in Excel. Im A1-Stil werden Spalten durch Buchstaben (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...) und Zeilen durch Zahlen (1, 2, 3, ...) identifiziert.
Zum Beispiel wird die Zelle in der ersten Spalte und der zweiten Zeile als A2 bezeichnet.

## **R1C1-Bezugsstil**

Im R1C1-Stil werden sowohl Zeilen als auch Spalten durch Zahlen identifiziert. Der Buchstabe "R" repräsentiert die Zeilennummer und der Buchstabe "C" repräsentiert die Spaltennummer. Zum Beispiel bezieht sich R2C1 auf die Zelle in der zweiten Zeile und der ersten Spalte.

Alle Zahlen in eckigen Klammern beziehen sich auf den relativen Abstand von der aktuellen Zelle. Im Gegensatz zu A1, das sich auf Spalten und dann auf Zeilennummer bezieht, macht R1C1 das Gegenteil: Zeilen gefolgt von Spalten (was etwas Übung erfordert). Positive Zahlen beziehen sich auf Zellen unterhalb und/oder rechts. Negative Zahlen beziehen sich auf Zellen oberhalb und/oder links.

Zum Beispiel steht R[2]C[3] für eine Zelle 2 Zeilen nach unten und 3 Spalten nach rechts. R[-1]C[-4] ist eine Zelle 1 Zeile nach oben und 4 Spalten nach links. Wenn keine Zahl in Klammern angegeben ist, beziehen Sie sich auf dieselbe Zeile oder Spalte, d.h. R[3]C bezieht sich auf eine Zelle 3 Zeilen unterhalb der aktuellen Zelle in derselben Spalte.
<br>
<image src="2.png" width="70%" />

## **Vergleich des R1C1-Bezugsstils und des A1-Bezugsstils**
Hier ist ein schneller Vergleich:
|**A1-Stil**|**R1C1-Stil**|
| :- | :- |	
|A1|R1C1
|B3|R3C2
|G10|R10C7
|AA25|R25C27

## **Wie man zwischen dem R1C1-Bezugsstil und dem A1-Bezugsstil wechselt**
Sie können zwischen diesen Bezugsstilen in den Excel-Einstellungen wechseln. Um den Bezugsstil zu ändern:

1. Gehen Sie zum "Datei"-Tab.
1. Wählen Sie unten "Optionen" aus.
1. In dem Dialogfeld Excel-Optionen gehen Sie zur Kategorie "Formeln".
1. Unter dem Abschnitt "Formeln bearbeiten" aktivieren oder deaktivieren Sie die Option "R1C1-Bezugsstil".
1. Klicken Sie auf "OK", um die Änderungen zu übernehmen.
<br>
<image src="1.png" width="70%" />

## **Wie man den R1C1-Bezugsstil und den A1-Bezugsstil in Excel verwendet**
Das folgende Beispiel zeigt, wie die Summe von zwei Zellwerten auf zwei verschiedene Arten berechnet wird.
<br>
A1-Bezugsstil:
<br>
<image src="4.png" width="70%" />

R1C1-Bezugsstil:
<br>
<image src="3.png" width="70%" />
{{< app/cells/assistant language="csharp" >}}
