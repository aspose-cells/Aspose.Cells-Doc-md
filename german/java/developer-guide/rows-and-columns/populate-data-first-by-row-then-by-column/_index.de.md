---
title: Füllen Sie zuerst die Daten nach Zeile und dann nach Spalte aus
type: docs
weight: 10
url: /de/java/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}}

Das Ausfüllen einer Tabelle mit Daten zuerst nach Zeile und dann nach Spalte verbessert die Gesamtperformance.

{{% /alert %}}

## Zuerst Daten nach Zeile, dann nach Spalte einfügen

Das Einsetzen von Daten in die Folge A1, B1, A2, B2 ist schneller als A1, A2, B1, B2. Wenn es viele Zellen in einem Arbeitsblatt gibt und Sie die zweite Sequenz befolgen, das heißt, Sie füllen die Daten Zeile für Zeile ein, kann dieser Tipp das Programm wesentlich schneller machen.

## Java-Code zum Zuerst-Daten-nach-Zeile-dann-nach-Spalte einfügen

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
{{< app/cells/assistant language="java" >}}
